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
dash.register_page(__name__, path='/loadingstrats')
## Read in Data
df = pd.read_csv("syntheticdata/synthetic_data.csv")

df = df.sort_values(['meta__person__unique_id', 'timestamp'])

def layout():
    return html.Div([
        dbc.Container([
            html.H2("Loading Strategies Workflow", style={'text-align': 'center'}),
            html.Br(),
            html.H5("Player"),
            dcc.Dropdown(
                id='playerid-dropdown',
                options=[{'label': i, 'value': i} for i in np.concatenate([df['meta__person__unique_id'].unique(), ['all']])],
                # value=df['meta__person__unique_id'].unique()[0]
                value = 'all'
            ),
            dbc.Row(
                    [
                        dbc.Col(html.Div([html.H2([html.Br(),'Loading Strategies'], style={'text-align': 'center'})]),width=12),
                        dbc.Col(html.Div([
                                    html.Div(id = 'loading-strat-table')]),
                                width=12)
                    ]
                ),
        ],fluid=True)
    ])

def create_conditional_style(df):
    style=[]
    for col in df.columns:
        name_length = len(col)
        pixel = 50 + round(name_length*PIXEL_FOR_CHAR)
        pixel = str(pixel) + "px"
        style.append({'if': {'column_id': col}, 'minWidth': pixel})

    return style

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
                                style_data_conditional= [{'if' : {'column_id': '{}'.format(i), 
                                                                  'filter_query': '{{{}}} = "knee"'.format(i)}, 
                                                          'backgroundColor':'#2582fa',
                                                          'color': 'white'} for i in df_transposed.columns] + 
                                                        [{'if' : {'column_id': '{}'.format(i), 
                                                                  'filter_query': '{{{}}} = "hip"'.format(i)}, 
                                                          'backgroundColor':'#d41815',
                                                          'color':'white'}
                                                         for i in df_transposed.columns] + 
                                                        [{'if' : {'column_id': '{}'.format(i)}, 
                                                          'minWidth':str(round(len(i) * 10) + 25) + 'px'}
                                                         for i in df_transposed.columns]
                            )
        ]
    )
