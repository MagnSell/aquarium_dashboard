from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import database_communication as db

from data_measurements_tab import data_measurements_layout
import styles
app = Dash(__name__)


app.layout = html.Div(
    [
        html.H1(
            children="Aquarium Digital Twin User Interface",
            style=styles.header_style,

        ),
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
        return data_measurements_layout
    elif tab == "tab-3":
        return data_measurements_layout


### Callbacks for the data measurements tab
@app.callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    return px.line(
        data_frame=db.select_node_measurements_as_df(conn).iloc[10:],
        x="timestamp",
        y=value,
        title=f"Line chart for {value}",
        color="node_id",
        labels={"timestamp": "Time", value: value, "node_id": "Node ID"},
    )

if __name__ == "__main__":
    conn = db.initialize_conn()
    app.run(debug=True)
