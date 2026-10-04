import streamlit as st
from paginas.login import pagina_login

st.set_page_config(page_title="Palete-Caixa",
                   page_icon="📦",
                   layout="centered")

# Pagina de usuario
if "usuario" not in st.session_state:
    st.session_state.usuario = None
print(st.session_state.usuario)

# Chamando a pagina login 
if st.session_state.usuario is None:
    pagina_login()

# print(st.session_state)

