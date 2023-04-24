import dash
from dash import html, dcc,dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
## Import classes for visuals
from utils.visuals import VisualsTool
visualTool = VisualsTool()

from utils.tabs import GenericTabs
tabObject = GenericTabs()
tabs = GenericTabs.constructTabs(tabObject,['Bilateral', 'Unilateral', 'UniVsBi'])

from collections import OrderedDict

from dash import html, dcc, callback, Input, Output
# dash.register_page(__name__)
dash.register_page(__name__, path='/squats')
## Read in Data
df = pd.read_csv("syntheticdata/synthetic_data.csv")

df = df.sort_values(['meta__person__unique_id', 'timestamp'])

def layout():
    return html.Div([
        dbc.Container([
            html.H2("Squats", style={'text-align': 'center'}),
            html.Br(),
            html.H5("Player"),
            dcc.Dropdown(
                id='playerid-dropdown',
                options=[{'label': i, 'value': i} for i in np.concatenate([df['meta__person__unique_id'].unique(), ['all']])],
                # value=df['meta__person__unique_id'].unique()[0]
                value = 'all'
            ),
            html.Br(),
            html.Br(),
            tabs[0],
            tabs[1]
        ],fluid=True)
    ])

@callback(Output('tabs-content-inline-3', 'children'),
              Input('tabs-inline', 'value'))
def render_content(tab):
    if tab == 'tab-Bilateral':
        return dbc.Col(html.Div([
                                    html.H4("Bilateral squat", style={'text-align': 'center'}),
                                    dcc.Graph(id='Bilateral-graph')
                                ]),
                                width=12)
    elif tab == 'tab-Unilateral':
        return dbc.Col(html.Div([
                                    html.H4("Unilateral squat", style={'text-align': 'center'}),
                                    dcc.Graph(id='Unilateral-graph')
                                ]),
                                width=12)
    elif tab == 'tab-UniVsBi':
        return dbc.Col(html.Div([
                                    html.H4("Unilateral vs Bilateral", style={'text-align': 'center'}),
                                    dcc.Graph(id='difference-graph')
                                ]),
                                width=12)
    
@callback(
    Output('Bilateral-graph', 'figure'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def get_bilateral(playerid):
    return visualTool.bilateral(playerid)

@callback(
    Output('Unilateral-graph', 'figure'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def get_unilateral(playerid):
    return visualTool.unilateral(playerid)

@callback(
    Output('difference-graph', 'figure'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def get_bivsuni(playerid):
    return visualTool.bivsuni(playerid)

