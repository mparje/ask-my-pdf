__version__ = "0.4.8.2"
app_name = "Ask my PDF"

# BOILERPLATE
import streamlit as st
from PIL import Image
import io
import requests
import json

st.set_page_config(layout='centered', page_title=f'{app_name} {__version__}')
ss = st.session_state
if 'debug' not in ss: ss['debug'] = {}

# IMPORTS
import model

# HANDLERS
def index_pdf_file():
    if ss['pdf_file']:
        ss['filename'] = ss['pdf_file'].name
        if ss['filename'] != ss.get('fielname_done'):  # UGLY
            with st.spinner(f'indexing {ss["filename"]}'):
                index = model.index_file(ss['pdf_file'], ss['filename'], fix_text=ss['fix_text'],
                                         frag_size=ss['frag_size'])
                ss['index'] = index
                debug_index()
                ss['filename_done'] = ss['filename']  # UGLY

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
    st.write('## 2. Upload or select your PDF file')
    disabled = not ss.get('user') or (not ss.get('api_key') and not ss.get('community_pct', 0))

    t1, t2 = st.columns([1, 1])
    with t1:
        pdf_file = st.file_uploader('Upload PDF file', type='pdf', key='pdf_file', accept_multiple_files=False,
                                    help='Upload a PDF file')
        if pdf_file is not None:
            ss['pdf_file'] = pdf_file

    with t2:
        filenames = ['']
        if ss.get('storage'):
            filenames += ss['storage'].list()
        selected_file = st.selectbox('Select a file', filenames, key='selected_file')
        ss['selected_file'] = selected_file

def ui_submit():
    st.write('## 4. Submit')
    st.button('Submit')

def main():
    if ss.get('filename') or ss.get('pdf_file'):
        index_pdf_file()

    st.write(f'# {app_name} {__version__}')
    ui_pdf_file()
    ui_submit()

main()
