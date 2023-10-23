import requests
import pandas as pd
from openpyxl import Workbook

# URL для получения данных о вакансиях
url = 'https://api.hh.ru/vacancies'

# Параметры запроса к API hh.ru
params = {
    'area': 1,            # Код региона (например, Москва)
    'per_page': 100,      # Количество вакансий на одной странице
    'page': 0             # Номер страницы (начинается с 0)
}

# Отправляем GET-запрос к API и получаем результат
response = requests.get(url, params=params)
data = response.json()

# Создаем пустой DataFrame для хранения данных
df = pd.DataFrame(columns=[
    'vacancy_name',
    'url',
    'company',
    'city',
    'employment',
    'experience',
    'salary_from',
    'salary_to',
    'salary_currency',
    'description'
])

# Итерируемся по вакансиям и добавляем их в DataFrame
for vacancy in data['items']:
    df = df.append({
        'vacancy_name': vacancy['name'],
        'url': vacancy['url'],
        'company': vacancy['employer']['name'],
        'city': vacancy['area']['name'],
        'employment': vacancy['employment']['name'],
        'experience': vacancy['experience']['name'],
        'salary_from': vacancy['salary']['from'],
        'salary_to': vacancy['salary']['to'],
        'salary_currency': vacancy['salary']['currency'],
        'description': vacancy['snippet']['requirement']
    }, ignore_index=True)

# Создаем Excel файл и записываем данные в него
wb = Workbook()
ws = wb.active

# Заголовки столбцов
columns = [
    'vacancy_name',
    'url',
    'company',
    'city',
    'employment',
    'experience',
    'salary_from',
    'salary_to',
    'salary_currency',
    'description'
]

ws.append(columns)

# Записываем данные
for index, row in df.iterrows():
    ws.append([row[column] for column in columns])

# Сохраняем Excel файл
wb.save('hh_vacancies.xlsx')
