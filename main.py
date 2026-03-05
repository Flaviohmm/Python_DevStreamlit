# Titulo
# Input do chat

# A cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# Streamlit - frontend e backend

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

modelo = OpenAI(api_key=OPENAI_API_KEY)

st.write("# Chatbot com IA") # Markdown

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagem"].append(mensagem_usuario)

    resposta_ia = "Você perguntou: " + texto_usuario

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem_ia)

print(st.session_state["lista_mensagem"])