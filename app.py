import streamlit as st 
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores, grafico_vendas_vendedores


# O arquivo 'app' sintetiza as informacoes e configura a forma de apresentacao da tela 
# principal, Titulo, abas, colunas e os graficos dentro do layout da pagina


st.set_page_config(layout='wide')

st.title("Manutencao LTQ - AGM:")

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),

)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)] # Se tiver algo no filtro, df recebe somento esse conteudo

aba1, aba2, aba3, aba4 = st.tabs(['Dataset', 'Receita', 'Vendedores','Mapa de Memoria SM'])
with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'RS' ))
        st.plotly_chart(grafico_map_estado, width='stretch')
        st.plotly_chart(grafico_rec_estado, width='stretch')
    with coluna2:
        st.metric('Quantidade de Vendas', format_number( df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, width='stretch')
        st.plotly_chart(grafico_rec_categoria, width='stretch')

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores)


