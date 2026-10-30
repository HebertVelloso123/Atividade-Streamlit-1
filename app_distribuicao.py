import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import streamlit as st #type: ignore

st.set_page_config(page_title="Distribuição de Idade", layout="centered")

st.title("Análise de Clientes")


try:
    df = pd.read_csv("dados_distribuicao.csv")

    df.columns = df.columns.str.strip()
    df["cliente_id"] = df["cliente_id"].astype(str).str.strip()
    df["idade"] = pd.to_numeric(
        df["idade"].astype(str).str.strip(), errors="coerce"
    )
    df = df.dropna(subset=["idade"])
    df_clientes_unicos = df.drop_duplicates(subset=["cliente_id"])

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(
        df_clientes_unicos["idade"],
        bins=15,
        color="mediumpurple",
        edgecolor="black",
        alpha=0.8,
    )

    ax.set_title("Distribuição de Idade dos Clientes")
    ax.set_xlabel("Idade (Anos)")
    ax.set_ylabel("Quantidade de Clientes")
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()

   
    st.pyplot(fig)

except FileNotFoundError:
    st.error(
        "O arquivo 'dados_distribuicao.csv' não foi encontrado. Verifique o caminho."
    )
