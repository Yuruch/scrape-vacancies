import asyncio

from scrape.config import CATEGORIES_URLS
from scrape.scraper import DouJobScraper

if __name__ == "__main__":
    for category, url in CATEGORIES_URLS.items():
        scraper = DouJobScraper(base_url=url)
        asyncio.run(scraper.scrape_jobs())
