# ==============================
# Bibliotecas
# ==============================

import streamlit as st
from PIL import Image
import pandas as pd
import limpeza as lp
import utilites as ul



# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title="Home",
    page_icon=":earth_americas:", 
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

st.header(':red[Visão Pais]')
st.header(":orange[Dataframe]")
st.dataframe(df1)

st.sidebar.markdown('# :orange[Filtros]')
paises = df1['countries'].unique()

# Filtros
paises = list(df1['countries'].unique())
country_opitions = st.sidebar.multiselect(':blue[Escolha os países que deseja visualizar os restaurante:]', paises, default=['Brazil', 'India', 'United States of America', 'England', 'South Africa'])

linhas = df1['countries'].isin(country_opitions)
df1 = df1.loc[linhas, :]

st.sidebar.markdown ('##### :orange[Powered by Comunidade DS]')
st.sidebar.markdown ('###### :orange[Data Analyst: Sostenes Jr]') 

st.header(':orange[Fome Zero Restaurantes!]')
st.subheader(':blue[O Melhor lugar para encontrar o melhor restaurante ou o pior!]', divider='red')

st.subheader(':blue[Temos os seguintes graficos dentro da nossa plataforma:]')

with st.container():
    # Coluna Experimental - Treemapgraph
    st.markdown('#### :orange[Diversidade Gastronômica: ]')
    st.markdown('###### :orange[Quantidade de culinárias únicas por país]')
    contagem = df1[['countries','cuisines']].groupby('countries').nunique().sort_values('cuisines', ascending = False).reset_index()
    contagem.columns=['País','Culinárias']

    fig = ul.treemap_graph(contagem, path='País', value='Culinárias', color='Culinárias')
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    st.markdown('###### :orange[Treemap Graph]')

with st.container():
    # Restaurantes por país
    df_aux = (df1.loc[:, ['countries', 'restaurant_id']].groupby('countries')
                                                         .nunique()
                                                         .sort_values(by='restaurant_id',ascending = False )
                                                         .reset_index())
    df_aux.columns = ['País', 'Num. Restaurantes']
    df_aux_mundi = df_aux.copy()
    fig = ul.bar_chart(df_aux, 'País', 'Num. Restaurantes', 'País', 'Quantidade de Restaurantes registrados por país', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
with st.container():
    # Cidade por país
    df_aux = (df1.loc[:, ['countries', 'city']].groupby('countries')
                                                .nunique()
                                                .sort_values(by='city',ascending = False)
                                                .reset_index())
    df_aux.columns = ['País', 'Num. Cidades']
    
    fig = ul.bar_chart(df_aux, 'País', 'Num. Cidades', 'País', 'Quantidade de Cidades registradas por país', True)
    st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        # Média de avaliações feitas por país
        df_aux = (df1.loc[:, ['countries', 'votes']].groupby('countries')
                                                     .sum()
                                                     .sort_values(by='votes', ascending = False)
                                                     .reset_index())
        df_aux.columns = ['Países', 'Quantidade de Avaliações']
        df_aux = df_aux.head(7)
        fig = ul.bar_chart(df_aux, 'Países', 'Quantidade de Avaliações', 'Países', 'Quantidade de avaliações por país', False)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
    with col2:
        # Média de preço de prato por duas pessoas por país
        df_aux = (df1.loc[:, ['countries', 'average_cost_for_two']].groupby('countries')
                                                                    .mean()
                                                                    .sort_values(by='average_cost_for_two', ascending = False)
                                                                    .reset_index())
        df_aux.columns = ['Países', 'Prato para 2 pessoas']
        df_aux = df_aux.head(7)
        
        fig = ul.bar_chart(df_aux, 'Países', 'Prato para 2 pessoas', 'Países', 'Média de preço de prato para duas pessoas por país', True)
        st.plotly_chart(fig, use_container_width = True, theme='streamlit')
