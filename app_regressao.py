import matplotlib.pyplot as plt #type: ignore
import numpy as np 
import pandas as pd #type: ignore
import seaborn as sns #type: ignore
import streamlit as st #type: ignore
from sklearn.linear_model import LinearRegression #type: ignore

st.set_page_config(page_title="Regressão Linear", layout="centered")

st.title("Análise de Regressão Linear")


def mostrar_regressao():
    try:
        # Carrega os dados
        df = pd.read_csv("dados_regressao.csv")

        # Limpeza e conversão dos dados
        df["gasto_mensal"] = pd.to_numeric(
            df["gasto_mensal"].astype(str).str.strip(), errors="coerce"
        )
        df["renda_mensal"] = pd.to_numeric(
            df["renda_mensal"].astype(str).str.strip(), errors="coerce"
        )

        df = df.dropna(subset=["gasto_mensal", "renda_mensal"])

        # Separa as variáveis e treina o modelo
        X = df[["gasto_mensal"]]
        y = df["renda_mensal"]

        modelo = LinearRegression()
        modelo.fit(X, y)

        # Gera a linha de tendência
        X_valores_linha = np.linspace(
            df["gasto_mensal"].min(), df["gasto_mensal"].max(), 100
        ).reshape(-1, 1)
        y_renda = modelo.predict(X_valores_linha)

        # --- Seção de Métricas do Modelo ---
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="Inclinação (Coeficiente Angular)",
                value=f"{modelo.coef_[0]:.4f}",
            )
        with col2:
            st.metric(
                label="Intercepto (Coeficiente Linear)",
                value=f"{modelo.intercept_:.2f}",
            )

        # --- Criação do Gráfico ---
        fig, ax = plt.subplots(figsize=(10, 6))

        # Dados Reais
        sns.scatterplot(
            data=df,
            x="gasto_mensal",
            y="renda_mensal",
            s=80,
            alpha=0.7,
            label="Dados Reais",
            ax=ax,
        )

        # Linha de Regressão
        ax.plot(
            X_valores_linha,
            y_renda,
            color="red",
            linewidth=3,
            label="Linha de Regressão",
        )

        # Configurações do gráfico
        ax.set_title(
            "Regressão Linear: Tendência de Renda Mensal por Gasto Mensal",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        ax.set_xlabel("Gasto Mensal", fontsize=12)
        ax.set_ylabel("Renda Mensal", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.5)

        # Ajusta legenda para funcionar bem no Streamlit
        ax.legend(loc="upper left")

        plt.tight_layout()

        # Renderiza no Streamlit
        st.pyplot(fig)

    except FileNotFoundError:
        st.error(
            "O arquivo 'dados_regressao.csv' não foi encontrado. Verifique o caminho."
        )


# Executa a função
mostrar_regressao()
