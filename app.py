import streamlit as st 
import pandas as pd
from main import extrai_dados_preco_popular, extrai_dados_saojoao, extrai_dados_paguemenos, extrai_dados_raia

data = pd.read_excel("rx.xls")

input_ean = str(st.text_input("Digite o EAN do medicamento"))
if input_ean != "":
    try:
        preco_pp = extrai_dados_preco_popular(input_ean)
    except:
        preco_pp = ["0,00", "0,00", "0,00", 0.00]
    try:
        preco_saojoao = extrai_dados_saojoao(input_ean)
    except:
        preco_saojoao = ["0,00", "0,00", 0.00]
    try:
        preco_paguemenos = extrai_dados_paguemenos(input_ean)
    except:
        preco_paguemenos = ["0,00", "0,00", 0.00] 
    try:
        preco_raia = extrai_dados_raia(input_ean)
    except:
        preco_raia = ["0,00", "0,00", 0.00]  

    try:
        st.subheader(preco_pp[0])
    except:
        pass
    
    col_a1, col_a2, col_a3, col_a4 = st.columns(4)
    with col_a1:
        st.image("image/logo_pp.png", width=100)
        st.subheader(f"R$ {preco_pp[3]}")
    with col_a2:
        st.image("image/logo_saojoao.png", width=100)
        st.subheader(f"R$ {preco_saojoao[2]}")
    #col_b1, col_b2 = st.columns(2)
    #with col_b1:
    with col_a3:
        st.image("image/logo_paguemenos.png", width=100)
        st.subheader(f"R$ {preco_paguemenos[2]}")
    #with col_b2:
    with col_a4:
        st.image("image/logo_raia.png", width=100)
        st.subheader(f"R$ {preco_raia[2]}")
else:
    pass

