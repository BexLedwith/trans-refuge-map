from dash import Dash, dcc, Output, Input, html, register_page, callback, callback_context  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd        #pip install pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots

register_page(__name__)

# incorporate data into app
df_states = pd.read_csv("https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_States-Table%201.csv")
df_states.drop(['State'], axis=1, inplace=True)
df_states.set_index('State Code').reset_index(inplace=True)
df_states = df_states.replace({True: 1, False: 0})


df_territories = pd.read_csv(
    "https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_Territories-Table%201.csv")
territory_names_list = df_territories['Territory Name'].to_list()
df_territories.drop(['Territory Name'], axis=1, inplace=True)
df_territories.set_index('Territory Code').reset_index(inplace=True)

df_electeds = pd.read_csv('https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/state_electeds.csv', dtype={'FIPS': str})
df_electeds_wide = df_electeds[['Name', 'Title', 'Lat', 'Lon']]

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


#legislative list
leg_list = state_refuge + state_family + state_gi + state_repro + state_hate

# territories
territory_refuge = ['Shield Law', 'Gender Marker on ID (adult)', 'Gender Marker on ID (minor)',
                'Gender Marker Options on ID', 'Gender Marker on Birth Certificate (adult)',
                'Gender Marker on Birth Certificate (minor)',
                'Gender Marker Options on Birth Certificate', 'Name Change (adult)', 'Name Change (minor)',
                'Non-Discrimination']
territory_refuge_data = df_territories.copy()
#convert bool to int
territory_refuge_data = territory_refuge_data.replace({True: 1, False: 0})
territory_refuge_data = territory_refuge_data[territory_refuge]
territory_refuge_data['Trans Refuge Rank'] = territory_refuge_data.mean(axis=1).astype(float)

#as list
territory_refuge_list=territory_refuge_data['Trans Refuge Rank'].tolist()
territory_refuge_data['Territory Code'] = df_territories['Territory Code']
territory_code_list=territory_refuge_data['Territory Code'].tolist()
territory_refuge_rank_wide = territory_refuge_data.copy()
territory_refuge_rank_wide = territory_refuge_data[['Territory Code', 'Trans Refuge Rank']]
territory_refuge_string = ', '.join(territory_refuge)

territory_family = ['Foster Care Non-Discrimination', 'Adoption Non-Discrimination',
                'Child Welfare Non-Discrimination for LGBTQ Youth', 'Recognition of Assisted-Reproduction',
                'VAP for Non-Genetic LGBTQ Parents']
territory_family_data = df_territories.copy()
territory_family_data = territory_family_data.replace({True: 1, False: 0})
territory_family_data = territory_family_data[territory_family]
territory_family_data['Family Services Rank'] = territory_family_data.mean(axis=1).astype(float)
territory_family_data['Territory Code'] = df_territories['Territory Code']
territory_family_string = ', '.join(territory_family)
territory_family_rank_wide = territory_family_data.copy()
territory_family_rank_wide = territory_family_rank_wide[['Territory Code', 'Family Services Rank']]

territory_gi = ['Gender Inclusive Bathroom Laws (Adult)', 'Gender Inclusive Bathroom Laws (minor)',
            'LGBTQ Inclusive Curriculum', 'Anti-Bullying Legal Protections for TGNC* students',
            'Non-Discrimination  Protections for LGBTQ Students', 'Gay/ Trans Panic Defense Ban',
            'Hate Crime Laws Specific to Gender Identity',
            'Jury Service Non-Discrimination Based on Gender Identity', 'Gender Inclusive Correctional Housing ',
            'Gender Affirming Care in Correctional Facilities']
territory_gi_data = df_territories.copy()
territory_gi_data = territory_gi_data.replace({True: 1, False: 0})
territory_gi_data = territory_gi_data[territory_gi]
territory_gi_data['G.I. Laws Rank'] = territory_gi_data.mean(axis=1).astype('float')
territory_gi_data['Territory Code'] = df_territories['Territory Code']
territory_gi_string = ', '.join(territory_gi)
territory_gi_rank_wide = territory_gi_data.copy()
territory_gi_rank_wide = territory_gi_rank_wide[['Territory Code', 'G.I. Laws Rank']]

territory_repro = ['Abortion Access', 'Interstate Abortion Shield Law']
territory_repro_data = df_territories.copy()
territory_repro_data = territory_repro_data.replace({True: 1, False: 0})
territory_repro_data = territory_repro_data[territory_repro]
territory_repro_data['Reproductive Rights Rank'] = territory_repro_data.mean(axis=1).astype('float')
territory_repro_data['Territory Code'] = df_territories['Territory Code']
territory_repro_string = ', '.join(territory_repro)
territory_repro_rank_wide = territory_repro_data.copy()
territory_repro_rank_wide = territory_repro_rank_wide[['Territory Code', 'Reproductive Rights Rank']]

territory_hate = ['Trans Bathroom Ban K-12', 'Trans Bathroom Ban in Schools and Government Buildings', 'State Defines Sex',
              'Broad ‘RFRA’',
              'Religious Exemption for Child Welfare', 'Religious Exemption for Medical Professionals',
              'Marriage Services and/or Marriage License Denial',
              'Drag Ban', 'Don’t Say Gay', 'Specific Subject Restrictions', 'Parental Notification (opt-in or opt-out)',
              'Sports Ban', 'Forced Outing in Schools', 'Ban on Best Practice Medical Care for Trans Youth',
              'Barriers to Identity Documents']
territory_hate_data = df_territories.copy()
territory_hate_data = territory_hate_data.replace({True: 1, False: 0})
territory_hate_data = territory_hate_data[territory_hate]
territory_hate_data['Hate Legislation Rank'] = territory_hate_data.mean(axis=1).astype('float')
territory_hate_data['Territory Code'] = df_territories['Territory Code']
territory_hate_string = ', '.join(territory_hate)
territory_hate_rank_wide = territory_hate_data.copy()
territory_hate_rank_wide = territory_hate_rank_wide[['Territory Code', 'Hate Legislation Rank']]

territory_wide = territory_refuge_rank_wide.copy()
territory_wide['Family Services'] = territory_family_data['Family Services Rank']
territory_wide['Gender Inclusive Laws & Policies'] = territory_gi_data['G.I. Laws Rank']
territory_wide['Reproductive Rights'] = territory_repro_data['Reproductive Rights Rank']
territory_wide['Hate Legislation'] = territory_hate_data['Hate Legislation Rank']

dc_wide = territory_wide['Territory Code'].isin(['DC'])
dc_wide = territory_wide[dc_wide]
as_wide = territory_wide['Territory Code'].isin(['AS'])
as_wide = territory_wide[as_wide]
gu_wide = territory_wide['Territory Code'].isin(['GU'])
gu_wide = territory_wide[gu_wide]
mp_wide = territory_wide['Territory Code'].isin(['MP'])
mp_wide = territory_wide[mp_wide]
pr_wide = territory_wide['Territory Code'].isin(['PR'])
pr_wide = territory_wide[pr_wide]
vi_wide = territory_wide['Territory Code'].isin(['VI'])
vi_wide = territory_wide[vi_wide]

# Build components
appInfo = dcc.Markdown('##### Create your own map view by selected legislation to rank:')
toggleInfo = dcc.Markdown('###### Use this toggle switch to view 2S+TGNC reps on the map:')
topicInfo = dcc.Markdown(children='') #empty markdown
mygraph = dcc.Graph(figure={}, config={
     'displaylogo':False,
    'modeBarButtonsToRemove': ['zoom', 'pan','select','zoomIn','zoomOut','autoScale','resetScale', 'lasso2d', 'reset'],
    'toImageButtonOptions': {'filename':'custom_map_download'},
     'scrollZoom':False

})
territory_graph = dcc.Graph(figure={}, config={
    'displayModeBar': False,
    'scrollZoom': False},
        style={'height':200})

territory_key = dbc.Col(['Territories Reference: AS - American Samoa, GU - Guam, MP - N. Mariana Islands, PR - Puerto Rico, VI - U.S. Virgin Islands'], width=12, className='fs-6')

select_all = dcc.Checklist(
                        options=[{'label':'Select All', 'value':'All'}],
                        value=['All'],
                        labelStyle={'display':'inline-block'},
                        id='all_checklist'

)
select_refuge_laws = dcc.Checklist(
    options=state_refuge,
    value=[],
    id='refuge_checklist'
)
select_family_laws = dcc.Checklist(
    options=state_family,
    value=[],
    id='family_checklist'
)
select_gi_laws = dcc.Checklist(
    options=state_gi,
    value=[],
    id='gi_checklist'
)
select_repro_laws = dcc.Checklist(
    options=state_repro,
    value=[],
    id='repro_checklist'
)
select_hate_laws = dcc.Checklist(
    options=state_hate,
    value=[],
    id='hate_checklist'
)
reps_toggle = dbc.Switch(
    label='2S+TGNC State Reps',
    value=False)
# Customize Layout
layout = dbc.Container([
            dbc.Card(
                dbc.CardBody(
                    [
            dbc.Row([
                dbc.Col([appInfo], width=9),
                dbc.Col([select_all], width=3)
            ],justify='center', class_name='mt-2'),
            dbc.Row([
                dbc.Col([dbc.Accordion([dbc.AccordionItem(select_refuge_laws, title='Trans Refuge Laws', class_name='border border-tertiary bg-transparent')], start_collapsed=True)], width=12),
                dbc.Col([dbc.Accordion([dbc.AccordionItem(select_family_laws, title="Family Services", class_name='border border-tertiary bg-transparent mt-1')], start_collapsed=True)], width=12),
                dbc.Col([dbc.Accordion([dbc.AccordionItem(select_gi_laws, title="GI Laws", class_name='border border-tertiary bg-transparent mt-1')], start_collapsed=True)], width=12),
                dbc.Col([dbc.Accordion([dbc.AccordionItem(select_repro_laws, title="Reproductive Rights", class_name='border border-tertiary bg-transparent mt-1')], start_collapsed=True)], width=12),
                dbc.Col([dbc.Accordion([dbc.AccordionItem(select_hate_laws, title="Hate Legislation", class_name='border border-tertiary bg-transparent mt-1')], start_collapsed=True)], width=12)
                ], justify='center',id='cols_of_checklists'),
            dbc.Row([
                dbc.Col([toggleInfo], width=6),
                dbc.Col([reps_toggle], width=6)
            ],justify='center', class_name='mt-2 mb-1'),
                    ]
                )
        ),
        dbc.Row([
            dbc.Col([mygraph], width=12)
        ], justify='center'),
        dbc.Row([
            dbc.Col([territory_graph], width=12)
            ], justify='center'),
dbc.Row([
            territory_key
            ], justify='center'),
        # dbc.Row([
        #     dbc.Row([' Laws & Policies Ranked:'], class_name='h3 mt-2'),
        #     dbc.Col([topicInfo], class_name='h6 fw-normal mt-2')
        # ], justify='center')
], fluid=True)

#callback

@callback(
    Output('refuge_checklist', 'value'),
    Output('family_checklist', 'value'),
    Output('gi_checklist', 'value'),
    Output('repro_checklist', 'value'),
    Output('hate_checklist', 'value'),
    Output('all_checklist', 'value'),
    Input('refuge_checklist', 'value'),
    Input('family_checklist', 'value'),
    Input('gi_checklist', 'value'),
    Input('repro_checklist', 'value'),
    Input('hate_checklist', 'value'),
    Input('all_checklist', 'value')
)

def sync_checklists(refuge_selected, family_selected, gi_selected, repro_selected, hate_selected, all_selected):
    ctx = callback_context
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if input_id == 'refuge_checklist':
        all_selected = ['All'] if set(refuge_selected) == set(state_refuge) else []
    elif input_id == 'family_checklist':
        all_selected = ['All'] if set(family_selected) == set(state_family) else []
    elif input_id == 'gi_checklist':
        all_selected = ['All'] if set(gi_selected) == set(state_gi) else []
    elif input_id == 'repro_checklist':
        all_selected = ['All'] if set(repro_selected) == set(state_repro) else []
    elif input_id == 'hate_checklist':
        all_selected = ['All'] if set(hate_selected) == set(state_hate) else []
    else:
        refuge_selected = state_refuge if all_selected else []
        family_selected = state_family if all_selected else []
        gi_selected = state_gi if all_selected else []
        repro_selected = state_repro if all_selected else []
        hate_selected = state_hate if all_selected else []

    return refuge_selected, family_selected, gi_selected, repro_selected, hate_selected, all_selected

@callback(
    Output(mygraph,'figure'),
    Output(territory_graph,'figure'),
    # Output(topicInfo,'children'),
    Input('refuge_checklist', 'value'),
    Input('family_checklist', 'value'),
    Input('gi_checklist', 'value'),
    Input('repro_checklist', 'value'),
    Input('hate_checklist', 'value'),
    Input('all_checklist', 'value'),
    Input(reps_toggle, 'value')

)

def update_graph(refuge_selected, family_selected, gi_selected, repro_selected, hate_selected, all_selected, toggle):
    df = df_states.copy()
    df_t = df_territories.copy()
    selected_laws = refuge_selected + family_selected + gi_selected + repro_selected + hate_selected
    selected_laws_string = ', '.join(selected_laws)
    if all_selected:
        df_selected = df
        df_t_selected = df_t
    else:
        df_selected = df[selected_laws]
        df_t_selected = df_t[selected_laws]
    df_selected['Selected Rank'] = df_selected.loc[:,selected_laws].mean(axis=1).astype('float')
    df_selected['State Code'] = df_states['State Code']
    df_t_selected['Selected Rank'] = df_t_selected.loc[:, selected_laws].mean(axis=1).astype('float')
    color_min = df_selected['Selected Rank'].min()
    color_max = df_selected['Selected Rank'].max()

    if df_t_selected['Selected Rank'].min() < color_min:
        color_min = df_t_selected['Selected Rank'].min()
    else:
        color_min = color_min
    if df_t_selected['Selected Rank'].max() > color_max:
        color_max = df_t_selected['Selected Rank'].max()
    else:
        color_max = color_max
    # fig = px.choropleth(df_selected,
    #                     locations='State Code',
    #                     locationmode='USA-states',
    #                     scope='usa',
    #                     height=600,
    #                     color='Selected Rank',
    #                     color_continuous_scale='Plotly3_r',
    #                     range_color=[color_min, color_max],
    #                     )
    fig = go.Figure(data=go.Choropleth(locations=df_selected['State Code'],
                                       z=df_selected['Selected Rank'],
                                       locationmode='USA-states',
                                       zmin=color_min,
                                       zmax=color_max,
                                       colorscale='Plotly3_r',
                                       colorbar=dict(orientation='h',
                                                     yref='container',
                                                     y=0.2,
                                                     tickmode='array',
                                                     tickvals=[color_min, -0.5, 0, 0.5, color_max],
                                                     ticktext=['Hostile to <br>Trans Refuge', -0.5, 0, 0.5,
                                                               'Greater <br>Trans Refuge'],
                                                     ticks='outside',
                                                     ticklabeloverflow='allow',
                                                     xpad=65,
                                                     ticklabelposition='outside top'
                                                     ),
                                       name=""
                                       )
                    )
    df_t_selected['Territory Code'] = df_t['Territory Code']
    dc_selected = df_t_selected['Territory Code'].isin(['DC'])
    dc_selected = df_t_selected[dc_selected]
    dc_text = dc_selected['Selected Rank'][0]
    fig.add_scattergeo(
        lat=[38.90478149],
        lon=[-77.01629654],
        mode='markers',
        marker=dict(color="cyan", size=10, symbol='star', line=dict(width=1, color="red")),
        hovertemplate="<b>DC</b>:" + f"<br><b>{dc_text}</b>" + f"<extra></extra>",
        showlegend=False
    )

    if toggle == True:
        fig.add_scattergeo(
            lat=df_electeds_wide['Lat'],
            lon=df_electeds_wide['Lon'],
            mode='markers',
            marker=dict(color='black', size=8, symbol='cross', line=dict(width=1.25, color='yellow')),
            hoverinfo='skip',
            showlegend=False
        )
    else:
        fig = fig
    fig.update_layout(dragmode=False, margin={'r': 0, 't': 0, 'l': 0, 'b': 0},
                      geo_scope='usa',
                      autosize=True,
        title={
            'text': '<b>Custom Map</b>',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'automargin': True,
            'yref': 'container'
        },
      images=[dict(
          source='https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/TRM_Logo.png',
          xref='paper', yref='paper',
          x=0, y=1.05,
          sizex=0.2, sizey=0.2,
          xanchor='left', yanchor='bottom'
      )],
      hoverlabel=dict(
          bgcolor='white'
      )
    )
    fig.update_geos(
        showlakes=False,
        visible=False
    )

    fig.update_coloraxes(
        colorbar=dict(
            orientation='h',
            yref='container',
            y=0.2,
            title=''
        )
    )
    # fig.update_traces(
    #     text = state_refuge_data['State Code'],
    #     hovertemplate='<b>%{text}:</b>' + '<br><b>%{z}</b>' + f'<extra></extra>',
    # )

    as_selected = df_t_selected['Territory Code'].isin(['AS'])
    as_selected = df_t_selected[as_selected]
    gu_selected = df_t_selected['Territory Code'].isin(['GU'])
    gu_selected = df_t_selected[gu_selected]
    mp_selected = df_t_selected['Territory Code'].isin(['MP'])
    mp_selected = df_t_selected[mp_selected]
    pr_selected = df_t_selected['Territory Code'].isin(['PR'])
    pr_selected = df_t_selected[pr_selected]
    vi_selected = df_t_selected['Territory Code'].isin(['VI'])
    vi_selected = df_t_selected[vi_selected]


    fig2 = make_subplots(rows=1, cols=11)
    # fig2.add_trace(go.Heatmap(
    #     z=[dc_selected['Selected Rank']],
    #     x=['DC'],
    #     hovertemplate='<b>%{z}</b>' + '<extra></extra>',
    #     showscale=False,
    #     zmin=color_min,
    #     zmax=color_max,
    #     colorscale='Plotly3_r'
    # ), row=1, col=2),
    fig2.add_trace(go.Heatmap(
        z=[as_selected['Selected Rank']],
        x=['AS'],
        hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        showscale=False,
        zmin=color_min,
        zmax=color_max,
        colorscale='Plotly3_r'
    ), row=1, col=2),
    fig2.add_trace(go.Heatmap(
        z=[gu_selected['Selected Rank']],
        x=['GU'],
        hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        showscale=False,
        zmin=color_min,
        zmax=color_max,
        colorscale='Plotly3_r'
    ), row=1, col=4),
    fig2.add_trace(go.Heatmap(
        z=[mp_selected['Selected Rank']],
        x=['MP'],
        hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        showscale=False,
        zmin=color_min,
        zmax=color_max,
        colorscale='Plotly3_r'
    ), row=1, col=6),
    fig2.add_trace(go.Heatmap(
        z=[pr_selected['Selected Rank']],
        x=['PR'],
        hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        showscale=False,
        zmin=color_min,
        zmax=color_max,
        colorscale='Plotly3_r'
    ), row=1, col=8),
    fig2.add_trace(go.Heatmap(
        z=[vi_selected['Selected Rank']],
        x=['VI'],
        hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        showscale=False,
        zmin=color_min,
        zmax=color_max,
        colorscale='Plotly3_r'
    ), row=1, col=10),

    fig2.update_layout(dragmode=False,
                      autosize=True)
    fig2.update_xaxes(side='top')
    fig2.update_yaxes(showticklabels=False,
                     automargin=True)

    return fig, fig2
