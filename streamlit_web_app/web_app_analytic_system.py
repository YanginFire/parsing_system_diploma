import plotly.express as px
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# инициализация конфига для шапки веб-сайта

st.set_page_config(page_title="Dashboard Vacancy Analysis", page_icon=":bar_chart:", layout='wide')

# загрузка датафрейма на сайт


with st.sidebar:
    selected = option_menu(
        menu_title="Меню",
        options=["🏠 Главная", "📈 Топ навыки IT", "❓ О проекте"]
    )

if selected == "🏠 Главная":
    # загрузка датафрейма на сайт
    df = pd.read_excel(
        io='C:/Users/Yangin/Desktop/VKR/parsing_system_diploma/streamlit_web_app/clear_dataframe.xlsx',
        engine='openpyxl',
        sheet_name="Sheet1",
        usecols="B:I",
    )

    st.header('Dashboard Vacancy Analysis :bar_chart:', divider='rainbow')

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
    selection_query = df.query(
        "`График работы` == @time_schedule_filter & `Требуемый опыт` == @working_experience_filter ")
    # подключение базы данных
    st.dataframe(selection_query)

    length_df = len(df)
    st.subheader(f"Количество вакансий :green[в базе] на данный момент - {length_df}", )

    # df = df.set_index("Начальная зарплата")
    # st.bar_chart(df["Конечная зарплата"], use_container_width=True)

    column1, column2 = st.columns(2)

    with column1:
        # Подсчет количества встречающихся значений в столбце
        counts = df['График работы'].value_counts().reset_index()
        counts.columns = ['График работы', 'Количество']

        # инициализация кругового графика
        fig = px.pie(counts, values='Количество', names='График работы',
                     title='Процентное соотношение по столбцу График работы', hole=.3)
        fig.update_traces(textposition='inside', textfont_size=16)
        st.plotly_chart(fig)
    with column2:
        # Подсчет количества встречающихся значений в столбце
        counts = df['Требуемый опыт'].value_counts().reset_index()
        counts.columns = ['Требуемый опыт', 'Количество']

        # инициализация кругового графика
        fig = px.pie(counts, values='Количество', names='Требуемый опыт',
                     title='Процентное соотношение по столбцу Требуемый опыт', hole=.3)
        fig.update_traces(textposition='inside', textfont_size=16)
        st.plotly_chart(fig)

    # Зарплаты - график

    df["Зарплата"] = df["Начальная зарплата"].astype(str) + '-' + df["Конечная зарплата"].astype(str)
    counts = df["Зарплата"].value_counts().reset_index()
    counts.columns = ["Зарплата", 'Количество предложений']

    fig = px.bar(counts[:21], x='Зарплата', y='Количество предложений', color="Зарплата",
                 title='Распределение популярных предложений работадателей по зарплатам')
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(counts, use_container_width=True)

    # Работадатели - график
    counts_employee = df["Работодатель"].value_counts().reset_index()
    counts_employee.columns = ["Работодатель", 'Количество вакансий']
    fig_2 = px.bar(counts_employee[:31], x='Работодатель', y='Количество вакансий', color="Работодатель",
                   title='Топ 30 популярных работадателей')
    st.plotly_chart(fig_2, use_container_width=True)

if selected == "📈 Топ навыки IT":
    st.header('Топ навыки для IT-специалистов :bar_chart:', divider='rainbow')

    st.caption(
        "Данный раздел веб-прилодения поможет вам определить какие навыки на данный момент"
        " чаще всего требуют в своих вакансиях компании-работадатели."
        " Здесь представлен как и весь список, так и удобный график первых 50 навыков для удобства просмотра")

    # загрузка датафрейма с навыками на сайт
    df_IT_skills = pd.read_excel(
        io='C:/Users/Yangin/Desktop/VKR/parsing_system_diploma/streamlit_web_app/top_skills_new.xlsx',
        engine='openpyxl',
        sheet_name="Sheet1",
        usecols="A:B",
    )

    df_IT_skills = df_IT_skills.set_index("Навык")

    st.dataframe(df_IT_skills, use_container_width=True)

    st.subheader('На данном графике представлены первые :blue[50 навыков] необходимые для каждого специалиста в '
                 'области IT :sunglasses:')

    fig = px.bar(df_IT_skills[:50], y=df_IT_skills['Частота'][:50], height=400)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

if selected == "❓ О проекте":
    st.header('О проекте :bar_chart:', divider='rainbow')
    st.caption('Данное веб-приложение предназначено для просмотра актуальности професиии и необходимых статистических '
               'данных отрасли IT специальностей. Здесь вы можете просмотреть такие данные как Зарплата, '
               'Компании-работадатели, средняя зарплата по определенной спцеальности и многое другое. Данное приложение '
               'подойдет не только для соискателей, но и для работадателей')
    st.divider()

# slider_of_low_salary = st.sidebar.slider(
#     "Укажите предпочитаемый диапазон зарплат:",
#     min_value=df['Начальная зарплата'].min(),
#     max_value=df['Начальная зарплата'].max(),
#     value=(35000,65000),
#     step=5000
# )
#
# slider_of_hight_salary = st.sidebar.slider(
#     "Укажите предпочитаемый диапазон зарплат:",
#     min_value=df['Конечная зарплата'].min(),
#     max_value=df['Конечная зарплата'].max(),
#     value=(100000,220000),
#     step=5000
# )
