import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import dash
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from dash import Dash, html
UVA_LOGO = 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Virginia_Cavaliers_sabre.svg/1200px-Virginia_Cavaliers_sabre.svg.png'
header = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=UVA_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("UVABBall", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Home")),
                                dbc.NavItem(dbc.NavLink("Page 1")),
                                dbc.NavItem(
                                    dbc.NavLink("Page 2"),
                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto",
                                ),
                                dbc.NavItem(dbc.NavLink("Help")),
                                dbc.NavItem(dbc.NavLink("About"))
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                # the row should expand to fill the available horizontal space
                className="flex-grow-1",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",
)

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

news_articles = [
    ['Louisville Cardinals lose to No. 7 Virginia Cavaliers in home ACC college basketball game', 'https://www.courier-journal.com/story/sports/college/louisville/2023/02/15/louisville-basketball-vs-uva-how-to-watch-stream-and-live-updates/69863328007/'],
    ['Virginia Avoids Disastrous Upset, Escapes Louisville With Sloppy 61-58 Win', 'https://www.si.com/college/virginia/basketball/virginia-avoids-disastrous-upset-escapes-louisville-with-sloppy-61-58-win'],
    ['Franklin, Clark help No. 7 UVA outlast ACC-worst Louisville', 'https://www.espn.com/mens-college-basketball/recap/_/gameId/401488496']
]


app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        header,
        html.Br(),
        dbc.Container(
            [
                html.Div(
                    [html.H1("UVABball Dashboard", style={'textAlign': 'center'})]
                ), 
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="https://cdn.vox-cdn.com/thumbor/O-tzXeJOjOWZpeoJP5JHRCajHFs=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/24432116/1247055249.jpg",
                                        style={
                                    'max-width': '100%',
                                    'height': 'auto',
                                }),
                                width=4),
                        dbc.Col(html.Div([
                                    html.H3("Recent News", style={'textAlign': 'center'}),
                                    html.Ul(id='news-list', children=[
                                        html.Li(html.A(i[0], href=i[1], target="_blank")) for i in news_articles
                                    ])
                                ]), 
                                width=8),
                    ]
                ),
                dcc.Graph(figure=fig)
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", mode='external', debug=True, port=8050)