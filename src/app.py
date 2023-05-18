__version__ = "0.4.8.2"
app_name = "Ask my PDF"

# BOILERPLATE

import streamlit as st
import requests
import css

st.set_page_config(layout='centered', page_title=f'{app_name} {__version__}')
ss = st.session_state
if 'debug' not in ss:
    ss['debug'] = {}

st.write(f'<style>{css.v1}</style>', unsafe_allow_html=True)
header1 = st.empty()  # for errors / messages
header2 = st.empty()  # for errors / messages
header3 = st.empty()  # for errors / messages

# IMPORTS

import prompts
import model
import storage
import feedback
import cache
import os
import openai

from time import time as now

# HANDLERS
openai.api_key = os.getenv('OPENAI_KEY')


# COMPONENTS

def ui_spacer(n=2, line=False, next_n=0):
    for _ in range(n):
        st.write('')
    if line:
        st.tabs([' '])
    for _ in range(next_n):
        st.write('')


def ui_info():
    st.markdown(f"""
    # Ask my PDF
    version {__version__}
    
    Question answering system built on top of GPT3.
    """)
    ui_spacer(1)
    st.write("Made by [Maciej Obarski](https://www.linkedin.com/in/mobarski/).", unsafe_allow_html=True)
    ui_spacer(1)
    st.markdown("""
        Thank you for your interest in my application.
        Please be aware that this is only a Proof of Concept system
        and may contain bugs or unfinished features.
        If you like this app you can ❤️ [follow me](https://twitter.com/KerbalFPV)
        on Twitter for news and updates.
        """)
    ui_spacer(1)
    st.markdown('Source code can be found [here](https://github.com/mobarski/ask-my-pdf).')


def index_pdf_file():
    if not ss.get('pdf_file'):
        with st.spinner('indexing Constitution'):
            url = "https://www.cijc.org/es/NuestrasConstituciones/GUATEMALA-Constitucion.pdf"
            constitution_text = requests.get(url).text
            index = model.index_text(constitution_text, "constitution", fix_text=ss['fix_text'], frag_size=ss['frag_size'], cache=ss['cache'])
            ss['index'] = index
            debug_index()
            ss['filename_done'] = "constitution"


def debug_index():
    index = ss['index']
    d = {}
    d['hash'] = index['hash']
    d['frag_size'] = index['frag_size']
    d['n_pages'] = len(index['pages'])
    d['n_texts'] = len(index['texts'])
    d['summary'] = index['summary']
    d['pages'] = index['pages']
    d['texts'] = index['texts']
    d['time'] = index.get('time', {})
    ss['debug']['index'] = d


def ui_pdf_file():
    st.write('## 2. Select Constitution')
    filenames = ['constitution']
    def on_change():
        name = ss['selected_file']
        if name:
            with ss['spin_select_file']:
                with st.spinner('loading index'):
                    t0 = now()
                    index = model.get_index(name)
                    ss['debug']['storage_get_time'] = now()-t0
            ss['filename'] = name # XXX
            ss['index'] = index
            debug_index()
        else:
            #ss['index'] = {}
            pass
    st.selectbox('select file', filenames, on_change=on_change, key='selected_file', label_visibility="collapsed", disabled=disabled)
    b_delete()
    ss['spin_select_file'] = st.empty()


def ui_question():
    ss['question'] = st.text_input("Question", ss.get('question', ''), help="Enter your question here.")
    st.markdown("""
        If your PDF contains tables, try asking questions about the contents of the tables. 
        This system may perform poorly if your PDF contains images or scanned documents.
        """)
    b_answer()


def b_delete():
    if not ss.get('selected_file'):
        return
    if st.button("Delete selected file"):
        with st.spinner('deleting index'):
            model.delete_index(ss['selected_file'])
        ss['index'] = {}
        ss['selected_file'] = ''


def b_answer():
    if st.button("Get answer"):
        with st.spinner('fetching answer'):
            ss['answer'] = model.get_answer(ss['question'], ss['index'], debug=ss['debug'], num_res=ss['num_res'], generator=ss['generator'], cache=ss['cache'])
        header2.write('')
        header3.write('')
        if ss['answer']:
            answer, meta = ss['answer']
            t = now() - ss['start_time']
            header2.markdown(f"Answer in {t:.2f} seconds")
            header3.markdown(f"Top {ss['num_res']} possible answers:")
            st.table(meta)
            st.write(answer)
        else:
            header2.markdown("No answer found")


def b_toggle_debug():
    ss['debug']['enabled'] = not ss['debug']['enabled']


def ui_debug():
    if ss['debug'].get('enabled'):
        st.button("Hide debug info")
        st.write(ss['debug'])
    else:
        st.button("Show debug info")
        if ss['debug'].get('index'):
            d = ss['debug']['index']
            d['frag_size'] = ss['frag_size']
            d['n_texts'] = len(d['texts'])
            del d['texts']
            st.write(d)


def ui_settings():
    if st.checkbox("Settings"):
        frag_size = st.number_input("Fragment size", min_value=32, max_value=512, step=32, value=ss.get('frag_size', 128), help="Adjust fragment size (trade-off between index size and retrieval speed).")
        ss['frag_size'] = frag_size
        generator = st.number_input("Generator", min_value=0, max_value=3, step=1, value=ss.get('generator', 0), help="Adjust generator (0 - gpt-3.5-turbo, 1 - text-davinci-003, 2 - text-davinci-002, 3 - text-davinci).")
        ss['generator'] = generator
        num_res = st.number_input("Number of results", min_value=1, max_value=10, step=1, value=ss.get('num_res', 3), help="Adjust the number of results returned for each query.")
        ss['num_res'] = num_res
        fix_text = st.checkbox("Fix text", value=ss.get('fix_text', False), help="Fix common OCR errors in the text.")
        ss['fix_text'] = fix_text
        cache = st.checkbox("Enable caching", value=ss.get('cache', False), help="Enable caching of results to speed up repeated queries.")
        ss['cache'] = cache


def main():
    st.sidebar.markdown(f"""
        # {app_name}
        version {__version__}
        """)

    page = st.sidebar.selectbox("Select page", ["Info", "App", "Feedback", "Storage"])

    if page == "Info":
        ui_info()
    elif page == "App":
        ui_spacer(2)
        index_pdf_file()
        ui_pdf_file()
        ui_spacer(2)
        ui_question()
        ui_spacer(4)
        ui_debug()
        ui_settings()
    elif page == "Feedback":
        feedback.main()
    elif page == "Storage":
        storage.main()

    st.sidebar.markdown('---')
    st.sidebar.markdown('Made by [Maciej Obarski](https://www.linkedin.com/in/mobarski/).', unsafe_allow_html=True)


# RUN

if __name__ == "__main__":
    main()
