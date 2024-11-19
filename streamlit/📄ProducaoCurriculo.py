import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
from PyPDF2 import PdfReader

from pathlib import Path
import hashlib


load_dotenv()

st.header("Resume Tailor")
st.write("Upload your Curriculum and a job description, and engage in a conversation to tailor you cv for the position you are interested in applying for")


system_instruction = """
Seu nome é Ana, uma assistente virtual que ajuda um usuário a preparar um currículo.
Você deve fornecer feedback sobre o currículo de um usuário.
Você irá receber a vaga que o usuário deseja e o currículo atual dele em formato PDF.
Você deve analisar o currículo e fornecer feedbacks construtivos para o usuário melhorar o currículo dele.
E no final, evidencie uma nota de 0 a 10 para o currículo dele.
Sempre que fornecer um feedback, forneça uma sugestão de melhoria com os pontos positivos e negativos.
"""


genai.configure(api_key=os.getenv("gemini_api_key"))


model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction=system_instruction
)


def text_from_pdf(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text




st.title('Produção de Currículo 📄')


st.write("Envie seu currículo atual e vaga desejada para receber feedbacks construtivos sobre o seu currículo.")


st.write("Por favor, faça o upload do seu currículo atual em formato PDF")
cv = st.file_uploader("Upload do currículo", type=['pdf'])


if cv is not None:
    with st.spinner('Carregando currículo...'):
        text = text_from_pdf(cv)
    st.success('Currículo carregado com sucesso!')
    vaga = st.text_input('Qual vaga você deseja se candidatar? Seja o mais específico possível.')
    if vaga:
        initial_message = f"Olá Ana, gostaria de me candidatar para a vaga de {vaga}. Aqui está o meu currículo atual {text}."
        button = st.button('Enviar')
        if button:
            with st.spinner("Processando..."):
                ai_query = model.generate_content(initial_message)
                st.markdown(ai_query.text)

    else:
        st.warning('Por favor, preencha o campo da vaga antes de continuar.')
else:
    st.warning('Por favor, faça o upload do seu currículo antes de continuar.')
