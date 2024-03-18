# Dashboard for Aquarium

To install clone repository, and create a python 3.8 virtual environment using the requirements.txt file.

Then create a .env file and create DATABASE_URL = "". Which can be supplied if asked.

### Suggestion from copilot when using flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import base64
import cv2
import io

# Create the Dash app
app = dash.Dash(__name__)

# Function to convert the image format into jpeg
def encode_image(image):
    image_buffer = cv2.imencode('.jpg', image)[1].tobytes()
    image_base64 = base64.b64encode(image_buffer)
    return 'data:image/jpeg;base64,{}'.format(image_base64.decode())

# Dash layout to display the image
app.layout = html.Div([
    html.Img(id='live-update-image'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

# Callback function to update the image
@app.callback(Output('live-update-image', 'src'),
              [Input('interval-component', 'n_intervals')])
def update_image(n):
    frame = global_image
    return encode_image(frame)

if __name__ == '__main__':
    app.run_server(debug=True)
