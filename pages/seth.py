import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from dash import html, dcc, callback, Input, Output
# dash.register_page(__name__)
dash.register_page(__name__, path='/seth')

## dbc.container just puts things in the middle with some margins
def layout():
    return html.Div([
        dbc.Container([
            html.H3("Seth's - PAGE")
        ])
    ])