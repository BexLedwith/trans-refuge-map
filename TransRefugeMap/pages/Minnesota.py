from dash import Dash, dcc, Output, Input, html, register_page, dash_table, callback, ctx  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import pandas as pd        #pip install pandas
import plotly.graph_objects as go
import plotly.express as px
from urllib.request import urlopen
import json

register_page(__name__)

pd.options.mode.copy_on_write = True

# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)


df = pd.read_csv('assets/ResourcesfromMNTIRNPhysicalLocations.csv')

df['text'] = df['Resource Name'] + ' ' + df['Service Category']
# fig=px.choropleth(df,locations=["MN"], locationmode='USA-states', scope='usa', color=[0], color_continuous_midpoint=0, color_continuous_scale='BrBG')
fig = go.Figure(
    # data = go.Choropleth(locations=['MN'], locationmode='USA-states', z=[0], colorscale='BrBG', hoverinfo='skip', showscale=False)
)

categories = ['Legal Services','Organizing and Advocacy','Support and Advocacy','TPOC Resources and Services',
'Youth and Family Support and Services', 'Youth Healthcare', 'Youth Housing Support and Services']
colors = df['Service Category'].apply(lambda x: 1 if x=='Legal Services' else (2 if x=='Organizing and Advocacy' else 3 if x=='Support and Advocacy' else 4 if x=='TPOC Resources and Services' else 5 if x=='Youth and Family Support and Services' else 6 if x== 'Youth Healthcare' else 7))
for i in range(len(categories)):
    cat=categories[i]
    df_sub = df['Service Category'].isin([cat])
    df_sub=df[df_sub]
    fig.add_scattermapbox(
            lon=df_sub['long'],
            lat=df_sub['lat'],
            text=df_sub['text'],
            # marker= dict(color=colors[i],
            #              size=10,
            #              line_color='rgb(40,40,40)',
            #              line_width=0.5),
            marker=dict(
                size=10
            ),
            mode='markers',
            name=cat,
            hoverinfo='text'
    )
lat_foc= 46.7296
lon_foc= -94.6859
# fig.update_geos(
#     visible=False,
#     projection_scale=3.8,
#     center=dict(lat=lat_foc,lon=lon_foc)
# )

fig.update_geos(
    visible=False
)


fig.update_layout(dragmode=False,
                  height=600,
                  mapbox_bounds={"west": -97.5, "east": -89, "south": 43, "north": 49.5},
                  geo_scope='usa',
                  autosize=True,
                  mapbox_style="open-street-map",
                  margin={'r': 0, 't': 0, 'l': 0, 'b': 0},
images=[dict(
            source='https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/TRM_Logo.png',
            xref = 'paper',yref='paper',
            x=0, y=1,
            sizex=0.15, sizey=0.15,
            xanchor='left',yanchor='bottom'
        )],
hoverlabel=dict(
            bgcolor='white'
        ),
                  legend=dict(
                      orientation="h",
                      yanchor="bottom",
                      xref='paper',
                      yref='paper',
                      y=1,
                      xanchor='right',
                      x=1

                  ),
            annotations=[dict(
                x=0.55,
                y=.1,
                xref='paper',
                yref='paper',
                yshift=-50,
                text='Data Source: <a href="https://docs.google.com/document/d/1-1Z7KYtcjrxwvMOy3Luwt6ICnCpt5sgNTrYGPZtW_yk/edit?usp=sharing", target= "_blank" >MNTIRN Trans Resource Directory</a>',
                showarrow=False
            )]
        )
my_graph=dcc.Graph(figure=fig, config = {
'displaylogo':False,
    'modeBarButtonsToRemove': ['pan2d','zoom', 'pan','select','zoomIn','zoomOut','autoScale','resetScale', 'lasso2d', 'reset', 'resetView'],
    'toImageButtonOptions': {'filename':'mn_trans_resource_map_download'},
     'scrollZoom':False
})
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll',
        'borderRadius': '5px'
    }
}
resource_table = dash_table.DataTable(df.to_dict('records'),
                                     editable=False,
                                    style_data={
                                          'whiteSpace': 'normal',
                                          'height': 'auto',
                                      },
    columns=[{"id": "Resource Name", "name": "Resource Name", "presentation":"input"},{"id": "Service Category", "name": "Service Category", "presentation":"input"},
        {"id": "Link", "name": "Link", "presentation": "markdown"},
             {"id": "city", "name": "City", "presentation":"input"}
    ],
                                      markdown_options={"html":True}
                                      )
df_web = pd.read_csv('assets/ResourcesfromMNTIRNOnline.csv')

online_resource_table = dash_table.DataTable(df_web.to_dict('records'),
                                     editable=False,
                                    style_data={
                                          'whiteSpace': 'normal',
                                          'height': 'auto',
                                      },
    columns=[{"id": "Resource Name", "name": "Resource Name", "presentation":"input"},{"id": "Service Category", "name": "Service Category", "presentation":"input"},
        {"id": "Link", "name": "Link", "presentation": "markdown"},
    ],
                                      markdown_options={"html":True}
                                      )

layout = dbc.Container(
    [
        html.Div([
            dbc.Card(
                dbc.CardBody([
                    html.Div('The Minnesota Trans Resource Map is an interactive digital map based on local Minnesota resources found in MNTIRN’s Trans Resource Directory',
                     className="h4 mt-2"),
                    html.Div('This map and resource database are currently in development, and will continue to be developed through open cooperation. MNTIRN,the Minnesota Trans and Intersex Resource Network, is a collaboration between local LGBTQIA+ organizations and individuals with the goal of assisting Trans and Intersex folx coming to Minnesota.',
                     className="fs-5 mt-2"),
                    html.Div(children=[
                        dbc.Button('Find MNTIRN here: https://mntirnetwork.org', href='https://mntirnetwork.org/',
                                   external_link=True, target='_blank', className='me-1')
                    ], className='text-body'),
                    html.Div(children=[
                        dbc.Button('Submit resources here', href='https://forms.gle/7Mcbu24rMesh26ke8',
                                   external_link=True, target='_blank', className='me-1')
                    ], className='text-body mt-2')
        ])
            )]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.P(['Local and Digital Resources'], className='fw-bold mt-2'),
                    dbc.Accordion(
                        dbc.AccordionItem(
                            html.Pre([resource_table], style=styles['pre'], className='pt-2 pb-2'), title='Local Resources'
),start_collapsed=True
                    ),
dbc.Accordion(
                        dbc.AccordionItem(
                            html.Pre([online_resource_table], style=styles['pre'], className='pt-2 pb-2'), title='MN Digital Resources'
),start_collapsed=True
                    )
                ])
            ], width=10)
        ], justify='center', class_name='mt-1'),
        dbc.Row([
            dbc.Col([my_graph], width=10)
        ], justify='center'),
    ], fluid=True)

