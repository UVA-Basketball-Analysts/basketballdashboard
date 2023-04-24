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
dash.register_page(__name__, path='/jumps')
## Read in Data
df = pd.read_csv("syntheticdata/synthetic_data.csv")

df = df.sort_values(['meta__person__unique_id', 'timestamp'])

jump_variable = [visualTool.column_names[i] for i in ["summary__vertical_jump__mobility__loading__hip_flex__right",
"summary__vertical_jump__mobility__loading__hip_flex__delta",
"summary__vertical_jump__mobility__loading__knee_flex__left",
"summary__vertical_jump__mobility__loading__knee_flex__right",
"summary__vertical_jump__mobility__loading__knee_flex__delta",
"summary__vertical_jump__mobility__loading__ankle_flex__left",
"summary__vertical_jump__mobility__loading__ankle_flex__right",
"summary__vertical_jump__mobility__loading__ankle_flex__delta",
"summary__vertical_jump__mobility__landing__hip_flex__left",
"summary__vertical_jump__mobility__landing__hip_flex__right",
"summary__vertical_jump__mobility__landing__hip_flex__delta",
"summary__vertical_jump__mobility__landing__knee_flex__left",
"summary__vertical_jump__mobility__landing__knee_flex__right",
"summary__vertical_jump__mobility__landing__knee_flex__delta",
"summary__vertical_jump__mobility__landing__ankle_flex__left",
"summary__vertical_jump__mobility__landing__ankle_flex__right",
"summary__vertical_jump__mobility__landing__ankle_flex__delta",
"summary__vertical_jump__alignment__loading__dyn_val__left",
"summary__vertical_jump__alignment__loading__dyn_val__right",
"summary__vertical_jump__alignment__loading__dyn_val__delta",
"summary__vertical_jump__alignment__landing__dyn_val__left",
"summary__vertical_jump__alignment__landing__dyn_val__right",
"summary__vertical_jump__alignment__landing__dyn_val__delta",
"summary__vertical_jump__performance__grf_takeoff__left",
"summary__vertical_jump__performance__grf_takeoff__right",
"summary__vertical_jump__performance__grf_takeoff__delta",
"summary__vertical_jump__performance__peak_grf__bilateral",
"summary__vertical_jump__landing_strategy__bilateral",
"summary__concentric_jump__mobility__loading__hip_flex__left",
"summary__concentric_jump__mobility__loading__hip_flex__right",
"summary__concentric_jump__mobility__loading__hip_flex__delta",
"summary__concentric_jump__mobility__loading__knee_flex__left",
"summary__concentric_jump__mobility__loading__knee_flex__right",
"summary__concentric_jump__mobility__loading__knee_flex__delta",
"summary__concentric_jump__mobility__loading__ankle_flex__left",
"summary__concentric_jump__mobility__loading__ankle_flex__right",
"summary__concentric_jump__mobility__loading__ankle_flex__delta",
"summary__concentric_jump__alignment__loading__dyn_val__left",
"summary__concentric_jump__alignment__loading__dyn_val__right",
"summary__concentric_jump__alignment__loading__dyn_val__delta",
"summary__concentric_jump__performance__jump_height__bilateral",
"summary__concentric_jump__performance__grf_takeoff__left",
"summary__concentric_jump__performance__grf_takeoff__right",
"summary__concentric_jump__performance__grf_takeoff__delta",
"summary__concentric_jump__landing_strategy__bilateral"]]



def layout():
    return html.Div([
        dbc.Container([
            html.H2("Jumps", style={'text-align': 'center'}),
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
                        dbc.Col(html.Div([html.H2([html.Br(),'Vertical Jump to Concentric Jump'], style={'text-align': 'center'})]),width=12),
                        dbc.Col(html.Div([html.H4("Variable Selection", style={'text-align': 'center'})]),width=12),
                        dbc.Col(
                                    html.Div([
                                    html.Label('Select Variables:', style={'font-weight': 'bold'}),
                                    dcc.Dropdown(options=[{'label': i, 'value': i} for i in jump_variable], id='variable-dropdown', style={'width': '600px'}, multi=True)
                                ], style={'display': 'inline-block', 'vertical-align': 'top'}),
                            width=4),
                        dbc.Col(html.Div([
                                    dcc.Graph(id = 'jump-graph')]),
                                width=8)
                    ]
                ),
        ],fluid=True)
    ])
                        
@callback(
    Output('jump-graph', 'figure'),
    [
        Input(component_id='playerid-dropdown', component_property='value'),
        Input(component_id='variable-dropdown', component_property='value')
    ]
)
def get_jump_plot(playerid, variables):
    return visualTool.jumps_figure(playerid, variables)