from flask import Flask
from dash import Dash, html, dcc
import pandas as pd
import os
import plotly.express as px

# Chemin relatif au fichier CSV
csv_path = '../Encoded/RGN/RGN_Date_Installation.csv'

# Lire les données du fichier CSV
data = pd.read_csv(csv_path)

# Convertir la colonne des dates en type datetime
data['Date de mise en service'] = pd.to_datetime(data['Date de mise en service'])


# Distribution des Dates de Mise en Service
fig1 = px.histogram(data, x='Date de mise en service', title='Distribution des Dates de Mise en Service')

# Nombre d'Équipements par Fabricant
fig2 = px.bar(data, x='Fabricant', title="Nombre d'Équipements par Fabricant")

# Répartition des Équipements par Fabricant
fig3 = px.pie(data, names='Fabricant', title='Répartition des Équipements par Fabricant')

# Évolution du Nombre d'Équipements Installés par Année
data['Année de mise en service'] = data['Date de mise en service'].dt.year
fig4 = px.line(data.groupby('Année de mise en service').size().reset_index(name='Nombre d\'équipements'),
               x='Année de mise en service', y='Nombre d\'équipements',
               title='Évolution du Nombre d\'Équipements Installés par Année')

# Créer une application Flask
server = Flask(__name__)
app = Dash(__name__, server=server, routes_pathname_prefix='/')

app.layout = html.Div([
    html.H1("Visualisation des Données des Équipements"),
    html.Div([
        html.H2("Distribution des Dates de Mise en Service"),
        dcc.Graph(figure=fig1)  # Afficher le graphique
    ]),
    html.Div([
        html.H2("Nombre d'Équipements par Fabricant"),
        dcc.Graph(figure=fig2)  # Afficher le graphique
    ]),
    html.Div([
        html.H2("Répartition des Équipements par Fabricant"),
        dcc.Graph(figure=fig3)  # Afficher le graphique
    ]),
    html.Div([
        html.H2("Évolution du Nombre d'Équipements Installés par Année"),
        dcc.Graph(figure=fig4)  # Afficher le graphique
    ])
])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)