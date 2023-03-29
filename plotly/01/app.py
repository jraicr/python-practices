from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children="Hello world")
])



if __name__ == '__main__':
    app.run_server(debug=True)