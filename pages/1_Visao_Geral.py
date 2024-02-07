import streamlit as st
import folium as fl
from PIL import Image
import pandas as pd
import limpeza as lp
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static


# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title="Home",
    page_icon=":world_map:", 
    layout='wide'
)

#importando imagem
image = Image.open(r"fome_zero.jpg")
# ==============================
# Layout no Streamlit
# ==============================
# Vizualização da imagem
st.sidebar.image(image, width =240)

st.sidebar.header(":orange[Fome Zero]")

st.sidebar.markdown('## :orange[Projeto de Análise de dados]')

st.sidebar.markdown("""---""")

# Importando Dataset
dataframe = pd.read_csv('zomato.csv')
df1 = lp.Clean_code(dataframe)

st.header(':orange[Visão Geral]')
st.header("Dataframe")
st.dataframe(df1)

st.sidebar.markdown('# :orange[Filtros]')
paises = df1['countries'].unique()

# Filtros
paises = list(df1['countries'].unique())
country_opitions = st.sidebar.multiselect('Escolha os países que deseja visualizar os restaurante:', paises, default=['Brazil', 'India', 'United States of America', 'England', 'South Africa'])

linhas = df1['countries'].isin(country_opitions)
df1 = df1.loc[linhas, :]

st.sidebar.markdown ('##### :orange[Powered by Comunidade DS]')
st.sidebar.markdown ('###### :orange[Data Analyst: Sostenes Jr]') 

st.header(':orange[Fome Zero Restaurantes!]')
st.subheader('O Melhor lugar para encontrar o melhor restaurante ou o pior!', divider='red')

st.subheader('Temos as seguintes métricas dentro da nossa plataforma')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        # Quantos restaurantes únicos estão registrados
        vl_uni = df1['restaurant_name'].nunique()
        col1.metric(':green[Restaurantes Cadastrado]', vl_uni, "quantidade")
    with col2:
        vl_countries = df1['countries'].nunique()
        col2.metric(':green[Países Cadastrados]', vl_countries, "quantidade")
    with col3:
        vl_city = df1['city'].nunique()
        col3.metric(':green[Cidades Cadastradas]', vl_city, "quantidade")
    with col4:
        vl_ranting = df1['aggregate_rating'].count()
        col4.metric(':green[Total de Avaliações Feitas]', vl_ranting, "quantidade")   
    with col5:
        vl_type = df1['cuisines'].nunique()
        col5.metric(':green[Culinárias Cadastradas]', vl_type, "quantidade")
with st.container():
    # Linha 2 - Mapa Mundi 
    st.subheader(':orange[Aqui está um mapa mundial mostrando os restaurantes cadastrados. Explore manualmente para ver informações como tipo de comida, avaliações e localização!]')
    with st.container():
        datamap = df1[['restaurant_name', 'longitude', 'latitude', 'cuisines', 'average_cost_for_two', 'currency', 'aggregate_rating', 'rating_color']].reset_index(drop = True)
        
        # Criando mapa com folium
        map = folium.Map(zoom_start = 20)
        cluster = MarkerCluster().add_to(map)
        
        icon = 'fa-cutlery'
        
        for index, location_info in datamap.iterrows():
            folium.Marker([location_info['latitude'],       
                        location_info['longitude']],
                        icon = folium.Icon(color=location_info['rating_color'], icon=icon, prefix='fa'),
                        popup = folium.Popup(f"""<h5> <b> {location_info['restaurant_name']} </b> </h5> <br>
                                                Cozinha: {location_info['cuisines']} <br>
                                                Preço médio para dois: {location_info['average_cost_for_two']} ({location_info['currency']}) <br>
                                                Avaliação: {location_info['aggregate_rating']} / 5.0 <br> """,
                                                max_width= len(f"{location_info['restaurant_name']}")*20)).add_to(cluster)

        # Exibindo o mapa
        folium_static(map, width = 1024, height = 600)  
        



    
    
