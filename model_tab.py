from dash import Dash, html, dcc, callback, Output, Input
import styles
import plotly.graph_objects as go

# Define the layout
model_tab_layout = html.Div(children=[
    html.H1('3D Model'),
    dcc.Graph(
        id='3d-model',
        figure=go.Figure(data=[go.Scatter3d(
            x=[1, 2, 3],
            y=[4, 5, 6],
            z=[7, 8, 9],
            mode='markers',
            marker=dict(
                size=12,
                color='blue',
                opacity=0.8
            )
        )]),
        style={'width': '800px', 'height': '600px'}
    )
])
