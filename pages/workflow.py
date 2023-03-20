import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

## Import classes for visuals
from utils.visuals import VisualsTool
visualTool = VisualsTool()

from dash import html, dcc, callback, Input, Output
# dash.register_page(__name__)
dash.register_page(__name__, path='/workflow')
## Read in Data
df = pd.read_csv("data/ClinicianReport.csv")

df = df.sort_values(['meta__person__unique_id', 'timestamp'])

def layout():
    return html.Div([
        dbc.Container([
            html.H3("Trainer Workflow"),
            dcc.Dropdown(
                id='playerid-dropdown',
                options=[{'label': i, 'value': i} for i in df['meta__person__unique_id'].unique()],
                value=df['meta__person__unique_id'].unique()[0]
            ),
            dbc.Row(
                    [
                        dbc.Col(html.Div([
                                    html.H4("Bilateral squat"),
                                    dcc.Graph(id='Bilateral-graph')
                                ]),
                                width=6),
                        dbc.Col(html.Div([
                                    html.H4("Unilateral squat"),
                                    dcc.Graph(id='Unilateral-graph')
                                ]),
                                width=6),
                        dbc.Col(html.Div([
                                    html.H4("Difference squat"),
                                    dcc.Graph(id='difference-graph')
                                ]),
                                width=12)
                    ]
                ),
        ],fluid=True)
    ])

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