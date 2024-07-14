from dash import html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import os
import json

# Chemin relatif au fichier CSV
base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, '..', '..', '..', 'Encoded', 'RGN', 'RGN_Date_Installation.csv')

# Lire les données du fichier CSV
data = pd.read_csv(csv_path)
data['Date de mise en service'] = pd.to_datetime(data['Date de mise en service'])

def generate_analysis1_figures(df):
    fig_date = px.histogram(df, x='Date de mise en service', title='Distribution des Dates de Mise en Service')
    fig_fabricant = px.histogram(df, x='Fabricant', title='Répartition par Fabricant')
    fig_modele = px.histogram(df, x='Description', title='Répartition par Modèle')
    return fig_date, fig_fabricant, fig_modele

def apply_mapping_to_df(df, mapping_dict):
    for column, mappings in mapping_dict.items():
        if column in df.columns:
            df[column] = df[column].map(mappings).fillna(df[column])
    return df

fig_date, fig_fabricant, fig_modele = generate_analysis1_figures(data)

layout = html.Div([
    html.H1("Analyse 1: Distribution des Dates de Mise en Service"),
    dcc.Graph(id='graph-date-1', figure=fig_date),
    html.H2("Répartition par Fabricant"),
    dcc.Graph(id='graph-fabricant-1', figure=fig_fabricant),
    html.H2("Répartition par Modèle"),
    dcc.Graph(id='graph-modele-1', figure=fig_modele),
    html.H2("Décrypter les données JSON"),
    dcc.Textarea(
        id='json-input-1',
        placeholder='Collez votre JSON ici...',
        style={'width': '100%', 'height': 200},
    ),
    html.Button('Décrypter', id='decrypt-button-1', n_clicks=0),
    html.Div(id='output-container-1')
])