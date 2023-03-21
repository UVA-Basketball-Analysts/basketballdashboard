import dash
from dash import html, dcc,dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
## Import classes for visuals
from utils.visuals import VisualsTool
visualTool = VisualsTool()

from collections import OrderedDict

from dash import html, dcc, callback, Input, Output
# dash.register_page(__name__)
dash.register_page(__name__, path='/workflow')
## Read in Data
df = pd.read_csv("data/ClinicianReport.csv")

df = df.sort_values(['meta__person__unique_id', 'timestamp'])

temp = pd.DataFrame(OrderedDict(
    [
        [
            'Column {}'.format(i + 1), list(range(30))
        ] for i in range(15)
    ]
))
def layout():
    return html.Div([
        dbc.Container([
            html.H3("Trainer Workflow"),
            dcc.Dropdown(
                id='playerid-dropdown',
                options=[{'label': i, 'value': i} for i in np.concatenate([df['meta__person__unique_id'].unique(), ['all']])],
                # value=df['meta__person__unique_id'].unique()[0]
                value = 'all'
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
                                width=12),
                        dbc.Col(html.Div([
                                    html.H4("Loading Strategies"),
                                    dcc.Graph(id='loading-strat-graph')
                                ]),
                                width=5),
                        dbc.Col(html.Div([
                                    html.H4("Loading Strategies Table"),
                                    html.Div(id = 'loading-strat-table')]),
                                width=7)
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


@callback(
    Output('loading-strat-graph', 'figure'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def get_loading_strategy(playerid):
    return visualTool.loading_strategy(playerid)

@callback(
    Output(component_id='loading-strat-table', component_property='children'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def loading_strat_table(playerid):
    df_transposed = visualTool.loading_strategy_table(playerid) 
    return html.Div(
        [dash_table.DataTable(
                                style_data={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                    },
                                data=df_transposed.to_dict('records'),
                                columns=[{'name': i, 'id': i,} for i in df_transposed.columns],
                                fixed_rows={'headers': True},
                                style_cell={
                                    'minWidth': 100, 'maxWidth': 100, 'width': 100
                                },
                                style_table={'overflowX': 'auto'},

            )])
                        
    