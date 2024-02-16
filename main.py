import database_communication as db
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            children="Aquarium Digital Twin User Interface",
            style={"textAlign": "center"},
        ),
        dcc.Dropdown(
            ["temperature", "ph", "dissolved_oxygen"],
            "temperature",
            id="dropdown-selection",
        ),
        dcc.Graph(id="graph-content"),
    ]
)


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    return px.line(
        data_frame=db.select_node_measurements_as_df(conn),
        x="timestamp",
        y=value,
        title=f"Line chart for {value}",
        color="node_id",
        labels={"timestamp": "Time", value: value, "node_id": "Node ID"},
    )


if __name__ == "__main__":
    conn = db.initialize_conn()
    app.run(debug=True)
