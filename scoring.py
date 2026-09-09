import pandas as pd
import numpy as np

HISTORY_COLUMNS = [
    "N-5",
    "N-4",
    "N-3",
    "N-2",
    "N-1"
]

def calculate_scores(df):

    valid_cols = [
        c for c in HISTORY_COLUMNS
        if c in df.columns
    ]

    if len(valid_cols) < 3:
        raise ValueError(
            "Au moins 3 années historiques sont requises"
        )

    df["Moyenne"] = df[valid_cols].mean(axis=1)

    df["Ecart-Type"] = (
        df[valid_cols]
        .std(axis=1, ddof=0)
    )

    df["Z-Score"] = (
        df["N"] - df["Moyenne"]
    ) / df["Ecart-Type"]

    def adjust(row):

        if row["Sens"].lower() == "bas":
            return -row["Z-Score"]

        return row["Z-Score"]

    df["Z Ajusté"] = df.apply(
        adjust,
        axis=1
    )

    df["Score Pondéré"] = (
        df["Poids %"]
        * df["Z Ajusté"]
    )

    score_global = (
        df["Score Pondéré"].sum()
        / df["Poids %"].sum()
    )

    return df, score_global
