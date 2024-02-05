import flet as ft

from web_servise_flet.views.router import Router
from user_controls_nav_bar.app_bar import Nav_bar


def main(page: ft.Page):
    page.theme_mode = "light"
    page.appbar = Nav_bar(page)
    myRouter = Router(page)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )

    page.go('/')


ft.app(target=main, port=8080, view=ft.AppView.WEB_BROWSER)
