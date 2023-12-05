import flet as ft


def Nav_bar(page):
    Nav_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        leading_width=100,
        title=ft.Text("Аналитическая система сайтов-рекрутеров"),
        center_title=True,
        bgcolor=ft.colors.WHITE,
        actions=[
            ft.IconButton(ft.icons.PEOPLE, on_click=lambda event: page.go('/'), icon_size=40,
                          tooltip="Топ работадателей", ),
            ft.IconButton(ft.icons.WORK, on_click=lambda event: page.go('/dashboard'), icon_size=40,
                          tooltip="DashBoard по профессиям", ),
            ft.IconButton(ft.icons.QUESTION_MARK, on_click=lambda event: page.go('/about_project'), icon_size=40,
                          tooltip="О проекте", ),
        ],
    )

    return Nav_bar
