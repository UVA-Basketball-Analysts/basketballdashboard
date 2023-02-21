import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

## news box
from utils.news import bballNews
newsObject = bballNews()
newsBox = newsObject.construct_news_pane()

## Tabs
from utils.tabs import BballTabs
tabObject = BballTabs()
tabs = BballTabs.constructTabs(tabObject,4)

from dash import html, dcc, callback, Input, Output
dash.register_page(__name__, path='/')

import plotly.graph_objects as go
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

layout =  html.Div(
    [
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
                        dbc.Col(newsBox,
                                width=8),
                    ]
                ),
                html.Br(),
                tabs[0],
                tabs[1]
            ]
        )
    ]
)

@callback(Output('tabs-content-inline-3', 'children'),
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
        return newsBox
    elif tab == 'tab-4':
        return dcc.Markdown(children = '''
        ## Markdown
        Yay!
        ''')
