import streamlit as st
import pandas as pd

from scoring import calculate_scores

st.set_page_config(page_title="Z-Score Calculator")

st.title("Application de Calcul de Z-Score")

uploaded_file = st.file_uploader(
    "Charger le fichier Excel",
    type=["xlsx"]
)

if uploaded_file:

    try:

        df = pd.read_excel(uploaded_file)

        result_df, score_global = calculate_scores(df)

        st.success("Calcul terminé")

        st.dataframe(result_df)

        st.metric(
            "Score Quantitatif Global",
            round(score_global, 2)
        )

        output_file = "rapport_zscore.xlsx"

        result_df.to_excel(
            output_file,
            index=False
        )

        with open(output_file, "rb") as f:
            st.download_button(
                "Télécharger le rapport",
                f,
                file_name=output_file
            )

    except Exception as e:
        st.error(f"Erreur : {e}")
