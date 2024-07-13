from dash.dependencies import Input, Output
from .analyses import analysis1

def register_callbacks(app):
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/dash/analysis1':
            return analysis1.layout
        
        else:
            return "Bienvenue sur l'application de Maintenance Prédictive"
