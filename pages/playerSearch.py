import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc, callback, Input, Output
dash.register_page(__name__, path='/players')

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

from utils.players.players import Player
player = Player(-1)
@callback(
    Output(component_id='player-output', component_property='children'),
    Input(component_id='player-search', component_property='value')
)
def construct_player_table(name):
    get_players = player.getAllPlayers()
    if name == '':
        filtered_players = get_players
    else:
        filtered_players = [player for player in get_players if name in player['Name']] 
    table_header = [
        html.Thead(html.Tr([html.Th("Name"), html.Th("Team"), html.Th("Info")]))
    ]
    
    rows = [html.Tr([html.Td(player["Name"]), 
                     html.Td(player["Team"]), 
                     html.Td(html.A("↗", href="/singlePlayer/" + str(player["id"])))]) for player in filtered_players]
    table_body = [html.Tbody(rows)]
    
    return dbc.Table(table_header + table_body, striped=True, bordered=True, hover=True)
    