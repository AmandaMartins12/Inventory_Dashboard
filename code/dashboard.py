import streamlit as st
import pandas as pd

# Dados de exemplo 
data = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
    'Quantidade': [25, 12, 8, 3, 30],
    'Limite': [10, 15, 5, 2, 20]
}

df = pd.DataFrame(data)

# Filtrar itens abaixo do limite
low_stock = df[df['Quantidade'] < df['Limite']]

# Configurações do Streamlit
st.title('Dashboard de Estoque')
st.write('Dados detalhados do estoque e destaque para estoque abaixo do limite')

# Tabela de estoque
st.subheader('Estoque')
st.dataframe(df)

# Gráfico de estoque
st.subheader('Gráfico de Estoque')
chart_data = pd.DataFrame(df[['Produto', 'Quantidade']])
st.bar_chart(chart_data.set_index('Produto'))

# Itens com estoque abaixo do limite
st.subheader('Itens Abaixo do Limite')
st.dataframe(low_stock)

# Mensagem de destaque
st.warning(f"{len(low_stock)} itens estão abaixo do limite de estoque!")