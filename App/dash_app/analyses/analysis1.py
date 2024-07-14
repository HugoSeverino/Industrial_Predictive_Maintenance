from dash import html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import os



# Chemin relatif au fichier CSV
base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, '..', '..', '..', 'Encoded', 'RGN', 'RGN_Date_Installation.csv')

# Lire les données du fichier CSV
data = pd.read_csv(csv_path)
data['Date de mise en service'] = pd.to_datetime(data['Date de mise en service'])
data['Année de mise en service'] = data['Date de mise en service'].dt.year

def generate_analysis1_figures(df):

    # Regrouper les données par année pour la courbe
    df_grouped = df.groupby('Année de mise en service').size().reset_index(name='Counts')
    
    # Générer un scatter plot pour les dates de mise en service, coloré par modèle et fabricant
    fig_date = px.scatter(df, x='Année de mise en service', y='Description', color='Fabricant', 
                          title='Points des Dates de Mise en Service par Modèle et Fabricant',
                          labels={'Année de mise en service': 'Année de mise en service', 'Description': 'Modèle'},
                          symbol='Description')

    # Générer un sunburst chart pour les modèles et les fabricants
    fig_modele_fabricant = px.sunburst(df, path=['Fabricant', 'Description'], title='Répartition des Modèles par Fabricant')

    # Modifier les traces pour afficher les descriptions à l'extérieur du graphique
    fig_modele_fabricant.update_traces(textinfo='label+percent parent',insidetextorientation='radial')
    fig_modele_fabricant.update_layout(
        margin=dict(t=40, l=0, r=0, b=0),
        sunburstcolorway=["#636efa","#EF553B","#00cc96","#ab63fa","#19d3f3",
                          "#e763fa", "#FECB52","#FFA15A","#FF6692","#B6E880"]
    )
    
    return fig_date, fig_modele_fabricant

def apply_mapping_to_df(df, mapping_dict):
    for column, mappings in mapping_dict.items():
        if column in df.columns:
            df[column] = df[column].map(mappings).fillna(df[column])
    return df

fig_date, fig_modele_fabricant = generate_analysis1_figures(data)

layout = html.Div([
    html.H1("Analyse 1: Distribution des Dates de Mise en Service"),
    dcc.Graph(id='graph-date-1', figure=fig_date),
    html.H2("Répartition des Modèles par Fabricant"),
    dcc.Graph(id='graph-modele-fabricant-1', figure=fig_modele_fabricant),
    html.H2("Décrypter les données JSON"),
    dcc.Textarea(
        id='json-input-1',
        placeholder='Collez votre JSON ici...',
        style={'width': '100%', 'height': 200},
    ),
    html.Button('Décrypter', id='decrypt-button-1', n_clicks=0),
    html.Div(id='output-container-1')
])