import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from geopy.geocoders import Nominatim

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

# make sure to include
import pandas as pd
import streamlit as st

def display_top_employers(csv_file):
    df = pd.read_csv(csv_file)
    
    employer_counts = df['Employer'].value_counts().reset_index()
    employer_counts.columns = ['Employer', 'Count']
    
    top_employers = employer_counts.head(55)
    
    st.title('Top 5 Employers for Spartan Engineering Graduates')
    
    for index, row in top_employers.iterrows():
        employer = row['Employer']
        count = row['Count']
        st.write(f"**{employer}**: {count} graduates")

csv_file = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(All Majors).csv"

display_top_employers(csv_file)

# include these!
import pandas as pd
import streamlit as st

def display_top_employers(csv_file):
    df = pd.read_csv(csv_file)
    
    employer_counts = df['Employer'].value_counts().reset_index()
    employer_counts.columns = ['Employer', 'Count']
    
    top_employers = employer_counts.head(10)
    
    logo_urls = {
        'General Motors': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/General_Motors_%282021%29.svg/2048px-General_Motors_%282021%29.svg.png',
        'Ford Motor Company': 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Ford-Motor-Company-Logo.png',
        'Epic Systems': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Epic_Systems.svg/2560px-Epic_Systems.svg.png',
        'Amazon': 'https://cdn.logojoy.com/wp-content/uploads/20230629132639/current-logo-600x338.png',
        'PepsiCo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/PepsiCo_logo.svg/2500px-PepsiCo_logo.svg.png',
        'General Mills': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/General_Mills_logo.svg/1200px-General_Mills_logo.svg.png',
        'GE': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/General_Electric_logo.svg/2048px-General_Electric_logo.svg.png',
        'Texas Instruments': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/TexasInstruments-Logo.svg/2560px-TexasInstruments-Logo.svg.png',
        'Target': 'https://1000logos.net/wp-content/uploads/2017/06/Target-logo-1.png',
        'Pfizer': 'https://upload.wikimedia.org/wikipedia/commons/5/57/Pfizer_%282021%29.svg',
        'Eaton': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eaton_Corporation_logo.svg/2560px-Eaton_Corporation_logo.svg.png',
        'Microsoft': 'https://static.vecteezy.com/system/resources/thumbnails/027/127/493/small_2x/microsoft-logo-microsoft-icon-transparent-free-png.png',
        'Bosch': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Bosch-logo.svg/2560px-Bosch-logo.svg.png',
        'Accenture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Accenture.svg/2560px-Accenture.svg.png',
        'Williams International': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Williams_International_logo.svg/2560px-Williams_International_logo.svg.png',
        'Textron': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Textron.svg/2560px-Textron.svg.png',
        'Caterpillar': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Caterpillar_logo.svg/1280px-Caterpillar_logo.svg.png',
        'IBM': 'https://cdn.freebiesupply.com/images/large/2x/ibm-logo-transparent.png',
        'Auto-Owners Insurance Company': 'https://res.cloudinary.com/value-penguin/image/upload/f_auto,q_auto/referral_logos/us/insurance/autoowners-3',
        'Gentex Corporation': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Gentex_Corporation_Logo.svg/2560px-Gentex_Corporation_Logo.svg.png',
        'Humana': 'https://crystalpng.com/wp-content/uploads/2023/05/humana-logo.png',
        'Magna International': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Magna_logo.svg/1200px-Magna_logo.svg.png',
        'Stellantis - FCA Fiat Chrylser Automobiles': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Stellantis.svg/2560px-Stellantis.svg.png',
        'Crowe LLP': 'https://www.agacgfm.org/CMSPages/GetFile.aspx?guid=cc284f6f-2964-4af8-8ded-dc848824773a',
        'Marathon Petroleum Corporation': 'https://download.logo.wine/logo/Marathon_Petroleum/Marathon_Petroleum-Logo.wine.png',
        'Stryker': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Stryker_logo.svg/1200px-Stryker_logo.svg.png',
        'MI - Department of Transportation': 'https://www.michigan.gov/mdot/-/media/Project/Websites/MDOT/News-and-Outreach/Media-Relations/Logos/MDOT-Wordmark-Logo-Color.png?h=90&w=300&rev=71abf5d9ddfc48b3839e8ae12fe74cf8&hash=4682D4676CDD081058FB94BFD3C3460B',
        'PPG Industries': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/PPG_Logo.svg/2560px-PPG_Logo.svg.png',
        'ZF': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/ZF_logo_STD_Blue_3CC.svg/768px-ZF_logo_STD_Blue_3CC.svg.png',
        'Dow': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Dow_Chemical_Company_logo.svg/1280px-Dow_Chemical_Company_logo.svg.png',
        'Gallo': 'https://gallocompanies.com/wp-content/uploads/2022/03/Smashcreate_Gallo-Companies-logo_BA_11-May-2021_V1-03-1536x1113.png',
        'MSU College Advising Corps': 'data:image/png;base64,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',
        'Black and Veatch': 'https://img.roadsbridges.com/files/base/ebm/roadsbridges/image/2022/06/1654817495395-bv_horizontal_rgb_digital.png?auto=format%2Ccompress&w=640&width=640',
        'Ally Financial Inc': 'https://1000logos.net/wp-content/uploads/2021/05/Ally-Financial-logo.png',
        'Consumers Energy': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Consumers_Energy_logo.svg/2560px-Consumers_Energy_logo.svg.png',
        'JPMorgan Chase & Co': 'https://media.licdn.com/dms/image/D4E12AQFE3eejqLsKxQ/article-cover_image-shrink_720_1280/0/1691375687496?e=2147483647&v=beta&t=u2sce86m0Db8J3Ldy_Kw2OzYTpdxfOJxhqs4y_iTRnc',
        'Lockheed Martin': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Lockheed_Martin_logo.svg/2560px-Lockheed_Martin_logo.svg.png',
        'Raytheon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Raytheon_Technologies_logo.svg/2560px-Raytheon_Technologies_logo.svg.png',
        'Deloitte': 'https://upload.wikimedia.org/wikipedia/commons/1/15/Deloitte_Logo.png',
        'Wade Trim': 'https://www.wadetrim.com/wp-content/uploads/wade-trim-logo_300x200.png',
        'Kimley-Horn': 'https://chambermaster.blob.core.windows.net/images/customers/854/members/336/logos/MEMBER_PAGE_HEADER/KimleyHorn_LG_LOGO_PRIMARY300.png',
        'Atwell, LLC': 'https://www.atwell-group.com/wp-content/themes/atwell-theme/images/logo-full.png',
        'AECOM': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/AECOM.svg/1200px-AECOM.svg.png',
        'Cleveland-Cliffs': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Cliffs_Natural_Resources_logo.svg/2560px-Cliffs_Natural_Resources_logo.svg.png',
        'Commonwealth Associates': 'https://online.fliphtml5.com/onguq/accountlogo.png',
        'MSU': 'https://cdn.freebiesupply.com/logos/large/2x/michigan-state-university-logo-png-transparent.png',
        'Eli Lilly & Company': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Eli_Lilly_and_Company.svg/1200px-Eli_Lilly_and_Company.svg.png',
        'Burns & McDonnell': 'https://www.offshorewindri.com/_files/public/logo_Burns%20McDonnell.png',
        'General Dynamics': 'https://1000logos.net/wp-content/uploads/2021/07/General-Dynamics-Logo.png',
        'Trane Technologies': 'https://www.jwlongmechanical.com/wp-content/uploads/2017/06/trane-logo-transparent.png',
        'Toyota Motor Corporation': 'https://upload.wikimedia.org/wikipedia/commons/7/7f/Toyota_Motor_North_America_logo_%282019%29.png',
        'Amway': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Amway_%28logo%29.svg/2560px-Amway_%28logo%29.svg.png',
        'KLA': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/KLA_Corp._logo.svg/2560px-KLA_Corp._logo.svg.png',
        'AAM - American Axle & Manufacturing': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/AAM_Logo.svg/1200px-AAM_Logo.svg.png',
        'BAE Systems': 'https://1000logos.net/wp-content/uploads/2020/09/BAE-Systems-Logo.png',
        'W.W. Grainger': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/W._W._Grainger_logo.svg/2560px-W._W._Grainger_logo.svg.png',
        'Cargill': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Cargill_logo.svg/1280px-Cargill_logo.svg.png',
        'Archer Daniels Midland': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Archer_Daniels_Midland_logo.svg/2560px-Archer_Daniels_Midland_logo.svg.png',
        'The Walsh Group': 'https://walshwebsiteassets.blob.core.windows.net/sitedocs/imagegallery/walshus-logo.png',
        'FK Engineering Associates': 'https://media.licdn.com/dms/image/C560BAQFQ4bObiwET-A/company-logo_200_200/0/1663338549021/fk_engineering_assoc_logo?e=2147483647&v=beta&t=eGhc3WEyzGAJWvxqsfN5AaD7R7tiI5zpZLBClUPHjl8',
        'Fast Enterprises': 'https://seeklogo.com/images/F/fast-enterprises-logo-A48A30468D-seeklogo.com.png',
        'Blue Cross Blue Shield': 'https://www.buildingbetternutrition.com/wp-content/uploads/2022/03/blue-cross-blue-shield-1-logo-png-transparent.png',
        'Humana': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Humana_logo.svg/2560px-Humana_logo.svg.png',
        'Nationwide': 'https://content.presspage.com/clients/o_2497.png',
        'Doeren Mayhew': 'https://www.foundationsoft.com/wp-content/uploads/2021/03/doeren-mayhew-logo.png',
        'Fleis and VandenBrink': 'https://www.fveng.com/wp-content/uploads/2018/12/2021-F_V-Logo.png',
        'Arcadis': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Arcadis_logo.svg/2560px-Arcadis_logo.svg.png',
        'Michigan Department of Environment, Great Lakes, and Energy': 'https://gl.audubon.org/sites/default/files/styles/bean_wysiwyg_full_width/public/2-egle_logo_primary_color-rgb.png?itok=-_uMaI3H',
        'G2 Consulting Group': 'https://g2consultinggroup.com/wp-content/themes/g2-consulting/images/G2_Logo_SmallG.png',
        'EMMA International': 'https://emmainternational.com/wp-content/uploads/2021/05/emma-international-logo@2x.png',
        'Hexcel Corporation': 'https://logo.stocklight.com/NYSE/HXL_original.png',
        'Tooling and Engineering International': 'https://www.teintl.com/wp-content/uploads/2015/07/logo_small.png'

    }
    
    # Display the top 5 employers with their logos
    st.title('Top 5 Employers for Spartan Engineering Graduates')
    
    for index, row in top_employers.iterrows():
        employer = row['Employer']
        count = row['Count']
        
        if employer in logo_urls:
            logo_url = logo_urls[employer]
        else:
            logo_url = ""
        
        if logo_url:
            st.image(logo_url, width=200)
        st.write(f"**{employer}**: {count} graduates\n\n")

csv_file = r"C:\Users\Shayna\Downloads\DestinationCumulativeDataset(Mechanical Engineering).csv"
display_top_employers(csv_file)


import streamlit as st
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim

def add_lat_long_to_dataframe(data):
    if 'Employer City' in data.columns:
        geolocator = Nominatim(user_agent='myapplication')
        employer_latitudes = []
        employer_longitudes = []

        for city in data['Employer City']:
            if pd.notna(city):
                try:
                    location = geolocator.geocode(city)
                    if location:
                        employer_latitudes.append(location.latitude)
                        employer_longitudes.append(location.longitude)
                    else:
                        employer_latitudes.append(None)
                        employer_longitudes.append(None)
                except Exception as e:
                    employer_latitudes.append(None)
                    employer_longitudes.append(None)
            else:
                employer_latitudes.append(None)
                employer_longitudes.append(None)

        data['Employer Latitude'] = employer_latitudes
        data['Employer Longitude'] = employer_longitudes

        st.success("Latitude and Longitude columns created successfully.")
    else:
        st.error("The uploaded CSV file does not contain the 'Employer City' column.")

def display_city_visualization(file_path):
    data = pd.read_csv(file_path)
    
    if 'Employer Latitude' not in data.columns or 'Employer Longitude' not in data.columns:
        st.warning("Latitude and Longitude columns not found. Creating columns... This may take a moment.")

        add_lat_long_to_dataframe(data)
        data.to_csv(file_path, index=False)
        st.info("Updated CSV file with Latitude and Longitude columns. Please reload the app to visualize.")

    if 'Employer Latitude' in data.columns and 'Employer Longitude' in data.columns:
        # Calculate count of graduates per city
        city_counts = data.groupby('Employer City').size().reset_index(name='Graduate Count')

        # Merge with original data to get latitude and longitude
        data_merged = pd.merge(data, city_counts, on='Employer City', how='left')

        fig = px.scatter_geo(
                data_merged,
                lat='Employer Latitude',
                lon='Employer Longitude',
                hover_name='Employer City',
                hover_data={
                    'Employer City': True,
                    'Graduate Count': True,
                    'Employer Latitude': False,
                    'Employer Longitude': False,
                    'Employer City': False
                },
                size='Graduate Count',
                size_max=25,
                color_discrete_sequence=px.colors.sequential.Greens
                )

        fig.update_traces(marker=dict(line=dict(width=2, color='#577b59')))


        fig.update_geos(
            showcountries=True, countrycolor="Black",
            showcoastlines=True, coastlinecolor="Black",
            showland=True, landcolor="#a3cf9e"
        )

        fig.update_layout(
            title="City Visualization",
            geo=dict(
                scope='usa',
                projection=dict(type='albers usa'),
                showlakes=True,
                lakecolor='#9ec1cf',
                showocean=True,  # Show ocean
                oceancolor='#9ec1cf'  # Color of ocean water (same as lake water color)
            ),
            margin={"r":0,"t":0,"l":0,"b":0}
        )

        st.plotly_chart(fig)
    else:
        st.error("Failed to create Latitude and Longitude columns. Please check your CSV file.")

# Streamlit app setup
st.title("City Visualization")

file_path = r"C:\Users\Shayna\Downloads\LATLONGDestinationCumulativeDataset(All Majors).csv"
display_city_visualization(file_path)



def top_5_employer_states(file_path):
    all_majors_data = pd.read_csv(file_path)
    state_counts = all_majors_data['Employer State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']
    top_5_states = state_counts.head(5)

    # Display top 5 employer states ranked
    for index, row in top_5_states.iterrows():
        st.write(f"{index + 1}. **{row['State']}**")

top_5_employer_states(csv_file)
