import pandas as pd
import numpy as np


def calculate_historical_scores(df):

    history_cols = [
        c for c in df.columns
        if c.startswith("N-")
    ]

    history_cols = sorted(
        history_cols,
        reverse=True
    )

    scores = {}

    for year_col in history_cols + ["N"]:

        temp = df.copy()

        hist_used = [
            c for c in history_cols
            if c != year_col
        ]

        if len(hist_used) < 3:
            continue

        temp["Moyenne"] = (
            temp[hist_used]
            .mean(axis=1)
        )

        temp["Ecart-Type"] = (
            temp[hist_used]
            .std(axis=1, ddof=0)
        )

        temp["Z"] = (
            temp[year_col]
            - temp["Moyenne"]
        ) / temp["Ecart-Type"]

        temp["Z Ajusté"] = temp.apply(

            lambda row:
            -row["Z"]
            if str(row["Sens"]).lower() == "bas"
            else row["Z"],

            axis=1
        )

        temp["Score"] = (
            temp["Poids %"]
            * temp["Z Ajusté"]
        )

        score_global = (
            temp["Score"].sum()
            / temp["Poids %"].sum()
        )

        scores[year_col] = score_global

    return scores
