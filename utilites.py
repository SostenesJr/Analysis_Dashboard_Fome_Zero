# ==============================
# Bibliotecas
# ==============================

from matplotlib import pyplot as plt
import plotly.express as px

def bar_chart(data, x, y, color, title, textauto):
    plt.figure(figsize = (20,15))
    fig = px.bar(data, x = x, y = y, color=color, text_auto=textauto, title = title, template='seaborn')
    return fig

def treemap_graph(data, path, value, color):
    
    fig = px.treemap(data, path=[path], values=value, color = color, color_continuous_scale = 'hot',
           template ='plotly_white')
    fig.data[0].texttemplate = "<b>%{label}</b><br>Qt. Culinárias: %{value}<br>"
    
    return fig

def bar_chart(data, x, y, color, title, textauto):
    if color:
        plt.figure(figsize = (20,15))
        fig = px.bar(data, x = x, y = y, color=color, text_auto=textauto, title = title, template='simple_white')
        return fig
    else:
        plt.figure(figsize = (20,15))
        fig = px.bar(data, x = x, y = y, text_auto=textauto, title = title, template='simple_white')
        return fig
    
def melhor_restaurante(df1, tipo):  
    linhas_selecionadas = (df1['cuisines'] == tipo)
    df_aux01 = (df1.loc[linhas_selecionadas, ['restaurant_id', 'aggregate_rating', 'restaurant_name']].groupby(['restaurant_id', 'restaurant_name'])
                                                                                                   .mean()
                                                                                                   .sort_values(by='aggregate_rating')
                                                                                                   .reset_index())
    maior_nota = df_aux01['aggregate_rating'].max()
    print(maior_nota)
    # Selecionando os que tem nota igual a maior
    linhas_selecionadas = (df_aux01['aggregate_rating'] == maior_nota)

    # Ordenando por ID
    df_aux01 = df_aux01.loc[linhas_selecionadas, :].sort_values(by='restaurant_id')

    return df_aux01    