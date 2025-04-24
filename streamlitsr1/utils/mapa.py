import plotly.express as px
import streamlit as st

def plot_map(df):
    if df.empty:
        st.write("Sem países para mostrar no mapa.")
        return

    # Agrupando os dados por país para contagem de corridas
    data = df["country"].value_counts().reset_index()
    data.columns = ["country", "count"]

    # Criando o mapa
    fig = px.choropleth(
        data,
        locations="country",
        locationmode="country names",
        color="count",
        color_continuous_scale="Reds",
        title="Países com corridas de F1"
    )

    # Ajuste do layout para fixar o tamanho do mapa e permitir zoom
    fig.update_geos(
        visible=True,
        projection_type="natural earth",
        showcountries=True,
        showcoastlines=True,
        showland=True,
        landcolor="white",
        coastlinecolor="black",
        countrycolor="black",
    )

    # Definindo o tamanho do gráfico e permitindo o zoom
    fig.update_layout(
        autosize=False,
        width=800,  
        height=600, 
        geo=dict(
            center=dict(lon=0, lat=0),
            projection_scale=1,
            showland=True,
            landcolor="white",
            subunitcolor="gray"
        ),
    )

    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

