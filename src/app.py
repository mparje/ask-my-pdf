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


ss['community_user'] = os.getenv('COMMUNITY_USER')
if 'user' not in ss and ss['community_user']:
    on_api_key_change() # use community key

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
    if ss['community_user']:
        st.write('## 1. Optional - enter your OpenAI API key')
        t1,t2 = st.tabs(['community version','enter your own API key'])
        with t1:
            pct = model.community_tokens_available_pct()
            st.write(f'Community tokens available: :{"green" if pct else "red"}[{int(pct)}%]')
            st.progress(pct/100)
            st.write('Refresh in: ' + model.community_tokens_refresh_in())
            st.write('You can sign up to OpenAI and/or create your API key [here](https://platform.openai.com/account/api-keys)')
            ss['community_pct'] = pct
            ss['community_tokens_refresh_in'] = model.community_tokens_refresh_in()
            if pct < 5:
                st.write('Please consider entering your own API key to be able to use the app.')
                return
            if st.button('I want to enter my own API key'):
                ss['community_user'] = False
                on_api_key_change()
                return
        with t2:
            api_key = st.text_input("API key")
            if api_key:
                ss['api_key'] = api_key
                on_api_key_change()
    else:
        if not ss['api_key']:
            st.write('## 1. Enter your OpenAI API key')
            api_key = st.text_input("API key")
            if api_key:
                ss['api_key'] = api_key
                on_api_key_change()
                ui_spacer(2)
                st.stop()
        else:
            st.write('## 1. API key set')

def ui_model_info():
    st.write('## 2. Select model')
    model_names = model.get_model_names()
    model_name = st.selectbox('Model', model_names, index=model_names.index(model.get_model_name()))
    model.use_model(model_name)
    ss['debug']['model.name'] = model_name

def ui_storage_info():
    st.write('## 3. Select storage')
    storage_names = storage.get_storage_names()
    storage_name = st.selectbox('Storage', storage_names, index=storage_names.index(ss['storage'].name if 'storage' in ss else ''))
    if 'storage' not in ss or storage_name != ss['storage'].name:
        ss['data_dict'] = ss['storage'].get_data_dict()
        ss['storage'] = storage.get_storage(storage_name, data_dict=ss['data_dict'])
    ss['debug']['storage.class'] = ss['storage'].__class__.__name__
    ss['debug']['storage.name'] = ss['storage'].name

def ui_file_upload():
    st.write('## 4. Upload PDF file')
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        file_name = uploaded_file.name
        ss['file_contents'] = file_contents
        ss['file_name'] = file_name

def ui_question_input():
    st.write('## 5. Enter your question')
    question = st.text_input("Question")
    if question:
        ss['question'] = question

def ui_feedback():
    if 'answer' in ss:
        st.write('## 6. Feedback')
        if 'feedback_text' not in ss:
            ss['feedback_text'] = ss.get('answer') or ss.get('debug').get('answer') or ''
        st.write(ss['feedback_text'])
        ss['feedback_text'] = st.text_input("If the answer is not satisfactory, please provide feedback.")

def ui_submit():
    if st.button('Submit'):
        header3.empty()
        header1.info('Working...')
        answer = model.get_answer(ss['question'], ss['file_contents'])
        ss['answer'] = answer
        header1.success('Done!')
        header2.write(answer)
        feedback_text = ss.get('feedback_text') or ss.get('answer') or ss.get('debug').get('answer')
        if feedback_text:
            ss['feedback'].save(feedback_text)
        ss['debug']['answer'] = answer

# MAIN

header1.info('Welcome to Ask my PDF')
ui_spacer()
ui_info()
ui_spacer()
ui_api_key()
ui_spacer()
ui_model_info()
ui_spacer()
ui_storage_info()
ui_spacer()
ui_file_upload
