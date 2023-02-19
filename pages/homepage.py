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