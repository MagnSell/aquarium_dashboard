from dash import Dash, html, dcc, callback, Output, Input
import styles
import plotly.graph_objects as go

# Define the layout
model_tab_layout = html.Div(children=[
    html.H1('3D Model'),
    dcc.Graph(
        id='3d-model',
        style={'width': '800px', 'height': '600px'}
    )
])
