import os

import pandas as pd
import numpy as np


def split_data(df: pd.DataFrame) -> pd.DataFrame:
    df["technologies"] = df[
        "technologies"
    ].apply(lambda x: x.split(', ') if pd.notna(x) else [])
    df["location"] = df[
        "location"
    ].apply(lambda x: x.split(', ') if pd.notna(x) else [])
    return df


def clean_technologies(df: pd.DataFrame) -> pd.DataFrame:
    df["location"] = df["location"].apply(lambda x: np.nan if len(str(x)) > 50 else x)


def clean_data(filename: str) -> pd.DataFrame:
    if os.path.exists(filename):
        df = pd.read_csv(filename)
    else:
        raise FileNotFoundError("File hasn't been found. You should scrape it first")

    df.replace("N/A", np.nan, inplace=True)
    df = split_data(df)
    clean_technologies(df)
    return df


