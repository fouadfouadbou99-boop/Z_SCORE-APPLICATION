import streamlit as st
import pandas as pd

from scoring import calculate_scores
from rating import get_rating_details, get_trend
from trend_analysis import calculate_historical_scores
from report_generator import generate_excel_report
from pdf_generator import generate_pdf_report
from chart_generator import generate_score_chart

# =====================================================
# CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Z-Score Quantitative Scoring",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# SESSION
# =====================================================

if "reset_counter" not in st.session_state:
    st.session_state["reset_counter"] = 0

# =====================================================
# TITRE
# =====================================================

st.title("📈 Application de Calcul de Z-Score")

st.markdown("""
Cette application permet de :

- Calculer les Z-Scores
- Calculer le Score Quantitatif Global
- Attribuer un Rating
- Analyser la tendance
- Générer un rapport Excel
- Générer un rapport PDF
""")

# =====================================================
# ACTIONS
# =====================================================

col1, col2 = st.columns([1, 4])

with col1:

    if st.button("🔄 Réinitialiser"):

        st.session_state["reset_counter"] += 1
        st.rerun()

# =====================================================
# UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "Charger le fichier Excel",
    type=["xlsx"],
    key=f"upload_{st.session_state['reset_counter']}"
)

# =====================================================
# ANALYSE
# =====================================================

if uploaded_file:

    try:

        # -------------------------------------------------
        # Calcul principal
        # -------------------------------------------------

        results_df, score_global = calculate_scores(
            uploaded_file
        )

        rating_info = get_rating_details(
            score_global
        )

        # -------------------------------------------------
        # Relecture du fichier
        # -------------------------------------------------

        uploaded_file.seek(0)

        source_df = pd.read_excel(
            uploaded_file
        )

        # -------------------------------------------------
        # Historique
        # -------------------------------------------------

        historical_scores = calculate_historical_scores(
            source_df
        )

        variation = 0.0
        trend = "N/A"

        if (
            "N" in historical_scores
            and "N-1" in historical_scores
        ):

            variation = (
                historical_scores["N"]
                - historical_scores["N-1"]
            )

            trend = get_trend(
                historical_scores["N"],
                historical_scores["N-1"]
            )

        # -------------------------------------------------
        # KPI
        # -------------------------------------------------

        st.success("Fichier traité avec succès")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Score Global",
                f"{score_global:.2f}"
            )

        with c2:
            st.metric(
                "Rating",
                rating_info["rating"]
            )

        with c3:
            st.metric(
                "Variation",
                f"{variation:.2f}"
            )

        with c4:
            st.metric(
                "Tendance",
                trend
            )

        # -------------------------------------------------
        # Description
        # -------------------------------------------------

        st.subheader("Notation")

        st.info(
            rating_info["description"]
        )

        # -------------------------------------------------
        # Tableau détaillé
        # -------------------------------------------------

        st.subheader("Résultats détaillés")

        columns_to_show = [
            "KPI",
            "Poids %",
            "Moyenne",
            "Ecart-Type",
            "Z-Score",
            "Sens",
            "Z Ajusté",
            "Score Pondéré"
        ]

        existing_columns = [

            col
            for col in columns_to_show
            if col in results_df.columns

        ]

        st.dataframe(
            results_df[existing_columns],
            use_container_width=True
        )

        # -------------------------------------------------
        # Historique
        # -------------------------------------------------

        st.subheader("Historique des Scores")

        hist_df = pd.DataFrame({

            "Période":
                list(historical_scores.keys()),

            "Score":
                [
                    round(x, 4)
                    for x in historical_scores.values()
                ]
        })

        st.dataframe(
            hist_df,
            use_container_width=True
        )

        # -------------------------------------------------
        # Graphique
        # -------------------------------------------------

        chart_path = generate_score_chart(
            historical_scores,
            "outputs/evolution_score.png"
        )

        st.subheader(
            "Evolution du Score Quantitatif"
        )

        st.image(
            chart_path,
            use_container_width=True
        )

        # -------------------------------------------------
        # Rapport Excel
        # -------------------------------------------------

        excel_path = generate_excel_report(
            results_df=results_df,
            score_global=score_global,
            rating_info=rating_info,
            history_scores=historical_scores
        )

        # -------------------------------------------------
        # Rapport PDF
        # -------------------------------------------------

        pdf_path = generate_pdf_report(
            results_df=results_df,
            score_global=score_global,
            rating_info=rating_info,
            history_scores=historical_scores,
            chart_path=chart_path
        )

        # -------------------------------------------------
        # Téléchargements
        # -------------------------------------------------

        st.subheader("Téléchargement")

        d1, d2 = st.columns(2)

        with d1:

            with open(excel_path, "rb") as f:

                st.download_button(
                    label="📊 Télécharger Excel",
                    data=f,
                    file_name="rapport_zscore.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

        with d2:

            with open(pdf_path, "rb") as f:

                st.download_button(
                    label="📄 Télécharger PDF",
                    data=f,
                    file_name="rapport_zscore.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        # -------------------------------------------------
        # Synthèse
        # -------------------------------------------------

        st.subheader("Synthèse")

        st.markdown(
            f"""
### Résultat

- **Score Quantitatif :** {score_global:.2f}
- **Rating :** {rating_info['rating']}
- **Tendance :** {trend}
- **Variation :** {variation:.2f}

**Commentaire**

{rating_info['description']}
"""
        )

    except Exception as e:

        st.error(
            f"Erreur durant le traitement : {str(e)}"
        )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Application de scoring quantitatif basée sur la méthode Z-Score"
)
