import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('PNLD - Ensino Médio')

st.write("Escolas do Brasil")



col1, col2, col3 = st.columns(3)
col1.metric("Alunado EM", "6.690.396")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

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
st.dataframe(df, hide_index=True)

# Exibir um gráfico de barras 
st.subheader('Alunado Médio por UF')
st.bar_chart(df.set_index('uf')['alunado medio'])

# Exibir um gráfico de barras 
st.subheader('Escolas com Médio por UF')
st.bar_chart(df.set_index('uf')['escolas'])


# Criar um gráfico com dois eixos y (um para escolas e outro para alunado médio)
st.subheader('Gráfico de Barras - Escolas e Alunado Médio por UF')

fig, ax1 = plt.subplots(figsize=(10, 6))

# Eixo y1 para o número de escolas
ax1.bar(df['uf'], df['escolas'], color='b', label='Escolas')
ax1.set_xlabel('UF')
ax1.set_ylabel('Número de Escolas', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Criar um segundo eixo y (compartilhando o mesmo eixo x)
ax2 = ax1.twinx()
ax2.plot(df['uf'], df['alunado medio'], color='r', marker='o', label='Alunado Médio')
ax2.set_ylabel('Alunado Médio', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Exibir a legenda
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)