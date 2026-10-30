import matplotlib.pyplot as plt #type: ignore
import pandas as pd #type: ignore
import streamlit as pd_st #type: ignore
import streamlit as st #type: ignore


st.set_page_config(page_title="Análise de Dispersão", layout="centered")

st.title("Relação entre Altura, Peso e Sexo")


try:
    df = pd.read_csv("dados_dispersao.csv")
    df.columns = df.columns.str.strip()
    df["altura_cm"] = pd.to_numeric(
        df["altura_cm"].astype(str).str.strip(), errors="coerce"
    )
    df["peso_kg"] = pd.to_numeric(
        df["peso_kg"].astype(str).str.strip(), errors="coerce"
    )
    df["sexo"] = df["sexo"].astype(str).str.strip().str.upper()
    df = df.dropna(subset=["altura_cm", 'peso_kg', "sexo"])

    cores_mapeamento = {
        "M": "#1f77b4",
        "MASCULINO": "#1f77b4",
        "F": "#e377c2",
        "FEMININO": "#e377c2",
    }

    
    fig, ax = plt.subplots(figsize=(10, 6))

    for sexo_grupo, dados_grupo in df.groupby("sexo"):
        cor = cores_mapeamento.get(sexo_grupo, "#7f7f7f")
        ax.scatter(
            dados_grupo["altura_cm"],
            dados_grupo["peso_kg"],
            label=sexo_grupo,
            color=cor,
            s=100,
            alpha=0.75,
            edgecolors="black",
        )

   
    ax.set_title("Relação entre Altura, Peso e Sexo", fontsize=14, fontweight="bold")
    ax.set_xlabel("Altura (cm)", fontsize=12)
    ax.set_ylabel("Peso (kg)", fontsize=12)
    ax.legend(title="Sexo", fontsize=10, title_fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()

    
    st.pyplot(fig)

    plt.close(fig)

    if st.checkbox("Mostrar tabela de dados tratados"):
        st.dataframe(df)

except FileNotFoundError:
    st.error(
        "O arquivo **dados_dispersao.csv** não foi encontrado no mesmo diretório do script."
    )
