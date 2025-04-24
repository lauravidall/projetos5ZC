import streamlit as st
import pandas as pd
from utils.mapa import plot_map
from utils.charts import plot_donut, plot_pie, plot_barchart
from datetime import datetime

st.set_page_config(page_title="Sports Analytics - F1 Dashboard", page_icon="🏎️", layout="wide")

# Sidebar com filtros
st.sidebar.title("Filtros")
ano_selecionado = st.sidebar.selectbox("Escolha o Ano", options=[2025, 2024, 2023, "Todos"], index=0)
mes_selecionado = st.sidebar.selectbox("Escolha o Mês", options=["Todos", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], index=0)

# Carregar dados do races
@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/races.csv", parse_dates=["date"])
    return df

df = carregar_dados()

# Filtrando os dados com base no ano e mês
if ano_selecionado != "Todos":
    df = df[df["date"].dt.year == ano_selecionado]

if mes_selecionado != "Todos":
    df = df[df["date"].dt.month == mes_selecionado]

# Título principal
st.title("🏎️ Sports Analytics - F1 Dashboard")
st.markdown("**Analisando os países sede e dados de corridas de Fórmula 1**")

# Selecionar visualização
st.sidebar.header("Escolha a Visualização")
opcao_visualizacao = st.sidebar.radio(
    "Tipo de visualização", ["Mapa dos Países Sede", "Países Sede", "Tempo Pilotos Monaco"] #, "Gráfico de Pizza"
)

# Exibir o gráfico de acordo com a escolha
if opcao_visualizacao == "Mapa dos Países Sede":
    st.subheader("Mapa dos Países Sede")
    plot_map(df)

elif opcao_visualizacao == "Países Sede":
    st.subheader("Países Sede")
    plot_donut(df)

elif opcao_visualizacao == "Tempo Pilotos Monaco":
    st.subheader("Tempo Pilotos Monaco")
    plot_barchart()

#elif opcao_visualizacao == "Gráfico de Pizza":
#    st.subheader("Gráfico de Pizza")
#    plot_pie(df)

# Exibindo a tabela de corridas filtradas
st.subheader("Tabela de Corridas")
st.write(df[["race", "date", "country"]].sort_values("date"))
