__version__ = "0.4.8.2"
app_name = "Ask my PDF"


# BOILERPLATE

import streamlit as st
st.set_page_config(layout='wide', page_title=f'{app_name} {__version__}')
ss = st.session_state
if 'debug' not in ss: ss['debug'] = {}
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


def ui_info():
    st.markdown(f"""
    # Ask my PDF
    version {__version__}
    
    Question answering system built on top of GPT3.
    """)
    ui_spacer(1)
    st.write("Por Moris Polanco, basado en [Maciej Obarski](https://www.linkedin.com/in/mobarski/).", unsafe_allow_html=True)
    ui_spacer(1)
    st.markdown("""
        Gracias por tu interés en mi aplicación.
        Ten en cuenta que esto es solo un sistema de prueba de concepto
        y puede contener errores o características incompletas.
        Si te gusta esta aplicación, puedes [seguirme](https://twitter.com/morispolanco)
        en Twitter para recibir noticias y actualizaciones.
        """)
    ui_spacer(1)
    st.markdown('El código fuente se puede encontrar [aquí](https://github.com/mobarski/ask-my-pdf).')

def ui_model():
    models = ['gpt-4','gpt-3.5-turbo','text-davinci-003','text-curie-001']
    st.selectbox('Modelo principal', models, key='model', disabled=not ss.get('api_key'))
    st.selectbox('Modelo de incrustación', ['text-embedding-ada-002'], key='model_embed') # FOR FUTURE USE

def ui_task_template():
    st.selectbox('Plantilla de tarea', prompts.TASK.keys(), key='task_name')

def ui_spacer(n=1):
    for _ in range(n):
        st.markdown("&nbsp;")
        
def ui_footer():
    st.sidebar.markdown(f'<sup>© {now()} | Ask my PDF {__version__}</sup>', unsafe_allow_html=True)

def ui_debug():
    with st.beta_expander("Depuración", expanded=False):
        for k,v in ss['debug'].items():
            st.write(f'{k}: {v}')

def ui_save():
    if st.button('Guardar'):
        # TODO: save task
        pass

def ui_delete():
    if st.button('Eliminar'):
        # TODO: delete task
        pass

def ui_header():
    with st.container():
        st.title(app_name)
        st.text_input('API key', key='api_key', on_change=on_api_key_change)
        if 'storage.folder' in ss['debug']: st.write(ss['debug']['storage.folder'])
        if 'storage.class' in ss['debug']: st.write(ss['debug']['storage.class'])
        ui_spacer(1)

# PAGES

def page_info():
    header1.warning('ℹ️ Información')
    ui_info()
    ui_footer()
    ui_spacer(5)

def page_model():
    header1.warning('⚙️ Modelo')
    ui_model()
    ui_footer()
    ui_spacer(5)

def page_task():
    header1.warning('📑 Plantilla de tarea')
    ui_task_template()
    ui_footer()
    ui_spacer(5)

def page_input():
    header1.warning('📥 Datos de entrada')
    header2.subheader('Documento PDF')
    # TODO: input field
    header2.subheader('Pregunta')
    # TODO: input field
    ui_footer()
    ui_spacer(5)

def page_output():
    header1.warning('📤 Resultado')
    # TODO: output field
    ui_footer()
    ui_spacer(5)

def page_debug():
    header1.warning('🐞 Depuración')
    ui_debug()
    ui_footer()
    ui_spacer(5)

def page_main():
    header1.warning('🚀 Página principal')
    ui_save()
    ui_delete()
    ui_footer()
    ui_spacer(5)


# MAIN

def main():
    ui_header()

    col1, col2 = st.beta_columns(2)

    with col1:
        page_info()

    with col2:
        page_main()

    col3, col4 = st.beta_columns(2)

    with col3:
        page_model()

    with col4:
        page_task()

    col5, col6 = st.beta_columns(2)

    with col5:
        page_input()

    with col6:
        page_output()

    page_debug()

if __name__ == '__main__':
    main()
