from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import database_communication as db
from dash_extensions import Lottie
import dash_bootstrap_components as dbc

from data_measurements_tab import data_measurements_layout
from fish_tracking import fish_tracking_layout
from model_tab import model_tab_layout

import styles
app = Dash(__name__,external_stylesheets=[dbc.themes.GRID])
app.config.suppress_callback_exceptions=True

app.layout = html.Div(
    [   
        dbc.Row([
            dbc.Col(
                Lottie(
                    options=dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice')),
                    width="100%", url="https://lottie.host/112227a8-57d8-481e-97ad-8d36d7ad0b8b/sTbI190hxb.json"
                ),
                style={'textAlign': 'left', 'background-color': styles.colors['background'], 'margin': '0px', 'padding': '10px 10px 10px 20px'},
                width=1,
            ),
            dbc.Col(
                html.H1(
                    children="Aquarium Digital Twin User Interface",
                    style=styles.header_style,
                ),  
            ),
            
        ], align="center"),

        dcc.Tabs(
            id="tabs",
            value="tab-1",
            children=[
                dcc.Tab(label="Data Measurements", value="tab-1"),
                dcc.Tab(label="Fish Tracking", value="tab-2"),
                dcc.Tab(label="3D Model", value="tab-3"),
            ],
        ),
        html.Div(id="tab-content"),
    ],
    style=styles.background_style,
)

@app.callback(Output("tab-content", "children"), Input("tabs", "value"))
def render_tab_content(tab):
    if tab == "tab-1":
        return data_measurements_layout
    elif tab == "tab-2":
        return fish_tracking_layout
    elif tab == "tab-3":
        return model_tab_layout


### Callbacks for the data measurements tab
@app.callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    return px.line(
        data_frame=db.get_newest_node_measurements_as_df(conn, n=100000),
        x="timestamp",
        y=value,
        title=f"Line chart for {value}",
        color="node_id",
        labels={"timestamp": "Time", value: value, "node_id": "Node ID"},
    )

### Callbacks for the fish tracking tab


### Callbacks for the 3D model tab
@app.callback(Output("3d-model", "figure"), Input("3d-model", "value"))
def update_3d_model(value):
    return px.scatter_3d(
        x=[10, 2, 3],
        y=[4, 5, 6],
        z=[7, 8, 9],
        title="3D scatter plot",
        labels={"x": "X", "y": "Y", "z": "Z"},
    )

if __name__ == "__main__":
    conn = db.initialize_conn()
    app.run(debug=True)
