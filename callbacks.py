import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app
from data_processing import iphone_data

@app.callback(
    Output("iphone-graph-average-price", "figure"),
    Input("iphone-type","value"),
    Input("iphone-capacity","value")
)
def update_graph(iphone_type, iphone_capacity):
    filtered_data = iphone_data[(iphone_data['name'] == iphone_type) & 
                                (iphone_data['capacity'] == iphone_capacity)]

    iphone_data_graph_min = filtered_data.sort_values(by=['days_to_buy_min_wage'])

    iphone_plot_min = px.bar(iphone_data_graph_min, 
             x="days_to_buy_min_wage", 
             y="country_name", 
             text="days_to_buy_min_wage", 
             orientation='h', 
             title='Days needed to buy an iPhone 13 with minimum wage', 
             labels={'days_to_buy_min_wage':'Days needed (Minimum wage)', 
                     'country_name':'Country'})

    iphone_plot_min.update_traces(texttemplate='%{text} days', textposition='auto')
    iphone_plot_min.update_traces(marker_color='#5C7AEA')

    iphone_plot_min.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

    iphone_plot_min.update_layout(xaxis={'visible': False, 'showticklabels': False})

    return iphone_plot_min