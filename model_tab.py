from dash import Dash, html, dcc, callback, Output, Input
import styles
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

# Define the layout
model_tab_layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id='3d-model',
                        style={'width': '100%', 'height': '600px'}
                    ),
                    width=6
                ),
                dbc.Col(
                    html.Img(
                        src='aquarium_solid.png',
                        style={'width': '100%', 'height': '600px'}
                    ),
                    width=6
                )
            ]
        )
    ],
    fluid=True
)
