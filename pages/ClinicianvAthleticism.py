import os
import glob
import pandas as pd
import re
import dash
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import numpy as np
import plotly.express as px
from dash import html, dcc,dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.figure_factory as ff
## Import classes for visuals
from utils.visuals import VisualToolsCombined
visualTool = VisualToolsCombined()

from collections import OrderedDict

from dash import html, dcc, callback, Input, Output
# dash.register_page(__name__)
dash.register_page(__name__, path='/ClinicianvAthleticism')


df1 = pd.read_csv('data/Athleticism.csv')
df2 = pd.read_csv("data/ClinicianReport.csv")

df = pd.merge(df1, df2, on=['meta__session__session_guid'], how='outer')

df['meta__person__unique_id'] = df.apply(lambda row: row['meta__person__unique_id_x'] if pd.notnull(row['meta__person__unique_id_x']) else row['meta__person__unique_id_y'], axis=1)

df['timestamp'] = df.apply(lambda row: row['timestamp_x'] if pd.notnull(row['timestamp_x']) else row['timestamp_y'], axis=1)


df = df.sort_values(['meta__person__unique_id', 'timestamp'])

def layout():
    return html.Div([
        dbc.Container([
            html.H1("Athleticism vs. Clinician Report", style={'text-align': 'center'}),
            dcc.Dropdown(
                id='playerid-dropdown',
                options=[{'label': i, 'value': i} for i in np.concatenate([df['meta__person__unique_id'].unique(), ['all']])],
                #value=df['meta__person__unique_id'].unique()[0]
                value = 'all'
            ),
            html.Br(),
            dbc.Row(
                    [
                        dbc.Col(
                                    html.Div([
                                    html.Label('Select Athleticism Variables:', style={'font-weight': 'bold'}),
                                    dcc.Dropdown(options=[{'label': i, 'value': i} for i in df.iloc[:, 14:176]], id='variable-dropdown1', style={'width': '600px'}, multi=True),
                                    html.Br(),
                                    html.Label('Select Clinician Report Variables:', style={'font-weight': 'bold'}),
                                    dcc.Dropdown(options=[{'label': i, 'value': i} for i in df.iloc[:, 194:1010]], id='variable-dropdown2', style={'width': '600px'}, multi=True)   
                                ], style={'display': 'inline-block', 'vertical-align': 'top'}),
                            width=4),
                        dbc.Col(html.Div([
                                    dcc.Graph(id='cva-graph')]),
                                width=8)
                    ]
                ),
        ],fluid=True)
    ])
                        
@callback(
    Output('cva-graph', 'figure'),
    [
        Input(component_id='playerid-dropdown', component_property='value'),
        Input(component_id='variable-dropdown1', component_property='value'),
        Input(component_id='variable-dropdown2', component_property='value'),
    ]
)
def get_big_plot(playerid, variables1, variables2):
    return visualTool.big_figure(playerid, variables1,variables2)           
