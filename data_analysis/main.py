import os

from data_analysis.analyse import (
    get_min_salary_by_level,
    get_counts_by_name, get_experience_count_df,

)
from data_analysis.clean import clean_data
from data_analysis.plots import (
    get_salaries_by_level_plots,
    get_count_plot, plot_experience_distribution,

)


if __name__ == "__main__":
    if not os.path.exists("./result_plots"):
        os.makedirs("./result_plots")
    dataframe = clean_data("../results/Python_jobs.csv")

    tech_df = get_counts_by_name(dataframe, "technologies")
    locations_df = get_counts_by_name(dataframe, "location")
    companies_df = get_counts_by_name(dataframe, "company")
    experience_summary_df = get_experience_count_df(dataframe)
    min_salary_by_level_df = get_min_salary_by_level(dataframe)

    get_count_plot(tech_df, "Technologies")
    get_count_plot(locations_df, "Locations")
    get_count_plot(companies_df, "Companies")
    get_salaries_by_level_plots(min_salary_by_level_df)
    plot_experience_distribution(experience_summary_df)

