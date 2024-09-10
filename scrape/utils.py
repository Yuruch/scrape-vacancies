def proces_salary(salary: str):
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
