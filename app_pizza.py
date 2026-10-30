import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import streamlit as st #type: ignore

st.set_page_config(page_title="Faturamento por Canal", layout="centered")

st.title("Canais de Venda")


def mostrar_grafico_pizza():
    try:
    
        df = pd.read_csv("dados_pizza.csv")

        categorias = df["canal_venda"]
        valores = df["faturamento"]

    
        fig, ax = plt.subplots(figsize=(8, 8))

      
        ax.pie(
            valores,
            labels=categorias,
            autopct="%1.1f%%",
            startangle=140,
            colors=["red", "green", "yellow", "purple", "pink"],
        )

        ax.set_title(
            "Gráfico de pizza faturamento dos meios de comunicação",
            fontsize=16,
        )

        st.pyplot(fig)

    except FileNotFoundError:
        st.error(
            "O arquivo 'dados_pizza.csv' não foi encontrado. Verifique o caminho."
        )

mostrar_grafico_pizza()
