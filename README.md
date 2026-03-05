# 🤖 ChatBot com IA usando Streamlit

Este projeto implementa um **chat interativo com Inteligência Artificial** utilizando **Python**, **Streamlit** e a **API da OpenAI**.
A aplicação permite que o usuário envie mensagens e receba respostas da IA em tempo real, mantendo o **histórico da conversa durante a sessão**.

---

# 📌 Funcionalidades

* Interface de chat simples usando **Streamlit**
* Entrada de mensagens do usuário
* Envio das mensagens para a **API da OpenAI**
* Exibição da resposta da IA na tela
* Histórico de mensagens mantido durante a sessão com `session_state`

---

# 🧠 Funcionamento do Chat

Fluxo da aplicação:

1. O usuário digita uma mensagem no campo de chat.
2. A mensagem enviada é exibida na tela.
3. Essa mensagem é enviada para o modelo de IA.
4. A IA processa a mensagem e gera uma resposta.
5. A resposta da IA aparece no chat.
6. Todo o histórico de mensagens fica armazenado na sessão do Streamlit.

---

# 🛠 Tecnologias Utilizadas

* **Python**
* **Streamlit**
* **OpenAI API**

---

# 📂 Estrutura do Projeto

```
chatbot-streamlit/
│
├── app.py
└── README.md
```

---

# ⚙️ Instalação

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-streamlit.git
cd chatbot-streamlit
```

## 2️⃣ Criar ambiente virtual (recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## 3️⃣ Instalar dependências

```bash
pip install streamlit openai
```

---

# 🔑 Configurar a API Key

**Nunca coloque sua chave diretamente no código.**
O ideal é usar **variáveis de ambiente**.

Linux / Mac:

```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

Windows:

```bash
setx OPENAI_API_KEY "sua_chave_aqui"
```

---

# ▶️ Executar o projeto

```bash
streamlit run app.py
```

Após executar, o navegador abrirá automaticamente em:

```
http://localhost:8501
```

---

# 💻 Código Principal

```python
import streamlit as st
from openai import OpenAI

modelo = OpenAI()

st.write("### ChatBot com IA")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)

    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )

    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)

    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
```

---

# 📸 Interface

A interface apresenta:

* Campo para digitar mensagens
* Histórico da conversa
* Respostas da IA em formato de chat

Tudo renderizado automaticamente pelo **Streamlit**.

---

# 🚀 Possíveis Melhorias

* Adicionar **streaming de resposta da IA**
* Salvar histórico em **banco de dados**
* Criar **login de usuários**
* Deploy na **Streamlit Cloud**
* Adicionar **upload de arquivos**
* Utilizar **RAG (Retrieval Augmented Generation)**

---

# 📄 Licença

Este projeto é livre para fins de estudo e aprendizado.
