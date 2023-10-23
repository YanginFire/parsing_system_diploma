import requests
import pandas as pd


def parse_hh_vacancies(page):
    url = "https://api.hh.ru/vacancies"

    params = {
        "text": "Java",
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


def parse_rabota_ru_vacancies(page):
    url = "http://opendata.trudvsem.ru/api/v1/vacancies"

    params = {
        "text": "Java",
        "page": page,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        vacancies = response.json()["results"]["vacancies"]

        data = list(map(parse_vacancy_rabota_ru, vacancies))
        return data

    else:
        print("Error occurred while fetching data from API.")
        return None


def parse_vacancy_rabota_ru(vacancy):
    title = vacancy['vacancy']["job-name"]
    skills = get_job_description_rabota_ru(vacancy) or ""
    salary_from = vacancy["salary_min"] if vacancy.get("salary_min") else ""
    salary_to = vacancy["salary_max"]["to"] if vacancy.get("salary_max") else ""
    schedule = vacancy["schedule"] if vacancy.get("schedule") else ""
    experience = vacancy["experience"] if vacancy.get("experience") else ""
    city = vacancy["region"]["name"] if vacancy.get("region") else ""
    employer = vacancy["company"]["name"] if vacancy.get("company") else ""

    return title, skills, salary_from, salary_to, schedule, experience, city, employer


def get_job_description(vacancy):
    return vacancy['snippet']['requirement']


def get_job_description_rabota_ru(vacancy):
    return vacancy['requirement']['qualification']


if __name__ == "__main__":
    data = []
    for page in range(0, 200):
        vacancies_data = parse_hh_vacancies(page)
        if vacancies_data:
            data += vacancies_data
        else:
            print("Парсинг закончен на странице", page)
            break

    df = pd.DataFrame(data, columns=["Название вакансии", "Ключевые навыки", "Начальная зарплата", "Конечная зарплата",
                                     "График работы", "Требуемый опыт", "Город", "Работодатель"])
    df.to_excel("vacancies_Java.xlsx", index=False)
    print("Excel файл создан успешно.")

    # for page in range(0, 200):
    #     vacancies_data = parse_rabota_ru_vacancies(page)
    #     if vacancies_data:
    #         data += vacancies_data
    #     else:
    #         print("Парсинг закончен на странице", page)
    #         break
    #
    # df = pd.DataFrame(data, columns=["Название вакансии", "Ключевые навыки", "Начальная зарплата", "Конечная зарплата",
    #                                  "График работы", "Требуемый опыт", "Город", "Работодатель"])
    # df.to_excel("vacancies_rabota_ru_Java.xlsx", index=False)
    # print("Excel файл создан успешно.")
