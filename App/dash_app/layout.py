from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Analyse 1", href="/dash/analysis1")),
            dbc.NavItem(dbc.NavLink("Analyse 2", href="/dash/analysis2")),
            dbc.NavItem(dbc.NavLink("Analyse 3", href="/dash/analysis3")),
        ],
        brand="Maintenance Prédictive",
        brand_href="/dash/",
        color="primary",
        dark=True,
    ),
    dbc.Container(id='page-content', className="mt-4"),
])
