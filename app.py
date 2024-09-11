import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(layout='wide',
                   page_icon=':book:',
                   page_title='PNLD - Ensino Médio',
                   initial_sidebar_state='expanded',
                   )
st.markdown("<h1 style='text-align: center; color: darkblue;'>PNLD - Ensino Médio</h1>", unsafe_allow_html=True)
st.title('PNLD - Ensino Médio')

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
st.markdown("<h3 style='color: darkblue;'>Tabela de Escolas e Alunado Médio por Estado (UF)</h3>", unsafe_allow_html=True)
st.dataframe(df.style.format({"alunado medio": "{:,.0f}", "escolas": "{:,.0f}"}), hide_index=True)




# Exibir a tabela no Streamlit
st.subheader('Tabela de Escolas e Alunado Médio por Estado (UF)')
st.dataframe(df, hide_index=True)

# Gráficos de barras
st.markdown("<h3 style='color: darkblue;'>Alunado Médio por UF</h3>", unsafe_allow_html=True)
st.bar_chart(df.set_index('uf')['alunado medio'])

st.markdown("<h3 style='color: darkblue;'>Escolas por UF</h3>", unsafe_allow_html=True)
st.bar_chart(df.set_index('uf')['escolas'])

# Gráfico combinado com dois eixos y
st.markdown("<h3 style='color: darkblue;'>Comparação de Escolas e Alunado Médio por UF</h3>", unsafe_allow_html=True)
fig, ax1 = plt.subplots(figsize=(12, 6))

# Eixo y1 para o número de escolas
ax1.bar(df['uf'], df['escolas'], color='lightblue', label='Escolas')
ax1.set_xlabel('UF', fontsize=12)
ax1.set_ylabel('Número de Escolas', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.tick_params(axis='x', rotation=45)

# Segundo eixo y para o alunado médio
ax2 = ax1.twinx()
ax2.plot(df['uf'], df['alunado medio'], color='darkred', marker='o', label='Alunado Médio', linewidth=2)
ax2.set_ylabel('Alunado Médio', color='darkred', fontsize=12)
ax2.tick_params(axis='y', labelcolor='darkred')

# Ajustar legendas e título
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.set_title('Comparação de Escolas e Alunado Médio por UF', fontsize=14, fontweight='bold')

# Exibir o gráfico no Streamlit
st.pyplot(fig)