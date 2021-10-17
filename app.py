import dash
from dash.html.Col import Col
from dash.html.Img import Img
from dash.html.Nav import Nav
from dash.html.Output import Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import plotly.express as px

import pandas as pd
import numpy as np

import frontend_components as fc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = "iPhone Index"

content = html.Div(id="page-content", children=[])

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        fc.navbar,
        content
    ]
)


### Navbar callback
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


### Content for navigation
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [html.H1("Days to buy an iPhone", className="ml-4")]

    elif pathname == "/index":
        return [html.H1("Index", className="ml-4")]
    
    return dbc.Jumbotron(
        [
            html.H1("404 Not Found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognized..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True)