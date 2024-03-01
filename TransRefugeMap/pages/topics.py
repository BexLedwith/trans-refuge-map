from dash import Dash, dcc, Output, Input, html, register_page, callback  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd                        # pip install pandas

register_page(__name__)


# incorporate data into app
df_states = pd.read_csv("https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_States-Table%201.csv")
df_states.drop(['State'], axis=1, inplace=True)
df_states.set_index('State Code').reset_index(inplace=True)


df_territories = pd.read_csv("https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_States-Table%201.csv")

topics = ['Trans Refuge', 'Family Services', 'Gender Inclusive Laws & Policies','Reproductive Rights', 'Hate Legislation']

state_refuge = ['Shield Law', 'Gender Marker on ID (adult)', 'Gender Marker on ID (minor)',
          'Gender Marker Options on ID', 'Gender Marker on Birth Certificate (adult)', 'Gender Marker on Birth Certificate (minor)',
           'Gender Marker Options on Birth Certificate', 'Name Change (adult)', 'Name Change (minor)', 'Non-Discrimination']
state_refuge_data = df_states.copy()
state_refuge_data = state_refuge_data[state_refuge] 
state_refuge_data['Trans Refuge Rank'] = state_refuge_data.mean(axis=1).astype(float)
state_refuge_data['State Code'] = df_states['State Code']
state_refuge_string = ', '.join(state_refuge)

state_family = ['Foster Care Non-Discrimination','Adoption Non-Discrimination',
                'Child Welfare Non-Discrimination for LGBTQ Youth','Recognition of Assisted-Reproduction','VAP for Non-Genetic LGBTQ Parents']
state_family_data = df_states.copy()
state_family_data = state_family_data[state_family]
state_family_data['Family Services Rank'] = state_family_data.mean(axis=1).astype(float)
state_family_data['State Code'] = df_states['State Code']
state_family_string = ', '.join(state_family)


state_gi = ['Gender Inclusive Bathroom Laws (Adult)','Gender Inclusive Bathroom Laws (minor)',
            'LGBTQ Inclusive Curriculum','Anti-Bullying Legal Protections for TGNC* students',
            'Non-Discrimination  Protections for LGBTQ Students','Gay/ Trans Panic Defense Ban','Hate Crime Laws Specific to Gender Identity',
            'Jury Service Non-Discrimination Based on Gender Identity','Gender Inclusive Correctional Housing ' ,'Gender Affirming Care in Correctional Facilities']
state_gi_data = df_states.copy()
state_gi_data = state_gi_data[state_gi]
state_gi_data['G.I. Laws Rank'] = state_gi_data.mean(axis=1).astype('float')
state_gi_data['State Code'] = df_states['State Code']
state_gi_string = ', '.join(state_gi)


state_repro = ['Abortion Access', 'Interstate Abortion Shield Law']
state_repro_data = df_states.copy()
state_repro_data = state_repro_data[state_repro]
state_repro_data['Reproductive Rights Rank'] = state_repro_data.mean(axis=1).astype('float')
state_repro_data['State Code'] = df_states['State Code']
state_repro_string = ', '.join(state_repro)

state_hate = ['Trans Bathroom Ban K-12','Trans Bathroom Ban in Schools and Government Buildings','State Defines Sex','Broad ‘RFRA’',
              'Religious Exemption for Child Welfare','Religious Exemption for Medical Professionals','Marriage Services and/or Marriage License Denial',
              'Drag Ban','Don’t Say Gay','Specific Subject Restrictions','Parental Notification (opt-in or opt-out)','Sports Ban','Forced Outing in Schools','Ban on Best Practice Medical Care for Trans Youth','Barriers to Identity Documents']
state_hate_data = df_states.copy()
state_hate_data = state_hate_data[state_hate]
state_hate_data['Hate Legislation Rank'] = state_hate_data.mean(axis=1).astype('float')
state_hate_data['State Code'] = df_states['State Code']
state_hate_string = ', '.join(state_hate)



# Build components
appInfo = dcc.Markdown('##### Select from the dropdown to view law collections based on category: ')
topicInfo = dcc.Markdown(children='') #empty markdown
mygraph = dcc.Graph(figure={}, config={
     'displayModeBar':False,
     'scrollZoom':False
        
})

dropdown = dcc.Dropdown(options=topics, 
                        value='Trans Refuge',  # initial value displayed when page first loads
                        clearable=False)

# Customize Layout
layout = dbc.Container([
    dbc.Container([
        dbc.Container(
            dbc.Row([
            dbc.Col([appInfo], width=6),
            dbc.Col([dropdown], width=6)
            ], justify='center', class_name='mt-5')
        ),    
        dbc.Row([
            dbc.Col([mygraph], width=12)
        ], justify='center'),
        dbc.Row([
            dbc.Col([topicInfo], width=12)
        ], justify='center')
    ])

], fluid=True)

#callback

@callback(
    Output(mygraph, 'figure'),
    Output(topicInfo, 'children'),
    Input(dropdown, 'value')
)
def update_graph(topic):  
    # https://plotly.com/python/choropleth-maps/
    if topic == 'Trans Refuge': 
        fig = px.choropleth(data_frame=state_refuge_data,
                            locations='State Code',
                            locationmode="USA-states",
                            scope="usa",
                            height=600,
                            color='Trans Refuge Rank',
                            color_continuous_scale='Darkmint'
                            )
        topic_descriptor = state_refuge_string
    elif topic == 'Family Services':
        fig = px.choropleth(data_frame=state_family_data,
                            locations='State Code',
                            locationmode="USA-states",
                            scope="usa",
                            height=600,
                            color='Family Services Rank')
        topic_descriptor = state_family_string
    elif topic == 'Gender Inclusive Laws & Policies':
        fig = px.choropleth(data_frame=state_gi_data,
                            locations='State Code',
                            locationmode="USA-states",
                            scope="usa",
                            height=600,
                            color='G.I. Laws Rank')
        topic_descriptor = state_gi_string
    elif topic == 'Reproductive Rights':
        fig = px.choropleth(data_frame=state_repro_data,
                            locations='State Code',
                            locationmode="USA-states",
                            scope="usa",
                            height=600,
                            color='Reproductive Rights Rank')
        topic_descriptor = state_repro_string
    else:
        fig = px.choropleth(data_frame=state_hate_data,
                            locations='State Code',
                            locationmode="USA-states",
                            scope="usa",
                            height=600,
                            color='Hate Legislation Rank')
        topic_descriptor = state_hate_string




    return fig, '**Laws & Policies Ranked:** ' + topic_descriptor  # returned objects are assigned to the component property of the Output
