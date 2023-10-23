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
        print(f"Error occurred while fetching data for {text} from API.")
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
    elif 'duty' in vacancy['vacancy']:
        skills = vacancy['vacancy']['duty']
    else:
        skills = ''

    return titles, skills, salary_from, salary_to, schedule, experience, city, employer


if __name__ == "__main__":
    lang = ["Python", "Java", "C++", "JavaScript", "PHP", "Ruby", "JavaScript", "C#", "Swift", "Go", "Rust",
            "TypeScript", "Kotlin", "Perl", "R", "Objective-C", "MATLAB", "HTML", "CSS", "SQL", "GIT",
            "Bash", "React", "Vue.js", "Aurora OS", "Аврора ОС"]

    for language in lang:
        offset = 0
        data = []
        text = language

        while offset <= 100:  # Adjust the limit as needed
            vacancies = fetch_vacancies(text, offset)
            if not vacancies:
                break

            for vacancy in vacancies:
                vacancy_data = process_vacancy(vacancy)
                data.append(vacancy_data)
                offset += 1
                time.sleep(3)

        df = pd.DataFrame(data,
                          columns=["Название вакансии", "Ключевые навыки", "Начальная зарплата", "Конечная зарплата",
                                   "График работы", "Требуемый опыт", "Город", "Работодатель"])
        df.to_excel(f"vacancies_rabota_ru_ААА2_{language}_{date.today()}.xlsx", index=False)
        print(f"Excel файл для {language} создан успешно.")
