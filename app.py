import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.image(logo.png.png, width=150)

st.set_page_config(layout='wide',
                   page_icon=':book:',
                   initial_sidebar_state='expanded',
                   )

st.markdown("<h1 style='text-align: center;'>PNLD - Ensino Médio</h1>", unsafe_allow_html=True)


st.write("Este relatório apresenta dados sobre escolas de Ensino Médio no Brasil.")



col1, col2, col3 = st.columns(3)
col1.metric("Alunado EM", "6.690.396")
col2.metric("Professores EM", "4508.317")
col3.metric("Escolas EM", "21.016")



st.metric(label="Municípios com EM", value="5.290")
# Divisão visual
st.markdown("---")


# Dados da tabela
data = {
    'uf': ['SP', 'MG', 'PR', 'RS', 'RJ', 'BA', 'MA', 'PE', 'GO', 'SC', 'PA', 'CE', 'MT', 'PI', 'PB', 'AM', 'MS', 'RN', 'TO', 'ES', 'AC', 'AL', 'RO', 'SE', 'RR', 'AP', 'DF'],
    'escolas': [4056, 2527, 1637, 1192, 1186, 1023, 895, 828, 769, 768, 746, 714, 548, 526, 495, 432, 339, 337, 326, 316, 270, 254, 214, 206, 167, 136, 109],
    'alunado medio': [1564118, 633929, 346223, 301636, 434869, 458710, 267084, 301399, 192889, 229595, 294563, 327385, 123668, 115382, 119569, 180514, 93108, 109759, 61844, 110931, 37942, 105517, 66321, 71638, 26367, 29810, 85626]
}

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Tabela estilizada
st.markdown("<h3 style='color: black;'>Tabela de Escolas e Alunado Médio por Estado (UF)</h3>", unsafe_allow_html=True)
st.dataframe(df.style.format({"alunado medio": "{:,.0f}", "escolas": "{:,.0f}"}), hide_index=True)


# Gráficos de barras
st.markdown("<h3 style='color: black;'>Alunado Ensino Médio por UF</h3>", unsafe_allow_html=True)
st.bar_chart(df.set_index('uf')['alunado medio'])  

st.markdown("<h3 style='color: black;'>Escolas com Ensino Médio por UF</h3>", unsafe_allow_html=True)
st.bar_chart(df.set_index('uf')['escolas'])

