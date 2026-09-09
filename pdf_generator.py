"""
Génération du rapport PDF de notation
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

PDF_OUTPUT_FILE = "outputs/rapport_zscore.pdf"


def generate_pdf_report(
    results_df,
    score_global,
    rating_info
):

    doc = SimpleDocTemplate(
        PDF_OUTPUT_FILE,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    # Titre

    elements.append(
        Paragraph(
            "Rapport de Scoring Quantitatif",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # Informations générales

    elements.append(
        Paragraph(
            f"Date : {datetime.now().strftime('%d/%m/%Y')}",
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
            f"Notation : {rating_info['rating']}",
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

    # Tableau KPI

    table_data = [[
        "KPI",
        "Poids",
        "Z Ajusté",
        "Score Pondéré"
    ]]

    for _, row in results_df.iterrows():

        table_data.append([

            str(row["KPI"]),
            round(row["Poids %"], 2),
            round(row["Z Ajusté"], 2),
            round(row["Score Pondéré"], 2)

        ])

    table = Table(table_data)

    table.setStyle(
        TableStyle([

            ('BACKGROUND', (0, 0), (-1, 0),
             colors.darkblue),

            ('TEXTCOLOR', (0, 0), (-1, 0),
             colors.white),

            ('GRID', (0, 0), (-1, -1),
             1, colors.black),

            ('FONTNAME', (0, 0), (-1, 0),
             'Helvetica-Bold'),

            ('BACKGROUND', (0, 1), (-1, -1),
             colors.
