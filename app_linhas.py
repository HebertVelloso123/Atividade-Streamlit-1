import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import streamlit as st #type: ignore

st.set_page_config(page_title="Comparativo de Vendas", layout="centered")

st.title("Análise de Desempenho")


def mostrar_grafico_linhas():
    try:
       
        df = pd.read_csv("dados_linhas.csv")

   
        df["data"] = pd.to_datetime(df["data"])

        df_pivot = df.pivot(index="data", columns="loja", values="vendas")

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            df_pivot.index,
            df_pivot["Loja A"],
            marker="o",
            label="Loja A",
            color="blue",
        )
        ax.plot(
            df_pivot.index,
            df_pivot["Loja B"],
            marker="s",
            label="Loja B",
            color="orange",
        )

        
        ax.set_title(
            "Comparativo de Vendas Diárias - Janeiro 2026",
            fontsize=14,
            fontweight="bold",
        )
        ax.set_xlabel("Data", fontsize=12)
        ax.set_ylabel("Vendas ($)", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.5)

        
        ax.legend()

      
        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

    except FileNotFoundError:
        st.error(
            "O arquivo 'dados_linhas.csv' não foi encontrado. Verifique o caminho."
        )


# Executa a função para exibir a tela
mostrar_grafico_linhas()
