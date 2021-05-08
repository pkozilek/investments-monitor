from dash.dependencies import Input, Output
import dash_html_components as html
from libs.transformations.assets_analysis import get_asset_timeserie


def add_load_page_callback(app, data):
    @app.callback(
        Output("page-content", "children"),
        [Input("load-page-trigger", "children")],
    )
    def load_page(_):
        get_asset_timeserie(1, data)
        return html.H1("PAGE")
