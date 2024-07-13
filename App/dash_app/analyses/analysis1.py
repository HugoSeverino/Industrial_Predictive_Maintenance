from dash import html, dcc
import plotly.express as px
import pandas as pd
import os

# Chemin relatif au fichier CSV
base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, '..', '..', '..', 'Encoded', 'RGN', 'RGN_Date_Installation.csv')

# Lire les données du fichier CSV
data = pd.read_csv(csv_path)
data['Date de mise en service'] = pd.to_datetime(data['Date de mise en service'])

# Distribution des Dates de Mise en Service
fig = px.histogram(data, x='Date de mise en service', title='Distribution des Dates de Mise en Service')

layout = html.Div([
    html.H1("Analyse 1: Distribution des Dates de Mise en Service"),
    dcc.Graph(figure=fig)
])
