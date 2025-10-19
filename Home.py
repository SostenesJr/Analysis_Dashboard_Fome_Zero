# ==============================
# Configs
# ==============================
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Fome Zero Analytics", # Título mais descritivo
    page_icon="🍔", # Ícone de hambúrguer para representar comida
    layout="wide"
)

# Importando imagem
# Certifique-se de que 'fome_zero.jpg' está no mesmo diretório ou forneça o caminho correto
try:
    image = Image.open("fome_zero.jpg")
except FileNotFoundError:
    st.error("Erro: A imagem 'fome_zero.jpg' não foi encontrada. Por favor, verifique o caminho.")
    image = None # Define como None para evitar erros posteriores se a imagem não for encontrada

# ==============================
# Layout no Streamlit
# ==============================
# Sidebar
st.sidebar.image(image, width=240) # A imagem deve representar o Fome Zero ou o logo

st.sidebar.markdown("# 🍔 Fome Zero Analytics") # Título principal do projeto na sidebar
st.sidebar.markdown("### Insights Estratégicos para o Crescimento")

st.sidebar.markdown("""---""")

st.sidebar.markdown('#### Desenvolvido por:')
st.sidebar.markdown('##### Sostenes Jr. | Data Analyst')
st.sidebar.markdown('##### Powered by Comunidade DS')

# Conteúdo Principal
st.markdown("# 🚀 Bem-vindo ao Painel de Análise Fome Zero!")
st.markdown("### Descubra insights valiosos para impulsionar o sucesso da sua plataforma.")

st.markdown(
    """
    Este painel interativo foi cuidadosamente desenvolvido para oferecer uma **visão 360º dos dados do Fome Zero**,
    permitindo uma compreensão aprofundada das métricas e tendências em diversas dimensões.
    Navegue pelas seções para explorar análises detalhadas sobre culinárias, restaurantes, cidades e países.

    ---

    ### 🧭 Como Navegar no Painel?

    Utilize o menu lateral (sidebar) para alternar entre as diferentes visões de análise:

    * **Visão Geral:** Explore as principais métricas e indicadores de performance do Fome Zero de forma consolidada.
        Ideal para ter uma rápida compreensão do panorama geral do negócio.

    * **Visão País:** Aprofunde-se na performance e características dos restaurantes e culinárias por país.
        Descubra onde estão as maiores concentrações de parceiros, as melhores avaliações e as tendências de preços.

    * **Visão Cidade:** Analise o cenário gastronômico a nível de cidade.
        Identifique as cidades com maior oferta de restaurantes, os que possuem as melhores notas e a disponibilidade de serviços como entrega e reservas.

    * **Visão Restaurantes:** Mergulhe nos detalhes dos estabelecimentos parceiros.
        Compare performances individuais, descubra os mais populares, os com as melhores avaliações e os valores médios de pratos para dois.

    * **Visão Culinária:** Entenda a popularidade e o desempenho dos diferentes tipos de culinária.
        Compare avaliações, preços e a adoção de serviços online para cada categoria gastronômica.

    ---

    ### ❓ Precisa de Ajuda ou Tem Sugestões?

    Estamos sempre abertos a feedback e colaboração!
    * **Time de Data Science (Discord):** @jrramos
    """
)
