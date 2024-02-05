import requests
import pandas as pd
import time
from datetime import date

lang = ["Python", "Java", "C++", "JavaScript", "PHP", "Ruby", "JavaScript", "C#", "Swift", "Go", "Rust",
        "TypeScript", "Kotlin", "Perl", "R", "Objective-C", "MATLAB", "HTML", "CSS", "SQL", "GIT",
        "Bash", "React", "Vue.js", "Aurora OS", "Аврора ОС"]


def parse_zarplata_ru_vacancies(page, text):
    url = "https://api.zarplata.ru/vacancies"


    params = {
            "text": text,
            "per_page": 100,
            "area": 1,
            "page": page,
            'premium': 'true'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        vacancies = response.json()["items"]

        data = list(map(parse_vacancy, vacancies))
        return data

    else:
        # print(response)
        print("Error occurred while fetching data from API.")
        return None


def parse_vacancy(vacancy):
    title = vacancy["name"]
    skills = get_job_description(vacancy) or ""
    salary_from = vacancy["salary"]["from"] if vacancy.get("salary") and vacancy["salary"].get("from") else ""
    salary_to = vacancy["salary"]["to"] if vacancy.get("salary") and vacancy["salary"].get("to") else ""
    schedule = vacancy["schedule"]["name"] if vacancy.get("schedule") else ""
    experience = vacancy["experience"]["name"] if vacancy.get("experience") else ""
    city = vacancy["area"]["name"] if vacancy.get("area") else ""
    employer = vacancy["employer"]["name"] if vacancy.get("employer") else ""

    return title, skills, salary_from, salary_to, schedule, experience, city, employer


def get_job_description(vacancy):
    return vacancy['snippet']['requirement']


if __name__ == "__main__":
    data = []
    for i in range(len(lang)):
        for page in range(0, 200):
            vacancies_data = parse_zarplata_ru_vacancies(page, lang[i])
            if vacancies_data:
                data += vacancies_data
            else:
                print("Парсинг закончен на странице", page)
                break
        df = pd.DataFrame(data,
                            columns=["Название вакансии", "Ключевые навыки", "Начальная зарплата", "Конечная зарплата",
                                        "График работы", "Требуемый опыт", "Город", "Работодатель"])
        df.to_excel(f"vacancies_{lang[i]}_{date.today()}.xlsx", index=False)
        print("Excel файл создан успешно.")
        data = []
        time.sleep(3)
