from dash import Dash
from .layout import layout
from .callbacks import register_callbacks

def create_dash_app(server):
    app = Dash(__name__, server=server, routes_pathname_prefix='/dash/')
    app.layout = layout
    register_callbacks(app)

    # Inclure les scripts Dash dans le template Flask
    with server.app_context():
        dash_scripts = app.config.external_scripts
        dash_stylesheets = app.config.external_stylesheets
        server.jinja_env.globals['dash_scripts'] = dash_scripts
        server.jinja_env.globals['dash_stylesheets'] = dash_stylesheets

    return app
