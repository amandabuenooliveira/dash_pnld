import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('PNLD - Ensino Médio')

st.write("Escolas do Brasil")

st.metric(label="Alunado EM", value="6.690.396")

st.metric(label="Professores EM", value="4508.317")

st.metric(label="Escolas EM", value="21.016")

st.metric(label="Municípios com EM", value="5.570")

st.metric(label="Estados com EM", value="27")

# Dados da tabela
data = {
    'uf': ['SP', 'MG', 'PR', 'RS', 'RJ', 'BA', 'MA', 'PE', 'GO', 'SC', 'PA', 'CE', 'MT', 'PI', 'PB', 'AM', 'MS', 'RN', 'TO', 'ES', 'AC', 'AL', 'RO', 'SE', 'RR', 'AP', 'DF'],
    'escolas': [4056, 2527, 1637, 1192, 1186, 1023, 895, 828, 769, 768, 746, 714, 548, 526, 495, 432, 339, 337, 326, 316, 270, 254, 214, 206, 167, 136, 109],
    'alunado medio': [1564118, 633929, 346223, 301636, 434869, 458710, 267084, 301399, 192889, 229595, 294563, 327385, 123668, 115382, 119569, 180514, 93108, 109759, 61844, 110931, 37942, 105517, 66321, 71638, 26367, 29810, 85626]
}

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Título do app
st.title('Informações de Escolas e Alunado Médio por UF')

# Exibir a tabela no Streamlit
st.subheader('Tabela de Escolas e Alunado Médio por Estado (UF)')
st.dataframe(df)

# Exibir um gráfico de barras 
st.subheader('Gráfico de Barras - Alunado Médio por UF')
st.bar_chart(df.set_index('uf')['alunado medio'])

# Exibir um gráfico de barras 
st.subheader('Gráfico de Barras - Escolas com Médio por UF')
st.bar_chart(df.set_index('uf')['escolas'])


