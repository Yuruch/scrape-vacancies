import asyncio
import csv
from datetime import datetime
from typing import List

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from tqdm.asyncio import tqdm

from scrape.config import CATEGORIES_URLS, LEVELS, TECHNOLOGIES
from scrape.utils import process_salary, process_level, process_technologies


class DouJobScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def load_page(self, page):
        await page.goto(self.base_url)
        await asyncio.sleep(3)

    async def click_show_more(self, page):
        while True:
            try:
                more_btn_div = await page.wait_for_selector(
                    ".more-btn", timeout=100
                )
                show_more_link = await more_btn_div.query_selector("a")

                if show_more_link:
                    await show_more_link.click()
                    await asyncio.sleep(1)
            except Exception as e:
                break

    async def scrape_jobs(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                await self.load_page(page)
                await self.click_show_more(page)

                content = await page.content()
                soup = BeautifulSoup(content, "html.parser")
                job_listings = await self.parse_job_listings(soup, browser)
            except Exception as e:
                print(f"Error during scraping: {e}")
                job_listings = []
            finally:
                await page.close()
                await browser.close()

            self.save_to_csv(job_listings)

    async def parse_job_listings(self, soup, browser) -> List[dict]:
        job_listings = []
        jobs = soup.find_all("li", class_="l-vacancy")

        print(f"Found {len(jobs)} jobs")

        async def process_job(job):
            title_tag = job.find("a", class_="vt")
            title = title_tag.text if title_tag else "N/A"
            level = process_level(title, LEVELS)
            link = title_tag["href"] if title_tag else "N/A"

            company_tag = job.find("a", class_="company")
            company = company_tag.text if company_tag else "N/A"

            salary = job.find(
                "span", class_="salary"
            ).text if job.find("span", class_="salary") else "N/A"
            min_salary, max_salary = process_salary(
                salary.replace("\xa0", "")
            )

            location_tag = job.find("span", class_="cities")
            location = location_tag.text.strip() if location_tag else "N/A"

            technologies = await self.fetch_job_technologies(link, browser)
            return {
                "title": title.replace("\xa0", ""),
                "level": level,
                "company": company.replace("\xa0", ""),
                "min_salary": min_salary,
                "max_salary": max_salary,
                "location": location.replace("\xa0", ""),
                "link": link.replace("\xa0", ""),
                "technologies": technologies
            }

        tasks = [process_job(job) for job in jobs]
        async for job in tqdm(
                asyncio.as_completed(tasks),
                total=len(tasks),
                desc="Processing jobs"
        ):
            job_listings.append(await job)

        print(len(job_listings))
        return job_listings

    async def fetch_job_technologies(self, job_link: str, browser) -> list:
        page = await browser.new_page()
        try:
            await page.goto(job_link, timeout=50000)
            await page.wait_for_load_state(timeout=50000)

            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")

            tech_tag = soup.find("div", class_="b-typo vacancy-section")
            description = tech_tag.text if tech_tag else "N/A"
            found_technologies = process_technologies(description, TECHNOLOGIES)
        except Exception as e:
            print(f"Error fetching technologies for {job_link}: {e}")
            found_technologies = []
        finally:
            await page.close()

        return found_technologies

    def save_to_csv(self, job_listings):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"jobs-{timestamp}.csv"

        with open(filename, mode="w", newline="") as file:
            fieldnames = [
                "title",
                "level",
                "company",
                "min_salary",
                "max_salary",
                "location",
                "link",
                "technologies"
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for job in tqdm(job_listings, desc="Saving jobs to CSV"):
                writer.writerow(job)


if __name__ == "__main__":
    for category, url in CATEGORIES_URLS.items():
        scraper = DouJobScraper(base_url=url)
        asyncio.run(scraper.scrape_jobs())
