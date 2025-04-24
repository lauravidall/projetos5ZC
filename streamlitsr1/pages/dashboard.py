import streamlit as st
import pandas as pd
from utils.charts import plot_donut, plot_pie, plot_barchart
from utils.mapa import plot_map
import plotly.graph_objects as go #

st.title("🏁 Dashboard F1")

# Carregando os dados 
df = pd.read_csv("data/races.csv", parse_dates=["date"])

# Filtros
anos_disponiveis = sorted(df["date"].dt.year.unique())
ano_selecionado = st.selectbox("Selecione o ano", anos_disponiveis, index=0)

meses_disponiveis = ["Todos"] + list(range(1, 13))
mes_selecionado = st.selectbox("Selecione o mês (1-12)", meses_disponiveis)

# Filtragem
df_filtrado = df[df["date"].dt.year == ano_selecionado]

if mes_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["date"].dt.month == mes_selecionado]

# Layout de colunas: 2 colunas para os gráficos lado a lado (esquerda donut direita bar)
col1, col2 = st.columns(2)

# Coluna 1: Donut
with col1:
    st.subheader("Países Sede")
    plot_donut(df_filtrado)

# Coluna 2: Bar
with col2:
    st.subheader("Tempos dos Pilotos na Corrida (GP de Mônaco 2023)")
    plot_barchart()

# Tabela de Corridas
st.subheader("Tabela de Corridas")
st.dataframe(df_filtrado.reset_index(drop=True))

# Mapa dos países sede
st.subheader("Mapa dos países sede")
plot_map(df_filtrado)
