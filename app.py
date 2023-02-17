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
external_stylesheets = [dbc.themes.BOOTSTRAP]
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
markdown_text = '''

### Header of Markdown
Some content

'''
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        header,
        html.Br(),
        dbc.Container(
            [
                # html.Div(
                    # [
                        html.H1(
                            [
                                html.Div([
                                    html.Div([
                                        html.Div([], className="lines")
                                    ], className="ball"),
                                    html.Div([],className="shadow")
                                ], className="basketball"),
                                "UVABball Dashboard"
                            ], style={'text-align': 'center'}),
                    # ]
                # ), 
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
                                    ]),
                                    dcc.Markdown(children = markdown_text)
                                ]),
                                width=8),
                    ]
                ),
                dbc.Row([
                    dbc.Col(dcc.Graph(figure=fig),width=6),
                    dbc.Col(dcc.Graph(figure=fig),width=6)
                ]),
                dcc.Tabs(id="tabs-inline", value='tab-1', children=[
                    dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Tab 3', value='tab-3', style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Tab 4', value='tab-4', style=tab_style, selected_style=tab_selected_style),
                ], style=tabs_styles),
                html.Div(id='tabs-content-inline-3')
            ]
        )
    ]
)
@app.callback(Output('tabs-content-inline-3', 'children'),
              Input('tabs-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return dbc.Row([
                    dbc.Col(dcc.Graph(figure=fig),width=6),
                    dbc.Col(dcc.Graph(figure=fig),width=6)
                ])
    elif tab == 'tab-2':
        return html.Div([
            html.Img(src="https://cdn.vox-cdn.com/thumbor/O-tzXeJOjOWZpeoJP5JHRCajHFs=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/24432116/1247055249.jpg",
                                        style={
                                    'max-width': '100%',
                                    'height': 'auto',
                                })
        ])
    elif tab == 'tab-3':
        return html.Div([
                html.H3("Recent News", style={'textAlign': 'center'}),
                html.Ul(id='news-list', children=[
                    html.Li(html.A(i[0], href=i[1], target="_blank")) for i in news_articles
                ])
            ])
    elif tab == 'tab-4':
        return dcc.Markdown(children = markdown_text)

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", mode='external', debug=True, port=8050)
