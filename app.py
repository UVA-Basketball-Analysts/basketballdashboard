import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import dash
from dash import Dash
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from utils.navbar import NavBarBball
from utils.footer import Footer
navbarObject = NavBarBball()
navbar = navbarObject.construct_nav()
footerObject = Footer()
footer = footerObject.construct_footer()
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = JupyterDash(__name__, 
                  external_stylesheets=external_stylesheets,
                  suppress_callback_exceptions=True, use_pages=True)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar, 
    html.Div([
        html.Br(),
        dash.page_container, 
        html.Br(),
    ],style={"flex":"1"}),
    footer
    
], style={"min-height":"100vh", 'display':'flex', 'flex-direction':'column'})

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", mode='external', debug=True, port=8050)
