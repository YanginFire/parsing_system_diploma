import pandas as pd
import os
from datetime import date

# Получаем список файлов в папке
folder_path = 'C:/Users/Yangin/Desktop/VKR/parsing_system_diploma/hh'
files = os.listdir(folder_path)

# Фильтруем файлы и создаем список путей к файлам xlsx, начинающимся с "vacancies"
xlsx_files = [os.path.join(folder_path, file) for file in files if file.endswith('.xlsx') and file.startswith('vacancies')]

# Создаем пустой датафрейм, в который будем добавлять данные из файлов
combined_df = pd.DataFrame()

# Читаем и объединяем данные из файлов xlsx в единый датафрейм
for file_path in xlsx_files:
    df = pd.read_excel(file_path)
    combined_df = combined_df.append(df, ignore_index=True)

# Создаем новый CSV-файл и сохраняем в него данные с кодировкой UTF-8
output_file = 'df_merged2023-11-13.xlsx'
combined_df.to_excel(output_file, index=False, encoding='utf-8')

print("Данные сохранены в файл:", output_file)