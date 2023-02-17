import dash_bootstrap_components as dbc
external_stylesheets = [dbc.themes.BOOTSTRAP]
from dash import Dash, html

class NavBarBball():
    def __init__(self):
        self.logo_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/d/d1/Virginia_Cavaliers_sabre.svg/1200px-Virginia_Cavaliers_sabre.svg.png'
        self.logo_name = 'BBALL-Dash'
        
    def construct_nav(self):
        return dbc.Navbar(
            dbc.Container(
                [
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src=self.logo_url, height="30px")),
                                dbc.Col(dbc.NavbarBrand(self.logo_name, className="ms-2")),
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