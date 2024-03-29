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
        io='C:/Users/User/Desktop/diploma/streamlit_web_app/clear_dataframe.xlsx',
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
    # фильтр города
    city_filter = st.sidebar.multiselect(
        "Выберите фильтр для поля 'Город': ",
        options=df["Город"].unique(),
        default=df["Город"].unique()
    )

    # Запрос к датафрейму для осуществелния обновления таблицы
    # по тем фильтрам кототрые задает пользователь системы
    selection_query = df.query(
        "`График работы` == @time_schedule_filter & `Требуемый опыт` == @working_experience_filter & `Город` == "
        "@city_filter ")
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

    # Зарплаты - график Начальная зарплата

    counts_start = df["Начальная зарплата"].value_counts().reset_index()
    counts_start.columns = ["Начальная зарплата", 'Количество предложений']

    fig = px.bar(counts_start, x='Начальная зарплата', y='Количество предложений', color="Начальная зарплата",
                 title='Распределение популярных предложений работадателей по начальным зарплатам',
                 color_continuous_scale='rainbow', text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

    # Зарплаты - график Конечная зарплата

    counts_end = df["Конечная зарплата"].value_counts().reset_index()
    counts_end.columns = ["Конечная зарплата", 'Количество предложений']

    fig_3 = px.bar(counts_end, x='Конечная зарплата', y='Количество предложений', color='Конечная зарплата',
                   title='Распределение популярных предложений работадателей по конечным зарплатам',
                   color_continuous_scale='rainbow', text_auto=True)
    st.plotly_chart(fig_3, use_container_width=True)

    # st.dataframe(counts, use_container_width=True)

    # Работадатели - график
    counts_employee = df["Работодатель"].value_counts().reset_index()
    counts_employee.columns = ["Работодатель", 'Количество вакансий']
    fig_2 = px.bar(counts_employee[:31], x='Работодатель', y='Количество вакансий', color="Работодатель",
                   title='Топ 30 популярных работадателей')
    st.plotly_chart(fig_2, use_container_width=True)

    # Города - график
    city_count = df['Город'].value_counts().reset_index()
    city_count.columns = ['Город', 'Количество вакансий']

    fig_4 = px.bar(city_count, x='Город', y='Количество вакансий', color='Город',
                   title='Количество вакансий по городам', text_auto=True)
    st.plotly_chart(fig_4, use_container_width=True)

if selected == "📈 Топ навыки IT":
    st.header('Топ навыки для IT-специалистов :bar_chart:', divider='rainbow')

    st.caption(
        "Данный раздел веб-приложения поможет Вам определить какие навыки на данный момент"
        " чаще всего требуют в своих вакансиях Компании-работадатели."
        " Здесь представлен как и весь список, так и удобный график первых 50 навыков для удобства просмотра")

    # загрузка датафрейма с навыками на сайт
    df_IT_skills = pd.read_excel(
        io='C:/Users/User/Desktop/diploma/streamlit_web_app/top_skills_new_cleared.xlsx',
        engine='openpyxl',
        sheet_name="Sheet1",
        usecols="A:B",
    )

    st.dataframe(df_IT_skills, use_container_width=True)

    st.subheader('На данном графике представлены первые :blue[50 навыков] необходимые для каждого специалиста в '
                 'области IT :sunglasses:')

    fig = px.bar(df_IT_skills, x=df_IT_skills['Навык'][:50], y=df_IT_skills['Частота'][:50],
                 color=df_IT_skills['Навык'][:50], height=400)
    st.plotly_chart(fig, use_container_width=True)

if selected == "❓ О проекте":
    st.header('О проекте :bar_chart:', divider='rainbow')
    st.caption('Данное веб-приложение предназначено для просмотра актуальности професиии и необходимых статистических '
               'данных отрасли IT специальностей. Здесь вы можете просмотреть такие данные как Зарплата, '
               'Компании-работадатели, средняя зарплата по определенной спцеальности и многое другое. Данное приложение'
               'подойдет не только для соискателей, но и для работадателей')
    st.divider()

    st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExajlqMWQxeWNlYWxmOWh1anMyb2Fybzd4YXU0bHRpNDZrYjZrejhmOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/coxQHKASG60HrHtvkt/giphy.gif)")


