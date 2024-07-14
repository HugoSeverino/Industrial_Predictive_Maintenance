from dash import Dash, Input, Output, State, html, dcc
from .analyses import analysis1
import json
import html
from App.utils import decrypt_json

def register_callbacks(app):
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/dash/analysis1':
            return analysis1.layout
        
        else:
            return "Bienvenue sur l'application de Maintenance Prédictive"

    @app.callback(
        [Output('graph-date-1', 'figure'),
         Output('graph-fabricant-1', 'figure'),
         Output('graph-modele-1', 'figure'),
         Output('output-container-1', 'children')],
        [Input('decrypt-button-1', 'n_clicks')],
        [State('json-input-1', 'value')]
    )
    def update_graphs_1(n_clicks, json_text):
        if n_clicks > 0 and json_text:
            mapping_df, error_message = decrypt_json(json_text)
            if mapping_df is not None:
                df_mapped = analysis1.apply_mapping_to_df(analysis1.data.copy(), mapping_df)
                fig_date, fig_fabricant, fig_modele = analysis1.generate_analysis1_figures(df_mapped)
                return fig_date, fig_fabricant, fig_modele, ""
            return {}, {}, {}, error_message
        
        fig_date, fig_fabricant, fig_modele = analysis1.generate_analysis1_figures(analysis1.data)
        return fig_date, fig_fabricant, fig_modele, ""