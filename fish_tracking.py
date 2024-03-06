from dash import Dash, html, dcc, callback, Output, Input
import styles
from dash_extensions import WebSocket
from dash_player import DashPlayer
import dash_bootstrap_components as dbc


fish_tracking_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H2(
                        children="Fish Tracking",
                        style=styles.header_style,
                    ),
                    width=6,
                ),
                dbc.Col(
                    html.H4(
                        children="Coordinates",
                        style=styles.header_style,
                    ),
                    width=6,
                ),
            ],
            align="center",
            style={'margin': '20px'}
        ),
        dbc.Row(
            [
                dbc.Col(
                    DashPlayer(
                        id="player",
                        url="https://www.youtube.com/watch?v=coUJ7Wge8zA",
                        controls=True,
                        width="100%",
                        height="500px",
                    ),
                    width=6,
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.Div(
                                "X: 0",
                                style=styles.sub_header_style,
                            ),
                            html.Div(
                                "Y: 0",
                                style=styles.sub_header_style,
                            ),
                            html.Div(
                                "Z: 0",
                                style=styles.sub_header_style,
                            ),
                        ],
                        style={'margin': '20px'}
                    ),
                    width=6,
                ),
            ],
            style={'margin': '20px'}
        ),
    ],
    style=styles.background_style
)
