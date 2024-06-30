from flask import Flask
from dash import Dash, html, dcc
import pandas as pd
import os
import plotly.express as px

# Prétraitement des données
data = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 30]
})

# Créer une figure Plotly
fig = px.bar(data, x='Category', y='Values', title='Exemple de Graphique')

# Créer une application Flask
server = Flask(__name__)
app = Dash(__name__, server=server, routes_pathname_prefix='/')

app.layout = html.Div([
    html.H1("Visualisation des Données"),
    html.Div([
        html.P("Voici un exemple de graphique"),
        dcc.Graph(figure=fig)  # Afficher le graphique
    ])
])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)