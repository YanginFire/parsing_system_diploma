import flet as ft

def Nav_Rail_bar(page, ft=ft):
    Nav_Rail_bar = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                ft.IconButton(ft.icons.PEOPLE, on_click=''),
                ft.NavigationRailDestination(
                    icon=ft.icons.PEOPLE, selected_icon=ft.icons.PEOPLE, label="Топ работадателей"
                ),
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
    return Nav_Rail_bar