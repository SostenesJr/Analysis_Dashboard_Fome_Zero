# ==============================
# Bibliotecas
# ==============================

import streamlit as st
import folium as fl
from PIL import Image
import pandas as pd
import limpeza as lp
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import utilites as ul
import plotly.express as px

# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title="Home",
    page_icon=":cityscape:", 
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

st.header('Visão Cidades')
st.header(":orange[Dataframe]")
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

st.subheader('Temos os seguintes gráficos dentro da nossa plataforma:')

# ==============================
# Visão Cidades
# ==============================

with st.container():
    # Top 10 cidades com mais restaurantes na base de dados
    df_aux = (df1.loc[:, ['countries','city', 'restaurant_id']].groupby(['countries', 'city'])
                                                                .nunique()
                                                                .sort_values(by='restaurant_id', ascending = False)
                                                                .reset_index())

    paises = list (df1['countries'].unique())
    df_final = pd.DataFrame()
    
    for pais in paises:
        df_aux1 = df_aux.loc[df_aux['countries'] == pais, :].head(1)
        df_final = pd.concat([df_final, df_aux1], ignore_index= True)
 
    df_final.columns = ['Pais', 'Cidade', 'Restaurantes']
    df_final = df_final.sort_values('Restaurantes', ascending=False).reset_index(drop= True)
    fig = ul.bar_chart(df_final, 'Cidade', 'Restaurantes', 'Pais', 'Cidade de cada país com mais restaurantes cadastrados', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Top 10 Cidades com Restaurantes com média de avaliação maior que 4
        df_aux = (df1.loc[df1['aggregate_rating'] > 4, ['countries','city', 'restaurant_id']].groupby(['countries', 'city'])
                                                                                              .nunique().sort_values(by='restaurant_id', ascending = False)
                                                                                              .reset_index()
                                                                                              .head(10))
        df_aux.columns = ['País', 'Cidade', 'Restaurantes']
        fig = ul.bar_chart(df_aux, 'Cidade', 'Restaurantes', 'País', 'Top 10 Cidades com Restaurantes com média de avaliação maior que 4', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
    with col2:
        # Top 10 Cidades com Restaurantes com média de avaliação menor que 2.5
        df_aux = (df1.loc[df1['aggregate_rating'] < 2.5, ['countries','city', 'restaurant_id']].groupby(['countries', 'city'])
                                                                                              .nunique().sort_values(by='restaurant_id', ascending = False)
                                                                                              .reset_index()
                                                                                              .head(10))
        df_aux.columns = ['País', 'Cidade', 'Restaurantes']
        fig = ul.bar_chart(df_aux, 'Cidade', 'Restaurantes', 'País', 'Top 10 Cidades com Restaurantes com média de avaliação menor que 2.5', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
with st.container():
    # Top 10 cidades com mais restaurantes com tipos de culinária distintos
    df_aux = (df1.loc[:, ['countries', 'city', 'cuisines']].groupby(['countries','city'])
                                                            .nunique()
                                                            .sort_values(by='cuisines', ascending = False)
                                                            .reset_index()
                                                            .head(10))
    df_aux.columns = ['País', 'Cidade', 'Restaurantes']
    fig = ul.bar_chart(df_aux, 'Cidade', 'Restaurantes', 'País', 'Top 10 cidades com mais restaurantes com tipos de culinária distintos', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
    
with st.container():
    # Coluna Experimental - Treemapgraph
    st.markdown('#### Restaurantes por Cidade: ')
    st.markdown('###### Quantidade de Restaurantes por Cidade')
    
    fig = px.pie(df_final, values='Restaurantes', names='Cidade')
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
