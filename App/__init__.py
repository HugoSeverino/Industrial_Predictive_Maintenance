from flask import Flask



def create_app():
    server = Flask(__name__)

    with server.app_context():
        # Enregistrer les routes Flask
        from . import routes
        routes.init_app(server)

        # Configurer Dash
        from .dash_app import create_dash_app
        create_dash_app(server)

    return server
