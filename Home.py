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

st.sidebar.markdown('## :orange[Projeto de Análise de Dados]')

st.sidebar.markdown("""---""")

st.sidebar.markdown ('##### :orange[Powered by Comunidade DS]')
st.sidebar.markdown ('###### :orange[Data Analyst: Sostenes Jr]') 

st.write("# Análise detalhada sobre os dados da companhia fome Zero")

st.markdown(
    """
    ### :orange[O Painel analítico Fome Zero foi construido para acamponhar as métricas de culinárias por regiâo, país, cidade e restaurantes:]
    ####  :orange[Como utilizar esses Painel de avaliações?]
    #### - :orange[Visão Geral:]
        - Analíse feita de modo geral onde aborda informação importantes de modo amplo.  
    #### - :orange[Visão País:]
        - Analíse feita de modo específico quantidade, qualidade, preço e avaliações por cada país.
    #### - :orange[Visão Cidade:]
        - Analíse feita de modo específico quantidade, qualidade, preço e avaliações por cada cidade.
    #### - :orange[Visão Restaurantes:]
        - Analíse feita de modo específico quantidade, qualidade, preço e avaliações por cada restaurante.
    #### - :orange[Visão Culinária:]
        - Analíse feita de modo específico quantidade, qualidade, preço e avaliações por cada tipo de culinária.
    
      
    #### :orange[Ask for Help]
    - :orange[Time de Data Science no Discord] 
        @jrramos
    """
)
