import requests
import pandas as pd

def parse_jobs():
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': 'Java OR Python OR C++ OR C# OR JavaScript',  # Параметры для поля text, включая популярные языки программирования
        'per_page': 100,
        'area': 1,
        'premium': 'true',
        'currency': 'RUR',
        'only_with_salary': 'true',
        'industry': 'Информационные технологии, системная интеграция, интернет'
    }

    jobs_data = []

    for page in range(0, 101):  # Значение параметра page от 0 до 100
        params['page'] = page
        response = requests.get(url, params=params)
        response_data = response.json()["items"]

        for item in response_data['items']:
            name = item['name']
            description = item['description']
            salary_from = item['salary'].get('from')
            salary_to = item['salary'].get('to')
            schedule = item['schedule']['name']
            experience = item['experience']['name']
            city = item['area']['name']
            employer = item['employer']['name']

            jobs_data.append([name, description, salary_from, salary_to, schedule, experience, city, employer])

    headers = ['Vacancy', 'Description', 'Salary From', 'Salary To', 'Schedule', 'Experience', 'City', 'Employer']
    df = pd.DataFrame(jobs_data, columns=headers)
    df.to_excel('jobs.xlsx', index=False)

parse_jobs()