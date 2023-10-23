from datetime import date

import requests
import pandas as pd
import time

lang = ["Python", "Java", "JavaScript", "PHP", "Ruby", "JavaScript", "C#", "Swift", "Go", "Rust",
        "TypeScript", "Kotlin", "Perl", "R", "Objective-C", "MATLAB", "HTML", "CSS", "SQL", "GIT",
        "Bash", "React", "Vue.js", "Aurora OS", "Аврора ОС"]


def parse_rabota_ru_vacancies(offset, text):
    url = "http://opendata.trudvsem.ru/api/v1/vacancies"

    params = {
        "text": text,
        "limit": 100,
        "offset": offset,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        vacancies = response.json()["results"]["vacancies"]
        data = list(map(parse_vacancy_rabota, vacancies))
        return data

    else:

        print("Error occurred while fetching data from API.")
        return None


def parse_vacancy_rabota(vacancies):
    for i in range(100):
        names_of_vacancies = vacancies[i]

        titles = names_of_vacancies["vacancy"]["job-name"]
        salary_from = names_of_vacancies["vacancy"]["salary_min"]
        salary_to = names_of_vacancies["vacancy"]["salary_max"]
        schedule = names_of_vacancies["vacancy"]["schedule"]
        experience = names_of_vacancies["vacancy"]["requirement"]["experience"]
        city = names_of_vacancies["vacancy"]["region"]["name"]
        employer = names_of_vacancies["vacancy"]["company"]["name"]

    if 'qualification' in names_of_vacancies['vacancy']['requirement']:
        skills = names_of_vacancies['vacancy']['requirement']['qualification']
        print(f"Номер {i + 1}", skills)
    else:
        skills = ''
        print(f"Номер {i + 1}", skills)

    return titles, skills, salary_from, salary_to, schedule, experience, city, employer


if __name__ == "__main__":
    data = []
    for i in range(len(lang)):
        for offset in range(0, 200):
            vacancies_data = parse_rabota_ru_vacancies(offset, lang[i])
            if vacancies_data:
                data += vacancies_data
            else:
                print("Парсинг закончен на странице", offset)
                break
        df = pd.DataFrame(data,
                          columns=["Название вакансии", "Ключевые навыки", "Начальная зарплата", "Конечная зарплата",
                                   "График работы", "Требуемый опыт", "Город", "Работодатель"])
        df.to_excel(f"vacancies_rabota_ru_{lang[i]}_{date.today()}.xlsx", index=False)
        print("Excel файл создан успешно.")
        data = []
        time.sleep(3)
