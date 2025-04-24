import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def plot_donut(df):
    if df.empty:
        st.write("Sem dados para o período.")
        return
    data = df["country"].value_counts().reset_index()
    data.columns = ["country", "count"]
    fig = px.pie(data, names="country", values="count", hole=0.5)
    st.plotly_chart(fig, use_container_width=True)

def plot_pie(df):
    if df.empty:
        st.write("Sem dados para o período.")
        return
    data = df["country"].value_counts().reset_index()
    data.columns = ["country", "count"]
    fig = px.pie(data, names="country", values="count")
    st.plotly_chart(fig, use_container_width=True)

def plot_barchart():
    # Carregar dados do CSV
    df_times = pd.read_csv('data/monaco.csv')

    if df_times.empty:
        st.write("Sem dados.")
        return

    # Converter tempo
    def time_to_seconds(time_str):
        hours, minutes, rest = time_str.split(':')
        seconds, milliseconds = rest.split('.')
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000

    df_times['time_seconds'] = df_times['time'].apply(time_to_seconds)

    # Cores para equipes
    team_colors = {
        'Ferrari': 'red',
        'Mercedes': 'green',
        'Red Bull': 'blue',
        'Aston Martin': 'darkgreen',
        'Alpine': 'lightblue',
        'McLaren': 'orange',
        'AlphaTauri': 'lightblue',
        'Alfa Romeo': 'darkred',
        'Haas': 'gray',
        'Williams': 'lightyellow'
    }

    # Criar o gráfico
    fig = go.Figure()

    # Adicionar barras horizontais para cada piloto
    for team in df_times['team'].unique():
        team_df = df_times[df_times['team'] == team]
        fig.add_trace(go.Bar(
            y=team_df['driver'],
            x=team_df['time_seconds'],
            name=team,
            orientation='h',
            marker=dict(color=team_colors[team]),
            hovertemplate='<b>%{y}</b><br>Tempo: %{customdata[0]}<extra></extra>',
            customdata=team_df[['time']].values  # Passa o tempo original para o hover
        ))

    # Ajustes no layout
    fig.update_layout(
        xaxis_title="Tempo (segundos)",
        yaxis_title="Piloto",
        barmode='stack',
        template="plotly_dark",
        showlegend=True,
        height=600,
        margin=dict(l=150)
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)