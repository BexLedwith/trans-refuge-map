from dash import Dash, html, page_container, page_registry, dcc  # pip install dash
import dash_bootstrap_components as dbc

trp_logo = 'assets/TRP_Logo.png'
trp_logo_blue = 'assets/TRP_logo_blue.png'
# Build your components
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LUX])
app.title = 'Trans Refuge Map'
server=app.server


navbar = dbc.NavbarSimple(
    children=[dbc.NavItem(
            dbc.NavLink(f"{page['name']}", href=page["relative_path"], class_name='text-uppercase fw-bold'),
) for page in page_registry.values()
    ],
    brand = html.Img(src=trp_logo_blue, height='90px'),
    brand_href= "/",
    color="secondary",
    dark=False,
    class_name='dbc'
               'text-end'
)


footer = html.Footer(
    [
        dbc.Card(
            dbc.CardBody([
                html.Div([
                             'Data is current through February 26, 2024'],
                         className='h6 fst-italic fw-normal mt-2'),
html.Div(children=[
                        html.A('Submit Legislative Updates/ Edits', href='https://forms.gle/XRrSekTeHXgZqBoAA',
                                 target='_blank')
                    ], className='text-body mt-2'),
                html.Div(['Disclaimer: The information on this website is not, nor is it intended to be, legal advice. © 2024 Queer Equity Institute'], className='blockquote-footer mt-2'),
                html.Div([dbc.Container([
                              dbc.Row([
                                  dbc.Col([
                                      html.Img(src='assets/TRP_Logo.png', style={'max-height': '50px', 'width': 'auto'})
                                  ],width=3),
                                  dbc.Col([html.Img(src='assets/FaviconQEI.png', style={'max-height': '50px','width':'auto'})], width=3),
                                    dbc.Col([
                                      html.A('Donate', href='https://app.hubspot.com/payments/FVtwGbJgyTT?referrer=PAYMENT_LINK', target='_blank')
                                  ], width=3),
                                  dbc.Col([
                                          html.A('Contact Us', href='mailto:info@queerequityinstitute.org', target='_blank')
                                  ], width=3)

                              ])
                          ])
                ])
                ]),
                className='border-top border white wrapper flex-grow-1'
        )
    ]
)


#customize layout
app.layout = html.Div([
    navbar,
    page_container,
    footer
], className="dbc")


# Run app
if __name__=='__main__':
    app.run_server(debug=True, port=8056)