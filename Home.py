# ==============================
# Bibliotecas
# ==============================
import streamlit as st
from PIL import Image

# ==============================
# Configs
# ==============================
st.set_page_config(
    page_title="Home",
    page_icon=":bank:"
    , layout= "wide"
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

st.sidebar.markdown ('##### :orange[Powered by Comunidade DS]')
st.sidebar.markdown ('###### :orange[Data Analyst: Sostenes Jr]') 

st.write("# Análise detalhada sobre os dados da companhia fome Zero")

st.markdown(
    """
    ### :blue[O Painel analítico Fome Zero foi construido para acamponhar as metricas de culinarias por regiâo, pais, cidade e restaurantes:]
    ####  :blue[Como utilizar esses Painel de avaliações?]
    #### - :blue[Visão Geral:]
        - Analíse feita de modo geral onde aborda informação importantes de modo amplo.  
    #### - :blue[Visão Pais:]
        - Analíse feita de modo espefico quantidade, qualidade, preço e avaliações por cada pais.
    #### - :blue[Visão Cidade:]
        - Analíse feita de modo espefico quantidade, qualidade, preço e avaliações por cada cidade.
    #### - :blue[Visão Restaurantes:]
        - Analíse feita de modo espefico quantidade, qualidade, preço e avaliações por cada restaurante.
    #### - :blue[Visão Culinaria:]
        - Analíse feita de modo espefico quantidade, qualidade, preço e avaliações por cada tipo de culinaria.
    
      
    #### :orange[Ask for Help]
    - :orange[Time de Data Science no Discord
        @jrramos
    """
)
