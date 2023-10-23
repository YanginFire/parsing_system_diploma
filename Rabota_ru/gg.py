import requests
import pandas as pd
import time

text = ''
offset = 1

params = {
        "text": text,
        "limit": 100,
        "offset": offset,
    }
url = "http://opendata.trudvsem.ru/api/v1/vacancies"
response = requests.get(url,params=params)

if response.status_code == 200:
    vacancies = response.json()["results"]["vacancies"]
    for i in range(0, 100):
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

        time.sleep(3)

else:
    print("Error occurred while fetching data from API.")