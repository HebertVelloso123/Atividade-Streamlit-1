import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import streamlit as st #type: ignore

st.title("Distribuição Salarial por Departamento")

df = pd.read_csv("dados_boxplot.csv")

fig, ax = plt.subplots(figsize=(10, 6))

df.boxplot(column="salario", by="departamento", grid=True, ax=ax)
ax.set_title("Distribuição Salarial por Departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")

plt.suptitle("")

st.pyplot(fig)
