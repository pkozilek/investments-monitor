import dash
from layout import layout
from libs.import_datasets import Datasets
from libs.callbacks.load_page import add_load_page_callback

app = dash.Dash(__name__)

app.layout = layout

data = Datasets()

add_load_page_callback(app, data)


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
