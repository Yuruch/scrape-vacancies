import pandas as pd
import matplotlib.pyplot as plt


def get_count_plot(df: pd.DataFrame, name: str) -> None:
    plt.figure(figsize=(12, 6))
    df.plot(kind="bar")
    plt.xticks(rotation=90)
    plt.ylabel("Count")
    plt.title(f"{name} Counts")
    plt.tight_layout()
    plt.savefig(f"./result_plots/{name}_plot.png")
    plt.close()


def get_salaries_by_level_plots(df: pd.DataFrame) -> None:
    for level in df.index:
        data = df.loc[level]
        data = data[data > 0]

        if not data.empty:
            ax = data.plot.pie(
                autopct=lambda p: "{:.1f}%".format(p) if p > 0 else "",
                startangle=90,
                counterclock=False,
                title=f"Salary Distribution for {level} Level"
            )
            ax.set_ylabel("")
            plt.tight_layout()
            plt.savefig(f"./result_plots/{level}_min_salary_plot.png")
            plt.close()


def plot_experience_distribution(df):
    levels = df.index

    for level in levels:
        level_df = df.loc[level]
        experience_counts = level_df[level_df > 0]

        if not experience_counts.empty:
            plt.figure(figsize=(8, 6))
            plt.pie(
                experience_counts,
                labels=experience_counts.index,
                autopct="%1.1f%%",
                startangle=140
            )
            plt.title(f"Experience Distribution for {level}")
            plt.savefig(f"./result_plots/{level}_experience_distribution_plot.png")
            plt.close()

