import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from geopy.geocoders import Nominatim

def report_salary(avgsal21 = "$10,000", avgsal22 = "$10,000", avgsal23 = "$10,000", avgsal2123 = "$10,000", medsal21 = "$10,000", medsal22 = "$10,000", medsal23 = "$10,000", medsal2123 = "$10,000", count21 = "5000", count22 = "5000", count23 = "5000", count2123 = "5000"):
    """
    Displays the average and median salary for 21, 22, 23, and cumulative in 4 columns

    Args:
        avgsal21 (string): Average Salary for 2021
        avgsal22 (string): Average Salary for 2022
        avgsal23 (string): Average Salary for 2023
        avgsal2123 (string): Average Salary for cumulative 2021-2023
        
        medsal21 (string): Median Salary for 2021
        medsal22 (string): Median Salary for 2022
        medsal23 (string): Median Salary for 2023
        medsal2123 (string): Median Salary for 2021-2023

        count21 (string): Count of how many students who did internships in 2021
        count22 (string): Count of how many students who did internships in 2022
        count23 (string): Count of how many students who did internships in 2023
        count2123 (string): Count of how many students who did internships cumulatively in 2021-2023

    Returns:
        Streamlit components
    """

    C1, C2, C3, C4 = st.columns(4) # divides the page into 4 vertical columns
    with C1: # first column
        st.header(":green[2021]")
        st.write(" ")
        st.subheader(avgsal21)
        st.write("Average Internship Salary (" + count21 + " students)")
        st.subheader(medsal21)
        st.write("Median Internship Salary (" + count21 + " students)")
    with C2: # second column 
        st.header(":green[2022]")
        st.write(" ")
        st.subheader(avgsal22)
        st.write("Average Internship Salary (" + count22 + " students)")
        st.subheader(medsal22)
        st.write("Median Internship Salary (" + count22 + " students)")
    with C3: # third column 
        st.header(":green[2023]")
        st.write(" ")
        st.subheader(avgsal23)
        st.write("Average Internship Salary (" + count23 + " students)")
        st.subheader(medsal23)
        st.write("Median Internship Salary (" + count23 + " students)")
    with C4: # fourth column 
        st.subheader(":green[Three Year Cumulative]")
        st.subheader(":green[" + avgsal2123 + "]")
        st.write("Average Internship Salary (" +  count2123 + " students)")
        st.subheader(":green[" + medsal2123 + "]")
        st.write("Median Internship Salary (" + count2123 + " students)")

def choropleth_state_map(file_path):
    all_majors_data = pd.read_csv(file_path, encoding='latin')
    
    # Create a city_to_state mapping
    city_to_state = {
        'Seattle': 'WA', 'San Francisco': 'CA', 'McLean': 'VA', 'Arlington': 'VA', 'Detroit': 'MI',
        'New York': 'NY', 'Boston': 'MA', 'Phoenix': 'AZ', 'San Diego': 'CA', 'Dallas': 'TX',
        'Charlotte': 'NC', 'Chicago': 'IL', 'Los Angeles': 'CA', 'Tampa': 'FL', 'Reno': 'NV',
        'Syracuse': 'NY', 'Portland': 'OR', 'Kenai': 'AK', 'Indianapolis': 'IN', 'Philadelphia': 'PA',
        'Findlay': 'OH', 'Ann Arbor': 'MI', 'Cincinnati': 'OH', 'Hoboken': 'NJ', 'Normal': 'IL',
        'Mandan': 'ND', 'Pittsburgh': 'PA', 'Corpus Christi': 'TX', 'Minneapolis': 'MN', 'Houston': 'TX',
        'Robinson': 'IL', 'Midland': 'MI', 'Dayton': 'OH', 'Salt Lake City': 'UT', 'Ames': 'IA',
        'Austin': 'TX', 'Lansing': 'MI', 'Hartford': 'CT', 'Exton': 'PA', 'Bohemia': 'NY',
        'Jacksonville': 'FL', 'Atlanta': 'GA', 'Washington DC': 'DC', 'St. Louis': 'MO', 'Kohler': 'WI',
        'Raleigh': 'NC', 'Saginaw': 'MI', 'Kalamazoo': 'MI', 'Milwaukee': 'WI', 'Benton Harbor': 'MI',
        'Hannibal': 'MO', 'San Antonio': 'TX', 'Durham': 'NC', 'Albany': 'NY', 'Piscataway': 'NJ',
        'Kansas City': 'MO', 'Traverse City': 'MI', 'Greenville': 'SC', 'Stamford': 'CT', 'Des Moines': 'IA',
        'Denver': 'CO', 'Baltimore': 'MD', 'East Chicago': 'IN', 'Au Gres': 'MI', 'Modesto': 'CA',
        'Fort Wayne': 'IN', 'Camden': 'NJ', 'Columbus': 'OH', 'Essex Junction': 'VT', 'La Crosse': 'WI',
        'Louisville': 'KY', 'Franklin': 'TN', 'Johnston': 'RI', 'Norway': 'MI', 'Quinnesec': 'MI',
        'Burns Harbor': 'IN', 'Pittsfield': 'MA', 'West Palm Beach': 'FL', 'Freeport': 'IL', 'Jackson': 'MI',
        'Manistee': 'MI', 'Columbia': 'SC', 'Preston': 'MD', 'Providence': 'RI', 'Fond Du Lac': 'WI',
        'Fort Worth': 'TX', 'Savannah': 'GA', 'West Greenwich': 'RI', 'Lynn': 'MA', 'Andover': 'MA',
        'Clark': 'NJ', 'Peoria': 'IL', 'Davidson': 'NC', 'Clarksville': 'TN', 'Warsaw': 'IN',
        'Skillman': 'NJ', 'Hastings': 'MI', 'Stafford Springs': 'CT', 'Battle Creek': 'MI', 'Crane': 'IN',
        'Oswego': 'NY', 'Livingston': 'TX', 'Fremont': 'CA', 'Somerset': 'NJ', 'Omaha': 'NE',
        'O\'Fallon': 'MO', 'Neenah': 'WI', 'Litchfield': 'IL', 'Flint': 'MI', 'Sidney': 'OH',
        'Oshkosh': 'WI', 'Harbor Beach': 'MI', 'Wichita': 'KS', 'Jefferson': 'WI', 'Shelby': 'NC',
        'Trumbull': 'CT', 'Hudson': 'OH', 'Novice': 'TX', 'Lexington': 'KY', 'Bloomington': 'IN',
        'Buffalo': 'NY', 'Toledo': 'OH', 'Gaylord': 'MI', 'Waupun': 'WI', 'Hoffman Estates': 'IL',
        'Fort Collins': 'CO', 'Spartanburg': 'SC', 'Port Huron': 'MI', 'Sault Sainte Marie': 'MI',
        'Tell City': 'IN', 'Charlevoix': 'MI', 'Cedar Rapids': 'IA', 'Cleveland': 'OH', 'Elk Rapids': 'MI',
        'Evansville': 'IN', 'Stratham': 'NH', 'Charleston': 'SC', 'Dothan': 'AL', 'Midland City': 'AL',
        'Killian': 'AL', 'Sewickley': 'PA', 'Appleton': 'WI', 'Elyria': 'OH', 'Adrian': 'MI',
        'Kewadin': 'MI', 'Muscatine': 'IA', 'Iron Mountain': 'MI', 'Accokeek': 'MD', 'Jamaica Plain': 'MA',
        'Newport News': 'VA', 'Nashville': 'TN', 'Rochester': 'NY', 'Mount Pleasant': 'MI', 'Tuscaloosa': 'AL',
        'New London': 'CT', 'Mason City': 'IA', 'Washington': 'WA', 'Titusville': 'FL', 'Greeley': 'CO',
        'West Lafayette': 'IN', 'Chantilly': 'VA', 'Petoskey': 'MI', 'Altoona': 'PA', 'Saint Petersburg': 'FL',
        'Des Plaines': 'IL', 'Pittston Township': 'PA', 'Ludington': 'MI', 'Middletown': 'OH',
        'Greenbay': 'WI', 'Plano': 'TX', 'Palmyra': 'NJ', 'Melbourne': 'FL', 'Tucson': 'AZ',
        'Middle River': 'MD', 'Riverton': 'NJ', 'Carlstadt': 'NJ', 'Hahnville': 'LA', 'Huntsville': 'AL',
        'California City': 'CA', 'Anchorage': 'AK', 'Verona': 'NJ', 'Sarasota': 'FL', 'Merrimack': 'NH',
        'Boulder': 'CO', 'Gainesville': 'FL', 'Thief River Falls': 'MN', 'Hammond': 'IN', 'Iowa City': 'IA',
        'Greenbelt': 'MD', 'Coraopolis': 'PA', 'Tinker AFB': 'OK', 'Lima': 'OH', 'Wallingford': 'CT',
        'Oregon': 'WI', 'Clifton': 'NJ'
    }
    
    all_majors_data['Employer State'] = all_majors_data['City'].map(lambda city: city_to_state.get(city, 'Unknown'))

    state_counts = all_majors_data['Employer State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']

    state_counts['LogCount'] = np.log1p(state_counts['Count'])

    fig = px.choropleth(
        state_counts,
        locations='State',
        locationmode='USA-states',
        color='LogCount',  # Use the log-transformed count
        color_continuous_scale='Greens',
        labels={'LogCount': 'Log Count'},
        scope='usa',
        range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
        hover_data={'State': True, 'Count': True, 'LogCount': False}
    )
    fig.update_layout(coloraxis_showscale=False)

    return fig

def display_top_5_states(file_path):
    data = pd.read_csv(file_path, encoding='latin1')

    city_to_state = {
        'Seattle': 'WA', 'San Francisco': 'CA', 'McLean': 'VA', 'Arlington': 'VA', 'Detroit': 'MI',
        'New York': 'NY', 'Boston': 'MA', 'Phoenix': 'AZ', 'San Diego': 'CA', 'Dallas': 'TX',
        'Charlotte': 'NC', 'Chicago': 'IL', 'Los Angeles': 'CA', 'Tampa': 'FL', 'Reno': 'NV',
        'Syracuse': 'NY', 'Portland': 'OR', 'Kenai': 'AK', 'Indianapolis': 'IN', 'Philadelphia': 'PA',
        'Findlay': 'OH', 'Ann Arbor': 'MI', 'Cincinnati': 'OH', 'Hoboken': 'NJ', 'Normal': 'IL',
        'Mandan': 'ND', 'Pittsburgh': 'PA', 'Corpus Christi': 'TX', 'Minneapolis': 'MN', 'Houston': 'TX',
        'Robinson': 'IL', 'Midland': 'MI', 'Dayton': 'OH', 'Salt Lake City': 'UT', 'Ames': 'IA',
        'Austin': 'TX', 'Lansing': 'MI', 'Hartford': 'CT', 'Exton': 'PA', 'Bohemia': 'NY',
        'Jacksonville': 'FL', 'Atlanta': 'GA', 'Washington DC': 'DC', 'St. Louis': 'MO', 'Kohler': 'WI',
        'Raleigh': 'NC', 'Saginaw': 'MI', 'Kalamazoo': 'MI', 'Milwaukee': 'WI', 'Benton Harbor': 'MI',
        'Hannibal': 'MO', 'San Antonio': 'TX', 'Durham': 'NC', 'Albany': 'NY', 'Piscataway': 'NJ',
        'Kansas City': 'MO', 'Traverse City': 'MI', 'Greenville': 'SC', 'Stamford': 'CT', 'Des Moines': 'IA',
        'Denver': 'CO', 'Baltimore': 'MD', 'East Chicago': 'IN', 'Au Gres': 'MI', 'Modesto': 'CA',
        'Fort Wayne': 'IN', 'Camden': 'NJ', 'Columbus': 'OH', 'Essex Junction': 'VT', 'La Crosse': 'WI',
        'Louisville': 'KY', 'Franklin': 'TN', 'Johnston': 'RI', 'Norway': 'MI', 'Quinnesec': 'MI',
        'Burns Harbor': 'IN', 'Pittsfield': 'MA', 'West Palm Beach': 'FL', 'Freeport': 'IL', 'Jackson': 'MI',
        'Manistee': 'MI', 'Columbia': 'SC', 'Preston': 'MD', 'Providence': 'RI', 'Fond Du Lac': 'WI',
        'Fort Worth': 'TX', 'Savannah': 'GA', 'West Greenwich': 'RI', 'Lynn': 'MA', 'Andover': 'MA',
        'Clark': 'NJ', 'Peoria': 'IL', 'Davidson': 'NC', 'Clarksville': 'TN', 'Warsaw': 'IN',
        'Skillman': 'NJ', 'Hastings': 'MI', 'Stafford Springs': 'CT', 'Battle Creek': 'MI', 'Crane': 'IN',
        'Oswego': 'NY', 'Livingston': 'TX', 'Fremont': 'CA', 'Somerset': 'NJ', 'Omaha': 'NE',
        'O\'Fallon': 'MO', 'Neenah': 'WI', 'Litchfield': 'IL', 'Flint': 'MI', 'Sidney': 'OH',
        'Oshkosh': 'WI', 'Harbor Beach': 'MI', 'Wichita': 'KS', 'Jefferson': 'WI', 'Shelby': 'NC',
        'Trumbull': 'CT', 'Hudson': 'OH', 'Novice': 'TX', 'Lexington': 'KY', 'Bloomington': 'IN',
        'Buffalo': 'NY', 'Toledo': 'OH', 'Gaylord': 'MI', 'Waupun': 'WI', 'Hoffman Estates': 'IL',
        'Fort Collins': 'CO', 'Spartanburg': 'SC', 'Port Huron': 'MI', 'Sault Sainte Marie': 'MI',
        'Tell City': 'IN', 'Charlevoix': 'MI', 'Cedar Rapids': 'IA', 'Cleveland': 'OH', 'Elk Rapids': 'MI',
        'Evansville': 'IN', 'Stratham': 'NH', 'Charleston': 'SC', 'Dothan': 'AL', 'Midland City': 'AL',
        'Killian': 'AL', 'Sewickley': 'PA', 'Appleton': 'WI', 'Elyria': 'OH', 'Adrian': 'MI',
        'Kewadin': 'MI', 'Muscatine': 'IA', 'Iron Mountain': 'MI', 'Accokeek': 'MD', 'Jamaica Plain': 'MA',
        'Newport News': 'VA', 'Nashville': 'TN', 'Rochester': 'NY', 'Mount Pleasant': 'MI', 'Tuscaloosa': 'AL',
        'New London': 'CT', 'Mason City': 'IA', 'Washington': 'WA', 'Titusville': 'FL', 'Greeley': 'CO',
        'West Lafayette': 'IN', 'Chantilly': 'VA', 'Petoskey': 'MI', 'Altoona': 'PA', 'Saint Petersburg': 'FL',
        'Des Plaines': 'IL', 'Pittston Township': 'PA', 'Ludington': 'MI', 'Middletown': 'OH',
        'Greenbay': 'WI', 'Plano': 'TX', 'Palmyra': 'NJ', 'Melbourne': 'FL', 'Tucson': 'AZ',
        'Middle River': 'MD', 'Riverton': 'NJ', 'Carlstadt': 'NJ', 'Hahnville': 'LA', 'Huntsville': 'AL',
        'California City': 'CA', 'Anchorage': 'AK', 'Verona': 'NJ', 'Sarasota': 'FL', 'Merrimack': 'NH',
        'Boulder': 'CO', 'Gainesville': 'FL', 'Thief River Falls': 'MN', 'Hammond': 'IN', 'Iowa City': 'IA',
        'Greenbelt': 'MD', 'Coraopolis': 'PA', 'Tinker AFB': 'OK', 'Lima': 'OH', 'Wallingford': 'CT',
        'Oregon': 'WI', 'Clifton': 'NJ'
    }

    data['Employer State'] = data['City'].map(lambda city: city_to_state.get(city, 'Unknown'))

    state_abbreviation_to_name = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
        'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
        'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
        'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
        'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
        'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
        'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
        'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
        'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
        'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
    }

    data['Employer State'] = data['Employer State'].map(lambda x: state_abbreviation_to_name.get(x, None))
    state_counts = data['Employer State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']

    state_counts = state_counts[state_counts['State'].notna()]

    top_5_states = state_counts.nlargest(5, 'Count')

    st.subheader("Top 5 States by Internship Count")
    for index, row in top_5_states.iterrows():
        st.write(f"**{row['State']}:** {row['Count']} internships")


def main():
    options = ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
    ms_intern = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major", label_visibility="visible", default=["All Engineering Majors"])

    if ms_intern == ["All Engineering Majors"]:
        file_path = "LATLONG(All Majors) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("whoops")  

        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path= "HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                st.title("Interactive City Visualization")
                file_path = "LATLONGHS EGRX-1220 Merge Combo_2021-2023.csv"
                # display_city_visualization(file_path)
                # display_top_5_cities(ms_intern[0])

        with T3:
            report_salary(avgsal21 = "$20.86", avgsal22 = "$22.69", avgsal23 = "$24.42", avgsal2123 = "$22.66", medsal21 = "$20.00", medsal22 = "$21.00", medsal23 = "$23.00", medsal2123 = "$21.33", count21 = "278", count22 = "506", count23 = "477", count2123 = "1261")
    

if __name__ == "__main__":
    main()
