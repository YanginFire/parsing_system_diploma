import pandas as pd
import os

# Получаем список файлов Excel в папке
folder_path = 'C:/Users/User/Desktop/diploma'
files = os.listdir(folder_path)

# Фильтруем файлы и создаем список путей к файлам Excel
excel_files = [os.path.join(folder_path, file) for file in files if file.endswith('.xlsx')]

# Создаем пустой датафрейм, в который будем добавлять данные из файлов
combined_df = pd.DataFrame()

# Читаем и объединяем данные из файлов Excel в единый датафрейм
for file_path in excel_files:
    df = pd.read_excel(file_path)
    combined_df = combined_df._append(df, ignore_index=True)

# Создаем новый Excel-файл и сохраняем в него данные
output_file = 'C:/Users/User/Desktop/diploma/df_merged_data_october_march.xlsx'
combined_df.to_excel(output_file, index=False)

print("Данные сохранены в файл:", output_file)