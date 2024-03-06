from dash import Dash, html, dcc, callback, Output, Input
import styles
data_measurements_layout = html.Div(
    [
        html.Div( children = [
            html.Div(
                children="Select the measurement to display",
                style=styles.sub_header_style,
        ),
            dcc.Dropdown(
                ["temperature", "ph", "dissolved_oxygen"],
                "temperature",
                id="dropdown-selection",
                style=styles.dropdown_style,
            ),
            dcc.Graph(id="graph-content"),
            html.Div()
        ],
            style={"margin": "100px"},
        ),
    ],
)
