from dash import Dash, html, register_page  # pip install dash
import dash_bootstrap_components as dbc

register_page(__name__)


shield_card = dbc.AccordionItem(
       [
           html.Div(['Shield Laws vary from state to state. In our research, we included any legislation or executive order which has a primary goal of protecting providers, patients, and advocates in providing and accessing trangender-related healthcare.'], className='fs-6 fw-normal'),
           html.Div(['Shield Laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'], className='fs-6 mt-1 fw-normal'),
           ], title='Shield Laws',className='h6 mt-1'
    )
name_card = dbc.AccordionItem(
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
    )
gender_marker_id_card = dbc.AccordionItem(
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
    )
gender_marker_bc_card = dbc.AccordionItem(
       [
           html.Div(["Gender Marker on Birth Certificate laws refer to state legislation regarding gender marker changes on birth certificates. These laws are ranked on a scale of (-1,1)."], className='fs-6 fw-normal mb-1'),
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
    )
nondiscrimination_card = dbc.AccordionItem(
       [
           html.Div(["Non-Discrimination laws refer to state non-discrimination laws regarding housing, employment, and public accomodations, that expicitly cover gender identity (-1,1)."], className='fs-6 fw-normal mb-1'),
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
    )


refuge_laws_cat = dbc.Accordion([
    dbc.AccordionItem([
dbc.Accordion(
                        [shield_card, name_card, gender_marker_id_card, gender_marker_bc_card, nondiscrimination_card], start_collapsed=True
                    )
], title='Trans Refuge Laws')], start_collapsed=True)

# family cards
foster_card = dbc.AccordionItem(
       [
           html.Div(['Foster Care Non-Discrimination Laws are protections from discrimination for 2S+TGNC foster parents and families by agencies and officials.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Foster Care Non-Discrimination',className='h6 mt-1'
    )


adoption_card = dbc.AccordionItem(
       [
           html.Div(['Adoption Non-Discrimination Laws are protections from discrimination for 2S+TGNC parents and families by adoption agencies and officials.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Adoption Non-Discrimination',className='h6 mt-1'
    )

child_welfare_card = dbc.AccordionItem(
       [
           html.Div(['Child Welfare Non-Discrimination Laws are protections from discrimination for 2S+TGNC youth in the child welfare system.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Child Welfare Non-Discrimination',className='h6 mt-1'
    )
assisted_repro_card = dbc.AccordionItem(
       [
           html.Div(['Assisted Reproduction Recognition Laws provide legal recognition for intended non-genetic parents regardless of marital status.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Assisted Reproduction Recognition',className='h6 mt-1'
    )
vap_card = dbc.AccordionItem(
       [
           html.Div(['VAP Recognition refers to legal recognition of parentage through "voluntary acknowledgement of parentage". For our purposes, we have only included VAP laws which explicitly apply to LGBTQ parents and non-genetic parents.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='VAP Recognition',className='h6 mt-1'
    )

family_laws_cat = dbc.Accordion([dbc.AccordionItem(
[dbc.Accordion([
    foster_card, adoption_card, assisted_repro_card, vap_card
], start_collapsed=True)],title='Family Services'
) ], start_collapsed=True)

#gi cards
gi_bathroom_card= dbc.AccordionItem(
       [
           html.Div(['Gender Inclusive Bathroom Laws refer to legal protections for people to access bathroom facilities consistent with their gender identity.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gender Inclusive Bathroom Laws',className='h6 mt-1'
    )
lgbtq_curriculum_card = dbc.AccordionItem(
       [
           html.Div(['LGBTQ Inclusive Curriculum refers laws which explicitly require inclusion of LGBTQ-related history and people in state curricular standards.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='LGBTQ Inclusive Curriculum',className='h6 mt-1'
    )
anti_bully_students_card = dbc.AccordionItem(
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
    )
non_discrimination_students_card = dbc.AccordionItem(
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
    )
gay_trans_panic_card = dbc.AccordionItem(
       [
           html.Div(["Gay/ Trans Panic Defense Ban refers to state 'panic defense' prohibit the use of a defense which attempts to blame a victim's sexual orientation or gender identity for the defendant's action(s)."], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gay/Trans Panic Defense Ban',className='h6 mt-1'
    )
hate_crime_gi_card = dbc.AccordionItem(
       [
           html.Div(['Hate Crime Laws refer to increased penalties or enhancements for crimes committed with bias toward a protected group. For the purpose of our research, we have only included hate crime laws which explicitely include gender identity or expression as a protected category.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Hate Crime Laws',className='h6 mt-1'
    )
jury_service_gi_card= dbc.AccordionItem(
       [
           html.Div(['Jury Service Nondiscrimination Laws proibit discrimination against jurors on the basis of protected characteristics. For the purpose of our research, we have only included laws which enumerate gender identiry or expression as a protected category.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Jury Service Non-Discrimination Laws',className='h6 mt-1'
    )
gi_correctional_housing_card= dbc.AccordionItem(
       [
           html.Div(['Gender Inclusive Correctional Housing Laws allow and provide guidance for incarcerated 2S+TGNC people to be housed according to their gender identity.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gender Inclusive Correctional Housing',className='h6 mt-1'
    )
gender_affirming_care_corr_card = dbc.AccordionItem(
       [
           html.Div(['Gender Affirming Care in Correctional Facilities refers to state law or policy providing for incarcerated 2S+TGNC people to receive gender-affirming care while incarcerated.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Gender Affirming Care in Correctional Facilities',className='h6 mt-1'
    )

gi_laws_cat = dbc.Accordion([
    dbc.AccordionItem([dbc.Accordion([
    gi_bathroom_card, lgbtq_curriculum_card, anti_bully_students_card, non_discrimination_students_card, gay_trans_panic_card, hate_crime_gi_card, jury_service_gi_card, gi_correctional_housing_card, gender_affirming_care_corr_card
], start_collapsed=True)
    ], title='Gender Inclusive Laws & Policies')
], start_collapsed=True)

#repro cards
abortion_card = dbc.AccordionItem(
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
    )
interstate_shield_card = dbc.AccordionItem(
       [
           html.Div(['Interstate Abortion Shield Laws protect providers, patients, and those who assist patients in access abortion from out-of-state investigation and/or legal action.'], className='fs-6 fw-normal mb-1'),
           html.Div([
                        'These laws are ranked as either TRUE or FALSE. For ranking purposes, TRUE values equate to 1, and FALSE values equate to 0.'],
                    className='fs-6 mt-1 fw-normal')
           ], title='Interstate Abortion Shield Law',className='h6 mt-1'
    )

repro_laws_cat = dbc.Accordion([
    dbc.AccordionItem([
        dbc.Accordion([
    abortion_card, interstate_shield_card
        ], start_collapsed=True)
    ], title ='Reproductive Rights')
], start_collapsed=True)



#hate cards
bathroom_k_12_card = dbc.AccordionItem(
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
    )
bathroom_schools_gov_card = dbc.AccordionItem(
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
    )
define_sex_card = dbc.AccordionItem(
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
    )
rfra_card = dbc.AccordionItem(
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
    )
re_child_welfare_card = dbc.AccordionItem(
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
    )
re_medical_card = dbc.AccordionItem(
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
    )
marriage_denial_card = dbc.AccordionItem(
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
    )
drag_ban_card = dbc.AccordionItem(
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
    )
dont_say_gay_card = dbc.AccordionItem(
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
    )
subject_rest_card = dbc.AccordionItem(
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
    )
parental_opt_card = dbc.AccordionItem(
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
    )
sports_ban_card = dbc.AccordionItem(
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
    )

forced_out_card = dbc.AccordionItem(
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
    )
youth_health_ban_card = dbc.AccordionItem(
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
    )
barriers_id_card = dbc.AccordionItem(
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
    )

hate_laws_cat = dbc.Accordion([
    dbc.AccordionItem([
dbc.Accordion([
            bathroom_k_12_card, bathroom_schools_gov_card, define_sex_card, rfra_card, re_child_welfare_card,
            re_medical_card, drag_ban_card, dont_say_gay_card, subject_rest_card, parental_opt_card, sports_ban_card, forced_out_card, barriers_id_card
], start_collapsed=True)], title='Hate Legislation')

    ], start_collapsed=True)




layout = dbc.Container(
    [
        dbc.Row([
            dbc.Row(['Catalog of All Laws and Policies We Ranked:'], class_name='h3 mt-2'),
            dbc.Col([refuge_laws_cat], width=6, class_name='h6 fw-normal mt-2'),
dbc.Col([family_laws_cat], width=6, class_name='h6 fw-normal mt-2'),
dbc.Col([gi_laws_cat], width=6, class_name='h6 fw-normal mt-2'),
dbc.Col([repro_laws_cat], width=6, class_name='h6 fw-normal mt-2'),
dbc.Col([hate_laws_cat], width=6, class_name='h6 fw-normal mt-2')
        ], justify='center')
    ], fluid=True, className='d-flex flex-column min-vh-100')
