from dash import Dash, html, register_page, dcc  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd                        # pip install pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots

register_page(__name__, "/")

# data
df_states = pd.read_csv("https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_States-Table%201.csv")
df_states.drop(['State'], axis=1, inplace=True)
df_states = df_states.replace({True: 1, False: 0})
df_states.set_index('State Code').reset_index(inplace=True)

df_territories = pd.read_csv(
    "https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_Territories-Table%201.csv")
territory_names_list = df_territories['Territory Name'].to_list()
# df_territories.drop(['Territory Name'], axis=1, inplace=True)
df_territories.set_index('Territory Code').reset_index(inplace=True)

state_refuge = ['Shield Law', 'Gender Marker on ID (adult)', 'Gender Marker on ID (minor)',
          'Gender Marker Options on ID', 'Gender Marker on Birth Certificate (adult)', 'Gender Marker on Birth Certificate (minor)',
           'Gender Marker Options on Birth Certificate', 'Name Change (adult)', 'Name Change (minor)', 'Non-Discrimination']
state_refuge_data = df_states.copy()
state_refuge_data = state_refuge_data[state_refuge] 
state_refuge_data['Trans Refuge Rank'] = state_refuge_data.mean(axis=1).astype(float)
state_refuge_data['State Code'] = df_states['State Code']

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

territory_wide = territory_refuge_rank_wide.copy()

color_min = state_refuge_data['Trans Refuge Rank'].min()
color_max = state_refuge_data['Trans Refuge Rank'].max()
if territory_refuge_rank_wide['Trans Refuge Rank'].min() < color_min:
    color_min = territory_refuge_rank_wide['Trans Refuge Rank'].min()
else:
    color_min = color_min
if territory_refuge_rank_wide['Trans Refuge Rank'].max() > color_max:
    color_max = territory_refuge_rank_wide['Trans Refuge Rank'].max()
else:
    color_max = color_max


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

refuge_color_min = state_refuge_data['Trans Refuge Rank'].min()
refuge_color_max = state_refuge_data['Trans Refuge Rank'].max()
if territory_refuge_rank_wide['Trans Refuge Rank'].min() < refuge_color_min:
    refuge_color_min = territory_refuge_rank_wide['Trans Refuge Rank'].min()
else:
    refuge_color_min = refuge_color_min
if territory_refuge_rank_wide['Trans Refuge Rank'].max() > refuge_color_max:
    refuge_color_max = territory_refuge_rank_wide['Trans Refuge Rank'].max()
else:
    refuge_color_max = refuge_color_max


#components

fig = go.Figure(data = go.Choropleth(locations=state_refuge_data['State Code'],
                            z= state_refuge_data['Trans Refuge Rank'],
                            locationmode='USA-states',
                            zmin=refuge_color_min,
                            zmax=refuge_color_max,
                            colorscale='Plotly3_r',
                            colorbar=dict(orientation='h',
                                        yref='container',
                                        y=0.2,
                                        tickmode='array',
                                        tickvals=[refuge_color_min, 0, 0.6, refuge_color_max],
                                        ticktext=['Hostile to <br>Trans Refuge', 0, 0.6, 'Greater <br>Trans Refuge'],
                                        ticks = 'outside',
                                        ticklabeloverflow='allow',
                                        xpad= 50
                                           )
                                    )
        )
fig.update_traces(
        text = state_refuge_data['State Code'],
        hovertemplate='<b>%{text}:</b>' + '<br><b>%{z}</b>' + '<extra></extra>',
    )
fig.add_scattergeo(
        lat=[38.90478149],
        lon=[-77.01629654],
        mode='markers',
    marker=dict(color="cyan", size=10, symbol='star', line=dict(width=1, color="red")),
    hovertemplate="<b>DC</b>:" + f"<br><b>{dc_wide['Trans Refuge Rank'][0]}</b>" + f"<extra></extra>"
    )
fig.update_layout(dragmode=False,
                  margin={'r': 0, 't': 0, 'l': 0, 'b': 0},
                  geo_scope='usa',
                    title={
                        'text': '<b>Trans Refuge</b>',
                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top',
                        'automargin': True,
                        'yref': 'container'
                    },
images=[dict(
            source='https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/TRM_Logo.png',
            xref = 'paper',yref='paper',
            x=0, y=1.05,
            sizex=0.2, sizey=0.2,
            xanchor='left',yanchor='bottom'
        )],
hoverlabel=dict(
            bgcolor='white'
        )
                  )
fig.update_geos(
    showlakes=False,
    visible=False
)

initial_phase_outline = go.Choropleth(
    locationmode='USA-states',
    z=[0,0,0,0,0,0,],
    locations=['MI','WI','PA','OH','IA','MN'],
    colorscale=[[0, 'rgba(0, 0, 0, 0)'], [1, 'rgba(0, 0, 0, 0)']],
    marker_line_color='limegreen',
    marker_line_width=2,
    showscale=False,
    hoverinfo='skip')
fig.add_trace(initial_phase_outline)

mygraph = dcc.Graph(figure=fig, config={
     'displayModeBar':False,
     'scrollZoom':False
        
})

fig2= make_subplots(rows=1, cols=11)
# fig2.add_trace(go.Heatmap(
#                 z=[dc_wide['Trans Refuge Rank']],
#                 x=['DC'],
#                 hovertemplate='<b>%{z}</b>' + '<extra></extra>',
#                 showscale=False,
#                 zmin=color_min,
#                 zmax=color_max,
#                 colorscale='Plotly3_r'
# )
#     ,row=1, col=2)
fig2.add_trace(go.Heatmap(
                z=[as_wide['Trans Refuge Rank']],
                x=['AS'],
                hovertemplate='<b>%{z}</b>' + '<extra></extra>',
                showscale=False,
                zmin=color_min,
                zmax=color_max,
                colorscale='Plotly3_r'
), row=1, col=2)
fig2.add_trace(go.Heatmap(
            z=[gu_wide['Trans Refuge Rank']],
            x=['GU'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=color_min,
            zmax=color_max,
            colorscale='Plotly3_r'
), row=1, col=4)
fig2.add_trace(go.Heatmap(
            z=[mp_wide['Trans Refuge Rank']],
            x=['MP'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=color_min,
            zmax=color_max,
            colorscale='Plotly3_r'
), row=1, col=6)
fig2.add_trace(go.Heatmap(
            z=[pr_wide['Trans Refuge Rank']],
            x=['PR'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=color_min,
            zmax=color_max,
            colorscale='Plotly3_r'
), row=1, col=8)
fig2.add_trace(go.Heatmap(
            z=[vi_wide['Trans Refuge Rank']],
            x=['VI'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=color_min,
            zmax=color_max,
            colorscale='Plotly3_r'
), row=1, col=10)
fig2.update_layout(dragmode=False,
                      autosize=True,
                   )
fig2.update_xaxes(side='top',
                  showgrid=False)
fig2.update_yaxes(showticklabels=False,
                  showgrid=False,
                     automargin=True)

territory_graph = dcc.Graph(figure=fig2, config={
    'displayModeBar': False,
    'scrollZoom': False},
        style={'height':200}
    )

territory_key = dbc.Col(['Territories Reference: AS - American Samoa, GU - Guam, MP - N. Mariana Islands, PR - Puerto Rico, VI - U.S. Virgin Islands'], width=12, className='fs-6')

shield_card = dbc.Accordion(
            dbc.AccordionItem(
       [
           html.Div(['Shield Laws vary from state to state. In our research, we included any legislation or executive order which has a primary goal of protecting providers, patients, and advocates in providing and accessing trangender-related healthcare.'], className='fs-6 fw-normal'),
           html.Div(['Shield Laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'], className='fs-6 mt-1 fw-normal'),
           ], title='Shield Laws', className='h6 mt-1'
    ), start_collapsed=True)
name_card = dbc.Accordion(
dbc.AccordionItem(
       [
           html.Div(['Name Change Laws apply to legal name change and are ranked on a scale of (-1,1).'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                    dbc.ListGroupItem('[-1] State has a negative targeted law, name change is not possible, or is extremely limited'),
                    dbc.ListGroupItem('[-1] State requires publication of name change, with no or extremely limited option to waive publication'),
                    dbc.ListGroupItem('[0] State requires publication, but offers broad options to waive publication'),
                    dbc.ListGroupItem('[0] Unclear state law, defer to county'),
                    dbc.ListGroupItem('[0.5] May only require publication for limited circumstances'),
                    dbc.ListGroupItem('[1] Accessible process that does not require publication')

               ], className='mt-1 fw-normal'
           )
           ], title='Name Change Laws',className='h6 mt-1'
    ), start_collapsed=True

)
gender_marker_id_card = dbc.Accordion(
dbc.AccordionItem(
       [
           html.Div(["Gender Marker on ID laws refer to state legislation regarding gender marker changes on a Driver's License or Non-Driver State ID. These laws are ranked on a scale of (-1,1)."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                    dbc.ListGroupItem('[-1] State has a negative targeted law, gender marker change is not possible, or is extremely limited'),
                    dbc.ListGroupItem('[-1] State requires surgery'),
                    dbc.ListGroupItem('[-1] State requires a court order or amended birth certificate'),
                    dbc.ListGroupItem('[0] State has confusing or unclear process, which requires some form of medical transition and/or provider documentation from a limited range of providers. Does not require surgery'),
                    dbc.ListGroupItem('[0.5] Clear process that requires provider documentation, but allows for a broad range of providers, and does not require any medical transition'),
                    dbc.ListGroupItem('[1] Accessible process that does not require provider documentation')

               ], className='mt-1 fw-normal'
           ),
           html.Div(['Gender options are notated separately as TRUE or FALSE. TRUE applies to any options outside of "M" or "F" (typically "X").For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 fw-normal mt-1'),

       ], title='Gender Marker Change ID',className='h6 mt-1'
    ), start_collapsed=True
)
gender_marker_bc_card = dbc.Accordion(
dbc.AccordionItem(
       [
           html.Div(["Gender Marker on Birth Certificate laws refer to state legislation regarding gender marker changes on birth certificates. These laws are ranked on a scale of (-1,1)"], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                    dbc.ListGroupItem('[-1] State has a negative targeted law, gender marker change is not possible, or is extremely limited'),
                    dbc.ListGroupItem('[-1] State requires surgery'),
                    dbc.ListGroupItem('[-1] State requires a court order'),
                    dbc.ListGroupItem('[-0.5] State will only issue an amended birth certificate'),
                    dbc.ListGroupItem('[-0.5] State has no specific provision for correcting gender on birth certificates and/or is likely to require a court order'),
                    dbc.ListGroupItem('[0] State has confusing or unclear process, which requires some form of medical transition and/or provider documentation from a limited range of providers. Does not require surgery'),
                    dbc.ListGroupItem('[0.5] Clear process that requires provider documentation, but allows for a broad range of providers, and does not require any medical transition'),
                    dbc.ListGroupItem('[1] Accessible process that does not require provider documentation')

               ], className='mt-1 fw-normal'
           ),
            html.Div(['Gender options are notated separately as TRUE or FALSE. TRUE applies to any options outside of "M" or "F" (typically "X").For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 fw-normal mt-1'),
           ], title='Gender Marker Change Birth Certificate',className='h6 mt-1'
    ), start_collapsed=True
)
nondiscrimination_card = dbc.Accordion(
dbc.AccordionItem(
       [
           html.Div(["Non-Discrimination laws refer to state non-discrimination laws regarding housing, employment, and public accomodations, that expicitly cover gender identity (-1,1)"], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                    dbc.ListGroupItem('[-1] State has no protections for gender identity or target laws allowing discrimination'),
                    dbc.ListGroupItem('[0] State non-discrimination protections covering gender identity in one of the three categories'),
                   dbc.ListGroupItem(
                       '[0.5] State non-discrimination protections covering gender identity in two of the three categories'),
                   dbc.ListGroupItem('[1] All three categories of non-discrimination laws explicitly cover gender identity')

               ], className='mt-1 fw-normal'
           )
           ], title='Non-Discrimination Laws',className='h6 mt-1'
    ), start_collapsed=True
)
#layout
layout = dbc.Container(
    [
        html.Div([
            dbc.Card(
                dbc.CardBody([
                    html.Div(['The world is a very dangerous place for trans people. Every day we are exposed to hateful speech, hateful actions and hateful bills being pushed by hateful politicians and media figures.'],className='text-body mt-2'),
                    html.Div(['The Trans Refuge Project, created by Queer Equity Institute, is an effort to give trans people guidance as to where they can go for safety, and find the resources they need to live full and authentic lives.'], className='text-body mt-2'),
                    html.Div('The Trans Refuge Map is an interactive, visual resource providing a guide to trans refuge policies, protections, legislation, and elected officials.',
                     className="text-body mt-2"),
                    html.Div('The Trans Refuge Project and Trans Refuge Map are ongoing projects, which will continue to grow through coalition, collaboration, and crowd sourced information. The initial phase of the Trans Refuge Project will focus on Iowa, Michigan, Minnesota, Ohio, Pennsylvania, and Wisconsin.',
                     className="text-body mt-2"),
                    html.Div('You can view the map by topic, state, or create your own map view.', className='text-body mt-2'),
                    html.Div('See the Trans Refuge Map below:', className='text-body')
                    ]), className=('w-80')
            )
        ]),
        dbc.Row([
            dbc.Col([mygraph], width=10)
        ], justify='center'),
        dbc.Row([
            dbc.Col([territory_graph], width=12)
            ], justify='center'),
        dbc.Row([
            territory_key
            ], justify='center', className='ml-5'),
        dbc.Row([
            dbc.Row([' Laws Ranked:'], class_name='h3 mt-2 ml-5'),
            dbc.Row([
                dbc.Col([shield_card], width=4),
                dbc.Col([name_card], width=4),
                dbc.Col([gender_marker_id_card], width=4)
            ]),
            dbc.Row([
                dbc.Col([gender_marker_bc_card], width=4),
                dbc.Col([nondiscrimination_card], width=4),
            ], justify='center'),
        ], justify='center', className='w-80')
    ], fluid=True)
