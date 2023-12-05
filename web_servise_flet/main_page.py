import flet as ft
from flet_core import colors
import plotly.express as px


def main(page: ft.Page):
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.IconButton(ft.icons.PEOPLE, on_click='', icon_size=40,
                          tooltip="Топ работадателей", ),

            ft.NavigationRailDestination(
                icon=ft.icons.COMPUTER, selected_icon=ft.icons.COMPUTER, label="Востребованные ЯП"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.WORK, selected_icon=ft.icons.WORK, label="Аналитика профессий"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.QUESTION_MARK),
                selected_icon_content=ft.Icon(ft.icons.QUESTION_MARK),
                label="О проекте",
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text(
                    "Здравствуйте, Вас приветствует персональный помощник АналитСист!" + "\n" + "На данный момент этот продукт является дипломным проектом студентки 4 курса группы "
                                                                                                "ПИ20-4 Финансового университета при Правительстве РФ" + "\n" + "Кудиновой Ирины Игоревны"),
                    ft.Image(
                        src=f"https://factohr-1a56a.kxcdn.com/wp-content/uploads/2021/03/jse.png",
                        height=700,
                        width=700,
                        border_radius=20,
                        fit=ft.ImageFit.CONTAIN, )],
                    alignment=ft.MainAxisAlignment.START, expand=True),

            ],
            expand=True,
        )
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)
