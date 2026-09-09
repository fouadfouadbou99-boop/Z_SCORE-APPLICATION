"""
pdf_generator.py
Génération du rapport PDF de notation
"""

from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet

from config import PDF_OUTPUT_FILE


def generate_pdf_report(
    results_df,
    score_global,
    rating_info,
    history_scores,
    chart_path
):
    """
    Génère le rapport PDF complet.
    """

    doc = SimpleDocTemplate(
        PDF_OUTPUT_FILE,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    # =====================================================
    # TITRE
    # =====================================================

    elements.append(
        Paragraph(
            "Rapport de Scoring Quantitatif",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # =====================================================
    # INFORMATIONS GENERALES
    # =====================================================

    elements.append(
        Paragraph(
            f"Date d'analyse : {datetime.now().strftime('%d/%m/%Y')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Score Global : {score_global:.2f}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Rating : {rating_info['rating']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Commentaire : {rating_info['description']}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    # =====================================================
    # TABLEAU KPI
    # =====================================================

    table_data = [[
        "KPI",
        "Poids %",
        "Z Ajusté",
        "Score Pondéré"
    ]]

    for _, row in results_df.iterrows():

        table_data.append([

            str(row["KPI"]),

            round(
                float(row["Poids %"]),
                2
            ),

            round(
                float(row["Z Ajusté"]),
                2
            ),

            round(
                float(row["Score Pondéré"]),
                2
            )
        ])

    table = Table(table_data)

    table.setStyle(

        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.darkblue
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                "BACKGROUND",
                (0, 1),
                (-1, -1),
                colors.whitesmoke
            )

        ])
    )

    elements.append(table)

    # =====================================================
    # PAGE SUIVANTE
    # =====================================================

    elements.append(PageBreak())

    elements.append(
        Paragraph(
            "Historique du Score",
            styles["Heading1"]
        )
    )

    # =====================================================
    # HISTORIQUE
    # =====================================================

    hist_data = [[
        "Période",
        "Score"
    ]]

    for period, score in history_scores.items
