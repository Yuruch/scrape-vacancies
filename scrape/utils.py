from typing import Tuple


def process_salary(salary: str) -> Tuple[str, str]:
    min_salary = "N/A"
    max_salary = "N/A"

    if salary == "N/A":
        return min_salary, max_salary

    salary = salary.replace("$", "")
    salary = salary.replace("–", " ")

    if "від" in salary:
        salary = salary.replace("від", "")
        min_salary = salary
    elif "до" in salary:
        salary = salary.replace("до", "")
        max_salary = salary
    else:
        min_salary, max_salary = tuple(salary.split())

    return min_salary, max_salary


def process_level(title: str, levels: set) -> str:
    title_upper = title.upper()
    matching_levels = {level for level in levels if level in title_upper}
    return matching_levels.pop() if matching_levels else "N/A"


def process_technologies(description: str, technologies: list) -> list:
    if description != "N/A":
        found_technologies = [tech for tech in technologies if tech.lower() in description.lower()]
    else:
        found_technologies = []
