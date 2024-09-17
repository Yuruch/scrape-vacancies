import numpy as np
import pandas as pd


def get_counts_by_name(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    if col_name not in df.columns:
        raise ValueError(f"Column '{col_name}' not found in DataFrame")
    df = df[col_name].explode().value_counts()
    return df.head(30)


def get_min_salary_by_level(df: pd.DataFrame) -> pd.DataFrame:
    salary_counts = df.groupby(
        ["level", "min_salary"]
    ).size().unstack(fill_value=np.nan)
    return salary_counts


def get_experience_count_df(df):
    experience_counts = df.groupby(
        ["level", "experience"]
    ).size().reset_index(name="count")

    experience_counts["experience_summary"] = experience_counts.apply(
        lambda x: f"{x['level']} - {x['experience']} ({x['count']})", axis=1
    )

    experience_summary_df = experience_counts.pivot(
        index="level", columns="experience", values="count"
    ).fillna(0).astype(int)

    return experience_summary_df
