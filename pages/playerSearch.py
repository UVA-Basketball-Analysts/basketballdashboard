import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

layout = html.Div([
    dbc.Container([
        html.H1(
            [
                html.Div([
                    html.Div([
                        html.Div([], className="lines")], className="ball"),
                        html.Div([],className="shadow")
                    ], className="basketball"),
                    "Player Search Index"
            ], style={'text-align': 'center'}
        ),
        html.Div([
            dcc.Input(id="player-search", value="", type="text"),
            html.Div(id = 'player-output')
        ], style={'textAlign': 'center'})
    ])
])