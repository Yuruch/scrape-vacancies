import asyncio

from scrape.scraper import scrape_with_experience

if __name__ == "__main__":
    asyncio.run(scrape_with_experience())
