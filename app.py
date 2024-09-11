import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore
import plotly.express as px # type: ignore

st.title('PNLD - Ensino Médio')

st.write("Escolas do Brasil")

st.metric(label="Alunado EM", value="6.690.396")

st.metric(label="Professores EM", value="4508.317")

st.metric(label="Escolas EM", value="21.016")

st.metric(label="Municípios com EM", value="5.570")

st.metric(label="Estados com EM", value="27")


# 1. Carregar o arquivo Excel
@st.cache_data
def load_data():
    # Carrega o arquivo Excel (substitua pelo nome do seu arquivo)
    file_path = '20240910_PNLD.xlsx'
    data = pd.read_excel(file_path)
    return data

# Carregar os dados
df = load_data()

# Exibir o dataframe no Streamlit
st.subheader('Dados do Excel:')
st.dataframe(df)


