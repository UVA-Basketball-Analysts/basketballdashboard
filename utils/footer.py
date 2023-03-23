import dash_bootstrap_components as dbc
external_stylesheets = [dbc.themes.BOOTSTRAP]
from dash import Dash, html

class Footer():
    def __init__(self):
        self.logo_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Virginia_Cavaliers_sabre.svg/1200px-Virginia_Cavaliers_sabre.svg.png'
        self.long_logo = 'assets/logos/logo_white_long.png'
        
    def construct_footer(self):
        return html.Footer(
            dbc.Container(
                [
                    dbc.Row([
                        dbc.Col(html.P("This dashboard was designed by Max Ryoo, Cepehr Alizadeh, and Seth Galluzzi under the supervision of Jonathan Kropko and Natalie Kupperman.", style={"margin-top":"1em"}),
                                width=8),
                    dbc.Col(html.Img(src=self.long_logo,
                                    style={
                                        'width': '100%',
                                        'height': 'auto',
                                    }
                                   ),
                                width=4)
                    ])
                ]
            ), className="footer"
        )