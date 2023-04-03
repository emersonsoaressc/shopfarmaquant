import streamlit as st 
import pandas as pd
from main import extrai_dados_preco_popular, extrai_dados_saojoao, extrai_dados_paguemenos, extrai_dados_raia

data = pd.read_excel("rx.xls")

input_ean = str(st.text_input("Digite o EAN do medicamento"))
if input_ean != "":
    try:
        preco_pp = extrai_dados_preco_popular(input_ean)
    except:
        preco_pp = "0,00"
    try:
        preco_saojoao = extrai_dados_saojoao(input_ean)
    except:
        preco_saojoao = "0,00"
    try:
        preco_raia = extrai_dados_raia(input_ean)
    except:
        preco_raia = "0,00"
    try:
        preco_paguemenos = extrai_dados_paguemenos(input_ean)
    except:
        preco_paguemenos = "0,00"   
else:
    preco_pp = "Digite o EAN do medicamento"


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("image\logo_pp.png", width=100)
    st.write(f"R$ {str(float(preco_pp[2])).replace('.', ',')}")
with col2:
    st.image("image\logo_saojoao.png", width=100)
    st.write(f"R$ {str(float(preco_saojoao[2])).replace('.', ',')}")
with col3:
    st.image("image\logo_paguemenos.png", width=100)
    st.write(f"R$ {str(float(preco_paguemenos[2])).replace('.', ',')}")
with col4:
    st.image("image\logo_raia.png", width=100)
    st.write(f"R$ {str(float(preco_raia[2])).replace('.', ',')}")



