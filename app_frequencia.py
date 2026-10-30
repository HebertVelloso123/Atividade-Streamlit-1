import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import streamlit as st #type: ignore

st.set_page_config(page_title="Frequência de Chamados", layout="centered")

st.title("Análise de Atendimentos")


def mostrar_grafico_frequencia():
    try:
        # Carrega e limpa os dados
        df = pd.read_csv("dados_frequencia.csv")
        df.columns = df.columns.str.strip()

        df = df.dropna(subset=["tipo_atendimento"])
        df["tipo_atendimento"] = df["tipo_atendimento"].astype(str).str.strip()

        # Faz a contagem dos tipos de atendimento
        contagem_atendimentos = df["tipo_atendimento"].value_counts()

        # Cria a figura explicitamente para o Streamlit
        fig, ax = plt.subplots(figsize=(10, 6))

        # Cores da paleta viridis que você escolheu
        cores = ["#440154", "#3b528b", "#21918c", "#5ec962", "#fde725"]

        # Plota as barras diretamente no objeto 'ax'
        contagem_atendimentos.plot(
            kind="bar",
            color=cores[: len(contagem_atendimentos)],
            edgecolor="black",
            ax=ax,
        )

        # Configurações do gráfico
        ax.set_title(
            "Quantidade de Chamados por Tipo de Atendimento",
            fontsize=14,
            fontweight="bold",
        )
        ax.set_xlabel("Tipo de Atendimento", fontsize=12)
        ax.set_ylabel("Quantidade de Chamados", fontsize=12)

        # Rotaciona os nomes do eixo X para ficarem retos (horizontal)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

        # Adiciona a grade de fundo
        ax.grid(axis="y", linestyle="--", alpha=0.5)

        # Adiciona os rótulos de dados (números) no topo de cada barra
        for p in ax.patches:
            height = p.get_height()
            if height > 0:
                ax.annotate(
                    f"{int(height)}",
                    (p.get_x() + p.get_width() / 2.0, height),
                    ha="center",
                    va="bottom",
                    xytext=(0, 5),
                    textcoords="offset points",
                    fontsize=10,
                    fontweight="bold",
                )

        plt.tight_layout()

        # Exibe o gráfico na tela do Streamlit
        st.pyplot(fig)

    except FileNotFoundError:
        st.error(
            "O arquivo 'dados_frequencia.csv' não foi encontrado. Verifique o caminho."
        )


# Executa a função para renderizar a tela
mostrar_grafico_frequencia()
