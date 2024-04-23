from dash import Dash, html, register_page  # pip install dash
import dash_bootstrap_components as dbc

register_page(__name__)

layout = dbc.Container([
html.Div([
            dbc.Card(
                dbc.CardBody([
                    html.Div(['Frequently Asked Questions:'],className='h3 mt-2'),

                    ])
            )
        ]),
    html.Div([
dbc.Card(
            dbc.CardBody([
        html.Div('Q: Who started this project and why?', className='text-body fw-bold'),
                    html.Div('A: This project is being developed by the Queer Equity Institute in collaboration with local, regional, and national partners. At the heart of our work lies a fundamental commitment to liberation, equity, and joy across the intersections of our communities. We hope to use this project and build upon it as a tool and resource for actualizing Trans Refuge.', className='text-body mt-2')
            ]),className='mt-2'
        ),
        dbc.Card(
            dbc.CardBody([
        html.Div('Q: What are the 5 best / worst states for trans people to live in?', className='text-body fw-bold'),
                    html.Div('A: This map is not meant to provide insight into direct comparison and rankings among states. Data from each state reflects the experiences of transgender people living in the state and how likely they are to face a dangerous situation given the political and legal landscape. Using different measures of this experience, such as access to health care and existence of discrimination protection laws, act as an indicator of the relative safety (and danger) in said state. Additionally, differences in state policy from on-the-ground enforcement, as well as ways the laws impact life (different impacts of an abortion protection law and anti-discrimination in schools law) make it difficult to draw ranked comparisons among the states.', className='text-body mt-2')
            ]), className='mt-2'
        )
    ], className='mt-2')
    ], fluid=True, className='d-flex flex-column min-vh-100 w-80')