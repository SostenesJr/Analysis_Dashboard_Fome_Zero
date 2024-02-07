import pandas as pd

# Renomeação das colunas 
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: ifn.titleize(x)
    snakecase = lambda x: ifn.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

# adicionando a coluna Countries
def country_name(country_id):
    COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}
    return COUNTRIES[country_id]

# tipo de comida
def create_price_type(price_range):
    if price_range == 1:
        return "Cheap"
    elif price_range == 2:
        return "Normal"
    elif price_range == 3:
        return "Expensive"
    else:
        return "Gourmet"
    
# criando uma coluna so com cores pelo tipo de codigo
def color_name(color_code):
    COLORS = {
    "3F7E00": "Darkgreen",
    "5BA829": "Green",
    "9ACD32": "Lightgreen",
    "CDD614": "Orange",
    "FFBA00": "Red",
    "CBCBC8": "Darkred",
    "FF7800": "Darkred",
}
    return COLORS[color_code]

# removendo colunas que so tem um valor
def remove_columns(df):
    if df['switch_to_order_menu'].nunique() == 1:
        # Remover a coluna
        df = df.drop(columns=['switch_to_order_menu'])
        print("A coluna foi removida.")
    else:
        print("A coluna não contém apenas um valor.")        
    return df

# codigo geral de limpeza do dataframe
def Clean_code(dataframe):
    df = rename_columns(dataframe)
    df = remove_columns(df)
    df1 = df.copy()  
    # tirando valores duplicados
    df1 = df1.drop_duplicates()
    # tirando o NaN dessa coluna
    df1['cuisines'] = df1['cuisines'].fillna(0)
    # criando uma nova coluna a parti do country_code
    df1['countries'] = df1['country_code'].apply(country_name)
    # criando uma nova coluna a parti do price_range
    df1['type_food'] = df1['price_range'].apply(create_price_type)
    # criando uma nova coluna a parti de rating_clor
    df1['color'] = df1['rating_color'].apply(color_name)
    # transformando o tipo cuisines para str
    df1['cuisines'] = df1['cuisines'].astype(str)
    # removendo as palavras exeto a primeira da coluna cuisines
    df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0]) 
    return df1 
