import asyncio
from typing import List

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, Page
from tqdm.asyncio import tqdm

from config import CATEGORIES_URLS, LEVELS, TECHNOLOGIES, EXPERIENCE
from scrape.file_handler import FileWriter
from scrape.utils import ProcessingData


class DouJobScraper:
    def __init__(
        self,
        base_url: str,
        experience: str,
        category: str,
        browser
    ) -> None:
        self.base_url = base_url
        self.experience = experience
        self.category = category
        self.browser = browser

    async def load_page(self, page):
        await page.goto(self.base_url)
        await asyncio.sleep(3)

    async def click_show_more(self, page: Page) -> None:
        while True:
            try:
                more_btn_div = await page.wait_for_selector(
                    ".more-btn", timeout=100
                )
                show_more_link = await more_btn_div.query_selector("a")

                if show_more_link:
                    await show_more_link.click()
                    await asyncio.sleep(1)
            except Exception:
                break

    async def scrape_jobs(self) -> list:
        page = await self.browser.new_page()
        try:
            await self.load_page(page)
            await self.click_show_more(page)

            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")
            job_listings = await self.parse_job_listings(soup)
        except Exception as e:
            print(f"Error during scraping: {e}")
            job_listings = []
        finally:
            await page.close()
        return job_listings

    async def parse_job_listings(self, soup: BeautifulSoup) -> List[dict]:
        job_listings = []
        jobs = soup.find_all("li", class_="l-vacancy")

        print(f"Found {len(jobs)} jobs")

        async def process_job(job) -> dict:
            title_tag = job.find("a", class_="vt")
            title = title_tag.text if title_tag else "N/A"
            level = ProcessingData.process_level(title, LEVELS)
            link = title_tag["href"] if title_tag else "N/A"

            company_tag = job.find("a", class_="company")
            company = company_tag.text if company_tag else "N/A"

            salary = job.find(
                "span", class_="salary"
            ).text if job.find("span", class_="salary") else "N/A"
            min_salary, max_salary = ProcessingData.process_salary(
                salary.replace("\xa0", "")
            )

            location_tag = job.find("span", class_="cities")
            location = location_tag.text.strip() if location_tag else "N/A"
            description = await self.fetch_job_technologies(link)
            technologies = ProcessingData.process_technologies(
                description, TECHNOLOGIES
            )

            return {
                "title": title.replace("\xa0", ""),
                "level": level,
                "company": company.replace("\xa0", ""),
                "experience": self.experience,
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

        return job_listings

    async def fetch_job_technologies(self, job_link: str) -> str:
        page = await self.browser.new_page()
        try:
            await page.goto(job_link, timeout=50000)
            await page.wait_for_load_state(timeout=50000)

            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")

            tech_tag = soup.find("div", class_="b-typo vacancy-section")
            description = tech_tag.text if tech_tag else "N/A"

        except Exception as e:
            print(f"Error fetching technologies for {job_link}: {e}")
            description = ""
        finally:
            await page.close()

        return description.replace("\xa0", "")


async def scrape_with_experience() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for category, base_url in CATEGORIES_URLS.items():
            jobs = []
            for experience in EXPERIENCE:
                url = f"{base_url}&exp={experience}"
                print(f"Scraping {url}")
                scraper = DouJobScraper(
                    base_url=url,
                    experience=experience,
                    category=category,
                    browser=browser
                )
                scraped_jobs = await scraper.scrape_jobs()
                jobs.extend(scraped_jobs)
            FileWriter.write_csv(data=jobs, category=category)
        await browser.close()
