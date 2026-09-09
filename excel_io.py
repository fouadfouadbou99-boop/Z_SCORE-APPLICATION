import pandas as pd

def read_excel(file):

    return pd.read_excel(file)


def save_excel(df, path):

    df.to_excel(
        path,
        index=False
    )
