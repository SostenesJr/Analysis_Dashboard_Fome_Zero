# ==============================
# Bibliotecas
# ==============================

import streamlit as st
from PIL import Image
import pandas as pd
import limpeza as lp
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

st.header('Visão Restaurantes')
st.header(":orange[Dataframe]")
st.dataframe(df1)

st.sidebar.markdown('# :orange[Filtros]')
paises = df1['countries'].unique()

# Filtros
paises = list(df1['countries'].unique())
country_opitions = st.sidebar.multiselect('Escolha os países que deseja visualizar os restaurante:', paises, default=['Brazil', 'India', 'United States of America', 'England', 'South Africa'])

linhas = df1['countries'].isin(country_opitions)
df1 = df1.loc[linhas, :]

# Número de restaurantes - Slider
num_slider = st.sidebar.slider('Selecione a quantidade de Restaurantes que deseja visualizar', value=25,
                 min_value=0,
                 max_value=50)


# Tipos de culinária
culinarias = list (df1['cuisines'].unique())
culinarias_options = st.sidebar.multiselect(
    ':orange[Escolha os tipos de culinária que deseja visualizar:]', culinarias)

linhas = df1['cuisines'].isin(culinarias_options)
df_culinaria = df1.loc[linhas, :]


st.sidebar.markdown ('##### :orange[Powered by Comunidade DS]')
st.sidebar.markdown ('###### :orange[Data Analyst: Sostenes Jr]') 

st.header(':orange[Fome Zero Restaurantes!]')
st.subheader('O Melhor lugar para encontrar o melhor restaurante ou o pior!', divider='red')

st.subheader('Temos as seguintes metricas e graficos dentro da nossa plataforma:')

with st.container():
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        # Selecionando restaurantes com a cozinha 'Italian'
        df_aux = ul.melhor_restaurante(df1,'Italian')
        st.metric(':green[Italiana:] ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
    
    with col2:
        # Selecionando restaurantes com a cozinha 'Brazilian'
        df_aux = ul.melhor_restaurante(df1, 'Brazilian')
        st.metric('Brasileira: ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
    
    with col3:
        # Selecionando restaurantes com a cozinha 'American'
        df_aux = ul.melhor_restaurante(df1, 'American')
        st.metric(':green[Americana:] ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
        
    with col4:
        # Selecionando restaurantes com a cozinha 'Japanese'
        df_aux = ul.melhor_restaurante(df1, 'Japanese')
        st.metric(':green[Japonesa:] ' + str(df_aux.iloc[0, 1]), value=df_aux.iloc[0, 2])
        
    with col5:
        # Selecionando restaurantes com a cozinha 'Indian'
        df_aux = ul.melhor_restaurante(df1,'Indian')
        st.metric(':green[Indiana:] ' + str(df_aux.iloc[0, 1])  , value=df_aux.iloc[0, 2])
          
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Top 10 melhores tipos de culinárias
        df_aux = df1.loc[:, ['cuisines', 'aggregate_rating']].groupby('cuisines').mean().sort_values('aggregate_rating', ascending = False).reset_index().head(num_slider)
        
        df_aux.columns = ['Culinárias', 'Nota']
        
        fig = ul.bar_chart(df_aux, 'Culinárias','Nota','','Top '+ str(num_slider) +  ' melhores tipos de culinária', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
    with col2:
        # Top 10 piores tipos de culinárias
        df_aux = df1.loc[:, ['cuisines', 'aggregate_rating']].groupby('cuisines').mean().sort_values('aggregate_rating', ascending = True).reset_index().head(num_slider)
        
        df_aux.columns = ['Culinárias', 'Nota']
        
        fig = ul.bar_chart(df_aux, 'Culinárias','Nota','','Top '+ str(num_slider) +  ' piores tipos de culinária', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
        
with st.container():
    
    st.header(':orange[As] '+ str(num_slider) +  ' :orange[culinárias mais ofertadas]')
    st.subheader(':orange[Quantidades de tipos de culinária]')
    
    contagem = df1[['cuisines', 'restaurant_id']].groupby('cuisines').count().sort_values('restaurant_id', ascending = False).reset_index().head(num_slider)
    contagem.columns=['Gastronomia', 'Qt. Restaurantes']

    fig = px.funnel(contagem, x='Qt. Restaurantes', y='Gastronomia', color='Gastronomia', template='seaborn')
    fig.update(layout_showlegend=False)

    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
with st.container():
    st.header(':orange[Top] '+ str(num_slider) +  ' :orange[restaurantes]')
    
    df_culinaria = df_culinaria.sort_values(['aggregate_rating', 'restaurant_id'], ascending = False).head(num_slider)
    
    df_culinaria = df_culinaria.drop(['address', 'locality', 'longitude', 'latitude', 'currency', 'has_table_booking', 'has_online_delivery', 'is_delivering_now', 'price_range', 'rating_color', 'rating_text'], axis=1)
    
    st.dataframe(df_culinaria, use_container_width= True)
