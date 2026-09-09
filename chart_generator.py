import pandas as pd

from config import OUTPUT_FILE


def generate_excel_report(
    results_df,
    score_global,
    rating_info,
    history_scores
):

    with pd.ExcelWriter(
        OUTPUT_FILE,
        engine="xlsxwriter"
    ) as writer:

        results_df.to_excel(
            writer,
            sheet_name="Scoring",
            index=False
        )

        synthese = pd.DataFrame([
            {
                "Score Global": round(score_global, 4),
                "Rating": rating_info["rating"],
                "Description": rating_info["description"]
            }
        ])

        synthese.to_excel(
            writer,
            sheet_name="Notation",
            index=False
        )

        historique = pd.DataFrame({
            "Periode": list(history_scores.keys()),
            "Score": list(history_scores.values())
        })

        historique.to_excel(
            writer,
            sheet_name="Historique",
            index=False
        )

    return OUTPUT_FILE
