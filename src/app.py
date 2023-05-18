__version__ = "0.4.8.2"
app_name = "Ask my PDF"


# BOILERPLATE

import streamlit as st
st.set_page_config(layout='centered', page_title=f'{app_name} {__version__}')
ss = st.session_state
if 'debug' not in ss:
    ss['debug'] = {}
import css
st.write(f'<style>{css.v1}</style>', unsafe_allow_html=True)
header1 = st.empty() # for errors / messages
header2 = st.empty() # for errors / messages
header3 = st.empty() # for errors / messages

# IMPORTS

import prompts
import model
import storage
import feedback
import cache
import os

from time import time as now
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


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
    st.write("Made by [Maciej Obarski](https://www.linkedin.com/in/mobarski/).",
             unsafe_allow_html=True)
    ui_spacer(1)
    st.markdown("""
        Thank you for your interest in my application.
        Please be aware that this is only a Proof of Concept system
        and may contain bugs or unfinished features.
        If you like this app you can ️ [follow me](https://twitter.com/KerbalFPV)
        on Twitter for news and updates.
        """)
    ui_spacer(1)
    st.markdown('Source code can be found [here](https://github.com/mobarski/ask-my-pdf).')


def index_pdf_file(file):
    if ss['pdf_file']:
        ss['filename'] = file.name
        if ss['filename'] != ss.get('filename_done'): # UGLY
            with st.spinner(f'indexing {ss["filename"]}'):
                index = model.index_file(file, ss['filename'], fix_text=ss['fix_text'],
                                         frag_size=ss['frag_size'], cache=ss['cache'])
                ss['index'] = index
                debug_index()
                ss['filename_done'] = ss['filename'] # UGLY


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
    d['time'] = index.get('time',{})
    ss['debug']['index'] = d


def ui_pdf_file():
    st.write('## 2. Upload or select your PDF file')
    disabled = not ss.get('user') or (not ss.get('api_key') and not ss.get('community_pct',0))
    t1,t2 = st.tabs(['UPLOAD','SELECT'])
    
    # 1. Upload file
    with t1:
        st.write("Choose a PDF file from your computer.")
        file = st.file_uploader('pdf file', type='pdf', key='pdf_file',
                                accept_multiple_files=False)
        if file is not None:
            index_pdf_file(file)
            st.write("File uploaded!")
        b_save()
    
    # 2. Select file
    with t2:
        filenames = ['']
        if ss.get('storage'):
            filenames += ss['storage'].list()
        def on_change():
            name = ss['selected_file']
            if name and ss.get('storage'):
                with ss['spin_select_file']:
                    with st.spinner('loading index'):
                        t0 = now()
                        index = ss['storage'].get(name)
                        ss['debug']['storage_get_time'] = now()-t0
                ss['filename'] = name # XXX
                ss['index'] = index
                debug_index()
            else:
                #ss['index'] = {}
                pass
        st.write("Select a PDF file from your cloud storage.")
        ss['selected_file'] = st.selectbox('select file', filenames, on_change=on_change,
                                           label_visibility="collapsed")
        b_save()

def b_save():
    col1,col2 = st.columns(2)
    if col1.button('Save'):
        if ss['pdf_file'] and ss['index']:
            name = ss['filename'] or 'index'
            with col2.spinner('Saving...'):
                ss['storage'].put(name, ss['index'])
                st.write(f'saved {name}')
        else:
            st.write('no index or PDF file to save')


ui_pdf_file()
