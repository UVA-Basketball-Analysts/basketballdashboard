import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import re

from dash import html, dcc, callback, Input, Output


dash.register_page(__name__, path='/hka')

## Read in DF
df = pd.read_csv("data/ClinicianReport.csv")

df = df.sort_values(['meta__person__unique_id', 'meta__session__session_datetime'])



## Define Layout
def layout():
    return html.Div([
        dbc.Container([
            html.H3("Hips, Knees, Ankles"),
            dcc.Dropdown(
                id='playerid-dropdown',
                options=[{'label': i, 'value': i} for i in df['meta__person__unique_id'].unique()],
                value=df['meta__person__unique_id'].unique()[0]
            ),       
            html.H2("Hips"),
            dcc.Graph(id='hips-graph'),
            html.H2("Knees"),
            dcc.Graph(id='knees-graph'),
            html.H2("Ankles"),
            dcc.Graph(id='ankle-graph')  
        ])
    ])
@callback(
    Output('hips-graph', 'figure'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def hips(playerid):
    one_athlete = df[df['meta__person__unique_id'].str.contains(playerid)]
    df_hips = one_athlete.filter(regex = re.compile(r'meta__person__unique_id|meta__session__session_guid|meta__session__session_datetime|hip|HIP|Hip'))
    lines = []
    for column in df_hips.columns[4:]:
        trace = go.Scatter(
            x=df_hips['meta__session__session_datetime'],
            y=df_hips[column],
            mode='markers',
            name=column
        )
        lines.append(trace)

    layout = go.Layout(
        title='Clinician Hips',
        xaxis=dict(title='Timestamp'),
        yaxis=dict(title='Value')
    )
    fig = go.Figure(data=lines, layout=layout)
    fig.update_traces(visible="legendonly")
    return fig

@callback(
    Output('knees-graph', 'figure'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def knees(playerid):
    one_athlete = df[df['meta__person__unique_id'].str.contains(playerid)]
    df_hips = one_athlete.filter(regex = re.compile(r'meta__person__unique_id|meta__session__session_guid|meta__session__session_datetime|knee|KNEE|Knee'))
    lines = []
    for column in df_hips.columns[4:]:
        trace = go.Scatter(
            x=df_hips['meta__session__session_datetime'],
            y=df_hips[column],
            mode='lines',
            name=column
        )
        lines.append(trace)

    layout = go.Layout(
        title='Clinician Ankle',
        xaxis=dict(title='Timestamp'),
        yaxis=dict(title='Value')
    )
    fig = go.Figure(data=lines, layout=layout)
    fig.update_traces(visible="legendonly")
    return fig

@callback(
    Output('ankle-graph', 'figure'),
    [Input(component_id='playerid-dropdown', component_property='value')]
)
def ankles(playerid):
    one_athlete = df[df['meta__person__unique_id'].str.contains(playerid)]
    df_hips = one_athlete.filter(regex = re.compile(r'meta__person__unique_id|meta__session__session_guid|meta__session__session_datetime|ankle|ANKLE|Ankle'))
    lines = []
    for column in df_hips.columns[4:]:
        trace = go.Scatter(
            x=df_hips['meta__session__session_datetime'],
            y=df_hips[column],
            mode='lines',
            name=column
        )
        lines.append(trace)

    layout = go.Layout(
        title='Clinician Ankle',
        xaxis=dict(title='Timestamp'),
        yaxis=dict(title='Value')
    )
    fig = go.Figure(data=lines, layout=layout)
    fig.update_traces(visible="legendonly")
    return fig
