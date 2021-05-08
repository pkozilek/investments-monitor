from dash.dependencies import Input, Output
import dash_html_components as html


def add_load_page_callback(app, data):
    @app.callback(
        Output("page-content", "children"),
        [Input("load-page-trigger", "children")],
    )
    def load_page(_):
        print(data.index_values)
        return html.H1("PAGE")
