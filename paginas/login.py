import streamlit as st
from banco_dados.db import autenticar

def pagina_login():
    st.title("🔐 Login")
    with st.form("form_login"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        entrar = st.form_submit_button("Entrar")

    if entrar:
        if not usuario or not senha:
            st.warning("Preencha usuário e senha.")
            return # não vai para frente

        resultado = autenticar(usuario, senha)
        # print(resultado)

        if resultado is None:
            st.error("Usuário ou senha inválidos")
        elif "erro" in resultado:
            st.error(resultado["erro"])
        else:
            st.session_state.usuario = resultado
            st.rerun()


