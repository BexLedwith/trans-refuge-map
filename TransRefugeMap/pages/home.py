from dash import Dash, html, register_page, dcc  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd                        # pip install pandas

register_page(__name__, "/")

# data
df_states = pd.read_csv("https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_States-Table%201.csv")
df_states.drop(['State'], axis=1, inplace=True)
df_states.set_index('State Code').reset_index(inplace=True)

state_refuge = ['Shield Law', 'Gender Marker on ID (adult)', 'Gender Marker on ID (minor)',
          'Gender Marker Options on ID', 'Gender Marker on Birth Certificate (adult)', 'Gender Marker on Birth Certificate (minor)',
           'Gender Marker Options on Birth Certificate', 'Name Change (adult)', 'Name Change (minor)', 'Non-Discrimination']
state_refuge_data = df_states.copy()
state_refuge_data = state_refuge_data[state_refuge] 
state_refuge_data['Trans Refuge Rank'] = state_refuge_data.mean(axis=1).astype(float)
state_refuge_data['State Code'] = df_states['State Code']

#components
fig = px.choropleth(data_frame=state_refuge_data,
                            locations='State Code',
                            locationmode="USA-states",
                            scope="usa",
                            height=600,
                            color='Trans Refuge Rank',
                            color_continuous_scale='Darkmint'
                            )

mygraph = dcc.Graph(figure=fig, config={
     'displayModeBar':False,
     'scrollZoom':False
        
})

#layout
layout = dbc.Container(
    [
        html.Div([
            html.Div('The Trans Refuge Map is an interactive, visual resource providing a guide to trans refuge policies, protections, legislation, elected officials.',
                     className="h6"),
            html.Div('View by topic, single-issue, or create your own map view.', className='text-body'),
            html.Div('See our Trans Refuge Map below:', className='text-body')
        ]),
        dbc.Row([
            dbc.Col([mygraph], width=12)
        ], justify='center'),
        dbc.Row([
            dbc.Row('This map shows compares data gathered on:'),
            dbc.Row('Shield Laws'),
            dbc.Row('Name and Gender Marker Changes'),
            dbc.Row('Nondiscrimination Protections')
        ], justify='center')
    ], fluid=True)
