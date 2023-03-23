#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import dash_bootstrap_components as dbc

import dash
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

teams_list = []
ids_list = []

for i in teams.get_teams():
    teams_list.append(list(i.items())[1][1])
    ids_list.append(list(i.items())[0][1])
    
id_dict = dict(zip(teams_list, ids_list))


app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    html.H1('Analysis of Team Performance in the NBA (2011 - 2015 Seasons)', style={'text-align': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Graphs', children=[
            dcc.Dropdown(options=[{'label': i, 'value': i} for i in teams_list], value='Atlanta Hawks', id='team-dropdown', style={'width': '300px'}),
            html.Div([
                dcc.Graph(id='WL_graph', style={'width': '50%', 'display': 'inline-block'}),
                dcc.Graph(id='plus_minus_graph', style={'width': '50%', 'display': 'inline-block'})
            ])
        ]),
        dcc.Tab(label='Future Work', children=[
            html.H2("This is the tab for future work.", style={'text-align': 'center'})
        ])
    ])
])

@app.callback(
    [Output('WL_graph', 'figure'), Output('plus_minus_graph', 'figure')],
    Input('team-dropdown', 'value'))

def update_graphs(value):
    
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_dict[value])
    games = gamefinder.get_data_frames()[0]
    reg_szn = games.loc[((games['SEASON_ID'].str[-4:] == '2015') | 
                    (games['SEASON_ID'].str[-4:] == '2014') | 
                    (games['SEASON_ID'].str[-4:] == '2013') |
                    (games['SEASON_ID'].str[-4:] == '2012') |
                    (games['SEASON_ID'].str[-4:] == '2011')) & # Last 5 Complete Seasons
         (games['SEASON_ID'].str[0] == '2') & # Filter Out Playoff Games
         (games['GAME_ID'].str[0] != '1')] # Filter Out Preseason Games
    
    reg_szn['SEASON'] = reg_szn['SEASON_ID'].str[-4:]
    
    reg_szn_graph = reg_szn.groupby(['SEASON','WL']).size().to_frame().reset_index()
    reg_szn_graph.rename(columns={0: 'Games', 'SEASON': 'Season'}, inplace = True)

    fig1 = px.bar(reg_szn_graph,
            x = "Season", 
            y = 'Games',
            color = "WL",
            barmode = 'group',
            title = "Wins and Loses for the 2011 - 2015 NBA Regular Seasons")
    
    reg_szn_graph1 = reg_szn.groupby(['SEASON'])['PLUS_MINUS'].mean().to_frame().reset_index()
    reg_szn_graph1.rename(columns={'PLUS_MINUS': 'Plus/Minus', 'SEASON': 'Season'}, inplace = True)

    fig2 = px.line(reg_szn_graph1,
            x = "Season", 
            y = 'Plus/Minus',
            title = "Avg. Game Plus/Minus for the 2011 - 2015 NBA Regular Seasons",
            markers = True)
    
    return fig1, fig2

if __name__ == '__main__':
    app.run_server(host = "0.0.0.0", debug=True, port=8050)




