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
                                dbc.Col(dbc.NavbarBrand(self.logo_name, className="ms-2", style={"color":"white"})),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        href="/",
                        style={"textDecoration": "none"},
                    ),
                    dbc.Row(
                        [
                            dbc.NavbarToggler(id="navbar-toggler"),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavItem(dbc.NavLink(html.A("Home", href="/",style={"textDecoration": "none",'color':'white'}))),
                                        dbc.NavItem(dbc.NavLink(html.A("HKA", href="/hka",style={"textDecoration": "none",'color':'white'}))),
                                        dbc.NavItem(dbc.NavLink(html.A("Athleticism v Clinician Report", href="/ClinicianvAthleticism",style={"textDecoration": "none",'color':'white'}))),
                                        dbc.NavItem(dbc.NavLink(html.A("Jumps", href="/jumps",style={"textDecoration": "none",'color':'white'}))),
                                        dbc.NavItem(dbc.NavLink(html.A("Loading Strategies", href="/loadingstrats",style={"textDecoration": "none",'color':'white'}))),
                                        dbc.NavItem(dbc.NavLink(html.A("Squats", href="/squats",style={"textDecoration": "none",'color':'white'})),className="me-auto",),
                                        dbc.NavItem(dbc.NavLink("Help", style={"color":"white"})),
                                        dbc.NavItem(dbc.NavLink("About", style={"color":"white"}))
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
            class_name="headerUVA"
        )
