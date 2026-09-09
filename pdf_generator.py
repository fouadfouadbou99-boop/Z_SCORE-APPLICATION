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

    doc = SimpleDocTemplate(
        PDF_OUTPUT_FILE,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Rapport de Scoring Quantitatif",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

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
            f"Rating : {rating_info['rating']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            rating_info["description"],
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    table_data = [[
        "KPI",
        "Poids %",
        "Z Ajuste",
        "Score Pondere"
    ]]

    for _, row in results_df.iterrows():

        table_data.append([
            str(row["KPI"]),
            round(float(row["Poids %"]), 2),
            round(float(row["Z Ajusté"]), 2),
            round(float(row["Score Pondéré"]), 2)
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

    elements.append(PageBreak())

    elements.append(
        Paragraph(
            "Historique des Scores",
            styles["Heading1"]
        )
    )

    hist_data = [["Periode", "Score"]]

    for period, score in history_scores.items():

        hist_data.append([
            str(period),
            round(float(score), 2)
        ])

    hist_table = Table(hist_data)

    hist_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            )
        ])
    )

    elements.append(hist_table)

    elements.append(Spacer(1, 20))

    try:

        elements.append(
            Image(
                chart_path,
                width=450,
                height=250
            )
        )

    except Exception:
        pass

    doc.build(elements)

    return PDF_OUTPUT_FILE
