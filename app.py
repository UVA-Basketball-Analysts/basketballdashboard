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

navbarObject = NavBarBball()
navbar = navbarObject.construct_nav()

import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = JupyterDash(__name__, 
                  external_stylesheets=external_stylesheets,
                  suppress_callback_exceptions=True, use_pages=True)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar, 
    html.Br(),
    dash.page_container, 
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", mode='external', debug=True, port=8050)