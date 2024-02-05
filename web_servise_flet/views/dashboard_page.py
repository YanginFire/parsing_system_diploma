import flet as ft
import pandas as pd
import plotly.express as px
from flet.plotly_chart import PlotlyChart

def DashBoardView(page, df):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
    fig = px.line(df, x='AAPL_x', y='AAPL_y', title='Apple Share Prices over time (2014)')
    content = ft.Column(
        fig.show()
    )
    return content
