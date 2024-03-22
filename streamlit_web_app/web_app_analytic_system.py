import plotly.express as px
import pandas as pd
import streamlit as st

# инициализация конфига для шапки веб-сайта

st.set_page_config(page_title="Dashboard Vacancy Analysis", page_icon=":bar_chart:", layout='wide')

# загрузка датафрейма на сайт

df = pd.read_excel(
    io='C:/Users/Yangin/Desktop/VKR/parsing_system_diploma/streamlit_web_app/clear_dataframe.xlsx',
    engine='openpyxl',
    sheet_name="Sheet1",
    usecols="B:I",
)

# инициализацяи бокового меню для фильтров
st.sidebar.header("Выберите нужные фильтры для Вас:")

# фильтр графика работы
time_schedule_filter = st.sidebar.multiselect(
    "Выберите фильтр для поля 'График работы': ",
    options=df["График работы"].unique(),
    default=df["График работы"].unique()
)
# фильтр опыта работы
working_experience_filter = st.sidebar.multiselect(
    "Выберите фильтр для поля 'Требуемый опыт': ",
    options=df["Требуемый опыт"].unique(),
    default=df["Требуемый опыт"].unique()
)

# Запрос к датафрейму для осуществелния обновления таблицы
# по тем фильтрам кототрые задает пользователь системы

selection_query = df.query("`График работы` == @time_schedule_filter & `Требуемый опыт` == @working_experience_filter")

st.header('Dashboard Vacancy Analysis :bar_chart:', divider='rainbow')

st.caption('Данное веб-приложение предназначено для просмотра актуальности професиии и необходимых статистических '
           'данных отрасли IT специальностей. Здесь вы можете просмотреть такие данные как Зарплата, '
           'Компании-работадатели, средняя зарплата по определенной спцеальности и многое другое. Данное приложение '
           'подойдет не только для соискателей, но и для работадателей')
st.divider()



# подключение базы данных
st.dataframe(selection_query)

