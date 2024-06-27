import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Load the dataset
file_path = r"C:\Users\Shayna\OneDrive - Michigan State University\Documents\MSU The Center - Shayna Laptop\DestinationCumulativeDataset.csv"
all_majors_data = pd.read_csv(file_path)

# ALL MAJORS

# Modify the dataset and processing the state data
state_counts = all_majors_data['Employer State'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']
state_counts = state_counts.drop([14, 43, 44])
state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}
state_counts['StateAbbrev'] = state_counts['State'].map(state_abbrev)
abbrev = state_counts['StateAbbrev']
state_counts['LogCount'] = np.log1p(state_counts['Count'])

# Process city data
city_counts = all_majors_data['Employer City'].value_counts().reset_index()
city_counts.columns = ['City', 'Count']

# Making the Choropleth map for states
fig = px.choropleth(
    state_counts,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig.update_layout(coloraxis_showscale=False)

# APPLIED ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Applied Engineering Sciences).csv"
applied_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_app = applied_data['Employer State'].value_counts().reset_index()
state_counts_app.columns = ['State', 'Count']
state_counts_app['StateAbbrev'] = state_counts_app['State'].map(state_abbrev)
abbrev = state_counts_app['StateAbbrev']
state_counts_app['LogCount'] = np.log1p(state_counts_app['Count'])

fig_app = px.choropleth(
    state_counts_app,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Applied Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_app.update_layout(coloraxis_showscale=False)

# BIOSYSTEMS ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Biosystems Engineering).csv"
biosystems_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_bio = biosystems_data['Employer State'].value_counts().reset_index()
state_counts_bio.columns = ['State', 'Count']
state_counts_bio['StateAbbrev'] = state_counts_bio['State'].map(state_abbrev)
abbrev = state_counts_bio['StateAbbrev']
state_counts_bio['LogCount'] = np.log1p(state_counts_bio['Count'])

fig_bio = px.choropleth(
    state_counts_bio,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Biosystems Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_bio.update_layout(coloraxis_showscale=False)

# CHEMICAL ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Chemical Engineering).csv"
chemical_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_chem = chemical_data['Employer State'].value_counts().reset_index()
state_counts_chem.columns = ['State', 'Count']
state_counts_chem['StateAbbrev'] = state_counts_chem['State'].map(state_abbrev)
abbrev = state_counts_chem['StateAbbrev']
state_counts_chem['LogCount'] = np.log1p(state_counts_chem['Count'])

fig_chem = px.choropleth(
    state_counts_chem,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Chemical Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_chem.update_layout(coloraxis_showscale=False)

# CIVIL ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Civil Engineering).csv"
civil_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_civ = civil_data['Employer State'].value_counts().reset_index()
state_counts_civ.columns = ['State', 'Count']
state_counts_civ['StateAbbrev'] = state_counts_civ['State'].map(state_abbrev)
abbrev = state_counts_civ['StateAbbrev']
state_counts_civ['LogCount'] = np.log1p(state_counts_civ['Count'])

fig_civ = px.choropleth(
    state_counts_civ,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Civil Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_civ.update_layout(coloraxis_showscale=False)

# COMPUTATIONAL DATA SCIENTISTS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Computational Data Science).csv"
cds_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_cds = cds_data['Employer State'].value_counts().reset_index()
state_counts_cds.columns = ['State', 'Count']
state_counts_cds['StateAbbrev'] = state_counts_cds['State'].map(state_abbrev)
abbrev = state_counts_cds['StateAbbrev']
state_counts_cds['LogCount'] = np.log1p(state_counts_cds['Count'])

fig_cds = px.choropleth(
    state_counts_cds,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Computational Data Science Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_cds.update_layout(coloraxis_showscale=False)

# COMPUTER ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Computer Engineering).csv"
computer_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_comp_e = computer_data['Employer State'].value_counts().reset_index()
state_counts_comp_e.columns = ['State', 'Count']
state_counts_comp_e['StateAbbrev'] = state_counts_comp_e['State'].map(state_abbrev)
abbrev = state_counts_comp_e['StateAbbrev']
state_counts_comp_e['LogCount'] = np.log1p(state_counts_comp_e['Count'])

fig_comp_e = px.choropleth(
    state_counts_comp_e,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Computer Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_comp_e.update_layout(coloraxis_showscale=False)

# COMPUTER SCIENTISTS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Computer Science).csv"
cs_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_cs = cs_data['Employer State'].value_counts().reset_index()
state_counts_cs.columns = ['State', 'Count']
state_counts_cs['StateAbbrev'] = state_counts_cs['State'].map(state_abbrev)
abbrev = state_counts_cs['StateAbbrev']
state_counts_cs['LogCount'] = np.log1p(state_counts_cs['Count'])

fig_cs = px.choropleth(
    state_counts_cs,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Computer Science Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_cs.update_layout(coloraxis_showscale=False)

# ELECTRICAL ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Electrical Engineering).csv"
elec_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_elec = elec_data['Employer State'].value_counts().reset_index()
state_counts_elec.columns = ['State', 'Count']
state_counts_elec['StateAbbrev'] = state_counts_elec['State'].map(state_abbrev)
abbrev = state_counts_elec['StateAbbrev']
state_counts_elec['LogCount'] = np.log1p(state_counts_elec['Count'])

fig_elec = px.choropleth(
    state_counts_elec,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Electrical Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_elec.update_layout(coloraxis_showscale=False)

# ENVIRONMENTAL ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Environmental Engineering).csv"
environmental_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_env = environmental_data['Employer State'].value_counts().reset_index()
state_counts_env.columns = ['State', 'Count']
state_counts_env['StateAbbrev'] = state_counts_env['State'].map(state_abbrev)
abbrev = state_counts_env['StateAbbrev']
state_counts_env['LogCount'] = np.log1p(state_counts_env['Count'])

fig_env = px.choropleth(
    state_counts_env,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Environmental Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_env.update_layout(coloraxis_showscale=False)

# MATERIAL SCIENTISTS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Materials Science and Eng).csv"
material_girl_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_mat = material_girl_data['Employer State'].value_counts().reset_index()
state_counts_mat.columns = ['State', 'Count']
state_counts_mat['StateAbbrev'] = state_counts_mat['State'].map(state_abbrev)
abbrev = state_counts_mat['StateAbbrev']
state_counts_mat['LogCount'] = np.log1p(state_counts_mat['Count'])

fig_mat = px.choropleth(
    state_counts_mat,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Material Science and Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_mat.update_layout(coloraxis_showscale=False)

# MECHANICAL ENGINEERS

# Load the dataset
file_path = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Mechanical Engineering).csv"
mechanical_data = pd.read_csv(file_path)


# Modify the dataset and processing the state data
state_counts_mech = mechanical_data['Employer State'].value_counts().reset_index()
state_counts_mech.columns = ['State', 'Count']
state_counts_mech['StateAbbrev'] = state_counts_mech['State'].map(state_abbrev)
abbrev = state_counts_mech['StateAbbrev']
state_counts_mech['LogCount'] = np.log1p(state_counts_mech['Count'])

fig_mech = px.choropleth(
    state_counts_mech,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Number of Employed Mechanical Engineering Spartan Graduates in the United States (Log-Scaled)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
    hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
)

fig_mech.update_layout(coloraxis_showscale=False)


st.subheader('Interactive Choropleth Map for States for All Majors')
st.plotly_chart(fig)
st.subheader('Interactive Choropleth Map for States for Applied Engineers')
st.plotly_chart(fig_app)
st.subheader('Interactive Choropleth Map for States for Biosystems Engineers')
st.plotly_chart(fig_bio)
st.subheader('Interactive Choropleth Map for States for Chemical Engineers')
st.plotly_chart(fig_chem)
st.subheader('Interactive Choropleth Map for States for Civil Engineers')
st.plotly_chart(fig_civ)
st.subheader('Interactive Choropleth Map for States for Computational Data Scientists')
st.plotly_chart(fig_cds)
st.subheader('Interactive Choropleth Map for States for Computer Engineers')
st.plotly_chart(fig_comp_e)
st.subheader('Interactive Choropleth Map for States for Computer Scientists')
st.plotly_chart(fig_cs)
st.subheader('Interactive Choropleth Map for States for Electrical Engineers')
st.plotly_chart(fig_elec)
st.subheader('Interactive Choropleth Map for States for Environmental Engineers')
st.plotly_chart(fig_env)
st.subheader('Interactive Choropleth Map for States for Material Scientists and Engineers')
st.plotly_chart(fig_mat)
st.subheader('Interactive Choropleth Map for States for Mechanical Engineers')
st.plotly_chart(fig_mech)

def choropleth_state_map(file_path, name_of_major_category = "All"):
    all_majors_data = pd.read_csv(file_path)
    state_counts = all_majors_data['Employer State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']
    state_abbrev = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
        'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
        'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
        'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
        'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
        'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
        'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
        'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    state_counts['StateAbbrev'] = state_counts['State'].map(state_abbrev)
    abbrev = state_counts['StateAbbrev']
    state_counts['LogCount'] = np.log1p(state_counts['Count'])
    fig = px.choropleth(
        state_counts,
        locations='StateAbbrev',
        locationmode='USA-states',
        color='LogCount',  # Use the log-transformed count
        color_continuous_scale='Greens',
        labels={'LogCount': 'Log Count'},
        scope='usa',
        title='Number of Employed ", name_of_major_category, " Spartan Graduates in the United States (Log-Scaled)',
        range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
        hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
    )
    return fig
