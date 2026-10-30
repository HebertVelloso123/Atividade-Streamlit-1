import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import streamlit as st #type: ignore


def abrir_barras():
    try:
    
        df = pd.read_csv("dados_barras.csv")

   
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.replace("vemdas", "vendas")
        df["categoria"] = df["categoria"].astype(str).str.strip()
        df["regiao"] = df["regiao"].astype(str).str.strip()

    
        coluna_vendas = (
            "vendas_medias" if "vendas_medias" in df.columns else "vendas_media"
        )

        df[coluna_vendas] = pd.to_numeric(
            df[coluna_vendas].astype(str).str.strip(), errors="coerce"
        )
        df = df.dropna(subset=[coluna_vendas])

        categorias = df["categoria"]
        valores = df[coluna_vendas]

        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(categorias, valores, color="skyblue", edgecolor="black")
        ax.set_title("Vendas por Categoria")
        ax.set_xlabel("Categoria")
        ax.set_ylabel("Vendas Médias")
        plt.tight_layout()

        
        st.pyplot(fig)

    except FileNotFoundError:
        st.error(
            "O arquivo 'dados_barras.csv' não foi encontrado. Certifique-se de que ele está na mesma pasta do script."
        )



st.title("Dashboard de Vendas")
st.write("Visualização das vendas médias por categoria.")

abrir_barras()
