from dash import Dash
from .layout import layout
from .callbacks import register_callbacks

def create_dash_app(server):
    app = Dash(__name__, server=server, routes_pathname_prefix='/dash/')
    app.layout = layout
    register_callbacks(app)
    return app
