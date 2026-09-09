import streamlit as st
import pandas as pd

from scoring import calculate_scores
from rating import (
    get_rating_details,
    get_trend
)

from trend_analysis import (
    calculate_historical_scores
)

from report_generator import (
    generate_excel_report
)

from pdf_generator import (
    generate_pdf_report
)

from chart_generator import (
    generate_score_chart
)

# =====================================================
# CONFIGURATION PAGE
# =====================================================

st.set_page_config(
    page_title="Z-Score Quantitative Scoring",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

# =====================================================
# HEADER
# =====================================================

st.title("📈 Application de Calcul de Z-Score")

st.markdown("""
Cette application permet :

- Calcul des Z-Scores
- Calcul du Score Quantitatif Global
- Attribution d'un Rating
- Analyse de Tendance
- Génération Excel
- Génération PDF
""")

# =====================================================
# BARRE D'ACTIONS
# =====================================================

col1, col2, col3 = st.columns([1, 1, 2])

with col1:

    reset_clicked = st.button(
        "🔄 Réinitialiser",
        use_container_width=True
    )

with col2:

    st.empty()

with col3:

    st.empty()

if reset_clicked:

    st.session_state.reset_counter += 1

    st.rerun()

# =====================================================
# UPLOAD FICHIER
# =====================================================

uploaded_file = st.file_uploader(
    "Charger le fichier Excel",
    type=["xlsx"],
    key=f"uploader_{st.session_state.reset_counter}"
)

# =====================================================
# TRAITEMENT
# =====================================================

if uploaded_file is not None:

    try:

        # ============================================
        # CALCUL PRINCIPAL
        # ============================================

        results_df, score_global = calculate_scores(
            uploaded_file
        )

        rating_info = get_rating_details(
            score_global
        )

        # ============================================
        # RELECTURE DU FICHIER
        # ============================================

        uploaded_file.seek(0)

        source_df = pd.read_excel(
            uploaded_file
        )

        # ============================================
        # HISTORIQUE
        # ============================================

        historical_scores = (
            calculate_historical_scores(
                source_df
            )
        )

        # ============================================
        # TREND
        # ============================================

        trend = "N/A"
        variation = 0

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

        # ============================================
        # KPI
        # ============================================

        st.success(
            "Calcul effectué avec succès"
        )

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        with kpi1:

            st.metric(
                "Score Global",
                f"{score_global:.2f}"
            )

        with kpi2:

            st.metric(
                "Rating",
                rating_info["rating"]
            )

        with kpi3:

            st.metric(
                "Variation",
                f"{variation:.2f}"
            )

        with kpi4:

            st.metric(
                "Tendance",
                trend
            )

        # ============================================
        # DESCRIPTION RATING
        # ============================================

        st.subheader("Notation")

        st.info(
            rating_info["description"]
        )

        # ============================================
        # RESULTATS DETAILLES
        # ============================================

        st.subheader(
            "Résultats détaillés"
        )

        display_cols = [

            "KPI",
            "Poids %",
            "Moyenne",
            "Ecart-Type",
            "Z-Score",
            "Sens",
            "Z Ajusté",
            "Score Pondéré"

        ]

        available_cols = [

            col
            for col in display_cols
            if col in results_df.columns

        ]

        st.dataframe(
            results_df[available_cols],
            use_container_width=True
        )

        # ============================================
        # HISTORIQUE SCORES
        # ============================================

        st.subheader(
            "Historique des Scores"
        )

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

        # ============================================
        # GRAPHIQUE EVOLUTION
        # ============================================

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

        # ============================================
