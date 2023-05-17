__version__ = "0.4.8.2"
app_name = "Ask my PDF"

# BOILERPLATE

import os
import streamlit as st
import openai
st.set_page_config(layout='centered', page_title=f'{app_name} {__version__}')
ss = st.session_state
if 'debug' not in ss: ss['debug'] = {}
import css
st.write(f'<style>{css.v1}</style>', unsafe_allow_html=True)
header1 = st.empty() # for errors / messages
header2 = st.empty() # for errors / messages
header3 = st.empty() # for errors / messages

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# IMPORTS

import prompts
import model
import storage
import feedback
import cache
import os

from time import time as now

# HANDLERS

def on_api_key_change():
    api_key = ss.get('api_key') or os.getenv('OPENAI_KEY')
    if api_key is None:
        return
    model.use_key(api_key) # TODO: empty api_key
    #
    if 'data_dict' not in ss: ss['data_dict'] = {} # used only with DictStorage
    ss['storage'] = storage.get_storage(api_key, data_dict=ss['data_dict'])
    ss['cache'] = cache.get_cache()
    ss['user'] = ss['storage'].folder # TODO: refactor user 'calculation' from get_storage
    model.set_user(ss['user'])
    ss['feedback'] = feedback.get_feedback_adapter(ss['user'])
    ss['feedback_score'] = ss['feedback'].get_score()
    #
    ss['debug']['storage.folder'] = ss['storage'].folder
    ss['debug']['storage.class'] = ss['storage'].__class__.__name__


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
    st.markdown('Source code can be found [here](https://github.com/mobarski/ask-my-pdf).')

def ui_api_key():
    st.write('## 1. Enter your OpenAI API key')
    openai.api_key = os.getenv("OPENAI_API_KEY")

def index_pdf_file():
    if ss['pdf_file']:
        ss['filename'] = ss['pdf_file'].name
        if ss['filename'] != ss.get('fielname_done'): # UGLY
            with st.spinner(f'indexing {ss["filename"]}'):
                index = model.index_file(ss['pdf_file'], ss['filename'], fix_text=ss['fix_text'], frag_size=ss['frag_size'], cache=ss['cache'])
                ss['index'] = index
                debug_index()
                ss['filename_done'] = ss['filename'] # UGLY

def debug_index():
    index = ss['index']
    d = {}
    d['hash'] = index['hash']
    d['frag_size'] = index['frag_size']
    d['n_pages'] = len(index['pages'])
    d['n_texts'] = sum([len(p['texts']) for p in index['pages']])
    ss['debug']['index'] = d

def debug_query():
    query = ss['query']
    d = {}
    d['query'] = query
    d['prompt'] = model.get_prompt(query)
    d['tokens'] = len(model.to_tokens(query))
    d['tokens_free'] = model.tokens_left()
    d['tokens_refresh_in'] = model.tokens_refresh_in()
    ss['debug']['query'] = d

def debug_model():
    ss['debug']['model'] = model.debug_model()

def debug_token_limit():
    ss['debug']['token_limit'] = model.debug_token_limit()

def st_buttons_group(buttons):
    cols = st.beta_columns(len(buttons))
    for col, button in zip(cols, buttons):
        col.button(button)

# MAIN ROUTINE

def main_routine():
    debug_model()
    #
    st.title(f'Ask my PDF {__version__}')
    ui_info()
    ui_api_key()
    #
    if st.button('I want to enter my own API key'):
        ss['api_key'] = None
        on_api_key_change()
        return
    #
    st.header("2. Upload your PDF")
    ss['pdf_file'] = st.file_uploader("Upload a PDF file", type=['pdf'])
    st.write('or')
    if st.button('Example PDFs'):
        ss['pdf_file'] = model.get_pdf_example()
    #
    st.header("3. Advanced options")
    ss['fix_text'] = st.checkbox("Attempt to fix text errors (experimental)", value=True)
    ss['frag_size'] = st.number_input("Text fragment size", value=3000)
    #
    if st.button('Index PDF'):
        index_pdf_file()
    #
    st.header("4. Ask a question")
    ss['query'] = st.text_input("Your question")
    if ss['query']:
        ss['query'] = ss['query'].strip()
        st.write(f"Query length: {len(ss['query'])}")
        debug_query()
        st.write(f'Tokens left: {model.tokens_left()}')
        st.write(f'Tokens refresh in: {model.tokens_refresh_in()}')
        #
        if model.tokens_left() < 5:
            st.write('Please consider entering your own API key to be able to use the app.')
            return
        #
        if st.button("Ask"):
            t0 = now()
            debug_query()
            #
            if not ss.get('index'):
                st.write("Please upload a PDF and index it first.")
                return
            #
            result = model.ask(ss['query'], ss['index'], cache=ss['cache'])
            ss['debug']['answer'] = result
            model.api_feedback(result)
            #
            ss['answer'] = result['answer']
            ss['tokens_left'] = model.tokens_left()
            ss['tokens_refresh_in'] = model.tokens_refresh_in()
            #
            header2.write(f"Answer ({round(now()-t0, 2)}s):")
            st.write(ss['answer'])
            st.markdown('---')
            #
            if st.button('Copy answer to clipboard'):
                st.write('Answer copied to clipboard.')
                st.text_area('', ss['answer'])
            #
            debug_token_limit()
        #
        if st.button('Hide answer'):
            del ss['answer']
            del ss['debug']['answer']
            del ss['tokens_left']
            del ss['tokens_refresh_in']
            header2.empty()
            header3.empty()

def app():
    on_api_key_change()
    main_routine()

app()
