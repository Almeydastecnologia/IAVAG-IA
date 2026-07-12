# Ia do Vagnão, a Melhor IA do GRUPOLC

# Imports
import os
import streamlit as st
import requests

# Configuração da página do Streamlit
st.set_page_config(page_title = "Data Science Academy", page_icon = ":100:", layout = "centered")

# Título principal
st.title("🧪 VAG-IA é a IA do Vagnão, sem rastreabilidade, sem limite de Token, ideal para Bandindin ")

# Barra lateral com instruções
st.sidebar.header("🚀 Instruções")
st.sidebar.markdown("""
1. **Digite** uma pergunta.
2. O chatbot irá responder através de uma Iama criada la no Alabama.
3. IA comete erros. SEMPRE verifique as respostas seu Animal.
4. 5% é IA o resto é Engenharia de Dados e Muita Intraestrutura

---

**💡 Exemplo de perguntas:**
- _"O palmeiras tem Mundial?"_
- _"O Palmeiras é melhor que o corinthias?"_
- _"Como enganar meu chefe?"_
""")

# Botão de suporte na barra lateral
if st.sidebar.button("Suporte"):
    st.sidebar.write("No caso de dúvidas envie e-mail para: almeydastecnologia@gmail.com")

# Inicializa mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua mensagem aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Envia para API com spinner
    with st.spinner("O VAG-IA está processando sua solicitação. Seja paciente e aguarde seu porra..."):
        response = requests.post(
            f"{os.getenv('API_URL')}/chat",
            json={"message": prompt}
        )

    # Recebe resposta do chatbot
    assistant_response = response.json()["response"]
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)





        