import asyncio

from scrape.scraper import scrape_with_experience


def main():
    asyncio.run(scrape_with_experience())


if __name__ == "__main__":
    main()
