from dash import Dash, html, page_container, page_registry  # pip install dash
import dash_bootstrap_components as dbc

trm_logo = 'assets/TRM_Logo.png'
# Build your components
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.PULSE])
server=app.server

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(f"{page['name']}", href=page["relative_path"])
         ) for page in page_registry.values()
    ],
    brand = html.Img(src=trm_logo, height='90px'),
    brand_href= "/",
    color="light",
    dark=False,
    class_name='dbc'
)

#customize layout
app.layout = html.Div([
    navbar,
    page_container
], className="dbc")


# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8054)