import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from utils.players.players import Player
player = Player(1)
import plotly.express as px
df = pd.DataFrame({
    'Game': [i for i in range(1, 11)] + [i for i in range(1, 11)],
    'Points' : player.playerInfo['Points'] + player.playerInfo['Assists'],
    'Type': ['Points' for i in range(1, 11)] + ['Assists' for i in range(1, 11)]
})
fig = px.line(df, x='Game', y='Points', color='Type', symbol="Type")

layout = html.Div([
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(html.Img(src=player.playerInfo['Profile'],
                                        style={
                                    'max-width': '100%',
                                    'height': 'auto',
                                    'border-radius': '50%'
                                }),
                                width=4),
                dbc.Col(dbc.Row([
                            dbc.Col(html.P('First Name'),width=6),
                            dbc.Col(html.P(player.playerInfo['Fname']),width=6),
                            dbc.Col(html.P('Last Name'),width=6),
                            dbc.Col(html.P(player.playerInfo['Lname']),width=6),
                            dbc.Col(html.P('ID'),width=6),
                            dbc.Col(html.P(player.playerInfo['PlayerId']),width=6),
                            dbc.Col(html.P('Position'),width=6),
                            dbc.Col(html.P(player.playerInfo['PlayerId']),width=6),
                            dbc.Col(html.P('Height'),width=6),
                            dbc.Col(html.P(player.playerInfo['PhysicalInformation']['Height']),width=6),
                            dbc.Col(html.P('Weight'),width=6),
                            dbc.Col(html.P(player.playerInfo['PhysicalInformation']['Weight']),width=6),
                            dbc.Col(html.P('Age'),width=6),
                            dbc.Col(html.P(player.playerInfo['PhysicalInformation']['Age']),width=6),
                            dbc.Col(html.P('Avg Points'),width=6),
                            dbc.Col(html.P(sum(player.playerInfo['Points'])/len(player.playerInfo['Points'])),width=6),
                            dbc.Col(html.P('Avg Assists'),width=6),
                            dbc.Col(html.P(sum(player.playerInfo['Assists'])/len(player.playerInfo['Points'])),width=6),
                        ]),
                                width=8),
            ], style={'text-align': 'center'}
        ),
        html.Br(),
        html.H3('Points & Assists per Game'),
        dcc.Graph(
            id='points-graph',
            figure=fig
        )
        
    ])
])