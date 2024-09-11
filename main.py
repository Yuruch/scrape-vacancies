import asyncio

from scrape.run import main as scrape_main
from data_analysis.run import main as data_analysis_main

if __name__ == "__main__":
    scrape_main()
    data_analysis_main()
