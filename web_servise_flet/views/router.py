import flet as ft

# import views

from web_servise_flet.views.dashboard_page import DashBoardView
from web_servise_flet.views.Employee_stat_page import EmployeeStatView
from web_servise_flet.views.about_project_page import AboutView


class Router():
    def __init__(self, page):
        self.page = page,
        self.ft = ft,
        self.routes = {
            "/": EmployeeStatView(page),
            "/dashboard": DashBoardView(page),
            "/about_project": AboutView(page)
        }
        self.body = ft.Container(content=self.routes["/"])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
