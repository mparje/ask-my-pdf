import streamlit as st
import storage
from model import Model
from utils import now

__version__ = '0.0.1'

# Initialize the model and storage
ss = {}
ss['debug'] = {}
ss['data_dict'] = storage.get_data_dict()
ss['api_key'] = st.secrets['OPENAI_API_KEY']
ss['storage'] = storage.get_storage(ss['api_key'], data_dict=ss['data_dict'])
model = Model(storage=ss['storage'], fix_text=True)

# UI FUNCTIONS

def ui_info():
    st.write(f'**Ask my PDF {__version__}**')
    st.write('An app that allows you to ask questions about the content of a PDF document.')

def ui_api_key():
    st.write('1. Enter your OpenAI API key')
    st.write('   (or leave it as is to use the community version)')
    ss['api_key'] = st.text_input("API key", value=ss['api_key'], type='password')

def on_api_key_change():
    ss['api_key'] = ss['api_key'].strip()
    if ss['api_key']:
        ss['storage'] = storage.get_storage(ss['api_key'], data_dict=ss['data_dict'])
        model.set_storage(ss['storage'])
        ss['fix_text'] = model.fix_text
        ss['frag_size'] = model.frag_size

def index_pdf_file():
    st.write('Indexing PDF file...')
    ss['index'] = model.index_pdf(ss['pdf_file'], fix_text=ss['fix_text'], frag_size=ss['frag_size'])
    st.write('PDF file indexed successfully.')

def debug_query():
    query = ss['query']
    d = {}
    d['query'] = query
    d['prompt'] = model.get_prompt(query)
    d['tokens'] = len(model.to_tokens(query))
    d['tokens_free'] = model.tokens_left()
    d['tokens_refresh_in'] = model.tokens_refresh_in()
    ss['debug']['query'] = d

def debug_token_limit():
    ss['debug']['token_limit'] = model.debug_token_limit()

def st_buttons_group(buttons):
    cols = st.beta_columns(len(buttons))
    for col, button in zip(cols, buttons):
        col.button(button)

# MAIN ROUTINE

def main_routine():
    st.title(f'Ask my PDF {__version__}')
    ui_info()
    ui_api_key()

    if st.button('I want to enter my own API key'):
        ss['api_key'] = None
        on_api_key_change()
        return

    st.header("2. Upload your PDF")
    ss['pdf_file'] = st.file_uploader("Upload a PDF file", type=['pdf'])
    st.write('or')
    if st.button('Example PDFs'):
        ss['pdf_file'] = model.get_pdf_example()

    st.header("3. Advanced options")
    ss['fix_text'] = st.checkbox("Attempt to fix text errors (experimental)", value=True)
    ss['frag_size'] = st.number_input("Text fragment size", value=3000)

    if st.button('Index PDF'):
        index_pdf_file()

    st.header("4. Ask a question")
    ss['query'] = st.text_input("Your question")
    if ss['query']:
        ss['query'] = ss['query'].strip()
        st.write(f"Tokens: {len(model.to_tokens(ss['query']))} / Tokens free: {model.tokens_left()}")
        st_buttons_group(["Ask", "Debug"])

        if st.button("Ask"):
            st.write(f'Query: {ss["query"]}')
            ss['answers'] = model.query(ss['query'], debug=False)
            st.write(ss['answers'])

        if st.button("Debug"):
            debug_query()
            st.write(ss['debug']['query'])

    st.header("5. Debug")
    st_buttons_group(["Token limit", "Clear debug info"])
    if st.button("Token limit"):
        debug_token_limit()

    if st.button("Clear debug info"):
        ss['debug'] = {}

# Run the app
app()
