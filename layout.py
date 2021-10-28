import dash
from dash.html.Col import Col
from dash.html.Img import Img
from dash.html.Nav import Nav
from dash.html.Output import Output
from dash_bootstrap_components._components.Navbar import Navbar
import dash_core_components as dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from data_processing import iphone_data

#####################################
# Styles & Colors
#####################################

SIDEBAR_STYLE = {
    "top": 0,
    "left": 0,
    "bottom": 0,
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "top":0,
    "margin-top":'1rem',
    "margin-left": "1rem",
    "margin-right": "1rem",
}

### Sidebar ###
sidebar = html.Div(
    [
        html.Div("iPhone type"),
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in iphone_data.name.unique()], 
            value="iPhone 13",
            id='iphone-type',
        ),

        html.Br(),

        html.Div("iPhone capacity (Gb)"),
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in iphone_data.capacity.unique()], 
            value=256,
            id='iphone-capacity',
        ),

        html.Br(),

    ],

    style=SIDEBAR_STYLE,
)

##############################
########### NavBar ###########
##############################

LOGO = "https://upload.wikimedia.org/wikipedia/commons/a/ab/Apple-logo.png"

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=LOGO, height="30px", className="ml-2")),
                    dbc.Col(dbc.NavbarBrand("iPhone Index", className="ml-2 mt-1 mb-1")),

                ],
                align="center",
                no_gutters=True,
            ),
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Days to buy", href="/", active="exact")),
                    dbc.NavItem(dbc.NavLink("Index", href="/index", active="exact")),
            ],
            className="ml-auto",
            navbar=True,
            ),
        id="navbar-collapse", navbar=True, is_open=False
        ), 
    ],
    color="dark",
    dark=True,
    className="mb-5"
)


############################################################
################# Days to buy an iphone ####################
############################################################

### Cards ###

iphone_price_card = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Price (USD)", className="card-title"),
            html.H3('xxx', className='card-text')
        ]
    ),
    color='primary',
    inverse=True
)

minimum_wage_card = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Minimum Wage", className="card-title"),
            html.H3('xxx', className='card-text')
        ]
    ),
    color='primary',
    inverse=True
)

average_wage_card = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Average Wage", className="card-title"),
            html.H3('xxx', className='card-text')
        ]
    ),
    color='primary',
    inverse=True
)

minimum_wage_plot = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Minimum Wage Plot", className="card-title"),
            dcc.Graph(id='iphone-graph-minimum-price')
        ]
    ),
    color='#FFFFFF',
    inverse=False
)

average_wage_plot = dbc.Card(
    dbc.CardBody(
        [
            html.H3("Average Wage Plot", className="card-title"),
            dcc.Graph(id='iphone-graph-average-price')
        ]
    ),
    color='#FFFFFF',
    inverse=False
)

### Layout Page 1

page_1 = dbc.Container(
    [
        html.H1("Days needed to buy an iPhone", className="ml-4 mb-5"),


        dbc.Row(
            [
                dbc.Col(iphone_price_card, width=3),
                #dbc.Col(minimum_wage_card, width=3),
                #dbc.Col(average_wage_card, width=3),
            ],
            className="ml-3 mr-3"
        ),
        dbc.Row(
            [
                dbc.Col(minimum_wage_plot)
            ],
            className="ml-3 mr-3 mt-5 mb-5"
        ),
        dbc.Row(
            [
                dbc.Col(average_wage_plot)
            ],
            className="ml-3 mr-3 mt-5 mb-5"
        ),
    ],
    fluid=True,
    style=CONTENT_STYLE
)