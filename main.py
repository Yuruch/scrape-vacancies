import os

from config import RESULT_DIR
from scrape.run import main as scrape_main
from data_analysis.run import main as data_analysis_main


def main():
    if os.path.exists(os.path.join(RESULT_DIR, "Python_jobs.csv")):
        answer = input("Scraped data already exists. Do you want to overwrite it? (y/n)")
        if answer.lower() == "y":
            scrape_main()
    else:
        scrape_main()

    data_analysis_main()


if __name__ == "__main__":
    main()
