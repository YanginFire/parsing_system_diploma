import flet as ft


def DashBoardView(page):
    content = ft.Column(

        [
            ft.Row(
                [
                    ft.Text(
                        "Welcome to my Flet Router Tutorial",
                        size=50)
                ],
            )
        ]

    )
    return content
