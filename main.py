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

texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    print(texto_usuario)