import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import seaborn as sns #type: ignore
import streamlit as st #type: ignore

st.set_page_config(page_title="Matriz de Movimento", layout="centered")

st.title("Análise de Fluxo")


def mostrar_heatmap_movimento():
    try:
        
        df = pd.read_csv("dados_heatmap.csv")

        df["dia_semana"] = df["dia_semana"].astype(str).str.strip()
        df["horario"] = df["horario"].astype(str).str.strip()

     
        ordem_dias = [
            "Segunda",
            "Terça",
            "Quarta",
            "Quinta",
            "Sexta",
            "Sábado",
            "Domingo",
        ]
        dias_presentes = [
            dia for dia in ordem_dias if dia in df["dia_semana"].unique()
        ]
        df["dia_semana"] = pd.Categorical(
            df["dia_semana"], categories=dias_presentes, ordered=True
        )

        
        df_pivot = df.pivot_table(
            index="horario",
            columns="dia_semana",
            values="movimento_clientes",
            aggfunc="mean",
        )

      
        fig, ax = plt.subplots(figsize=(10, 6))

        sns.heatmap(
            df_pivot,
            annot=True,
            fmt=".0f",
            cmap="coolwarm",
            linewidths=1,
            ax=ax,
        )

        
        ax.set_title(
            "Matriz de Movimento de Clientes por Dia e Horário",
            fontsize=14,
            fontweight="bold",
            pad=20,
        )
        ax.set_xlabel("Dia da Semana", fontsize=12)
        ax.set_ylabel("Horário", fontsize=12)

        plt.tight_layout()

      
        st.pyplot(fig)

    except FileNotFoundError:
        st.error(
            "O arquivo 'dados_heatmap.csv' não foi encontrado. Verifique o caminho."
        )

mostrar_heatmap_movimento()
