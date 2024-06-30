from flask import Flask
from dash import Dash, html
import pandas as pd

# Prétraitement des données
data = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 30]
})

# Créer une application Flask
server = Flask(__name__)
app = Dash(__name__, server=server, routes_pathname_prefix='/')

app.layout = html.Div([
    html.H1("Visualisation des Données"),
    html.Div([
        html.P("Voici un exemple de graphique"),
        # Graphique ou autres composants Dash
    ])
])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)