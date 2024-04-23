from dash import Dash, dcc, Output, Input, html, register_page, callback, dash_table, ctx  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import json
import pandas as pd        #pip install pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots

register_page(__name__)

pd.options.mode.copy_on_write = True
# incorporate data into app
df_states = pd.read_csv("https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_States-Table%201.csv", index_col = False)
state_name_col = df_states['State']
df_states.drop(['State'], axis=1, inplace=True)
df_states.set_index('State Code').reset_index(inplace=True)

df_territories = pd.read_csv(
    "https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/US_Territories-Table%201.csv", index_col=False)
territory_names_list = df_territories['Territory Name'].to_list()
terr_name_col = df_territories['Territory Name']
df_territories.drop(['Territory Name'], axis=1, inplace=True)
df_territories.set_index('Territory Code').reset_index(inplace=True)
#

df_electeds = pd.read_csv('https://raw.githubusercontent.com/BexLedwith/trans-refuge-map/main/state_electeds.csv', dtype={'FIPS': str}, index_col=False)
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
# territory_refuge_data = territory_refuge_data.replace({True: 1, False: 0})
territory_refuge_data = territory_refuge_data[territory_refuge]
territory_refuge_data['Trans Refuge Rank'] = territory_refuge_data.mean(axis=1).astype(float)

#as list
# territory_refuge_list=territory_refuge_data['Trans Refuge Rank'].tolist()
territory_refuge_data['Territory Code'] = df_territories['Territory Code']
territory_code_list=territory_refuge_data['Territory Code'].tolist()
territory_refuge_rank_wide = territory_refuge_data.copy()
territory_refuge_rank_wide = territory_refuge_data[['Territory Code', 'Trans Refuge Rank']]
territory_refuge_string = ', '.join(territory_refuge)

territory_family = ['Foster Care Non-Discrimination', 'Adoption Non-Discrimination',
                'Child Welfare Non-Discrimination for LGBTQ Youth', 'Recognition of Assisted-Reproduction',
                'VAP for Non-Genetic LGBTQ Parents']
territory_family_data = df_territories.copy()
# territory_family_data = territory_family_data.replace({True: 1, False: 0})
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
# territory_gi_data = territory_gi_data.replace({True: 1, False: 0})
territory_gi_data = territory_gi_data[territory_gi]
territory_gi_data['G.I. Laws Rank'] = territory_gi_data.mean(axis=1).astype('float')
territory_gi_data['Territory Code'] = df_territories['Territory Code']
territory_gi_string = ', '.join(territory_gi)
territory_gi_rank_wide = territory_gi_data.copy()
territory_gi_rank_wide = territory_gi_rank_wide[['Territory Code', 'G.I. Laws Rank']]

territory_repro = ['Abortion Access', 'Interstate Abortion Shield Law']
territory_repro_data = df_territories.copy()
# territory_repro_data = territory_repro_data.replace({True: 1, False: 0})
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
# territory_hate_data = territory_hate_data.replace({True: 1, False: 0})
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

family_color_min = state_family_data['Family Services Rank'].min()
family_color_max = state_family_data['Family Services Rank'].max()
if territory_wide['Family Services'].min() < family_color_min:
    family_color_min = territory_wide['Family Services'].min()
else:
    family_color_min = family_color_min
if territory_wide['Family Services'].max() > family_color_max:
    family_color_max = territory_wide['Family Services'].max()
else:
    family_color_max = family_color_max
gi_color_min = state_gi_data['G.I. Laws Rank'].min()
gi_color_max = state_gi_data['G.I. Laws Rank'].max()
if territory_wide['Gender Inclusive Laws & Policies'].min() < gi_color_min:
    gi_color_min = territory_wide['Gender Inclusive Laws & Policies'].min()
else:
    gi_color_min = gi_color_min
if territory_wide['Gender Inclusive Laws & Policies'].max() > gi_color_max:
    gi_color_max = territory_wide['Gender Inclusive Laws & Policies'].max()
else:
    gi_color_max = gi_color_max
repro_color_min = state_repro_data['Reproductive Rights Rank'].min()
repro_color_max = state_repro_data['Reproductive Rights Rank'].max()
if territory_wide['Reproductive Rights'].min() < repro_color_min:
    repro_color_min = territory_wide['Reproductive Rights'].min()
else:
    repro_color_min = repro_color_min
if territory_wide['Reproductive Rights'].max() > repro_color_max:
    repro_color_max = territory_wide['Reproductive Rights'].max()
else:
    repro_color_max = repro_color_max
hate_color_min = state_hate_data['Hate Legislation Rank'].min()
hate_color_max = state_hate_data['Hate Legislation Rank'].max()
if territory_wide['Hate Legislation'].min() < hate_color_min:
    hate_color_min = territory_wide['Hate Legislation'].min()
else:
    hate_color_min = hate_color_min
if territory_wide['Hate Legislation'].max() > hate_color_max:
    hate_color_max = territory_wide['Hate Legislation'].max()
else:
    hate_color_max = hate_color_max
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
appInfo = dcc.Markdown('##### Select from the list to view law collections grouped by category: ')
toggleInfo = dcc.Markdown('###### Use this toggle switch to view 2S+TGNC reps on the map:')
law_cards = dbc.Row('') #emptyrow
mygraph = dcc.Graph(figure={}, config={
    'displaylogo':False,
    'modeBarButtonsToRemove': ['zoom', 'pan','select','zoomIn','zoomOut','autoScale','resetScale', 'lasso2d', 'reset'],
    'toImageButtonOptions': {'filename':'trans_refuge_map_download'},
     'scrollZoom':False}, id='stateMap'
                    )
territory_graph = dcc.Graph(figure={}, config={
    'displayModeBar': False,
    'scrollZoom': False},
        style={'height':200},
        id='terrMap'
    )

territory_key = dbc.Col(['Territories Reference: AS - American Samoa, GU - Guam, MP - N. Mariana Islands, PR - Puerto Rico, VI - U.S. Virgin Islands'], width=12, className='fs-6')


radioitems = dbc.RadioItems(
    options=topics,
    value='Trans Refuge'
)

reps_toggle = dbc.Switch(
    label='2S+TGNC State Reps',
    value=False)
#cards
shield_card = dbc.Accordion(
            dbc.AccordionItem(
       [
           html.Div(['Shield Laws vary from state to state. In our research, we included any legislation or executive order which has a primary goal of protecting providers, patients, and advocates in providing and accessing trangender-related healthcare.'], className='fs-6 fw-normal'),
           html.Div(['Shield Laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'], className='fs-6 mt-1 fw-normal'),
           ], title='Shield Laws',className='h6 mt-1'
    ), start_collapsed=True)

name_card = dbc.Accordion(
dbc.AccordionItem(
       [
           html.Div(['Name Change Laws apply to legal name change and are ranked on a scale of (-1,1).'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                    dbc.ListGroupItem('[-1] State has a negative targeted law, name change is not possible, or is extremely limited'),
                    dbc.ListGroupItem('[1] State requires publication of name change, with no or extremely limited option to waive publication'),
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

foster_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Foster Care Non-Discrimination Laws are protections from discrimination for 2S+TGNC foster parents and families by agencies and officials.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Foster Care Non-Discrimination',className='h6 mt-1'
    ), start_collapsed=True)


adoption_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Adoption Non-Discrimination Laws are protections from discrimination for 2S+TGNC parents and families by adoption agencies and officials.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Adoption Non-Discrimination',className='h6 mt-1'
    ), start_collapsed=True)

child_welfare_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Child Welfare Non-Discrimination Laws are protections from discrimination for 2S+TGNC youth in the child welfare system.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Child Welfare Non-Discrimination',className='h6 mt-1'
    ),start_collapsed=True)
assisted_repro_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Assisted Reproduction Recognition Laws provide legal recognition for intended non-genetic parents regardless of marital status.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Assisted Reproduction Recognition',className='h6 mt-1'
    ), start_collapsed=True)
vap_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['VAP Recognition refers to legal recognition of parentage through "voluntary acknowledgement of parentage". For our purposes, we have only included VAP laws which explicitly apply to LGBTQ parents and non-genetic parents.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='VAP Recognition',className='h6 mt-1'
    ), start_collapsed=True)

gi_bathroom_card= dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Gender Inclusive Bathroom Laws refer to legal protections for people to access bathroom facilities consistent with their gender identity.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gender Inclusive Bathroom Laws',className='h6 mt-1'
    ),start_collapsed=True)
lgbtq_curriculum_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['LGBTQ Inclusive Curriculum refers laws which explicitly require inclusion of LGBTQ-related history and people in state curricular standards.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='LGBTQ Inclusive Curriculum',className='h6 mt-1'
    ),start_collapsed=True)
anti_bully_students_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Anti-Bullying Laws protect students from bullying from students and staff. For the purpose of our research, we have only included anti-bullying laws that explicity prohibit bullying on the basis of gender identity or expression. These laws are ranked on a scale of (-1,1).'], className='fs-6 fw-normal mb-1'),
            dbc.ListGroup(
               [
                    dbc.ListGroupItem('[-1] State has a law preventing protections'),
                    dbc.ListGroupItem(
                       '[0] State has no law or policy'),
                    dbc.ListGroupItem('[0.5] State regulation, but not law'),
                    dbc.ListGroupItem('[1] State law')

               ], className='mt-1 fw-normal'
           )
           ], title='Anti-Bullying 2S+TGNC Students',className='h6 mt-1'
    ), start_collapsed=True)
non_discrimination_students_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Non-Discrimination for LGBTQ Students refers to state non-discrimination laws which protect LGBTQ students from discrimination in all aspects of student life. For the purposes of our research, we have only included laws which prohibit discrimination on the basis of gender identity or expression. These laws are ranked on a scale of (-1,1).'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has a law preventing protections'),
                   dbc.ListGroupItem(
                       '[0] State has no law or policy'),
                   dbc.ListGroupItem('[0.5] State regulation, but not law'),
                   dbc.ListGroupItem('[1] State law')

               ], className='mt-1 fw-normal'
           )
           ], title='Non-Discrimination LGBTQ Students',className='h6 mt-1'
    ),start_collapsed=True)
gay_trans_panic_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Gay/ Trans Panic Defense Ban refers to state 'panic defense' prohibit the use of a defense which attempts to blame a victim's sexual orientation or gender identity for the defendant's action(s)."], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gay/Trans Panic Defense Ban',className='h6 mt-1'
    ),start_collapsed=True)
hate_crime_gi_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Hate Crime Laws refer to increased penalties or enhancements for crimes committed with bias toward a protected group. For the purpose of our research, we have only included hate crime laws which explicitely include gender identity or expression as a protected category.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Hate Crime Laws',className='h6 mt-1'
    ),start_collapsed=True)
jury_service_gi_card= dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Jury Service Nondiscrimination Laws proibit discrimination against jurors on the basis of protected characteristics. For the purpose of our research, we have only included laws which enumerate gender identiry or expression as a protected category.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Jury Service Non-Discrimination Laws',className='h6 mt-1'
    ),start_collapsed=True)
gi_correctional_housing_card= dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Gender Inclusive Correctional Housing Laws allow and provide guidance for incarcerated 2S+TGNC people to be housed according to their gender identity.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gender Inclusive Correctional Housing',className='h6 mt-1'
    ),start_collapsed=True)
gender_affirming_care_corr_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Gender Affirming Care in Correctional Facilities refers to state law or policy providing for incarcerated 2S+TGNC people to receive gender-affirming care while incarcerated.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gender Affirming Care in Correctional Facilities',className='h6 mt-1'
    ),start_collapsed=True)

abortion_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Abortion Access refers to laws which protect or restrict access to legal abortion. These laws are ranked on a scale of (-1,1).'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] Abortion is criminalized or illegal.'),
                   dbc.ListGroupItem('[-0.5] Abortion access is not protected. State has hostile laws regarding abortion providers and access to abortion.'),
                   dbc.ListGroupItem(
                       '[0] Abortion access is not protected by state law. Access may be limited.'),
                   dbc.ListGroupItem('[0.5] State has codified right to abortion with limited restrictions to access'),
                   dbc.ListGroupItem('[1] State has codified right to abortion with expanded access')

               ], className='mt-1 fw-normal'
           )
           ], title='Abortion Access',className='h6 mt-1'
    ),start_collapsed=True)
interstate_shield_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Interstate Abortion Shield Laws protect providers, patients, and those who assist patients in access abortion from out-of-state investigation and/or legal action.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Interstate Abortion Shield Law',className='h6 mt-1'
    ),start_collapsed=True)

bathroom_k_12_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Trans Bathroom Ban K-12 refers to laws which prohibit trans people from using bathrooms and other sex-segregated facilities aligned with their gender identity in K-12 school settings.'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has ban'),
                   dbc.ListGroupItem(
                       '[0] State does not have ban')
               ], className='mt-1 fw-normal'
           )
           ], title='Trans Bathroom Ban K-12',className='h6 mt-1'
    ),start_collapsed=True)
bathroom_schools_gov_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Trans Bathroom Ban in Schools and Government Buildings refers to laws which prohibit trans people from using bathrooms and other sex-segregated facilities aligned with their gender identity in schools and government buildings.'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has ban'),
                   dbc.ListGroupItem(
                       '[0] State does not have ban')
               ], className='mt-1 fw-normal'
           )
           ], title='Trans Bathroom Ban in Schools and Government Buildings',className='h6 mt-1'
    ),start_collapsed=True)
define_sex_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['State Defines "Sex" refers to laws which explicitly define "sex" to exclude 2S+TGNC people, and/or to allow discrimination against them.'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State defines "sex"'),
                   dbc.ListGroupItem(
                       '[0] State does not define "sex"')
               ], className='mt-1 fw-normal'
           )
           ], title='State Defines "Sex"',className='h6 mt-1'
    ),start_collapsed=True)
rfra_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Broad "RFRA" refers to laws which permit broad religious exemptions from state laws.'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has broad "RFRA"'),
                   dbc.ListGroupItem(
                       '[0] State does not have broad "RFRA"')
               ], className='mt-1 fw-normal'
           )
           ], title='Broad "RFRA"',className='h6 mt-1'
    ),start_collapsed=True)
re_child_welfare_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Targeted Religious Exemption for Child Welfare refers to laws which permit state-licensed child welfare agencies religious exemptions from state laws.'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has targeted religious exemption for child welfare services'),
                   dbc.ListGroupItem(
                       '[0] State does not have targeted religious exemption for child welfare services')
               ], className='mt-1 fw-normal'
           )
           ], title='Targeted Religious Exemption for Child Welfare',className='h6 mt-1'
    ),start_collapsed=True)
re_medical_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Targeted Religious Exemption for Medical Professionals refers to laws which permit medical professionals to decline services which conflict with their religious beliefs.'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has targeted religious exemption for medical professionals'),
                   dbc.ListGroupItem(
                       '[0] State does not have targeted religious exemption for medical professionals')
               ], className='mt-1 fw-normal'
           )
           ], title='Targeted Religious Exemption for Medical Professionals',className='h6 mt-1'
    ),start_collapsed=True)
marriage_denial_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Marriage Services and/or License Denial refers to laws which permit public officials to decline marriage services or licenses which conflict with their religious beliefs.'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has targeted religious exemption for public officials'),
                   dbc.ListGroupItem(
                       '[0] State does not have targeted religious exemption for public officials')
               ], className='mt-1 fw-normal'
           )
           ], title='Marriage Services and/or License Denial',className='h6 mt-1'
    ),start_collapsed=True)
drag_ban_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(['Drag Ban laws aim to place restrictions on drag performances'], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem('[-1] State has drag ban'),
                   dbc.ListGroupItem(
                       '[0] State does not have drag ban, or ban is not currently enforceable')
               ], className='mt-1 fw-normal'
           )
           ], title='Drag Ban',className='h6 mt-1'
    ),start_collapsed=True)
dont_say_gay_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Don't Say Gay laws are school censorship laws which prevent teachers and school staff from discussing LGBTQIA+ people, issues, or history."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem("[-1] State has Don't Say Gay Law"),
                   dbc.ListGroupItem(
                       "[0] State does not have Don't Say Gay Law")
               ], className='mt-1 fw-normal'
           )
           ], title="Don't Say Gay",className='h6 mt-1'
    ),start_collapsed=True)
subject_rest_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Specific Subject Restrictions refer to laws which prohibit positive portrayals of homosexuality. These laws may apply to specific subjects such as sex ed."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem("[-1] State has Specific Subject Restrictions"),
                   dbc.ListGroupItem(
                       "[0] State does not have Specific Subject Restrictions")
               ], className='mt-1 fw-normal'
           )
           ], title="Specific Subject Restrictions",className='h6 mt-1'
    ),start_collapsed=True)
parental_opt_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Parental Notification Laws require parents to be notified of any planned LGBTQ-related subjects. They either allow parents to opt their children out, or requires parents to opt their children in."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem("[-1] State has Parental Notification Law"),
                   dbc.ListGroupItem(
                       "[0] State does not have Parental Notification Law")
               ], className='mt-1 fw-normal'
           )
           ], title="Parental Notification (opt-in or opt-out)",className='h6 mt-1'
    ),start_collapsed=True)
sports_ban_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Sports Bans are laws to prohibit 2S+TGNC youth from participating in school sports consistent with their gender identity."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem("[-1] State has a Sports Ban"),
                   dbc.ListGroupItem(
                       "[0] State does not have a Sports Ban")
               ], className='mt-1 fw-normal'
           )
           ], title="Sports Ban",className='h6 mt-1'
    ),start_collapsed=True)

forced_out_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Forced Outing in Schools Laws require school staff, teachers, and/or public service workers to out 2S+TGNC youth to their families."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem("[-1] State law requires forced outing of 2S+TGNC youth in schools"),
                    dbc.ListGroupItem(
                       '[-0.5] State law promotes, but does not enforce, forced outing of 2S+TGNC youth in schools.'),
                   dbc.ListGroupItem(
                       "[0] State law does not require forced outing.")
               ], className='mt-1 fw-normal'
           )
           ], title="Forced Outing in Schools",className='h6 mt-1'
    ),start_collapsed=True)
youth_health_ban_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Bans on Best Practice Medical care for 2S+TGNC Youth target and block access to best-practice medical care for 2S+TGNC youth. Some laws also criminalize provicers or parents seeking to provide care."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem("[-1] State has 2S+TGNC youth healthcare ban"),
                   dbc.ListGroupItem(
                       "[0] State does not have 2S+TGNC youth healthcare ban")
               ], className='mt-1 fw-normal'
           )
           ], title="Ban on Best Practice Medical Care for 2S+TGNC Youth",className='h6 mt-1'
    ),start_collapsed=True)
barriers_id_card = dbc.Accordion(
    dbc.AccordionItem(
       [
           html.Div(["Barriers to Identity Documents refer to state laws which do not allow changes to vital records or identification documents which targets 2S+TGNS people."], className='fs-6 fw-normal mb-1'),
           dbc.ListGroup(
               [
                   dbc.ListGroupItem("[-1] State has Barriers to Identity Documents"),
                   dbc.ListGroupItem(
                       "[0] State does not have Barriers to Identity Documents")
               ], className='mt-1 fw-normal'
           )
           ], title="Barriers to Identity Documents",className='h6 mt-1'
    ),start_collapsed=True)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll',
        'borderRadius': '5px'
    }
}

national_resources = dbc.Container([
                dbc.Label('National 2S+TGNC Resources and Organizations:', style=dict(fontWeight='bold', textAlign='center', fontFamily='sans-serif'),
                          className='fs-4'),
                dbc.Accordion([
                    dbc.AccordionItem([
html.Div([
                                 "Advocates for Trans Equality (A4TE) offers detailed ID change guides, pro bono name change services, and more community tools and services."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                        html.A('A4TE.org', href='https://a4te.org/#home', target='_blank')
                ], title="Advocates for Trans Equality", className='h6 mt-1'),
            dbc.AccordionItem([
html.Div([
                                 "The TransLatin@ Coalition (TLC) is represented across 10 states, specifically serving the TransLatin@ community."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                html.A('TransLatinaCoalition.org', href='https://www.translatinacoalition.org/', target='_blank')

            ], title="TransLatin@ Coalition", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["The Transgender Gender-Variant & Intersex Justice Project is composed of and serves Black and Black/Brown Transgender, GNC/nonbinary, intersex people impacted by the carceral justice complex, and their families."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.A('TGIJP.org', href='https://tgijp.org/', target='_blank')

], title="TGI Justice Project", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["The Transgender Law Center provides legal resources for interacting with ICE, discrimination, housing, health care and more "],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.A('TransgenderLawCenter.org', href='https://transgenderlawcenter.org/resources/', target='_blank')

], title="Transgender Law Center", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["Queer Youth Assemble provides events, professional development, resources and more, by and for Queer Youth 25 and under."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.A('QueerYouthAssemble.org', href='https://queeryouthassemble.org/', target='_blank')

], title="Queer Youth Assemble", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["Gender Spectrum provides resources for families, education, health, and ID changes."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.A('GenderSpectrum.org', href='https://www.genderspectrum.org/resources', target='_blank')

], title="Gender Spectrum", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["Point of Pride provides financial and direct support through surgery and hrd access funds, electrolysis support, free binders, shapewear, and more."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.A('PointofPride.org', href='https://www.pointofpride.org/', target='_blank')

], title="Point of Pride", className='h6 mt-1')



                    ],start_collapsed=True)
            ])

mi_resources = dbc.Accordion([
                    dbc.AccordionItem([
                    html.Div([
                                 "Transgender Michigan provides advocacy, support, education, and resources."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                        html.A('TransGenderMichigan.org', href='https://www.transgendermichigan.org/', target='_blank')
                ], title="Transgender Michigan", className='h6 mt-1'),
            dbc.AccordionItem([
html.Div(["Queering Medicine offers a community-gathered list of queer or affirming providers in Michigan."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                html.A('QueeringMedicine.org', href='https://www.queeringmedicine.com/resources/provider-directory', target='_blank')

            ], title="Queering Medicine", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["Stand With Trans provides support for trans youth and their families."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.A('StandWithTrans.org', href='https://standwithtrans.org/', target='_blank')

], title="Stand with Trans", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["Michigan Legal Help, in addition to many other resources, provides guidance for name and gender marker changes."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.Div(html.A('Name Change', href='https://michiganlegalhelp.org/resources/name-change', target='_blank'),
), html.Div(
html.A('Gender Marker Change', href='https://michiganlegalhelp.org/resources/crime-traffic-and-id/changing-your-gender-marker-id-or-birth-certificate',
           target='_blank')
    )
], title="Michigan Legal Help", className='h6 mt-1')
                    ],start_collapsed=True)
wi_resources = dbc.Accordion([
            dbc.AccordionItem([
html.Div(["Trans Advocacy Madison offers resources, a robust collection of laws affecting 2S+TGNC people in Wisconsin, and health and safety guidance. "],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                html.A('TransAdvocacyMadison.org', href='https://transadvocacymadison.org/', target='_blank')
            ], title="Trans Advocacy Madison", className='h6 mt-1'),


            dbc.AccordionItem([
html.Div(["Diverse & Resilient has a robust Trans Resource List for people based in Wisconsin."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                html.A('DiverseAndResilient.org', href='https://www.diverseandresilient.org/resources/trans-resource-list/', target='_blank')

            ], title="Diverse & Resilient", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["The Teens Like Us Program (TLU) provides support groups and education for LGBTQIA2s+ youth across Wisconsin."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.Div(html.A('BriarPatch.org', href='https://www.briarpatch.org/programs/youth-and-family-services/teens-like-us-lgbtqia2s/', target='_blank'),
)
], title="Teens Like Us", className='h6 mt-1')
                    ],start_collapsed=True)
pa_resources = dbc.Accordion([
                    dbc.AccordionItem([
                    html.Div([
                                 "PA Law Help provides comprehensive guides to changing your name in PA."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                        html.A('PALawHelp.org', href='https://www.palawhelp.org/classroom/changing-your-name-in-pennsylvania', target='_blank')
                ], title="PALawHelp.org ", className='h6 mt-1'),
dbc.AccordionItem([html.Div(["The Welcome Project PA provides advocacy, support, and resources."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                        html.A('WelcomeProjectPA.org', href='https://welcomeprojectpa.org/saga/trans-care-resources/', target='_blank')
], title="The Welcome Project PA", className='h6 mt-1'),
                    dbc.AccordionItem([
                    html.Div([
                                 "The Eastern PA Trans Equity Project offers services including: name change assistance, mutual aid, and food assistance."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                        html.A('PATransEquity.org', href='https://www.patransequity.org/', target='_blank')
                ], title="Eastern PA Trans Equity Project", className='h6 mt-1')
                    ],start_collapsed=True)
ia_resources = dbc.Accordion([
                    dbc.AccordionItem([
                    html.Div([
                                 "The Iowa Trans Mutual Aid fund supports 2S+TGNS Iowans access gender affirming care."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                        html.A('IowaTransMutualAidFund.org', href='https://www.iowatransmutualaidfund.org/', target='_blank')
                ], title="Iowa Trans Mutual Aid Network", className='h6 mt-1'),
            dbc.AccordionItem([
html.Div(["The Des Moines Pride Center provides a robust list of resources for 2S+TGNC Iowans."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                html.A('DesMoinesPrideCenter.org', href='https://www.desmoinespridecenter.org/resources/', target='_blank')

            ], title="Des Moines Pride Center | Resources", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["Iowa Safe Schools provides comprehensive support and resources to LGBTQ youth and educators."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.A('IowaSafeSchools.org', href='https://iowasafeschools.org/', target='_blank')

], title="Iowa Safe Schools", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["The University of Iowa provides guidance for name and gender marker changes in Iowa."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.Div(html.A('The Iowa Guide to Changing Legal Identity Documents', href='https://trans-resources.org.uiowa.edu/sites/trans-resources.org.uiowa.edu/files/2020-04/iowa_guide_to_changing_legal_identity_documents_january_2019_0.pdf', target='_blank'),
)
], title="UIOWA | Document Change", className='h6 mt-1'),
dbc.AccordionItem([
html.Div(["ACLU of Iowa provides a comprehensive Know Your Rights guide for 2S+TGNC Iowans."],
                             className='fs-6 fw-normal mb-1 text-wrap'),
    html.Div(html.A('ACLU-IA.org', href='https://www.aclu-ia.org/sites/default/files/07.27.23_trans_rights_trifold.pdf', target='_blank'),
)
], title="ACLU IA | Trans KYR", className='h6 mt-1')
                    ],start_collapsed=True)
oh_resources = dbc.Accordion([
                    dbc.AccordionItem([
                    html.Div([
                                 "Blurb"],
                             className='fs-6 fw-normal mb-1 text-wrap'),
                        html.A('link', href='#', target='_blank')
                ], title="Ohio Resource", className='h6 mt-1'),
    dbc.AccordionItem([
        html.Div([
            "Blurb"],
            className='fs-6 fw-normal mb-1 text-wrap'),
        html.A('link', href='#', target='_blank')
    ], title="Ohio Resource", className='h6 mt-1'),
    dbc.AccordionItem([
        html.Div([
            "Blurb"],
            className='fs-6 fw-normal mb-1 text-wrap'),
        html.A('link', href='#', target='_blank')
    ], title="Ohio Resource", className='h6 mt-1'),
    dbc.AccordionItem([
        html.Div([
            "Blurb"],
            className='fs-6 fw-normal mb-1 text-wrap'),
        html.A('link', href='#', target='_blank')
    ], title="Ohio Resource", className='h6 mt-1'),
    dbc.AccordionItem([
        html.Div([
            "Blurb"],
            className='fs-6 fw-normal mb-1 text-wrap'),
        html.A('link', href='#', target='_blank')
    ], title="Ohio Resource", className='h6 mt-1'),
                    ],start_collapsed=True)

# Customize Layout
layout = dbc.Container([
            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                    dbc.Col([appInfo], width=6),
                    dbc.Col([radioitems], width=6)
                     ], justify='center', class_name='mt-2'),
                    dbc.Row([
                        dbc.Col([toggleInfo], width=6),
                        dbc.Col([reps_toggle], width=6)
                    ], justify='center', class_name='mt-1 mb-2')
                ])
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
        dbc.Row([
            dbc.Card(
                dbc.CardBody([
        dbc.Row([
                    dbc.Col([
                        html.Div([
                            dcc.Markdown("""Click on a state or territory to view data and resources"""),
                            html.Pre(id='click-data', style=styles['pre'], className='pt-2 pb-2')
                        ])
                    ], width=12)
                     ], justify='center', class_name='mt-1'),
                    dbc.Row([
dbc.Col([
                        html.Div(
                            html.Pre(id='resources', className='pt-2 pb-2', style=dict(fontFamily='sans-serif'))
                        )
                    ], width=12)


                    ])
                ])
            )
        ]),
        law_cards
], fluid=True)

#callback

@callback(
    Output(mygraph, 'figure'),
    Input(radioitems, 'value'),
    Input(reps_toggle, 'value')
)
def update_graph(topic, toggle):
    # https://plotly.com/python/choropleth-maps/
    if topic == 'Trans Refuge':
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
                                          ticktext=['Hostile to <br>Trans Refuge', 0, 0.6,
                                                    'Greater <br>Trans Refuge'],
                                          ticks='outside',
                                          ticklabeloverflow='allow',
                                          xpad=65,
                                          ticklabelposition='outside top'
                                          ),
                            name="")
        )
        fig.add_scattergeo(
            lat=[38.90478149],
            lon=[-77.01629654],
            mode='markers',
            marker=dict(color="cyan", size=10, symbol='star', line=dict(width=1, color="red")),
            hovertemplate="<b>DC</b>:" + f"<br><b>{dc_wide['Trans Refuge Rank'][0]}</b>" + f"<extra></extra>",
            showlegend=False
        )
        fig.update_layout(
            title={
                'text': '<b>Trans Refuge</b>',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'automargin': True,
                'yref': 'container'
            }
        )
    elif topic == 'Family Services':
        fig = go.Figure(data=go.Choropleth(locations=state_family_data['State Code'],
                                           z=state_family_data['Family Services Rank'],
                                           locationmode='USA-states',
                                           zmin=family_color_min,
                                           zmax=family_color_max,
                                           colorscale='RdPu',
                                           colorbar=dict(orientation='h',
                                                         yref='container',
                                                         y=0.2,
                                                         tickmode='array',
                                                         tickvals=[family_color_min, 0.3, 0.7,
                                                                   family_color_max],
                                                         ticktext=['Less <br>Family Services', 0.3, 0.7,
                                                                   'Greater <br>Family Services'],
                                                         ticks='outside',
                                                         ticklabeloverflow='allow',
                                                         xpad=65,
                                                         ticklabelposition='outside top'
                                                         ),
                                           name=""
                                           )
                        )
        fig.add_scattergeo(
            lat=[38.90478149],
            lon=[-77.01629654],
            mode='markers',
            marker=dict(color="cyan", size=10, symbol='star', line=dict(width=1, color="red")),
            hovertemplate="<b>DC</b>:" + f"<br><b>{dc_wide['Family Services'][0]}</b>" + f"<extra></extra>",
            showlegend=False
        )
        fig.update_layout(
            title = {
                'text': '<b>Family Services</b>',
                'y': 0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'automargin':True,
                'yref':'container'
            }
        )
    elif topic == 'Gender Inclusive Laws & Policies':
        fig = go.Figure(data=go.Choropleth(locations=state_gi_data['State Code'],
                                           z=state_gi_data['G.I. Laws Rank'],
                                           locationmode='USA-states',
                                           zmin=gi_color_min,
                                           zmax=gi_color_max,
                                           colorscale='BuPu',
                                           colorbar=dict(orientation='h',
                                                         yref='container',
                                                         y=0.2,
                                                         tickmode='array',
                                                         tickvals=[gi_color_min, 0.2, 0.6,
                                                                   gi_color_max],
                                                         ticktext=['Less Gender <br>Inclusive', 0.2, 0.6,
                                                                   'More Gender <br>Inclusive'],
                                                         ticks='outside',
                                                         ticklabeloverflow='allow',
                                                         xpad=65,
                                                         ticklabelposition='outside top'
                                                         ),
                                           name=""
                                           )
                        )
        fig.add_scattergeo(
            lat=[38.90478149],
            lon=[-77.01629654],
            mode='markers',
            marker=dict(color="cyan", size=10, symbol='star', line=dict(width=1, color="red")),
            hovertemplate="<b>DC</b>:" + f"<br><b>{dc_wide['Gender Inclusive Laws & Policies'][0]}</b>" + f"<extra></extra>",
            showlegend=False
        )
        fig.update_layout(
            title={
                'text': '<b>Gender Inclusive Laws & Policies</b>',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'automargin': True,
                'yref': 'container'
            }
        )
    elif topic == 'Reproductive Rights':
        fig = go.Figure(data=go.Choropleth(locations=state_repro_data['State Code'],
                                           z=state_repro_data['Reproductive Rights Rank'],
                                           locationmode='USA-states',
                                           zmin=repro_color_min,
                                           zmax=repro_color_max,
                                           colorscale='PuBuGn',
                                           colorbar=dict(orientation='h',
                                                         yref='container',
                                                         y=0.2,
                                                         tickmode='array',
                                                         tickvals=[repro_color_min, 0, 0.5,
                                                                   repro_color_max],
                                                         ticktext=['Hostile Legislation', 0, 0.5,
                                                                   'Greater Reproductive <br> Rights/ Access'],
                                                         ticks='outside',
                                                         ticklabeloverflow='allow',
                                                         xpad=65,
                                                         ticklabelposition='outside top'
                                                         ),
                                           name=""
                                           )
                        )
        fig.add_scattergeo(
            lat=[38.90478149],
            lon=[-77.01629654],
            mode='markers',
            marker=dict(color="cyan", size=10, symbol='star', line=dict(width=1, color="red")),
            hovertemplate="<b>DC</b>:" + f"<br><b>{dc_wide['Reproductive Rights'][0]}</b>" + f"<extra></extra>",
            showlegend=False
        )
        fig.update_layout(
            title={
                'text': '<b>Reproductive Rights</b>',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'automargin': True,
                'yref': 'container'
            }
        )
    else:
        fig = go.Figure(data=go.Choropleth(locations=state_hate_data['State Code'],
                                           z=state_hate_data['Hate Legislation Rank'],
                                           locationmode='USA-states',
                                           zmin=hate_color_min,
                                           zmax=hate_color_max,
                                           colorscale='Dense',
                                           colorbar=dict(orientation='h',
                                                         yref='container',
                                                         y=0.2,
                                                         tickmode='array',
                                                         tickvals=[hate_color_min, -0.4, -0.2,
                                                                   hate_color_max],
                                                         ticktext=['Most Hate<br> Legislation', -0.4,
                                                                   -0.2,
                                                                   'No Hate<br>Legislation'],
                                                         ticks='outside',
                                                         ticklabeloverflow='allow',
                                                         xpad=65,
                                                         ticklabelposition='outside bottom'
                                                         ),
                                           name=""
                                           )
                        )
        fig.add_scattergeo(
            lat=[38.90478149],
            lon=[-77.01629654],
            mode='markers',
            marker=dict(color="cyan", size=10, symbol='star', line=dict(width=1, color="red")),
            hovertemplate="<b>DC</b>:" + f"<br><b>{dc_wide['Hate Legislation'][0]}</b>" + f"<extra></extra>",
            showlegend=False
        )
        fig.update_layout(
            title={
                'text': '<b>Hate Legislation</b>',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'automargin': True,
                'yref': 'container'
            }
        )
    #reps toggle
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

    fig.update_layout(dragmode=False,
                      margin={'r': 0, 't': 0, 'l': 0, 'b': 0},
                      geo_scope='usa',
                    autosize=True,
                      clickmode='event',
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



    return fig # returned objects are assigned to the component property of the Output

@callback(
    Output(territory_graph, 'figure'),
    Input(radioitems, 'value')
)

def filter_heatmap(topic):
    # https://plotly.com/python/heatmaps/
    fig = make_subplots(rows=1, cols=11)
    if topic == 'Trans Refuge':
        # fig.add_trace(go.Heatmap(
        #         z=[dc_wide['Trans Refuge Rank']],
        #         x=['DC'],
        #         hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        #         showscale=False,
        #         zmin=refuge_color_min,
        #         zmax=refuge_color_max,
        #         colorscale='Plotly3_r'
        #
        # ), row=1, col=2)
        fig.add_trace(go.Heatmap(
                z=[as_wide['Trans Refuge Rank']],
                x=['AS'],
                hovertemplate='<b>%{z}</b>' + '<extra></extra>',
                showscale=False,
                zmin=refuge_color_min,
                zmax=refuge_color_max,
                colorscale='Plotly3_r'
            ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[gu_wide['Trans Refuge Rank']],
            x=['GU'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=refuge_color_min,
            zmax=refuge_color_max,
            colorscale='Plotly3_r'
        ), row=1, col=4)
        fig.add_trace(go.Heatmap(
            z=[mp_wide['Trans Refuge Rank']],
            x=['MP'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=refuge_color_min,
            zmax=refuge_color_max,
            colorscale='Plotly3_r'
        ), row=1, col=6)
        fig.add_trace(go.Heatmap(
            z=[pr_wide['Trans Refuge Rank']],
            x=['PR'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=refuge_color_min,
            zmax=refuge_color_max,
            colorscale='Plotly3_r'
        ), row=1, col=8)
        fig.add_trace(go.Heatmap(
            z=[vi_wide['Trans Refuge Rank']],
            x=['VI'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=refuge_color_min,
            zmax=refuge_color_max,
            colorscale='Plotly3_r'
        ), row=1, col=10)
        fig.update_layout(
            annotations=[dict(
                x=0.55,
                y=0.1,
                xref='paper',
                yref='paper',
                yshift=-50,
                text='Sources: <a href="assets/TransRefugeDataSources.pdf", target="_blank">Trans Refuge Data</a> | <a href="assets/TransRepsTableDoc.pdf", target="_blank">2S+TGNC State Reps</a>',
                showarrow=False
            )]
        )
    elif topic == 'Family Services':
        # fig.add_trace(go.Heatmap(
        #     z=[dc_wide['Family Services']],
        #     x=['DC'],
        #     hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        #     showscale=False,
        #     zmin=family_color_min,
        #     zmax=family_color_max,
        #     colorscale='RdPu'
        # ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[as_wide['Family Services']],
            x=['AS'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=family_color_min,
            zmax=family_color_max,
            colorscale='RdPu'
        ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[gu_wide['Family Services']],
            x=['GU'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=family_color_min,
            zmax=family_color_max,
            colorscale='RdPu'
        ), row=1, col=4)
        fig.add_trace(go.Heatmap(
            z=[mp_wide['Family Services']],
            x=['MP'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=family_color_min,
            zmax=family_color_max,
            colorscale='RdPu'
        ), row=1, col=6)
        fig.add_trace(go.Heatmap(
            z=[pr_wide['Family Services']],
            x=['PR'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=family_color_min,
            zmax=family_color_max,
            colorscale='RdPu'
        ), row=1, col=8)
        fig.add_trace(go.Heatmap(
            z=[vi_wide['Family Services']],
            x=['VI'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=family_color_min,
            zmax=family_color_max,
            colorscale='RdPu'
        ), row=1, col=10)
        fig.update_layout(
            annotations=[dict(
                x=0.55,
                y=0.1,
                xref='paper',
                yref='paper',
                yshift=-50,
                text='Sources: <a href="#">Family Services Data </a> | <a href="assets/TransRepsTableDoc.pdf", target="_blank">2S+TGNC State Reps</a>',
                showarrow=False
            )]
        )
    elif topic == 'Gender Inclusive Laws & Policies':
        # fig.add_trace(go.Heatmap(
        #     z=[dc_wide['Gender Inclusive Laws & Policies']],
        #     x=['DC'],
        #     hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        #     showscale=False,
        #     zmin=gi_color_min,
        #     zmax=gi_color_max,
        #     colorscale='BuPu'
        # ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[as_wide['Gender Inclusive Laws & Policies']],
            x=['AS'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=gi_color_min,
            zmax=gi_color_max,
            colorscale='BuPu'
        ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[gu_wide['Gender Inclusive Laws & Policies']],
            x=['GU'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=gi_color_min,
            zmax=gi_color_max,
            colorscale='BuPu'
        ), row=1, col=4)
        fig.add_trace(go.Heatmap(
            z=[mp_wide['Gender Inclusive Laws & Policies']],
            x=['MP'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=gi_color_min,
            zmax=gi_color_max,
            colorscale='BuPu'
        ), row=1, col=6)
        fig.add_trace(go.Heatmap(
            z=[pr_wide['Gender Inclusive Laws & Policies']],
            x=['PR'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=gi_color_min,
            zmax=gi_color_max,
            colorscale='BuPu'
        ), row=1, col=8)
        fig.add_trace(go.Heatmap(
            z=[vi_wide['Gender Inclusive Laws & Policies']],
            x=['VI'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=gi_color_min,
            zmax=gi_color_max,
            colorscale='BuPu'
        ), row=1, col=10),
        fig.update_layout(
            annotations=[dict(
                x=0.55,
                y=0.1,
                xref='paper',
                yref='paper',
                yshift=-50,
                text='Sources: <a href="#">G.I. Laws & Policies Data</a> | <<a href="assets/TransRepsTableDoc.pdf", target="_blank">2S+TGNC State Reps</a>',
                showarrow=False
            )]
        )
    elif topic == 'Reproductive Rights':
        # fig.add_trace(go.Heatmap(
        #     z=[dc_wide['Reproductive Rights']],
        #     x=['DC'],
        #     hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        #     showscale=False,
        #     zmin=repro_color_min,
        #     zmax=repro_color_max,
        #     colorscale='PuBuGn'
        # ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[as_wide['Reproductive Rights']],
            x=['AS'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=repro_color_min,
            zmax=repro_color_max,
            colorscale='PuBuGn'
        ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[gu_wide['Reproductive Rights']],
            x=['GU'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=repro_color_min,
            zmax=repro_color_max,
            colorscale='PuBuGn'
        ), row=1, col=4)
        fig.add_trace(go.Heatmap(
            z=[mp_wide['Reproductive Rights']],
            x=['MP'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=repro_color_min,
            zmax=repro_color_max,
            colorscale='PuBuGn'
        ), row=1, col=6)
        fig.add_trace(go.Heatmap(
            z=[pr_wide['Reproductive Rights']],
            x=['PR'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=repro_color_min,
            zmax=repro_color_max,
            colorscale='PuBuGn'
        ), row=1, col=8)
        fig.add_trace(go.Heatmap(
            z=[vi_wide['Reproductive Rights']],
            x=['VI'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=repro_color_min,
            zmax=repro_color_max,
            colorscale='PuBuGn'
        ), row=1, col=10)
        fig.update_layout(
            annotations=[dict(
                x=0.55,
                y=0.1,
                xref='paper',
                yref='paper',
                yshift=-50,
                text='Sources: <a href="#">Reproductive Rights Data</a> | <a href="assets/TransRepsTableDoc.pdf", target="_blank">2S+TGNC State Reps</a>',
                showarrow=False
            )]
        )
    else:
        # fig.add_trace(go.Heatmap(
        #     z=[dc_wide['Hate Legislation']],
        #     x=['DC'],
        #     hovertemplate='<b>%{z}</b>' + '<extra></extra>',
        #     showscale=False,
        #     zmin=hate_color_min,
        #     zmax=hate_color_max,
        #     colorscale='Dense'
        # ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[as_wide['Hate Legislation']],
            x=['AS'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=hate_color_min,
            zmax=hate_color_max,
            colorscale='Dense'
        ), row=1, col=2)
        fig.add_trace(go.Heatmap(
            z=[gu_wide['Hate Legislation']],
            x=['GU'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=hate_color_min,
            zmax=hate_color_max,
            colorscale='Dense'
        ), row=1, col=4)
        fig.add_trace(go.Heatmap(
            z=[mp_wide['Hate Legislation']],
            x=['MP'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=hate_color_min,
            zmax=hate_color_max,
            colorscale='Dense'
        ), row=1, col=6)
        fig.add_trace(go.Heatmap(
            z=[pr_wide['Hate Legislation']],
            x=['PR'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=hate_color_min,
            zmax=hate_color_max,
            colorscale='Dense'
        ), row=1, col=8)
        fig.add_trace(go.Heatmap(
            z=[vi_wide['Hate Legislation']],
            x=['VI'],
            hovertemplate='<b>%{z}</b>' + '<extra></extra>',
            showscale=False,
            zmin=hate_color_min,
            zmax=hate_color_max,
            colorscale='Dense'
        ), row=1, col=10)
        fig.update_layout(
            annotations=[dict(
                x=0.55,
                y=0.1,
                xref='paper',
                yref='paper',
                yshift=-50,
                text='Sources: <a href="#">Hate Legislation Data</a> | <a href="assets/TransRepsTableDoc.pdf", target="_blank">2S+TGNC State Reps</a>',
                showarrow=False
            )]
        )

    fig.update_layout(dragmode=False,
                      autosize=True,
                      clickmode='event'
                      )
    fig.update_xaxes(side='top')
    fig.update_yaxes(showticklabels=False,
                     automargin=True)

    return fig  # returned objects are assigned to the component property of the Output


# update cards
@callback(
    Output(law_cards, 'children'),
    Input(radioitems, 'value'),
)

def update_cards(topic):
    if topic == 'Trans Refuge':
        law_cards= dbc.Row([
    dbc.Row([' Laws & Polices Ranked:'], class_name='h3 mt-2'),
    dbc.Row([
                dbc.Col([shield_card], width=6),
                dbc.Col([name_card], width=6)
            ], justify='center'),dbc.Row([
                dbc.Col([gender_marker_id_card], width=6),
                dbc.Col([gender_marker_bc_card], width=6),
                dbc.Col([nondiscrimination_card], width=6),
            ], justify='center')

], justify='center'
    )
    elif topic == 'Family Services':
        law_cards = dbc.Row([
    dbc.Row([' Laws & Polices Ranked:'], class_name='h3 mt-2'),
    dbc.Row([
                dbc.Col([foster_card], width=6),
                dbc.Col([adoption_card], width=6)
            ],justify='center'),
            dbc.Row([dbc.Col([child_welfare_card], width=6),
                     dbc.Col([assisted_repro_card], width=6)
                     ],justify='center'),
            dbc.Row([
                dbc.Col([vap_card], width=6)
            ], justify='center')
], justify='center'
    )
    elif topic == 'Gender Inclusive Laws & Policies':
        law_cards = dbc.Row([
            dbc.Row([' Laws & Polices Ranked:'], class_name='h3 mt-2'),
            dbc.Row([
                dbc.Col([gi_bathroom_card], width=6),
                dbc.Col([lgbtq_curriculum_card], width=6),
            ],justify='center'),
            dbc.Row([
                dbc.Col([anti_bully_students_card], width=6),
                dbc.Col([non_discrimination_students_card], width=6)
            ],justify='center'),
            dbc.Row([
                     dbc.Col([gay_trans_panic_card], width=6),
                     dbc.Col([hate_crime_gi_card], width=6)
                     ], justify='center'),
            dbc.Row([
                dbc.Col([jury_service_gi_card], width=6),
                dbc.Col([gi_correctional_housing_card], width=6),
                dbc.Col([gender_affirming_care_corr_card], width=6)
            ], justify='center')
        ], justify='center'
        )
    elif topic == 'Reproductive Rights':
        law_cards = dbc.Row([
            dbc.Row([' Laws & Polices Ranked:'], class_name='h3 mt-2'),
            dbc.Row([
                dbc.Col([abortion_card], width=6),
                dbc.Col([interstate_shield_card], width=6),
            ],justify='center')
        ], justify='center'
        )
    else:
        law_cards = dbc.Row([
            dbc.Row([' Laws & Polices Ranked:'], class_name='h3 mt-2'),
            dbc.Row([
                dbc.Col([bathroom_k_12_card], width=6),
                dbc.Col([bathroom_schools_gov_card], width=6),
            ], justify='center'),
            dbc.Row([
                dbc.Col([define_sex_card], width=6),
                dbc.Col([rfra_card], width=6)
            ], justify='center'),
            dbc.Row([
                dbc.Col([re_child_welfare_card], width=6),
                dbc.Col([re_medical_card], width=6)
            ], justify='center'),
            dbc.Row([
                dbc.Col([marriage_denial_card], width=6),
                dbc.Col([drag_ban_card], width=6),
                dbc.Col([dont_say_gay_card], width=6),
                dbc.Col([subject_rest_card], width=6),
                dbc.Col([parental_opt_card], width=6),
                dbc.Col([sports_ban_card], width=6),
                dbc.Col([forced_out_card], width=6),
                dbc.Col([youth_health_ban_card], width=6),
                dbc.Col([barriers_id_card], width=6)
            ], justify='center')
        ], justify='center'
        )

    return law_cards

@callback(
    Output('click-data', 'children'),
    Input(radioitems,'value'),
    Input(mygraph, 'clickData'),
    Input(territory_graph, 'clickData'))

def display_click_data(topic, clickData, t_clickData):
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if input_id == 'stateMap':
        state_code = clickData['points'][0]['location']
        state_refuge_df = state_refuge_data.copy()
        state_refuge_df.insert(0, 'State Name', state_name_col)
        if topic == 'Trans Refuge':
            state_df = state_refuge_df[state_refuge_df['State Code'] == state_code]
            state_name = state_df.iloc[0]['State Name']
            state_df.reset_index(drop=True, inplace=True)
            state_df.drop('State Code', axis=1, inplace=True)
            state_df.drop('State Name', axis=1, inplace=True)
            state_df1 = pd.DataFrame(data=state_df).transpose()
            state_df1['Laws and Policies'] = state_df1.index
            rank = state_df1.pop(0)
            state_df1.insert(1, 'Rank', rank)
            state_table = dbc.Container([
                dbc.Label(f'{state_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(state_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                 style_header={
                     'backgroundColor': 'rgb(93, 101, 178)',
                     'color': 'white',
                     'fontFamily': 'sans-serif',
                     'fontWeight': 'bold'

                 },
                 style_data={
                     'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                 style_data_conditional=[
                     {
                         'if': {'row_index': 'odd'},
                         'backgroundColor': 'rgb(156, 163, 209)',
                     },
                     {
                         "if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                         "border": "inherit !important",
                     },
                     {
                         "if": {"row_index": len(state_df1) - 1},
                         'backgroundColor': 'rgb(93, 101, 178)',
                         'color': 'white',
                         'fontFamily': 'sans-serif',
                         'fontWeight': 'bold'
                     }
                 ],
                                     export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                 )
            ])
            return state_table
        elif topic == 'Family Services':
            state_family_df = state_family_data.copy()
            state_family_df.insert(0, 'State Name', state_name_col)
            state_df = state_family_df[state_family_df['State Code'] == state_code]
            state_name = state_df.iloc[0]['State Name']
            state_df.reset_index(drop=True, inplace=True)
            state_df.drop('State Code', axis=1, inplace=True)
            state_df.drop('State Name', axis=1, inplace=True)
            state_df1 = pd.DataFrame(data=state_df).transpose()
            state_df1['Laws and Policies'] = state_df1.index
            rank = state_df1.pop(0)
            state_df1.insert(1, 'Rank', rank)
            state_table = dbc.Container([
                dbc.Label(f'{state_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(state_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                 style_header={
                     'backgroundColor': 'rgb(93, 101, 178)',
                     'color': 'white',
                     'fontFamily': 'sans-serif',
                     'fontWeight': 'bold'

                 },
                 style_data={
                     'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                 style_data_conditional=[
                     {
                         'if': {'row_index': 'odd'},
                         'backgroundColor': 'rgb(156, 163, 209)',
                     },
                     {
                         "if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                         "border": "inherit !important",
                     },
                     {
                         "if": {"row_index": len(state_df1) - 1},
                         'backgroundColor': 'rgb(93, 101, 178)',
                         'color': 'white',
                         'fontFamily': 'sans-serif',
                         'fontWeight': 'bold'
                     }
                 ],
                                     export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                 )
            ])
            return state_table
        elif topic == 'Gender Inclusive Laws & Policies':
            state_gi_df = state_gi_data.copy()
            state_gi_df.insert(0, 'State Name', state_name_col)
            state_df = state_gi_df[state_gi_df['State Code'] == state_code]
            state_name = state_df.iloc[0]['State Name']
            state_df.reset_index(drop=True, inplace=True)
            state_df.drop('State Code', axis=1, inplace=True)
            state_df.drop('State Name', axis=1, inplace=True)
            state_df1 = pd.DataFrame(data=state_df).transpose()
            state_df1['Laws and Policies'] = state_df1.index
            rank = state_df1.pop(0)
            state_df1.insert(1, 'Rank', rank)
            state_table = dbc.Container([
                dbc.Label(f'{state_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(state_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                 style_header={
                     'backgroundColor': 'rgb(93, 101, 178)',
                     'color': 'white',
                     'fontFamily': 'sans-serif',
                     'fontWeight': 'bold'

                 },
                 style_data={
                     'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                 style_data_conditional=[
                     {
                         'if': {'row_index': 'odd'},
                         'backgroundColor': 'rgb(156, 163, 209)',
                     },
                     {
                         "if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                         "border": "inherit !important",
                     },
                     {
                         "if": {"row_index": len(state_df1) - 1},
                         'backgroundColor': 'rgb(93, 101, 178)',
                         'color': 'white',
                         'fontFamily': 'sans-serif',
                         'fontWeight': 'bold'
                     }
                 ],  export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                 )
            ])
            return state_table
        elif topic == 'Reproductive Rights':
            state_repro_df = state_repro_data.copy()
            state_repro_df.insert(0, 'State Name', state_name_col)
            state_df = state_repro_df[state_repro_df['State Code'] == state_code]
            state_name = state_df.iloc[0]['State Name']
            state_df.reset_index(drop=True, inplace=True)
            state_df.drop('State Code', axis=1, inplace=True)
            state_df.drop('State Name', axis=1, inplace=True)
            state_df1 = pd.DataFrame(data=state_df).transpose()
            state_df1['Laws and Policies'] = state_df1.index
            rank = state_df1.pop(0)
            state_df1.insert(1, 'Rank', rank)
            state_table = dbc.Container([
                dbc.Label(f'{state_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(state_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                 style_header={
                     'backgroundColor': 'rgb(93, 101, 178)',
                     'color': 'white',
                     'fontFamily': 'sans-serif',
                     'fontWeight': 'bold'

                 },
                 style_data={
                     'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                 style_data_conditional=[
                     {
                         'if': {'row_index': 'odd'},
                         'backgroundColor': 'rgb(156, 163, 209)',
                     },
                     {
                         "if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                         "border": "inherit !important",
                     },
                     {
                         "if": {"row_index": len(state_df1) - 1},
                         'backgroundColor': 'rgb(93, 101, 178)',
                         'color': 'white',
                         'fontFamily': 'sans-serif',
                         'fontWeight': 'bold'
                     }
                 ],  export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                 )
            ])
            return state_table
        elif topic == 'Hate Legislation':
            state_hate_df = state_hate_data.copy()
            state_hate_df.insert(0, 'State Name', state_name_col)
            state_df = state_hate_df[state_hate_df['State Code'] == state_code]
            state_name = state_df.iloc[0]['State Name']
            state_df.reset_index(drop=True, inplace=True)
            state_df.drop('State Code', axis=1, inplace=True)
            state_df.drop('State Name', axis=1, inplace=True)
            state_df1 = pd.DataFrame(data=state_df).transpose()
            state_df1['Laws and Policies'] = state_df1.index
            rank = state_df1.pop(0)
            state_df1.insert(1, 'Rank', rank)
            state_table = dbc.Container([
                dbc.Label(f'{state_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(state_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                 style_header={
                     'backgroundColor': 'rgb(93, 101, 178)',
                     'color': 'white',
                     'fontFamily': 'sans-serif',
                     'fontWeight': 'bold'

                 },
                 style_data={
                     'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                 style_data_conditional=[
                     {
                         'if': {'row_index': 'odd'},
                         'backgroundColor': 'rgb(156, 163, 209)',
                     },
                     {
                         "if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                         "border": "inherit !important",
                     },
                     {
                         "if": {"row_index": len(state_df1) - 1},
                         'backgroundColor': 'rgb(93, 101, 178)',
                         'color': 'white',
                         'fontFamily': 'sans-serif',
                         'fontWeight': 'bold'
                     }
                 ],
                                     export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                 )
            ])
            return state_table
    elif input_id == 'terrMap':
        terr_code = t_clickData['points'][0]['x']
        terr_refuge_df = territory_refuge_data.copy()
        terr_refuge_df.insert(0, 'Territory Name', terr_name_col)
        if topic == 'Trans Refuge':
            terr_df = terr_refuge_df[terr_refuge_df['Territory Code'] == terr_code]
            terr_name = terr_df.iloc[0]['Territory Name']
            terr_df.reset_index(drop=True, inplace=True)
            terr_df.drop('Territory Code', axis=1, inplace=True)
            terr_df.drop('Territory Name', axis=1, inplace=True)
            terr_df1 = pd.DataFrame(data=terr_df).transpose()
            terr_df1['Laws and Policies'] = terr_df1.index
            rank = terr_df1.pop(0)
            terr_df1.insert(1, 'Rank', rank)
            terr_table = dbc.Container([
                dbc.Label(f'{terr_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(terr_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                                     style_header={
                                         'backgroundColor': 'rgb(93, 101, 178)',
                                         'color': 'white',
                                         'fontFamily': 'sans-serif',
                                         'fontWeight': 'bold'

                                     },
                                     style_data={
                                         'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                                     style_data_conditional=[
                                         {
                                             'if': {'row_index': 'odd'},
                                             'backgroundColor': 'rgb(156, 163, 209)',
                                         },
                                         {
                                             "if": {"state": "selected"},
                                             "backgroundColor": "inherit !important",
                                             "border": "inherit !important",
                                         },
                                         {
                                             "if": {"row_index": len(terr_df1) - 1},
                                             'backgroundColor': 'rgb(93, 101, 178)',
                                             'color': 'white',
                                             'fontFamily': 'sans-serif',
                                             'fontWeight': 'bold'
                                         }
                                     ],
                                     export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                                     )
            ])
            return terr_table
        elif topic == 'Family Services':
            terr_family_df = territory_family_data.copy()
            terr_family_df.insert(0, 'Territory Name', terr_name_col)
            terr_df = terr_family_df[terr_family_df['Territory Code'] == terr_code]
            terr_name = terr_df.iloc[0]['Territory Name']
            terr_df.reset_index(drop=True, inplace=True)
            terr_df.drop('Territory Code', axis=1, inplace=True)
            terr_df.drop('Territory Name', axis=1, inplace=True)
            terr_df1 = pd.DataFrame(data=terr_df).transpose()
            terr_df1['Laws and Policies'] = terr_df1.index
            rank = terr_df1.pop(0)
            terr_df1.insert(1, 'Rank', rank)
            terr_table = dbc.Container([
                dbc.Label(f'{terr_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(terr_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                                     style_header={
                                         'backgroundColor': 'rgb(93, 101, 178)',
                                         'color': 'white',
                                         'fontFamily': 'sans-serif',
                                         'fontWeight': 'bold'

                                     },
                                     style_data={
                                         'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                                     style_data_conditional=[
                                         {
                                             'if': {'row_index': 'odd'},
                                             'backgroundColor': 'rgb(156, 163, 209)',
                                         },
                                         {
                                             "if": {"state": "selected"},
                                             "backgroundColor": "inherit !important",
                                             "border": "inherit !important",
                                         },
                                         {
                                             "if": {"row_index": len(terr_df1) - 1},
                                             'backgroundColor': 'rgb(93, 101, 178)',
                                             'color': 'white',
                                             'fontFamily': 'sans-serif',
                                             'fontWeight': 'bold'
                                         }
                                     ],
                                     export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                                     )
            ])
            return terr_table
        elif topic == 'Gender Inclusive Laws & Policies':
            terr_gi_df = territory_gi_data.copy()
            terr_gi_df.insert(0, 'Territory Name', terr_name_col)
            terr_df = terr_gi_df[terr_gi_df['Territory Code'] == terr_code]
            terr_name = terr_df.iloc[0]['Territory Name']
            terr_df.reset_index(drop=True, inplace=True)
            terr_df.drop('Territory Code', axis=1, inplace=True)
            terr_df.drop('Territory Name', axis=1, inplace=True)
            terr_df1 = pd.DataFrame(data=terr_df).transpose()
            terr_df1['Laws and Policies'] = terr_df1.index
            rank = terr_df1.pop(0)
            terr_df1.insert(1, 'Rank', rank)
            terr_table = dbc.Container([
                dbc.Label(f'{terr_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(terr_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                                     style_header={
                                         'backgroundColor': 'rgb(93, 101, 178)',
                                         'color': 'white',
                                         'fontFamily': 'sans-serif',
                                         'fontWeight': 'bold'

                                     },
                                     style_data={
                                         'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                                     style_data_conditional=[
                                         {
                                             'if': {'row_index': 'odd'},
                                             'backgroundColor': 'rgb(156, 163, 209)',
                                         },
                                         {
                                             "if": {"state": "selected"},
                                             "backgroundColor": "inherit !important",
                                             "border": "inherit !important",
                                         },
                                         {
                                             "if": {"row_index": len(terr_df1) - 1},
                                             'backgroundColor': 'rgb(93, 101, 178)',
                                             'color': 'white',
                                             'fontFamily': 'sans-serif',
                                             'fontWeight': 'bold'
                                         }
                                     ],
                                     export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                                     )
            ])
            return terr_table
        elif topic == 'Reproductive Rights':
            terr_repro_df = territory_repro_data.copy()
            terr_repro_df.insert(0, 'Territory Name', terr_name_col)
            terr_df = terr_repro_df[terr_repro_df['Territory Code'] == terr_code]
            terr_name = terr_df.iloc[0]['Territory Name']
            terr_df.reset_index(drop=True, inplace=True)
            terr_df.drop('Territory Code', axis=1, inplace=True)
            terr_df.drop('Territory Name', axis=1, inplace=True)
            terr_df1 = pd.DataFrame(data=terr_df).transpose()
            terr_df1['Laws and Policies'] = terr_df1.index
            rank = terr_df1.pop(0)
            terr_df1.insert(1, 'Rank', rank)
            terr_table = dbc.Container([
                dbc.Label(f'{terr_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(terr_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                                     style_header={
                                         'backgroundColor': 'rgb(93, 101, 178)',
                                         'color': 'white',
                                         'fontFamily': 'sans-serif',
                                         'fontWeight': 'bold'

                                     },
                                     style_data={
                                         'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                                     style_data_conditional=[
                                         {
                                             'if': {'row_index': 'odd'},
                                             'backgroundColor': 'rgb(156, 163, 209)',
                                         },
                                         {
                                             "if": {"state": "selected"},
                                             "backgroundColor": "inherit !important",
                                             "border": "inherit !important",
                                         },
                                         {
                                             "if": {"row_index": len(terr_df1) - 1},
                                             'backgroundColor': 'rgb(93, 101, 178)',
                                             'color': 'white',
                                             'fontFamily': 'sans-serif',
                                             'fontWeight': 'bold'
                                         }
                                     ],
                                     export_format='xlsx',
                                     export_headers='display',
                                     merge_duplicate_headers=True
                                     )
            ])
            return terr_table
        elif topic == 'Hate Legislation':
            terr_hate_df = territory_hate_data.copy()
            terr_hate_df.insert(0, 'Territory Name', terr_name_col)
            terr_df = terr_hate_df[terr_hate_df['Territory Code'] == terr_code]
            terr_name = terr_df.iloc[0]['Territory Name']
            terr_df.reset_index(drop=True, inplace=True)
            terr_df.drop('Territory Code', axis=1, inplace=True)
            terr_df.drop('Territory Name', axis=1, inplace=True)
            terr_df1 = pd.DataFrame(data=terr_df).transpose()
            terr_df1['Laws and Policies'] = terr_df1.index
            rank = terr_df1.pop(0)
            terr_df1.insert(1, 'Rank', rank)
            terr_table = dbc.Container([
                dbc.Label(f'{terr_name}', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-1'),
                dash_table.DataTable(terr_df1.to_dict('records'),
                                     editable=False,
                                     style_cell={'textAlign': 'left'},
                                     style_header={
                                         'backgroundColor': 'rgb(93, 101, 178)',
                                         'color': 'white',
                                         'fontFamily': 'sans-serif',
                                         'fontWeight': 'bold'

                                     },
                                     style_data={
                                         'backgroundColor': 'white',
                                         'fontFamily': 'sans-serif',
                                         'color': 'Black'
                                     },
                                     style_data_conditional=[
                                         {
                                             'if': {'row_index': 'odd'},
                                             'backgroundColor': 'rgb(156, 163, 209)',
                                         },
                                         {
                                             "if": {"state": "selected"},
                                             "backgroundColor": "inherit !important",
                                             "border": "inherit !important",
                                         },
                                         {
                                             "if": {"row_index": len(terr_df1) - 1},
                                             'backgroundColor': 'rgb(93, 101, 178)',
                                             'color': 'white',
                                             'fontFamily': 'sans-serif',
                                             'fontWeight': 'bold'
                                         }
                                     ],
                                     )
            ])
            return terr_table



@callback(
    Output('resources', 'children'),
    Input(radioitems,'value'),
    Input(mygraph, 'clickData'),
    Input(territory_graph, 'clickData')
)

def update_resources(topic, clickData, t_clickData):
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if input_id == 'stateMap':
        state_code = clickData['points'][0]['location']
        rust_states = ['PA', 'IA', 'WI', 'OH', 'MI']
        if topic == 'Trans Refuge' and state_code in rust_states:
            state_refuge_df = state_refuge_data.copy()
            state_refuge_df.insert(0, 'State Name', state_name_col)
            state_df = state_refuge_df[state_refuge_df['State Code'] == state_code]
            state_name = state_df.iloc[0]['State Name']
            if state_code == 'MI':
                state_resource = dbc.Container([
                    dbc.Label(f'{state_name} 2S+TGNC Resources and Organizations:', style=dict(fontWeight = 'bold', textAlign = 'center', fontFamily='sans-serif'), className='fs-4'),
                    mi_resources
                ])
                return state_resource
            elif state_code == 'WI':
                state_resource = dbc.Container([
                    dbc.Label(f'{state_name} 2S+TGNC Resources and Organizations:',
                              style=dict(fontWeight='bold', textAlign='center', fontFamily='sans-serif'),
                              className='fs-4'),
                    wi_resources
                ])
                return state_resource
            elif state_code == 'PA':
                state_resource = dbc.Container([
                    dbc.Label(f'{state_name} 2S+TGNC Resources and Organizations:',
                              style=dict(fontWeight='bold', textAlign='center', fontFamily='sans-serif'),
                              className='fs-4'),
                    pa_resources
                ])
                return state_resource
            elif state_code == 'OH':
                state_resource = dbc.Container([
                    dbc.Label(f'{state_name} 2S+TGNC Resources and Organizations:',
                              style=dict(fontWeight='bold', textAlign='center', fontFamily='sans-serif'),
                              className='fs-4'),
                    oh_resources
                ])
                return state_resource
            elif state_code == 'IA':
                state_resource = dbc.Container([
                    dbc.Label(f'{state_name} 2S+TGNC Resources and Organizations:',
                              style=dict(fontWeight='bold', textAlign='center', fontFamily='sans-serif'),
                              className='fs-4'),
                    ia_resources
                ])
                return state_resource
        else:
            return national_resources
    elif input_id == 'terrMap':
        return national_resources