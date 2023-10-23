from datetime import date

import requests
import pandas as pd
import time

def fetch_vacancies(text, offset):
    params = {
        "text": text,
        "limit": 100,
        "offset": offset,
    }
    url = "http://opendata.trudvsem.ru/api/v1/vacancies"
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["results"]["vacancies"]
    else:
        print("Error occurred while fetching data from API.")
        return []

def process_vacancy(vacancy):
    titles = vacancy["vacancy"]["job-name"]
    salary_from = vacancy["vacancy"]["salary_min"]
    salary_to = vacancy["vacancy"]["salary_max"]
    schedule = vacancy["vacancy"]["schedule"]
    experience = vacancy["vacancy"]["requirement"]["experience"]
    city = vacancy["vacancy"]["region"]["name"]
    employer = vacancy["vacancy"]["company"]["name"]

    if 'qualification' in vacancy['vacancy']['requirement']:
        skills = vacancy['vacancy']['requirement']['qualification']
    else:
        skills = ''

    return titles, skills, salary_from, salary_to, schedule, experience, city, employer

if __name__ == "__main__":
    text = 'python'
    offset = 1
    data = []

    while offset <= 100:  # Adjust the limit as needed
        vacancies = fetch_vacancies(text, offset)
        if not vacancies:
            break

        for vacancy in vacancies:
            vacancy_data = process_vacancy(vacancy)
            data.append(vacancy_data)
            offset += 1
            time.sleep(0.25)

    df = pd.DataFrame(data, columns=["Название вакансии", "Ключевые навыки", "Начальная зарплата", "Конечная зарплата",
                                     "График работы", "Требуемый опыт", "Город", "Работодатель"])
    df.to_excel(f"vacancies_rabota_ru_{date.today()}.xlsx", index=False)
    print("Excel файл создан успешно.")
