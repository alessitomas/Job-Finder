import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

from PyPDF2 import PdfReader

from pathlib import Path



load_dotenv()



system_instruction = """
Você é um assistente virtual que ajuda um usuário a fazer a sua melhor versão de currículo para uma vaga específica.
Você irá receber a descrição de vaga específica e o currículo do usuário.
Você deve analisar os requisitos da vagas, palavras chaves, técnologias esperadas. 
Forneá feedback de quais informações são relevantes do seu currículo para a vaga e quais informações seriam interessantes incluir.
Elenque pontos positivos do currículo que se alinham com a vaga caso existam.
Elenque pontos faltantes que caso o usuário tivesse experiência e pudesse incluir aumentariam suas chances para a vaga.
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


st.write("Envie seu currículo atual e vaga descrição da vaga desejada para receber feedbacks personalizados focados em melhorar seu currículo para a dada vaga.")


st.write("Por favor, faça o upload do seu currículo atual em formato PDF.")
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
