import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from geopy.geocoders import Nominatim

#Initalize Functions Here
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

def add_lat_long_to_dataframe(data):
    if 'City' in data.columns:
        geolocator = Nominatim(user_agent='myapplication')
        employer_latitudes = []
        employer_longitudes = []

        for city in data['City']:
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

def create_pie_chart(file_path):
    df = pd.read_csv(file_path, encoding='latin')
    company_counts = df['Employer Name'].value_counts().reset_index()
    company_counts.columns = ['Employer Name', 'Count'] 
    filtered_company_counts = company_counts[company_counts['Count'] > 1]
  
    fig = px.pie(filtered_company_counts, 
                 names='Employer Name', 
                 values='Count',
                 color_discrete_sequence=px.colors.qualitative.T10)

    fig.update_traces(textinfo='none',
                      hoverinfo='label+value+percent')
    
    return fig

def display_city_visualization(file_path):
    data = pd.read_csv(file_path)
    
    if 'Employer Latitude' not in data.columns or 'Employer Longitude' not in data.columns:
        st.warning("Latitude and Longitude columns not found. Creating columns... This may take a moment.")

        add_lat_long_to_dataframe(data)
        data.to_csv(file_path, index=False)
        st.info("Updated CSV file with Latitude and Longitude columns. Please reload the app to visualize.")

    if 'Employer Latitude' in data.columns and 'Employer Longitude' in data.columns:
        city_counts = data.groupby('City').size().reset_index(name='Internship Count')

        data_merged = pd.merge(data, city_counts, on='City', how='left')

        fig = px.scatter_geo(
                data_merged,
                lat='Employer Latitude',
                lon='Employer Longitude',
                hover_name='City',
                hover_data={
                    'City': True,
                    'Internship Count': True,
                    'Employer Latitude': False,
                    'Employer Longitude': False,
                    'City': False
                },
                size='Internship Count',
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
    
    return fig

def display_top_5_states(file_path):
    if selected_major == "All Engineering Majors":
        states = ["Michigan: 1098 positions", "California: 74 positions", "Illinois: 50 positions", "Wisconsin: 45 positions", "Ohio: 43 positions"]
    elif selected_major == "Applied Engineering Sciences":
        states = ["Michigan: 76 positions", "Illinois: 9 positions", "Minnesota: 7 positions", "North Carolina: 5 positions", "Arizona: 4 positions"]
    elif selected_major == "Biosystems Engineering":
        states = ["Michigan: 38 positions", "Minnesota: 5 positions", "Wisconsin: 3 positions", "Illinois: 2 positions", "Indiana: 2 positions"]
    elif selected_major == "Chemical Engineering":
        states = ["Michigan: 107 positions", "Wisconsin: 10 positions", "California: 9 positions", "Illinois: 7 positions", "Iowa: 6 positions"]
    elif selected_major == "Civil Engineering":
        states = ["Michigan: 89 positions", "Texas: 9 positions", "New York: 4 positions", "Ohio: 4 positions", "California: 3 positions"]
    elif selected_major == "Computational Data Science":
        states = ["Michigan: 19 positions", "California: 2 positions", "Texas: 2 positions"]
    elif selected_major == "Computer Engineering":
        states = ["Michigan: 65 positions", "California: 8 positions", "Illinois: 2 positions", "Texas: 2 positions", "Washington: 2 positions"]
    elif selected_major == "Computer Science":
        states = ["Michigan: 194 positions", "California: 25 positions", "Washington: 15 positions", "Illinois: 13 positions", "Kentucky: 8 positions"]
    elif selected_major == "Electrical Engineering":
        states = ["Michigan: 174 positions", "Texas: 8 positions", "Ohio: 7 positions", "California: 6 positions", "Minnesota: 6 positions"]
    elif selected_major == "Environmental Engineering":
        states = ["Michigan: 41 positions", "Illinois: 3 positions", "Indiana: 2 positions"]
    elif selected_major == "Materials Science & Engineering":
        states = ["Michigan: 18 positions", "California: 5 positions", "Wisconsin: 2 positions"]
    elif selected_major == "Mechanical Engineering":
        states = ["Michigan: 277 positions", "Wisconsin: 24 positions", "Ohio: 16 positions", "California: 11 positions", "Texas: 8 positions"]
    else:
        states = []

    st.subheader("Top 5 States")
    for i, state in enumerate(states, start=1):
        st.write(f"{i}. {state}")

def display_top_5_cities(selected_major):
    if selected_major == "All Engineering Majors":
        michigan_cities = ["Detroit: 134 positions", "Lansing: 59 positions", "Grand Rapids: 38 positions", "Ann Arbor: 11 positions", "Jackson: 9 positions"]
        non_michigan_cities = ["San Francisco, CA: 7 positions", "Toledo, OH: 5 positions", "Findlay, OH: 4 positions", "La Crosse, WI: 3 positions", "Los Angeles, CA: 3 positions"]
    elif selected_major == "Applied Engineering Sciences":
        michigan_cities = ["Detroit: 35 positions", "Lansing: 14 positions", "Grand Rapids: 7 positions", "Ann Arbor: 5 positions", "Jackson: 4 positions"]
        non_michigan_cities = ["Chicago, IL: 6 positions", "Minneapolis, MN: 5 positions", "Phoenix, AZ: 4 positions", "Cincinnati, OH: 3 positions", "Fond Du Lac, WI: 3 positions"]
    elif selected_major == "Biosystems Engineering":
        michigan_cities = ["Lansing: 23 positions", "Detroit: 4 positions", "Grand Rapids: 4 positions"]
        non_michigan_cities = ["Preston, MN: 3 positions", "Boston, MA: 2 positions", "Chicago, IL: 2 positions", "Fremont, CA: 2 positions", "Minneapolis, MN: 2 positions"]
    elif selected_major == "Chemical Engineering":
        michigan_cities = ["Detroit: 32 positions", "Lansing: 28 positions", "Jackson: 13 positions", "Midland: 12 positions", "Grand Rapids: 8 positions"]
        non_michigan_cities = ["Chicago, IL: 6 positions", "Boston, MA: 4 positions", "Neenah, WI: 4 positions", "Atlanta, GA: 3 positions", "Cincinnati, OH: 3 positions"]
    elif selected_major == "Civil Engineering":
        michigan_cities = ["Lansing: 39 positions", "Detroit: 28 positions", "Grand Rapids: 7 positions", "Flint: 4 positions", "Jackson: 3 positions"]
        non_michigan_cities = ["Dallas, TX: 9 positions", "Los Angeles, CA: 3 positions", "Chicago, IL: 2 positions", "Dayton, OH: 2 positions", "Kansas City, MO: 2 positions"]
    elif selected_major == "Computational Data Science":
        michigan_cities = ["Detroit: 10 positions", "Lansing: 9 positions"]
        non_michigan_cities = ["Dallas, TX: 2 positions", "San Francisco, CA: 2 positions"]
    elif selected_major == "Computer Engineering":
        michigan_cities = ["Detroit: 29 positions", "Lansing: 21 positions", "Saginaw: 6 positions", "Ann Arbor: 3 positions", "Grand Rapids: 3 positions"]
        non_michigan_cities = ["San Francisco, CA: 6 positions", "Chicago, IL: 2 positions", "Dallas, TX: 2 positions", "Seattle, WA: 2 positions"]
    elif selected_major == "Computer Science":
        michigan_cities = ["Detroit: 87 positions", "Lansing: 86 positions", "Grand Rapids: 11 positions", "Ann Arbor: 7 positions", "Midland: 2 positions"]
        non_michigan_cities = ["San Francisco, CA: 17 positions", "Seattle, WA: 15 positions", "Chicago, IL: 12 positions", "Louisville, KY: 8 positions", "Minneapolis, MN: 7 positions"]
    elif selected_major == "Electrical Engineering":
        michigan_cities = ["Detroit: 84 positions", "Lansing: 42 positions", "Grand Rapids: 17 positions", "Jackson: 15 positions", "Saginaw: 5 positions"]
        non_michigan_cities = ["Dallas, TX: 5 positions", "San Francisco, CA: 5 positions", "Baltimore, MD: 4 positions", "Des Moines, IA: 4 positions", "Minneapolis, MN: 4 positions"]
    elif selected_major == "Environmental Engineering":
        michigan_cities = ["Lansing: 18 positions", "Detroit: 11 positions", "Grand Rapids: 5 positions", "Saginaw: 2 positions"]
        non_michigan_cities = ["Chicago, IL: 3 positions"]
    elif selected_major == "Materials Science & Engineering":
        michigan_cities = ["Detroit: 9 positions", "Lansing: 5 positions", "Saginaw: 2 positions"]
        non_michigan_cities = ["San Francisco, CA: 3 positions"]
    elif selected_major == "Mechanical Engineering":
        michigan_cities = ["Detroit: 134 positions", "Lansing: 59 positions", "Grand Rapids: 38 positions", "Ann Arbor: 11 positions", "Jackson: 9 positions"]
        non_michigan_cities = ["San Francisco, CA: 7 positions", "Toledo, OH: 5 positions", "Los Angeles, CA: 3 positions", "Milwaukee, WI: 3 positions", "Oshkosh, WI: 3 positions"]
    else:
        michigan_cities = []
        non_michigan_cities = []

    st.subheader("Top 5 Michigan Cities")
    for i, city in enumerate(michigan_cities, start=1):
        st.write(f"{i}. {city}")

    st.subheader("Top 5 Non-Michigan Cities")
    for i, city in enumerate(non_michigan_cities, start=1):
        st.write(f"{i}. {city}")

def main():
    options = ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
    ms_intern = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major", label_visibility="visible", default=["All Engineering Majors"])

    if ms_intern == ["All Engineering Majors"]:
        file_path = "LATLONG(All Majors) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (1).jpg") 
            
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                st.title("Interactive City Visualization")
                file_path = "LATLONGHS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("All Engineering Majors")

        with T3:
            report_salary(avgsal21 = "$20.86", avgsal22 = "$22.69", avgsal23 = "$24.42", avgsal2123 = "$22.66", medsal21 = "$20.00", medsal22 = "$21.00", medsal23 = "$23.00", medsal2123 = "$21.33", count21 = "278", count22 = "506", count23 = "477", count2123 = "1261")
    
    elif ms_intern == ["Applied Engineering Sciences"]:
        file_path = "LATLONG(Applied Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv" 
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
           st.image("FT (2).jpg") 
            
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                fig = choropleth_state_map(file_path)
                st.plotly_chart(fig)
                display_top_5_states(file_path)
            with tab2:
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Applied Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Applied Engineering Sciences")
        with T3:
            report_salary(avgsal21 = "$20.73", avgsal22 = "$22.14", avgsal23 = "$24.48", avgsal2123 = "$22.45", medsal21 = "$20.13", medsal22 = "$21.00", medsal23 = "$25.00", medsal2123 = "$22.04", count21 = "22", count22 = "55", count23 = "41", count2123 = "118")

    elif ms_intern == ["Biosystems Engineering"]:
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (3).jpg") 
            
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Biosystems Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Biosystems Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Biosystems Engineering")
        with T3:
            report_salary(avgsal21 = "$18.30", avgsal22 = "$19.04", avgsal23 = "$20.49", avgsal2123 = "$19.28", medsal21 = "$18.25", medsal22 = "$17.00", medsal23 = "$20.00", medsal2123 = "$18.42", count21 = "10", count22 = "21", count23 = "19", count2123 = "50")

    elif ms_intern == ["Chemical Engineering"]:
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (4).jpg") 
        
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Chemical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:                
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Chemical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Chemical Engineering")
        with T3:
            report_salary(avgsal21 = "$22.46", avgsal22 = "$24.39", avgsal23 = "$22.85", avgsal2123 = "$23.23", medsal21 = "$22.50", medsal22 = "$24.00", medsal23 = "$22.50", medsal2123 = "$23.00", count21 = "39", count22 = "61", count23 = "54", count2123 = "154")
    
    elif ms_intern == ["Civil Engineering"]:
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (5).jpg") 
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Civil Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Civil Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Civil Engineering")
        with T3:
            report_salary(avgsal21 = "$17.86", avgsal22 = "$19.75", avgsal23 = "$22.22", avgsal2123 = "$19.94", medsal21 = "$18.00", medsal22 = "$18.00", medsal23 = "$21.00", medsal2123 = "$19.00", count21 = "14", count22 = "39", count23 = "50", count2123 = "103")

    elif ms_intern == ["Computational Data Science"]:
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (6).jpg")                        
            
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Computational Data Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Computational Data Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Computational Data Science")
        with T3:
            report_salary(avgsal21 = "$16.75", avgsal22 = "$24.37", avgsal23 = "$26.83", avgsal2123 = "$22.65", medsal21 = "$16.75", medsal22 = "$20.50", medsal23 = "$23.50", medsal2123 = "$20.25", count21 = "2", count22 = "12", count23 = "6", count2123 = "20")
    
    elif ms_intern == ["Computer Engineering"]:
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (7).jpg")                  
            
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Computer Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Computer Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Computer Engineering")
        with T3:
            report_salary(avgsal21 = "$19.99", avgsal22 = "$20.33", avgsal23 = "$25.48", avgsal2123 = "$21.93", medsal21 = "$20.00", medsal22 = "$20.00", medsal23 = "$23.00", medsal2123 = "$21.00", count21 = "18", count22 = "18", count23 = "22", count2123 = "58")
    
    elif ms_intern == ["Computer Science"]:

        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (8).jpg")  
           
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Computer Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
              
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Computer Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Computer Science")
        with T3:
            report_salary(avgsal21 = "$23.03", avgsal22 = "$26.84", avgsal23 = "$29.96", avgsal2123 = "$26.61", medsal21 = "$25.00", medsal22 = "$25.00", medsal23 = "$25.00", medsal2123 = "$23.67", count21 = "36", count22 = "92", count23 = "97", count2123 = "225")
    
    elif ms_intern == ["Electrical Engineering"]:

        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (9).jpg")  
            
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Electrical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Electrical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Electrical Engineering")
        with T3:
            report_salary(avgsal21 = "$19.86", avgsal22 = "$22.00", avgsal23 = "$23.13", avgsal2123 = "$21.66", medsal21 = "$19.75", medsal22 = "$22.00", medsal23 = "$22.25", medsal2123 = "$21.33", count21 = "48", count22 = "63", count23 = "58", count2123 = "169")
    
    elif ms_intern == ["Environmental Engineering"]:

        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
           st.image("FT (10).jpg") 
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Environmental Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Environmental Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Environmental Engineering")
        with T3:
            report_salary(avgsal21 = "$15.00", avgsal22 = "$17.53", avgsal23 = "$21.66", avgsal2123 = "$18.06", medsal21 = "$15.00", medsal22 = "$17.00", medsal23 = "$20.50", medsal2123 = "$17.50", count21 = "5", count22 = "15", count23 = "20", count2123 = "40")

    elif ms_intern == ["Materials Science & Engineering"]:
       
        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (11).jpg")                   

        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Materials Science and Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Materials Science and Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Materials Science & Engineering")
        with T3:
            report_salary(avgsal21 = "$26.66", avgsal22 = "$25.61", avgsal23 = "$21.06", avgsal2123 = "$24.44", medsal21 = "$24.25", medsal22 = "$21.88", medsal23 = "$19.00", medsal2123 = "$21.71", count21 = "8", count22 = "11", count23 = "10", count2123 = "29")
    
    elif ms_intern == ["Mechanical Engineering"]:

        T3, T1, T2 = st.tabs(["By Salary","By Employer", "By Geography"])
        with T1:
            st.image("FT (12).jpg")   
        with T2:
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
                choropleth_file_path = "LATLONG(Mechanical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                fig = choropleth_state_map(choropleth_file_path)
                st.plotly_chart(fig)
                display_top_5_states(choropleth_file_path)
            with tab2:   
                st.title("Interactive City Visualization")
                file_path = "LATLONG(Mechanical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
                display_city_visualization(file_path)
                display_top_5_cities("Mechanical Engineering")
        with T3:
            report_salary(avgsal21 = "$20.68", avgsal22 = "$21.40", avgsal23 = "$22.96", avgsal2123 = "$21.68", medsal21 = "$20.00", medsal22 = "$20.30", medsal23 = "$22.00", medsal2123 = "$20.77", count21 = "76", count22 = "119", count23 = "100", count2123 = "295")

if __name__ == "__main__":
    main()
