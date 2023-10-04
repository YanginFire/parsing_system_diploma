import requests
import pandas as pd
import time


def get_job_description(vacancy):
    return vacancy['snippet']['requirement']


url = "http://opendata.trudvsem.ru/api/v1/vacancies"
response = requests.get(url)

if response.status_code == 200:
    vacancies = response.json()["results"]["vacancies"]
    for i in range(0, 100):
        names_of_vacancies = vacancies[i]

        titles = names_of_vacancies["vacancy"]["job-name"]
        # skills = names_of_vacancies["vacancy"]["requirement"]["qualification"]
        salary_from = names_of_vacancies["vacancy"]["salary_min"]
        salary_to = names_of_vacancies["vacancy"]["salary_max"]
        schedule = names_of_vacancies["vacancy"]["schedule"]
        experience = names_of_vacancies["vacancy"]["requirement"]["experience"]
        city = names_of_vacancies["vacancy"]["region"]["name"]
        employer = names_of_vacancies["vacancy"]["company"]["name"]

        # if names_of_vacancies["vacancy"]["requirement"]["qualification"] == '':
        #     # print(len(names_of_vacancies["vacancy"]["requirement"]["qualification"]))
        #     skills = names_of_vacancies["vacancy"]["requirement"]["education"]
        # else:
        #     skills = names_of_vacancies["vacancy"]["requirement"]["qualification"]

        print(f"Номер {i+1}", skills)
        time.sleep(3)

        # data = list(map(parse_vacancy, vacancies))
        # print(f"Номер {i+1}",names_of_vacancies)
        # print(employer)
else:
    print("Error occurred while fetching data from API.")
