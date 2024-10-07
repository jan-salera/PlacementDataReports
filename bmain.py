import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

# Shows the entire graduating class breakdown by major
def data_major(colors = [], count = [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16], majors = ["Applied Engineering Sciences", "Biosystems Engineering",        "Computational Data Science", "Civil Engineering","Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Mechanical Engineering", "Materials Science & Engineering"]):
    """Shows the entire graduating class breakdown by major
    
    Args:
        colors (list): list of strings, Hex values, needs one per value in the graph, default is [] 
        count (list) : list of ints, count of how many students of each major
        majors (list) : list of strings, all majors in the graph
    
    Returns:
        streamlit plotly_chart: Circle graph with all majors and how many in each major 
    """
    class_data = {
    'Major': majors,
    'Count': count
    }
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    
    st.plotly_chart(major_fig)

# Shows the entire graduating class breakdown by gender
def data_gender(count = [], color = ['#0B1799', '#C70F0F'], name = ['Male', 'Female']):
    gender_data = {'Gender': name, 'Count': count}
    colors = color
    gender_fig = px.pie(gender_data, values='Count', names='Gender', title='Gender Distribution', color_discrete_sequence=colors)
    st.plotly_chart(gender_fig)

# Shows the entire graduating class breakdown by ethnicity
def data_ethnicity(count = [], ethnicity = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', 'Not Specified', "Black/African American"]):
    ethnicity_data = {
    'Ethnicity': ethnicity,
    'Count': count}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934', "#00BF49", "#C3C3C3"]
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

def key_stats(year= "2023", kr = "90.5%", krinfo = "742/820", pr = "94.3%", prinfo = "700/742", avgsal = "$76,806", medsal = "$75,000", employ = "79.3%", grad = "14.2%", vol = 0, other = 0):
    st.markdown("""<h1 style="font-weight: normal; text-align:center;">Spartan Engineering Statistics </h1>""", unsafe_allow_html=True,)

    H3, H0 = st.columns([1, 3.55])
    with H3:
        st.write("")
    with H0:    
        st.write("Data Represents Spring",year,"Graduating Undergraduates")
    
    A1, A2, A3 = st.columns([3, 2.5, 2])
    
    with A1:
        st.header(kr)
        st.write("Knowledge Rate (" + krinfo + " graduates)")
        st.header(pr)
        st.write("Placement Rate (" + prinfo + " graduates)")
    with A3:
        st.header(avgsal)
        st.write("Average Starting Salary")
        st.header(medsal)
        st.write("Median Starting Salary")
    with A2:
        st.header(employ)
        st.write("Employed")
        if type(grad) is str:
            st.header(grad)
            st.write("Continuing Education")
        elif grad == 0:
            print("No Con. Ed Statistic")
        if type(vol) is str:
            st.header(vol)
            st.write("Service/Volunteering")
        elif vol == 1:
            st.header("1%")
            st.write("Fellowship")
        if type(other) is str:
            st.header(other)
            st.write("Other Intentions")

def c_key_stats(kr21, kr22, kr23, ya_kr, pr21, pr22, pr23, ya_pr, as21, as22, as23, ya_as, ms21, ms22, ms23, ya_ms, ya = "Three"):
    st.markdown("""<h1 style="font-weight: normal; text-align:center;">Spartan Engineering Key Statistics </h1>""", unsafe_allow_html=True)    
    C1, C2, C3, C4 = st.columns(4)
    with C1:
        st.header(":green[" + ya_kr + "]")
        st.write(ya, "Year Average Knowledge Rate")
        sm1 = st.checkbox("See More", key = 3)    
        if sm1:
            st.header(kr23)
            st.write("2023 Knowledge Rate")
            st.header(kr22)
            st.write("2022 Knowledge Rate")
            if type(kr21) != int:
                st.header(kr21)
                st.write("2021 Knowledge Rate")

    with C2:
        st.header(":green[" + ya_pr + "]")
        st.write(ya, "Year Average Placement Rate")
        sm1 = st.checkbox("See More", key = 0)    
        if sm1:
            st.header(pr23 + "")
            st.write("2023 Placement Rate")
            st.header(pr22 + "")
            st.write("2022 Placement Rate")
            if type(pr21) != int:
                st.header(pr21 + "")
                st.write("2021 Placement Rate")

    with C3:
        st.header(":green[$" + ya_as + "]")
        st.write(ya, "Year Average Average Salary")
        sm1 = st.checkbox("See More", key = 1)    
        if sm1:
            st.header("$" + as23)
            st.write("2023 Average Salary")
            st.header("$" + as22)
            st.write("2022 Average Salary")
            if type(as21) != int:
                st.header("$" + as21)
                st.write("2021 Average Salary")

    with C4:
        st.header(":green[$" + ya_ms + "]")
        st.write(ya, "Year Average Median Salary")
        sm1 = st.checkbox("See More", key = 2)    
        if sm1:
            st.header("$" + ms23)
            st.write("2023 Median Salary")
            st.header("$" + ms22)
            st.write("2022 Median Salary")
            if type(ms21) != int:
                st.header("$" + ms21)
                st.write("2021 Median Salary")

def research_readings(size = [3,3,3], pagelink= "https://www.google.com/", custom = "insert label here"):
        M1, M2, M3  = st.columns(size)
        with M1:
            st.write("")
        with M2:
            st.write("")
            st.page_link(page = pagelink, label = custom)
        with M3:
            st.write("")

def choropleth_state_map(file_path):
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
        range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
        hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
    )
    fig.update_layout(coloraxis_showscale=False)
    return fig

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

def top_5_employer_states(file_path):
    all_majors_data = pd.read_csv(file_path)
    state_counts = all_majors_data['Employer State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']
    top_5_states = state_counts.head(5)

    # Display top 5 employer states ranked
    for index, row in top_5_states.iterrows():
        st.write(f"{index + 1}. **{row['State']}**")

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

def create_pie_chart(file_path):
    df = pd.read_csv(file_path, encoding='latin')
    company_counts = df['Employer Name'].value_counts().reset_index()
    company_counts.columns = ['Employer Name', 'Count'] 
    filtered_company_counts = company_counts[company_counts['Count'] > 1]
  
    fig = px.pie(filtered_company_counts, 
                 names='Employer Name', 
                 values='Count',
                 color_discrete_sequence=px.colors.sequential.Greens)

    fig.update_traces(textinfo='none',
                      hoverinfo='label+value+percent')
    
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

def display_top_5_cities(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    if 'State' not in data.columns:
        st.error("'State' column not found in the data.")
        return
    mi_cities = data[data['State'] == 'Michigan']
    non_mi_cities = data[data['State'] != 'Michigan']
    top_5_mi_cities = mi_cities['City'].value_counts().head(5)
    top_5_non_mi_cities = non_mi_cities['City'].value_counts().head(5)
    st.subheader("Top 5 Michigan Cities by Internship Count")
    for city, count in top_5_mi_cities.items():
        st.write(f"**{city}:** {count} internships")    
    st.subheader("Top 5 Non-Michigan Cities by Internship Count")
    for city, count in top_5_non_mi_cities.items():
        st.write(f"**{city}:** {count} internships")

AllEthnicity = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'Not Reported','American Indian/Alaskan Native']
Major2022 = [57, 50, 7, 51, 91, 42, 193, 60, 20, 164, 23]
InverseGender = ['#C70F0F', '#0B1799']
Major2021 = [72, 47, 44, 100, 42, 173, 67, 24, 155, 22]
MajorList2021 = ["Applied Engineering Sciences", "Biosystems Engineering", "Civil Engineering" , "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Mechanical Engineering", "Materials Science & Engineering"]
Major2123 = [207, 141, 21, 153, 286, 108, 593, 203, 61, 490, 61]

def main():  
    st.subheader("DESTINATION DATA") 
    st.write("Summary of placement, salary and geographic destinations for all undergraduate students in the College of Engineering")
    col1, col2 = st.columns([2,3]) 
    with col1:
        options = ("Cumulative Data 21-23: Key Stats", "2023", "2022", "2021")
        ms1 = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Year", label_visibility="visible", default=["2021"])

    with col2:
        if ms1 == ["2021"]:
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
        else:
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
        ms = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major", default=["All Engineering Majors"],  label_visibility="hidden")

    if ["All Engineering Majors"] == ms:
        if ["2023"] == ms1:
            key_stats()
            st.caption("Note: 0.8% of graduates indicate “other intentions” - placed and not seeking")
            st.header("Spring 2023 Graduating Class Composition: All Engineering Majors")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                data_major()
            with tab2:
                AllEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'American Indian/Alaskan Native']
                AllCount2023 = [552, 89, 86, 35, 29, 18, 10, 1]
                data_ethnicity(AllCount2023, AllEthnicity2023)
            with tab3:
                AllGender2023 = [625, 195]
                data_gender(AllGender2023)
            fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv")
            st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
            st.plotly_chart(fig)
        elif ["2022"] == ms1:
            key_stats("2022", "82.5%", "625/758", "98%", "612/625", "$73,922", "$72,500", "82.9%", "14.6%", "0.2%")
            st.caption("Note: 0.3% of graduates indicate “other intentions” - placed and not seeking")
            st.header("Spring 2022 Graduating Class Composition: All Engineering Majors")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                data_major([], Major2022)
            with tab2:
                AllCount2022 = [532, 72, 77, 23, 14, 25, 12, 1, 2]
                data_ethnicity(AllCount2022, AllEthnicity)
            with tab3:
                AllGender2022 = [541, 217]
                data_gender(AllGender2022)
            fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv")
            st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
            st.plotly_chart(fig)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "80.3%", krinfo = "599/746", pr = "96%", prinfo = "575/599", avgsal = "$69,838", medsal = "$70,000", employ = "82%", grad = "13.5%", vol = "0.5%")
            st.header("Spring 2021 Graduating Class Composition: All Engineering Majors")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                data_major([], Major2021, MajorList2021)
            with tab2:
                AllCount2021 = [523, 73, 19, 1, 19, 83, 2, 1, 25]
                AllEthnicity2021 = ["White", "Asian", "Black/African American", "Hawaiian/Pacific Islander", "Hispanic/Latine", "International", "Not Reported", "Not Specified", "Two or More Races"]
                data_ethnicity(AllCount2021, AllEthnicity2021)
            with tab3:
                AllGender2021 = [556, 190]
                data_gender(AllGender2021)
            fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv")
            st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
            st.plotly_chart(fig)
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('80.3%', '82.5%', '90.5%', '84.4%', '96.0%', '98.0%','94.3%', '96.1%', '69,838', '73,922', '76,806', '73,522', '70,000','72,500', '75,000', '72,500')
            tab1, tab2= st.tabs(["By State", "By City"])
            with tab1:
                AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                st.plotly_chart(AllFig)
                top_5_employer_states("LATLONGDestinationCumulativeDataset(All Majors).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City')
                display_city_visualization("LATLONGDestinationCumulativeDataset(All Majors).csv")

    elif ["Applied Engineering Sciences"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "100%", krinfo = "78/78", pr = "92%", prinfo = "72/78", avgsal = "$72,233", medsal = "$70,000", employ = "87%", grad = "5%")
            st.header("Spring 2023 Graduating Class Composition: AES Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                AESColors = ['#CECECE', '#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(AESColors)
            with tab2:
                AESCount2023 = [58, 6, 2, 6, 2, 3, 1]
                data_ethnicity(AESCount2023)
            with tab3:
                AESGender2023 = [51, 27]
                data_gender(AESGender2023)
        elif ["2022"] == ms1:
            key_stats("2022", "81%", "46/57", "100%", "46/46", "$67,579", "$70,000", "98%", 0, "2%")
            st.header("Spring 2022 Graduating Class Composition: AES Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                AESColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE', '#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(AESColors, Major2022)
            with tab2:
                AESEthnicity2022 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races']
                AESCount2022 = [48, 3, 2, 2, 2]
                data_ethnicity(AESCount2022, AESEthnicity2022)
            with tab3:
                AESGender2022 = [32, 25]
                data_gender(AESGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "88%", krinfo = "63/72", pr = "100%", prinfo = "63/63", avgsal = "$66,697", medsal = "$65,000", employ = "97%", grad = "3%")

            st.header("Spring 2021 Graduating Class Composition: AES Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                AESColors = ['#CECECE', '#CECECE', '#CECECE', '#18453B','#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(AESColors, Major2021, MajorList2021)
            with tab2:
                AESEthnicity2021 = ["White", "Asian", "Black/African American", "Hispanic/Latine", "International", "Not Reported", "Two or More Races"]
                AESCount2021 = [53, 4, 2, 3, 4, 2, 4]
                data_ethnicity(AESCount2021, AESEthnicity2021)
            with tab3:
                AESGender2021 = [46, 26]
                data_gender(AESGender2021)
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('88%', '81%', '100%', '90%', '100%', '100%', '92%','97%', '66,697', '67,579', '72,233', '68,836', '65,000', '70,000','70,000', '68,333')
             
            tab1, tab2= st.tabs(["By State", "By City"])
            with tab1:
                AESFig = choropleth_state_map("DestinationCumulativeDataset(Applied Engineering Sciences).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: AES Major')
                st.plotly_chart(AESFig) 
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Applied Engineering Sciences).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: AES Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Applied Engineering Sciences).csv")
    
    elif ["Biosystems Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "93%", krinfo = "41/44", pr = "93%", prinfo = "38/41", avgsal = "$68,768", medsal = "$72,500", employ = "78%", grad = "15%")
            st.header("Spring 2023 Graduating Class Composition: BE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                BEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#18453B', '#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(BEColors)
            with tab2:
                BEEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races']
                BECount2023 = [36, 3, 3, 1, 1]
                data_ethnicity(BECount2023, BEEthnicity2023)
            with tab3:
                BEGender2023 = [22, 22]
                data_gender(BEGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "100%", krinfo = "50/50", pr = "94%", prinfo = "47/50", avgsal = "$64,547", medsal = "$64,500", employ = "66%", grad = "26%", other = "2%")
            st.header("Spring 2022 Graduating Class Composition: BE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                BEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#18453B', '#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(BEColors, Major2022)
            with tab2:
                BECount2022 = [37, 4, 2, 1, 2, 3, 1]
                data_ethnicity(BECount2022, AllEthnicity[:7])
            with tab3:
                BEGender2022 = [21, 29]
                data_gender(BEGender2022, InverseGender)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "87%", krinfo = "41/47", pr = "87%", prinfo = "36/41", avgsal = "$58,792", medsal = "$56,160", employ = "68%", grad = "17%", vol = "2%")
            st.header("Spring 2021 Graduating Class Composition: BE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                BEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE', '#18453B','#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(BEColors, Major2021, MajorList2021)
            with tab2:
                BEEthnicity2021 = ["White", "Asian", "Black/African American", "Hispanic/Latine", "International"]
                BECount2021 = [37, 4, 1, 2, 3]
                data_ethnicity(BECount2021, BEEthnicity2021)
            with tab3:
                BEGender2021 = [27, 20]
                data_gender(BEGender2021)        
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('87%', '100%', '93%', '93%', '87%', '94%', '93%', '91%',
                        '58,792', '64,547', '68,768', '64,036', '56,160', '64,500', '72,500', '64,387')

            tab1, tab2= st.tabs(["By State", "By City"])
            with tab1:
                BEFig = choropleth_state_map("DestinationCumulativeDataset(Biosystems Engineering).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: BE Major')
                st.plotly_chart(BEFig) 
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Biosystems Engineering).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: BE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Biosystems Engineering).csv")
                
    elif ["Computational Data Science"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "93%", krinfo = "13/14", pr = "92%", prinfo = "12/13", avgsal = "$91,357", medsal = "$95,000", employ = "84%", grad = "8%")
            st.header("Spring 2023 Graduating Class Composition: CDS Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CDSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE',
                '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#18453B']  
                data_major(CDSColors)                              
            with tab2:
                CDSEthnicity2023 = ['White', 'Asian', 'Hispanic/Latine', 'Two or More Races']
                CDSCount2023 = [8, 3, 1, 2]
                data_ethnicity(CDSCount2023, CDSEthnicity2023)
            with tab3:
                CDSGender2023 = [9, 5]
                data_gender(CDSGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "86%", krinfo = "6/7", pr = "100%", prinfo = "6/6", avgsal = "$70,333", medsal = "$75,000", employ = "83%", grad = "17%")
            st.header("Spring 2022 Graduating Class Composition: CDS Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CDSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE', '#18453B']
                data_major(CDSColors, Major2022)
            with tab2:
                CDSEthnicity2022 = ['White', 'Asian', 'International', 'Not Reported']
                CDSCount2022 = [4, 1, 1, 1]
                data_ethnicity(CDSCount2022, CDSEthnicity2022)
            with tab3:
                data_gender([4, 3])
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats(0, '86%', '93%', '90%', 0, '100%', '92%', '96%', 0, '70,333', '91,357', '80,845', 0, '75,000', '95,000', '85,000', "Two") 
            
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                CDSFig = choropleth_state_map("DestinationCumulativeDataset(Computational Data Science).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: CDS Major')
                st.plotly_chart(CDSFig) 
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Computational Data Science).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: BE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Computational Data Science).csv")

    elif ["Civil Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "95%", krinfo = "55/58", pr = "96%", prinfo = "53/55", avgsal = "$65,895", medsal = "$65,000", employ = "84%", grad = "9%", other = "3%")
            st.header("Spring 2023 Graduating Class Composition: CE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(CEColors)
            with tab2:
                CEEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races']
                CECount2023 = [41, 1, 4, 6, 4, 2]
                data_ethnicity(CECount2023, CEEthnicity2023)
            with tab3:
                CDSGender2023 = [46, 12]
                data_gender(CDSGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "76%", krinfo = "39/51", pr = "95%", prinfo = "37/39", avgsal = "$66,729", medsal = "$67,800", employ = "87%", grad = "13%")
            st.header("Spring 2022 Graduating Class Composition: CE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(CEColors, Major2022)
            with tab2:
                CEEthnicity2022 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Not Specified', 'American Indian/Alaskan Native']
                CECount2022 = [39, 1, 4, 4, 1, 1, 1]
                data_ethnicity(CECount2022, CEEthnicity2022)
            with tab3:
                CEGender2022 = [31, 20]
                data_gender(CEGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "75%", krinfo = "33/44", pr = "97%", prinfo = "32/33", avgsal = "$58,612", medsal = "$55,640", employ = "85%", grad = "12%")
            st.header("Spring 2021 Graduating Class Composition: CE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE', '#18453B','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(CEColors, Major2021, MajorList2021)
            with tab2:
                CECount2021 = [35, 3, 2, 3, 1]
                CEEthnicity2021 = ["White", "Black/African American", "Hispanic/Latine", "International", "Two or More Races"]
                data_ethnicity(CECount2021, CEEthnicity2021)
            with tab3:
                CEGender2021 = [37, 7]
                data_gender(CEGender2021)
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('75%', '76%', '95%', '82%', '97%', '95%', '96%', '96%','58,612', '66,729', '65,895', '63,745', '55,640', '67,800', '65,000', '62,813')

            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                CEFig = choropleth_state_map("DestinationCumulativeDataset(Civil Engineering).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: CE Major')
                st.plotly_chart(CEFig)
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Civil Engineering).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: CE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Civil Engineering).csv")

            
    elif ["Chemical Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "95%", krinfo = "90/95", pr = "98%", prinfo = "88/90", avgsal = "$77,315", medsal = "$76,000", employ = "83%", grad = "15%")
            st.header("Spring 2023 Graduating Class Composition: ChemE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                ChemEColors = ['#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(ChemEColors)
            with tab2:
                ChemEEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', 'Not Specified', "Black/African American"]
                ChemECount2023 = [74, 6, 4, 3, 2, 2, 4]
                data_ethnicity(ChemECount2023, ChemEEthnicity2023)
            with tab3:
                ChemEGender2023 = [54, 41]
                data_gender(ChemEGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "82%", krinfo = "75/91", pr = "97%", prinfo = "73/75", avgsal = "$71,561", medsal = "$72,500", employ = "87%", grad = "10%")
            st.header("Spring 2022 Graduating Class Composition: ChemE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                ChemEColors = ['#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(ChemEColors, Major2022)
            with tab2:
                ChemEEthnicity2022 = ['White', 'Asian', 'International', 'Two or More Races', 'Not Specified', "Black/African American"]
                ChemECount2022 = [75, 6, 5, 3, 1 , 1]
                data_ethnicity(ChemECount2022, ChemEEthnicity2022)
            with tab3:
                ChemEGender2022 = [53, 38]
                data_gender(ChemEGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "83%", krinfo = "83/100", pr = "94%", prinfo = "78/83", avgsal = "$69,604", medsal = "$70,000", employ = "86%", grad = "8%")
            st.header("Spring 2021 Graduating Class Composition: ChemE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                ChemEColors = ['#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(ChemEColors, Major2021, MajorList2021)
            with tab2:
                ChemECount2021 = [73, 8, 2, 4, 10, 3]
                ChemEEthnicity2021 = ["White", "Asian", "Black/African American", "Hispanic/Latine", "International", "Two or More Races"]
                data_ethnicity(ChemECount2021, ChemEEthnicity2021)
            with tab3:
                ChemEGender2021 = [66, 34]
                data_gender(ChemEGender2021)         
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('83%', '82%', '95%', '87%', '94%', '97%', '98%', '96%','69,604', '71,561', '77,315', '72,827', '70,000', '72,500', '76,000', '72,833')

            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                ChemEFig = choropleth_state_map("DestinationCumulativeDataset(Chemical Engineering).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: ChemE Major')
                st.plotly_chart(ChemEFig)
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Chemical Engineering).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: ChemE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Chemical Engineering).csv")
               
    elif ["Computer Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "92", krinfo = "22/24", pr = "100%", prinfo = "22/24", avgsal = "$80,112", medsal = "$79,040", employ = "91%", grad = "9%")
            st.header("Spring 2023 Graduating Class Composition: CpE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CpEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE']
                data_major(CpEColors)
            with tab2:
                CpEEthnicity2023 = ['White', 'International']
                CpECount2023 = [22, 2]
                data_ethnicity(CpECount2023, CpEEthnicity2023)
            with tab3:
                CpEGender2023 = [21, 3]
                data_gender(CpEGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "76%", krinfo = "32/42", pr = "97%", prinfo = "31/32", avgsal = "$83,698", medsal = "$80,500", employ = "81%", grad = "16%")
            st.header("Spring 2022 Graduating Class Composition: CpE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CpEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE']
                data_major(CpEColors, Major2022)
            with tab2:
                CpEEthnicity2022 = ['White', 'Asian', 'International', 'Hispanic/Latine', "Black/African American"]
                CpECount2022 = [28, 4, 5, 1, 4 ]
                data_ethnicity(CpECount2022, CpEEthnicity2022)
            with tab3:
                CpEGender2022 = [34, 8]
                data_gender(CpEGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "79%", krinfo = "33/42", pr = "97%", prinfo = "32/33", avgsal = "$81,500", medsal = "$77,500", employ = "73%", grad = "21%", vol = "3%")
            st.header("Spring 2021 Graduating Class Composition: CpE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CpEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE']
                data_major(CpEColors, Major2021, MajorList2021)
            with tab2:
                CpECount2021 = [25, 5, 1, 1, 8, 2]
                CpEEthnicity2021 = ["White", "Asian", "Black/African American", "Hispanic/Latine", "International", "Two or More Races"]
                data_ethnicity(CpECount2021, CpEEthnicity2021)
            with tab3:
                CpEGender2021 = [37, 5]
                data_gender(CpEGender2021)
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('79%', '76%', '92%', '82%', '97%', '97%', '100%',	'98%', '81,500', '83,698', '80,112', '81,770','77,500',	'80,500',	'79,040', '79,013')      

            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                CpEFig = choropleth_state_map("DestinationCumulativeDataset(Computer Engineering).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: CpE Major')
                st.plotly_chart(CpEFig)  
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Computer Engineering).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: CpE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Engineering).csv")
                

    elif ["Computer Science"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "81%", krinfo = "184/227", pr = "92%", prinfo = "169/184", avgsal = "$89,826", medsal = "$85,000", employ = "73%", grad = "19%")
            st.header("Spring 2023 Graduating Class Composition: CSE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CSEColors = ['#18453B', '#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(CSEColors)
            with tab2:
                CSEEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', "Black/African American"]
                CSECount2023 = [125, 43, 42, 4, 5, 8]
                data_ethnicity(CSECount2023, CSEEthnicity2023)
            with tab3:
                CSEGender2023 = [189, 38]
                data_gender(CSEGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "79%", krinfo = "152/193", pr = "98%", prinfo = "149/152", avgsal = "$85,220", medsal = "$80,000", employ = "82%", grad = "15%", other = "1%")
            st.header("Spring 2022 Graduating Class Composition: CSE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CSEColors = ['#18453B', '#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(CSEColors, Major2022)
            with tab2:
                CSECount2022 = [100, 32, 39, 7, 3, 9, 3]
                data_ethnicity(CSECount2022, AllEthnicity[:7])
            with tab3:
                CSEGender2022 = [164, 29]
                data_gender(CSEGender2022)   
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "71%", krinfo = "123/173", pr = "98%", prinfo = "120/123", avgsal = "$76,365", medsal = "$75,000", employ = "87%", grad = "10%", vol = 1)
            st.header("Spring 2021 Graduating Class Composition: CSE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CSEColors = ['#18453B', '#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(CSEColors, Major2021, MajorList2021)
            with tab2:
                CSECount2021 = [104, 26, 3, 3, 32, 5]
                CSEEthnicity2021 = ["White", "Asian", "Black/African American", "Hispanic/Latine", "International", "Two or More Races"]
                data_ethnicity(CSECount2021, CSEEthnicity2021)
            with tab3:
                CSEGender2021 = [139, 34]
                data_gender(CSEGender2021)  
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('71%', '79%', '81%', '77%', '98%', '98%', '92%', '96%','76,365', '85,220', '89,826', '83,804', '75,000', '80,000', '85,000', '80,000') 
    
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                CSEFig = choropleth_state_map("DestinationCumulativeDataset(Computer Science).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: CSE Major')
                st.plotly_chart(CSEFig) 
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Computer Science).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: CSE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Science).csv")

    
    elif ["Electrical Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "93%", krinfo = "71/76", pr = "96%", prinfo = "68/71", avgsal = "$76,512", medsal = "$79,500", employ = "77%", grad = "16%", other = "3%")
            st.header("Spring 2023 Graduating Class Composition: EE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                EEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE', '#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(EEColors)
            with tab2:
                EECount2023 = [47, 8, 6, 4, 2, 2, 7]
                data_ethnicity(EECount2023)
            with tab3:
                EEGender2023 = [69, 7]
                data_gender(EEGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "83%", krinfo = "50/60", pr = "100%", prinfo = "50/50", avgsal = "$79,650", medsal = "$77,500", employ = "80%", grad = "20%")
            st.header("Spring 2022 Graduating Class Composition: EE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                EEColors = ['#CECECE', '#CECECE', '#CECECE','#18453B', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(EEColors, Major2022)
            with tab2:
                EECount2022 = [36, 10, 8, 1, 1, 2, 2]
                data_ethnicity(EECount2022)
            with tab3:
                EEGender2022 = [50, 10]
                data_gender(EEGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "85%", krinfo = "57/67", pr = "95%", prinfo = "54/57", avgsal = "$73,322", medsal = "$75,000", employ = "70%", grad = "25%")
            st.header("Spring 2021 Graduating Class Composition: EE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                EEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE', '#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(EEColors, Major2021, MajorList2021)
            with tab2:
                EECount2021 = [43, 10, 5, 1, 1, 5, 2]
                EEEthnicity2021 = ["White", "Asian", "Black/African American", "Hawaiian/Pacific Islander", "Hispanic/Latine", "International", "Two or More Races"]
                data_ethnicity(EECount2021, EEEthnicity2021)
            with tab3:
                EEGender2021 = [56, 11]
                data_gender(EEGender2021)  
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('85%', '83%', '93%', '87%', '95%', '100%', '96%', '97%', '73,322', '79,650', '76,512', '76,495', '75,000', '77,500', '79,500', '77,333')
            
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                EEFig = choropleth_state_map("DestinationCumulativeDataset(Electrical Engineering).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: EE Major')
                st.plotly_chart(EEFig)
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Electrical Engineering).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: EE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Electrical Engineering).csv")
       
    elif ["Environmental Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "94%", krinfo = "16/17", pr = "94%", prinfo = "15/16", avgsal = "$58,102", medsal = "$61,950", employ = "75%", grad = "19%")
            st.header("Spring 2023 Graduating Class Composition: ENE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                ENEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE']
                data_major(ENEColors)
            with tab2:
                ENEEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races']
                ENECount2023 = [11, 3, 1, 1, 1]
                data_ethnicity(ENECount2023, ENEEthnicity2023)
            with tab3:
                ENEGender2023 = [8, 9]
                data_gender(ENEGender2023, InverseGender)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "90%", krinfo = "18/20", pr = "100%", prinfo = "18/18", avgsal = "$63,697", medsal = "$62,400", employ = "83%", grad = "17%")
            st.header("Spring 2022 Graduating Class Composition: ENE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                ENEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B', '#CECECE']
                data_major(ENEColors, Major2022)
            with tab2:
                ENEEthnicity2022 = ['White', 'American Indian/Alaskan Native', 'Not Specified']
                ENECount2022 = [18, 1, 1]
                data_ethnicity(ENECount2022, ENEEthnicity2022)
            with tab3:
                ENEGender2022 = [10, 10]
                data_gender(ENEGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "71%", krinfo = "17/24", pr = "94%", prinfo = "16/17", avgsal = "$60,560", medsal = "$60,000", employ = "94%", grad = "0%")
            st.header("Spring 2021 Graduating Class Composition: ENE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                ENEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#18453B', '#CECECE']
                data_major(ENEColors, Major2021, MajorList2021)
            with tab2:
                ENECount2021 = [20, 2, 1, 1]
                ENEEthnicity2021 = ["White", "Asian", "International", "Two or More Races"]
                data_ethnicity(ENECount2021, ENEEthnicity2021)
            with tab3:
                ENEGender2021 = [11, 13]
                data_gender(ENEGender2021, InverseGender)
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('71%', '90%', '94%', '85%', '94%', '100%', '94%', '96%','60,560', '63,697', '58,102', '60,786 ', '60,000', '62,400', '61,950', '61,450')
            
            tab1, tab2= st.tabs(["By State", "By City"])
            with tab1:
                ENEFig = choropleth_state_map("DestinationCumulativeDataset(Environmental Engineering).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: ENE Major')
                st.plotly_chart(ENEFig)
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Environmental Engineering).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: ENE Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Environmental Engineering).csv")

    elif ["Mechanical Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "92%", krinfo = "157/171", pr = "95%", prinfo = "149/157", avgsal = "$75,069", medsal = "$74,500", employ = "79%", grad = "15%", other = "1%")
            st.header("Spring 2023 Graduating Class Composition: ME Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                MEColors = ['#CECECE', '#18453B', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(MEColors)
            with tab2:
                MEEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'American Indian/Alaskan Native']
                MECount2023 = [117, 15, 20, 9, 5, 1, 3, 1]
                data_ethnicity(MECount2023, MEEthnicity2023)
            with tab3:
                MEGender2023 = [146, 25]
                data_gender(MEGender2023)
        if ["2022"] == ms1:
            key_stats(year= "2022", kr = "84%", krinfo = "137/164", pr = "98%", prinfo = "134/137", avgsal = "$70,685", medsal = "$72,000", employ = "84%", grad = "14%")
            st.header("Spring 2022 Graduating Class Composition: ME Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                MEColors = ['#CECECE', '#18453B', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(MEColors, Major2022)
            with tab2:
                MECount2022 = [128, 11, 10, 5, 1, 6, 3]
                data_ethnicity(MECount2022, AllEthnicity[:7])
            with tab3:
                MEGender2022 = [127, 37]
                data_gender(MEGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "85%", krinfo = "131/155", pr = "97%", prinfo = "127/131", avgsal = "$69,674", medsal = "$71,000", employ = "79%", grad = "18%")
            st.header("Spring 2021 Graduating Class Composition: ME Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                MEColors = ['#CECECE', '#18453B', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                data_major(MEColors, Major2021, MajorList2021)
            with tab2:
                MECount2021 = [120, 13, 2, 3, 12, 5]
                MEEthnicity2021 = ["White", "Asian", "Black/African American", "Hispanic/Latine", "International", "Two or More Races"]
                data_ethnicity(MECount2021, MEEthnicity2021)
            with tab3:
                MEGender2021 = [120, 35]
                data_gender(MEGender2021)          
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('85%', '84%', '92%', '87%', '97%', '98%', '95%', '97%','69,674', '70,685', '75,069', '71,809', '71,000', '72,000', '74,500', '72,500')
            
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                MEFig = choropleth_state_map("DestinationCumulativeDataset(Mechanical Engineering).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: ME Major')
                st.plotly_chart(MEFig)
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Mechanical Engineering).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: ME Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Mechanical Engineering).csv")
    
    elif ["Materials Science & Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "94%", krinfo = "15/16", pr = "93%", prinfo = "14/15", avgsal = "$70,447", medsal = "$72,500", employ = "73%", grad = "13%")
            st.header("Spring 2023 Graduating Class Composition: MS Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                MSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#CECECE', '#18453B', '#CECECE']
                data_major(MSColors)
            with tab2:
                MSEthnicity2023 = ['White', 'Asian', 'International']
                MSCount2023 = [13, 1, 2]
                data_ethnicity(MSCount2023, MSEthnicity2023)
            with tab3:
                MEGender2023 = [10, 6]
                data_gender(MEGender2023)
        elif ["2022"] == ms1:
            key_stats(year= "2022", kr = "87%", krinfo = "20/23", pr = "95%", prinfo = "19/20", avgsal = "$72,147", medsal = "$75,000", employ = "75%", grad = "20%")
            st.header("Spring 2022 Graduating Class Composition: MS Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                MSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#18453B', '#CECECE', '#CECECE']
                data_major(MSColors, Major2022)
            with tab2:
                MSEthnicity2022 = ['White', 'International', 'Hispanic/Latine', 'Two or More Races']
                MSCount2022 = [19, 1, 2, 1]
                data_ethnicity(MSCount2022, MSEthnicity2022)
            with tab3:
                MSGender2022 = [15, 8]
                data_gender(MSGender2022)
        elif ["2021"] == ms1:
            key_stats(year= "2021", kr = "82%", krinfo = "18/22", pr = "94%", prinfo = "17/18", avgsal = "$63,581", medsal = "$60,320", employ = "67%", grad = "27%")
            st.header("Spring 2021 Graduating Class Composition: MS Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                MSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#CECECE','#18453B']
                data_major(MSColors, Major2021, MajorList2021)
            with tab2:
                MSCount2021 = [13, 1, 5, 1, 2]
                MSEthnicity2021 = ["White", "Asian", "International", "Not Specified", "Two or More Races"]
                data_ethnicity(MSCount2021, MSEthnicity2021)
            with tab3:
                MSGender2021 = [17, 5]
                data_gender(MSGender2021)    
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('82%', '87%', '94%', '88%', '94%', '95%', '93%', '94%', '63,581', '72,147', '70,447', '68,725', '60,320', '75,000', '72,500', '69,273')
            
            tab1, tab2 = st.tabs(["By State", "By City"])
            with tab1:
                MSFig = choropleth_state_map("DestinationCumulativeDataset(Materials Science and Eng).csv")
                st.header('College of Engineering Spring 21-23 Destination Locations - By State: MS Major')
                st.plotly_chart(MSFig)
                top_5_employer_states("LATLONGDestinationCumulativeDataset(Materials Science and Eng).csv")
            with tab2:
                st.header('College of Engineering Spring 21-23 Destination Locations - By City: MS Major')
                display_city_visualization("LATLONGDestinationCumulativeDataset(Materials Science and Eng).csv")
    # Internship Data Section
    options = ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
    ms_intern = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major", label_visibility="visible", default=["All Engineering Majors"])

    if ms_intern == ["All Engineering Majors"]:
        file_path = "LATLONG(All Majors) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("DTE Energy")
                st.image("https://www.detroitnews.com/gcdn/-mm-/d6c3b2e154dec7b878c3a925988ce89f7382da06/c=0-84-909-598/local/-/media/2017/10/16/DetroitNews/DetroitNews/636437400389592182-DTElogo4.jpg?width=660&height=374&fit=crop&format=pjpg&auto=webp")
            with C2:
                st.write("Ford Motor Company")
                st.image("https://download.logo.wine/logo/Ford_Motor_Company/Ford_Motor_Company-Logo.wine.png")
            with C3:
                st.write("General Motors")
                st.image("https://www.cnet.com/a/img/resize/881915eb938253a9d5e22f3d4ed0efb172186076/hub/2021/01/08/16573426-bb3b-4513-9451-a5e05f729f9a/gm.jpg?auto=webp&fit=crop&height=675&width=1200")
            with C4:
                st.write("Lansing Board of Water and Light")
                st.image("https://res.cloudinary.com/micronetonline/image/upload/c_crop,h_1194,w_3000,x_0,y_0/f_auto/q_auto:best/v1664295825/tenants/b5f7c51e-b36e-4985-b65c-20bdb9fe3401/e2099576c1044364b24ca764a67540e7/bwl.png")
            with C5:
                st.write("Marathon Petroleum Company")
                st.image("https://www.marathonpetroleum.com/content/inline-images/marathonpetroleum/News/Corporate_Logos/Mlogo_600_px_width.jpg")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Trane Technologies")
                st.image("https://logovectorseek.com/wp-content/uploads/2020/09/trane-technologies-logo-vector.png")
            with C2:
                st.write("Amcor")
                st.image("https://images.ctfassets.net/f7tuyt85vtoa/15Bjgla8JMGEkIUU8WskIE/c3c98de4a8f72de8bf0dea30500ac692/BRANDMARK_POS_V_RGB_64624d7b26f4826922b0488831d7f069.jpg")
            with C3:
                st.write("Delta Dental")
                st.image("https://www.kspdonline.com/wp-content/uploads/2019/11/delta-dental-of-michigan-log.png")
            with C4:
                st.write("BASF")
                st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXcAAACGCAMAAAARpzrEAAAAtFBMVEX///8AAABMr0VHrUBDrDs7qjJAqzhFrT7j8+I3qS76+vr5/PlUs016wXZVVVUrKyu33LUzMzOSy4+y2rBzc3O3t7eHxoOi05+WlpZ0v2/u7u6BxXykpKTc79tvvmrk5OTn8uYXFxddtldDQ0PS6tCAgIBra2vA4b7w+PCQkJBfX1/FxcWurq5NTU3Y2Njz8/N2dnbNzc0eHh4nJyer16jM58plul+c0JhFRUVYWFgrpiAhoxJPKPcaAAARm0lEQVR4nO1da2OquhKlQIIUbRV3sdYXum21te8qdnv///+6ExLCayKoPefsFtaXWkzCZCWZrEwCaloNFDerx+Gvp89O57Lz++nu/vFq8l9b9ONxPrl+OkPwef18jqY/AtqgdSr6/ulVvX+6KIGHX7fXqwla9xyusBKfroozTq47GOkcH7fP+RzD98uDoemWcSLsxoEkI7hTVzWHzuuqBPU4eU9F2d4eim5/8ZbNc32A8RG0pn4qyBfw/uswqzvDogKfFTn3e+ln1L9k8SdTSHV4h45bMM3dKvJd78tUmsDr47Il8F15Pzt73Ffe+aWywuo8F+Vv/vRSWd7PbveUt1LmynnnCDfvh9z8I0F8xXg/u1eXp56nXxU5XpQjBMdlTHzVeD9TqsKbqTqTQguVmlGTiKVR5Xg/u1EU97gnD95Y94ffXA636vH+S1HcvhnyAsswOebukaSqHu8KOb6fRSzP72NuHrVgBXnHNc1+IpA1l1r+7MVzZXm/fEEKU4v3EL/zOT4VST8ubm9/qcfCXWV5P0PCVNrboXlwv/Q+FB7p/EpB/fSlsrxjgZrXgjw553SFpXpIDiWFQHr7iby//0riAV9OIg7+vKjOOeeErbLe0xoVnwHufyLvn+kkL2j17vJlob03hVUmBxYzzkpUVOD/+Ym8/86uLIfKmqdQvPLMNBYamckOJHQO+K3mvbMf34l3DdEpD7mibgppPztLO5rJFEmSKxhrTu6xUN6Laozyrtxb+m95Rzp83s9goyKL9GyMR3Oyqged+kPF82W8N/sqBGV5d0YqoK1UjnfEc+fn1Y9sEqTs9HbfSy4LQyezrj2/QaB9Je+Wp0zdpiV5bxAF7D5W7tG856Jc+Q2+N8R9pzlVbGQ/lttB/6t491GXxAofYOWW4x2pYC7Ykt/gwwpPb9SpwmidYalDMz+e92kuTW72O8917gds0TNNZdozJVwM8TMzSfx03pF1aG7XLr++eUQVTiqj6vABx+VDwVmxb8w7tmLMrJue/+ST5OPv+eMvE9SPpHPuOanE8XF7pdpj+XG8Xw5j3KMbpu85F4CsbjR8rZnKVrzEZbjNrnMFfhjvxch3wbynZgIf8yNpIVR23+NhiHT7ivF+iVCQX1SyYzYviB9JS/gD9vk+r7Pevlq8vyI6A+nYE1XxafbKeRqBh/R0jvJ+pcbbN+a9g/ravCOfKlnNRO7LhBdipI5IHhqPvPvGvP/GeEc2+PgxJcyNdDKZ9539QJBotkN5//WNeYeenN9qQjb4xClKbAM1G/gq2h7MII7IVYt3kJElQoZi7sW8SC6kdl549j0FGfqvGu/ZMAuywdcRky+mJD/yZxFWhQuoJKKjltXjPX3KFPHQsk9jW0rYFKE6OoBiWFneU84C2RGSqyPsjAGyNwtYHeBtnivLe2LdiYkWubRCzwMoQi43V2WPlTxUl/eYPKT6n3JthR7uUD8l9fJ2W8rVP1eXd+lppnu+wyMw+5/uuxkiEdAMXn8g77kD0yv8hIaQJZj8Tsyc6Hq0cDtpdY/uvUpMbyrAu6KGYmmEzZwJB44e79jzpI7E5PHPniefVpXgHSWXp8Mc+PttAhgDU+QWGFZKb39fDd7ReG34zUEBRQkWGkQPaGSlzrkibnZXDd7PsUBL6OCL50AMd2GLTfPo5BazePiGKaa/ifcGVYC0TuEd3QBnYu6oB5TOwrGCSvtpXtujAcvLI3hXxYGNoKdCC+nGKO/Ltgqbk3jHFpNsbjssfB7jSnWaAHmgYYokY48eoLwP1VgpeNcNUwXMe3zF+ciyvL8ouFM+KVOET9VQQdZUWJuzwBt6RLuoxn/HeeCyvKNjfVV0AmYfJtoNKtGRp6Aw3pmRP593vGu+qV+/UYxr1ZSc7/BTJNVrFXh/xmrOnnw/37+q3IeO8lnt7Fk0dAoZ/jzenyYpPK9UQZyjnz8N8aZ0Uukej++/Tn4e72Xxelr2W/UxvcTm+TMelQ/3syrK+wpXOWXx8bJHhE7/DK9Wq6tr1S5UGOCpKO/Hi3eOU9ptUl3er498q4PEw3FPQjLwncJq8v6iUJfYWxunaMobTTvy3pPq8v6oqPft+UsO53jQcnisIBLHSKrIOxvp6Bfo+cmXKZaUbfcds/CKlrQV5J2Fa/EALf5UEq4Gmbs4+P1i8dPHFeR9osqLBjNVuyNMDZ4fdFSMQUYsK8d7hwXJ8ddvKN6LiivGcLvvkNd2MsSB4qrxzp8Nw7sw9j4gBpxcHoo5xMd/JvZFqsX7hzgphjrmd+z9Vwx4K4mn+1bTsjdPnSWuEu+doZg4cfGuesGh6qVAorCbcl3+Ij2aKsP7R+IN8PhSU/3SZly3yPST22nR3T+zEhVtrKIaU/tU/O8LeC99Bvfj4nY4SToRXIaoD4Lh4dzE7tLL415J+Zp/sfNRvDun4yCGcRzwwxilch58q1SSmyFO/e979JcWDrWgxh5Mrob3d59RRKfzcF3/oE2NGjVq1KhRo0aNGjVq1KhRo0aNGjVq1KhRo0aNGjVq1KhRo0aNGjVq1KhRo0aNGjUEfATh1SOOtTvznjtoedvFUl5aHlVQGlDGsjhVZENov8K2/sBdlC/qHwXyS526owW2PTq4qPaMmBbApPo2qt3A3qEv0DsE692uWzrxaGePkctdxLb/FIk35YnX6NGmo40N69CnZ/wxNQxKdMumlk6botk8i85PNbFr0nbpxCPTyL+hshFQwwLbdErAttnhXerrIV4MuQ4MY7wWn4/h3W9aOmktlo6z3LjQAoTT/RW8r237gP6O8D7SwbbBBmxz5ltiGNbfQLyAa1lu/N/BvDszQyfSozSahk5Dv/4VvDcWi/LGILwvm7IbcNuM5lc8k/U18E7j3TV1msjRMHRzy4s9nfeDgPA+MHXDj//1oU+s/02T9uI03humThbJC2uoq6P9FbyP7MRIZFhTXf83TdoLhHen7YHwaiemfxBj3sDt5gWBaxppFbEkZDfXBO/OwmsNvFS2kdtquWtf/OdvNvDlqNfqe23WWs7G7XvbzVJ+68t8axeEatKmRhe060Bq1zzvnpW54hMin7n1F1tWo7j8zcYJb9/ywrZatr2W15s7iW+XXS+rR8EGr9WSNnCDoTqQld9ovtnE/djZbOK+mOd9PqNMetGmTLQAMQaXqJEdpk5Tp4v0pUajsdQ476Mg1HBUl0nmY34lumV3t5svW4RaoDrGvsYzmETceW1HOnIE+ULJJS1o9Ak1eWJeeo53h+o0I2V9bht8t6U0LI94gjLPtpfh7Q2LDBxt0aRh4WAUQ9/e+W09vER1SYIf2mDGNix2u4U2CKtoktDdbu2Eul3s7PiN41ne9S7k0WfAlmHym2prYlA6mxGqk8ybykdEp7gqhmK7BitIJ1CQ0BELCpeaMwqM9MMLbWq1Z5RdMnWzNWeSj985LFTqyDnTSbPW2JAW+LplkGYQ6JCYrzhyvM+J3lQodj+guklmzBBTiEuYpxagNqGWIDh7bRIZNQ57fMsw19QC45qEKSRRisVtMKCGZMTrZ7b70KKQDNQG6zM+TUwxLZEM5x3KHYHw2ui6yb9oE52s4cpyzT6kKtCmRoBXzbNANPfnTME1DfFieaCP9Jioa0PdXJ6fpWK328Ingwwa4ttekvcl0DNmw9UBDx1WR2tZRjBymAOE0lso711q9HHbnADI2y55jQzeOC7YSzzfcXw2Gxt063OjuB5qGdAXZqw2jQF0mi3nKrJhE9VwQfWZ2VxAMr9vcfHUN2ikhZegp5IEZXjndda0DTQV+wsyIFrDzm3dSHWhnql6Vz/wLppNa8C6JXTeM6nqRkIFAe+mKACqFn3siUkj4r1vWRGlaxra7kORkV+3eG1yvINAVtgGrWcLQxpUmAm8C7HDlHHEFfTznjDOihqxB1kaYbWMaDyNqDFjf4F3KVWhQzHWNkROgG2alFNZ3mUyJzBsVsbWjJP3zLQS25rJzEkA77Jx+4bth/c1e9ElcDCexvv7MrqiW9EsZvJqCN5BM8nWdppkB9XZ2ETet8mrmuN9YClsA2JlHwReeOGuJSsOH2exmWEZrL/LDjc2wqZK2MCaitkAvMuXlKxNfhOLt1JIA0l02izv8dIc0vkh/USuNpYkPXa3e/p7TLJrhX4Nhlx8X6DWieulhU4o4s03UryDZ41/G2QUSoblfO5HJukK3j0V7zApJeRkYITKwLVkxdcmX4JobMxHvCfK2oBzdVI2sB814bzH6m4helnPFET4NPUTJznepesH3hssuTFbSkDDJh0NeAT051JCPSPFBPAOw9oBqv2oHIcvFGAIRD1vRKQdGd4HVlYzSTj+YizqXN7PrFOdpcdZ5jaG6FI5HOaS96Q0slPLMWcpbQCuoxaTvENXDRxebGo1oV43cd5Z74CJRgAmn8QtmbtVzqvxuonXaWlnCpqHLk9WUck79AVkCeb4G7cVmCCydLy/r03FvOpaZsJZCo+X5j3q+pJ3iyaq3dSFLnEazAbKbIh4l4Ncfm7x0Q7T8CwZpSjifc4kRwK7JAeb2CnL6g4Gaw3jnU2vyYLsRUneg8QYjOCsgXKGoNc08P4OzjarI8G2duhSEuG2DZc9Bf3dsvw4SyA6QhcoZ/HzoCf9O8L7hlfMJ/FY0LRS/X3WTSJhAAwinWT64tgkPU3R35upgkbH8+6MqWEH2/Z8yeZVnPeGrZNMPrCtG/b3It7z/T1ayzBwXeYEIIuDbRdscPbx7vCJf03NhpZAEe++qXIlIn168lrCClbGCQREnfhUmkIp3vtGdt0JWs5oCjsdFe/QIOkeBlNwKDd6KRHW5f8V+fdkE9JQBLMVh7i4l3e4H3PsMysdUCninakuTQkmhf3khbaIPSG8j43c2rYU766Z4M/b/a8txXFYZyXvPVhupmzrctvAOSbWLzBlrrVi3hNTQoMvhGFdGeXYz7vPZpCGnREHRbwzdyi7m7Oz032WhbiD9P983YXwnhL/xGaNUIp3mGFk3JytvXzNseMrsART8L40dSt5iQ1FdjfW7eMdA8KVQhHvQpQwgHhuce0YdaMR3TOvhoKMrbbSna6Qd1iMyUoCdb1Ubta/aazKnBYsE3L7HqJOPljny2xi3VSCd+jRsgpdytaNwHtUCxCkCv0OiYkIR/CU0dKdBVFljaDCg4SN/B55/x4v49kyjnXEpRGryb7BB7mC9w2li5mZEbWFvGsD0wrCD06bGHrWVbiwbA545NbZBKZuL0SxOd4hqTHjkdWNxR1FKd5ZgMhch5GGrsnnStkSo1ak4bB9Pg86xVjEcpltwjHAoBQ18vswJhpJGzUV7xbl++IsIBR6ajl9NFrU0E32ScE7DNKZntXCxbwvA9Mw+t7WZRN4fgXjwUqbzgbu1puxsGE7KjbPO1MhkBIKguYJXU453jUXiJ957AYiMLeGC2O4Y2DScaAbrTXOuzMQtrleQAzDjIxn8U2r77p9FtVcpGxU8W65lDbB9LFpWFye9ohuMRvGJg3YqOkpeWczjQw9SNooTfJO47eg9qnNPy/7Nos8s7g5djajzeLnBnwPrEfHCaBYO+Y9+ux4tmmEBfGoImSVAc65Lf2Vb9ImZzdqxV5kgMineTa7o0ntvhMOOKZ3KbJMAg5hkWZZLKwexJKkMSNWiCjUH9vI3BORncGmkZ5Zdm0W8GfliCE/EDaQcWgDmLywScy7TaQaYLuf2a2LruclDkv0PM+PPq9d+XnuNqltB118W9hZtKjNVhD9eDRAsbIB2/Hnhkts2571hOkbz4tasuF5MmDqutvMt34vMG0zWEsvt+nDzNx02bpgFgaofM/DNk+ddouAbdCo6XG+GOiEWC1pcMLGtFEhOS02m/u9pk2MQVzHBdhA9NCGwGZbGnPPi7d4Ep/BjZCsf/4iOI2G/8+UfDqck00LeT8efhxFrnEITuR9nQ6J1SiL03hny6ovM6VSOJ53Z6k5rvkXndv5Vjied1/vz8y/6Zzat0Kf7Pzjcvo7Jj3/3SNcPweLLnJmqxQcbxy4fvz//wHLGexLdE56BAAAAABJRU5ErkJggg==")
            with C5:
                st.write("Consumers Energy")
                st.image("data:image/png;base64,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")
            st.header("Top Internship Destinations")
            file_path = "LATLONGHS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONGHS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)

        with T3:
            report_salary(avgsal21 = "$20.86", avgsal22 = "$22.69", avgsal23 = "$24.42", avgsal2123 = "$22.66", medsal21 = "$20.00", medsal22 = "$21.00", medsal23 = "$23.00", medsal2123 = "$21.33", count21 = "278", count22 = "506", count23 = "477", count2123 = "1261")
    
    elif ms_intern == ["Applied Engineering Sciences"]:
        file_path = "LATLONG(Applied Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv" 
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("DTE Energy")
                st.image("https://www.detroitnews.com/gcdn/-mm-/d6c3b2e154dec7b878c3a925988ce89f7382da06/c=0-84-909-598/local/-/media/2017/10/16/DetroitNews/DetroitNews/636437400389592182-DTElogo4.jpg?width=660&height=374&fit=crop&format=pjpg&auto=webp")
            with C2:
                st.write("Trane Technologies")
                st.image("https://logovectorseek.com/wp-content/uploads/2020/09/trane-technologies-logo-vector.png")
            with C3:
                st.write("GE")
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/General_Electric_logo.svg/500px-General_Electric_logo.svg.png?20160707134006")            
            with C4:
                st.write("PepsiCo")
                st.image("https://1000logos.net/wp-content/uploads/2020/08/PepsiCo-Logo.png")
            with C5:
                st.write("Intel Corporation")
                st.image("data:image/png;base64,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")
            st.header("Top Internship Destinations")
            fig = create_pie_chart("LATLONG(Applied Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv")
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            fig = choropleth_state_map(file_path)
            st.plotly_chart(fig)
            display_top_5_states(file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Applied Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$20.73", avgsal22 = "$22.14", avgsal23 = "$24.48", avgsal2123 = "$22.45", medsal21 = "$20.13", medsal22 = "$21.00", medsal23 = "$25.00", medsal2123 = "$22.04", count21 = "22", count22 = "55", count23 = "41", count2123 = "118")

    elif ms_intern == ["Biosystems Engineering"]:
        file_path = "LATLONG(Biosystems Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("POET")
                st.image("data:image/png;base64,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")
            with C2:
                st.write("Gentex Corporation")
                st.image("data:image/jpeg;base64,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")
            with C3:
                st.write("PepsiCo")
                st.image("https://1000logos.net/wp-content/uploads/2020/08/PepsiCo-Logo.png")
            with C4:
                st.write("Boston Scientific")
                st.image("https://logowik.com/content/uploads/images/boston-scientific6168.jpg")
            with C5:
                st.write("Cargill")
                st.image("https://www.cargill.com/image/1432080092113/cargill-color-logo.jpg?v=1684747481000")                        
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Biosystems Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Biosystems Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$18.30", avgsal22 = "$19.04", avgsal23 = "$20.49", avgsal2123 = "$19.28", medsal21 = "$18.25", medsal22 = "$17.00", medsal23 = "$20.00", medsal2123 = "$18.42", count21 = "10", count22 = "21", count23 = "19", count2123 = "50")

    elif ms_intern == ["Chemical Engineering"]:
        file_path = "LATLONG(Chemical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"

        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("BASF")
                st.image("data:image/png;base64,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")
            with C2:
                st.write("Packaging Corporation of America")
                st.image("data:image/png;base64,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")
            with C3:
                st.write("Dow")
                st.image("https://download.logo.wine/logo/Dow_Chemical_Company/Dow_Chemical_Company-Logo.wine.png")
            with C4:
                st.write("Amcor")
                st.image("https://images.ctfassets.net/f7tuyt85vtoa/15Bjgla8JMGEkIUU8WskIE/c3c98de4a8f72de8bf0dea30500ac692/BRANDMARK_POS_V_RGB_64624d7b26f4826922b0488831d7f069.jpg")
            with C5:
                st.write("Corteva Agriscience")
                st.image("https://www.agriculture.com/thmb/CvuL0JSVrXoYR5KGQyw75PHJNJQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/CortevaLegal_VerColor-6c8dbdeb7a384ebf83d06078ab53850f.png")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Marathon Petroleum Company")
                st.image("https://www.marathonpetroleum.com/content/inline-images/marathonpetroleum/News/Corporate_Logos/Mlogo_600_px_width.jpg")
            with C2:
                st.write("Consumers Energy")
                st.image("data:image/png;base64,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")
            with C3:
                st.write("Gallo")
                st.image("https://drinks-intel.com/wp-content/uploads/2024/02/Gallo-Logo.png")
            with C4:
                st.write("Boston Beer Company")
                st.image("data:image/png;base64,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")
            with C5:
                st.write("General Mills")
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/General_Mills_logo.svg/1200px-General_Mills_logo.svg.png")                                   
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Chemical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Chemical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$22.46", avgsal22 = "$24.39", avgsal23 = "$22.85", avgsal2123 = "$23.23", medsal21 = "$22.50", medsal22 = "$24.00", medsal23 = "$22.50", medsal2123 = "$23.00", count21 = "39", count22 = "61", count23 = "54", count2123 = "154")
    
    elif ms_intern == ["Civil Engineering"]:
        file_path = "LATLONG(Civil Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("MI - Department of Transportation")
                st.image("https://pavecampaign.org/wp-content/uploads/2020/08/Website-PSAC-Logo-template-25.jpg")
            with C2:
                st.write("GMcivil")
                st.image("data:image/png;base64,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")
            with C3:
                st.write("The Christman Company")
                st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAllBMVEX///8EBwcAAACgZy5hYmKysrLFxcXw8PC7u7uur6/h4eFRUVHDpIv6+vqdYSKwg16eZCiaWxHt5NtERkZXV1ebXhncyrrp6ekvMDB3d3fV1dX29vaDhITOzs6nqKgNEBBsbGyLi4uenp4iJCRAQUFoaGg2NjaioqIdHR2SkpIqKyt0dXUWFxeIiIjNs5/z7eeVUQDax7aPjudDAAAF+klEQVR4nO2Z6ZajNhCFZYVFxiHJBCbYYGy8YtzdWd7/5VKlDYw909OesU9Ozv1+NOXSgq5U2mghAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8J/nz5+v+Yv8xTIgNkI0gSZPhTECLqVybS68mUeitelBSd7QeGsy39hqhdi69EYUeTDCuTaisx6q25kvqWlr5IrlpXGkNt3nDOprhb9+/mXM37+T/0VqYmWeshHO4lIrY+7JPBtzmkrHjLxrYyqXNRC1T1diIUd0YiltPu8L+xq3pq1z71gax9T8mlc+YXJD4W8/jfnECnM5IWR81s+JLEVmPGujUNuZoIabdLUxBpk59bbzCmo6GwfSbJNnonBZXQnqNWlqbFa+ms3Um4EZQl9Mnpxk/Wu/7VOKjyp8s03di1L61gwV5tY9eAkpzMYKXxa+uYloxgpXorUFgrnPt9x7czbQ4yoRfe8ed/Iy4QMKJ31kBc6RDhUm0g2NjhGrsJRjhWsfRwtO9ZknNvBvVLPztlEY2h+6vo49+2EheZ9CmcQGIeJI3lBYVTZ42yquTJ+Swiq18eMVBmnsa6r4USkbYZRQibRqbVn6mdiApXyF0aMVVhVXKpuO/57ZE4cm55xrXMv7FA7Curyl0AWknJKZOIV+hgzm4Zior4Ixk07PuNiYvFCLgUIzfaUyD63E9tKc7R+scHpDYVKGX1bY3KcwHSpcWWnsM8vrgxQKtVjmNxQO5uG1wuPSsajvVTiTZqHjl+uN6mFj2E/rgULVr+03FPoVi1jfqbDSY0f5O+laVj9E4avfsS4UhruvKuy5W6Fyi6gx2kcpnLwebyqc9Sv3i3AL+Q9VqHdRGbkVJ3uYwuHm0yuc2M1qZzPPvMJiPYjQ71FozIosHS4yflSUyqQoiuXVSrOdmGc3VkgtdhTfo1CroR48v9rOXD1MIdvdlUIV2rEsrhT2fFihNVmhPvfK5dYH0OxS4elOhUnquNgP2xu7Rd7vhiOFroqPj+FA4cQsNP2spjAdKjzep3Cwyr97pils9ERjhfuvzcP9NypMLjYdbYc/RKGvM3j/1Gad65HCl/7QbafSUKFbmt5TqO8u8lwzpb4FULR8l0K3+ruQiL7hXGq3iM2FwtbvkzsTpee7FOrXmLOqn3/ptyn89HmMvuMv5QUT4S49dh5qjlqhhlY2vkppSh+ZioR4olg/Xp3C4QnHfTXItSxN05sZTwFTn8H8Cm2T9H34ZOxrhX9c8w/vOWl0ARWMp6GGSyXG5hdG2pzqmiOlM9PJU4XWG3qUSKeuEFH0VQxq5Elssk1rb1Km2DTDfrARpWlUPKijNjmqK4UAgP8tcVHE/Cz4+wqtGIWxBZuFNtK4TyajTn3ZRNvVRXpSprZs7LKlqanOvM+6n7fQHM8ZL+0VnWK3S95HyGeOrKXM9D4aZZw81cliM2mk/Y4ttqcD51wFnK7EG3+vaM4B+0K5tt9OSfwx0rXNGnq0O6nX+Hz5PIWFWDVWIZ0AEt6ypO7nkvb4nK6v0Uxf28XqzXRA5Bo3V2JFjefidLUQHeel4vwMc/+CeK+Ph+1K6M5LYz46TE9vT1OY7WeyNgrbkUIyp41T2C1CapQ6iGgV2aKRnPOw6Q46brot/8vDNlzJ427qXhFwgUKe+Zwja0VvijP1xDGsq+hsx/DtagzbhVMoTgfqAJWJqDs5haLMOqvwJGRAp6X2hdwh50tjP19zVti0OviTbEGHo9miyZ42EY+qaDlupCpONB8TPpzJOkl45hQRzzkzD+mIueFoVNXCnleFDNOGFR50uuLzYCzrmKd1eCwSf2PVCg9tygqbMqQOqdVi9jSFXdO88EGu3L/yrb/g6Fk2DS0TRdM0eo0gf0pj0/ESkcxOq40tSvaCBiqi6Eyp2FJn3u/44Fs3zcFlE1temuJgzuXLY6Cl1eGzBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgC/yL21tdy18X8coAAAAAElFTkSuQmCC")
            with C4:
                st.write("OHM Advisors")
                st.image("https://chambermaster.blob.core.windows.net/images/customers/2969/members/2427/logos/MEMBER_PAGE_HEADER/OHM_Advisors_No_Tag_Line%C2%AE.png")                        
            with C5:
                st.write("Eaton County Road Commission")
                st.image("https://eatoncountyroad.com/wp-content/uploads/2023/02/ecrc_logo-full-1024x683.png")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Kimley-Horn")
                st.image("https://mma.prnewswire.com/media/1890007/kimley_horn_logo.jpg?p=twitter")
            with C2:
                st.write("SME")
                st.image("https://www.sme-usa.com/wp-content/uploads/2022/09/SME-insights.png")
            with C3:
                st.write("Hubbell Roth and Clark")
                st.image("https://content.energage.com/company-images/SE86458/SE86458_logo_orig.png")
            with C4:
                st.write("WSP")
                st.image("data:image/png;base64,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")
            with C5:
                st.write("Black and Veatch")
                st.image("data:image/png;base64,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")                       
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Civil Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Civil Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$17.86", avgsal22 = "$19.75", avgsal23 = "$22.22", avgsal2123 = "$19.94", medsal21 = "$18.00", medsal22 = "$18.00", medsal23 = "$21.00", medsal2123 = "$19.00", count21 = "14", count22 = "39", count23 = "50", count2123 = "103")

    elif ms_intern == ["Computational Data Science"]:
        file_path = "LATLONG(Computational Data Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Ford Motor Company")
                st.image("https://download.logo.wine/logo/Ford_Motor_Company/Ford_Motor_Company-Logo.wine.png")
            with C2:
                st.write("Blue Cross Blue Shield")
                st.image("https://logowik.com/content/uploads/images/bluecross-blueshield8335.jpg")
            with C3:
                st.write("Roosevelt Innovations")
                st.image("https://media.licdn.com/dms/image/D560BAQEJEwhIeR6RMQ/company-logo_200_200/0/1706904134242/roosevelt_innovations_logo?e=2147483647&v=beta&t=8XPO1EC7K0pyU3w1-C3osvzQqU-tJUoyjF_I0zLqzGw")
            with C4:
                st.write("Google")
                st.image("data:image/png;base64,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")
            with C5:
                st.write("Comerica")
                st.image("https://mma.prnewswire.com/media/1830002/Comerica_Logo.jpg?p=facebook")                        
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Computational Data Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Computational Data Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$16.75", avgsal22 = "$24.37", avgsal23 = "$26.83", avgsal2123 = "$22.65", medsal21 = "$16.75", medsal22 = "$20.50", medsal23 = "$23.50", medsal2123 = "$20.25", count21 = "2", count22 = "12", count23 = "6", count2123 = "20")
    
    elif ms_intern == ["Computer Engineering"]:
        file_path = "LATLONG(Computer Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("General Motors")
                st.image("https://www.cnet.com/a/img/resize/881915eb938253a9d5e22f3d4ed0efb172186076/hub/2021/01/08/16573426-bb3b-4513-9451-a5e05f729f9a/gm.jpg?auto=webp&fit=crop&height=675&width=1200")
            with C2:
                st.write("Bosch")
                st.image("https://logos-world.net/wp-content/uploads/2020/08/Bosch-Emblem.png")                        
            with C3:
                st.write("Electric Software, LLC")
                st.image("https://media.licdn.com/dms/image/D560BAQEI6BWqmc2xMg/company-logo_200_200/0/1688817843401/electric_software_llc_logo?e=2147483647&v=beta&t=o9N7ml-6y6yR5atA6563-zIKL1AG6tadUOmSRnNVYZU")
            with C4:
                st.write("U.S. Environmental Protection Agency")
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Seal_of_the_United_States_Environmental_Protection_Agency.svg/2048px-Seal_of_the_United_States_Environmental_Protection_Agency.svg.png")
            with C5:
                st.write("Gentherm")
                st.image("https://eco-cdn.iqpc.com/eco/images/partners/xcvbopX42CiTDsCqrfaWKWwReQAQpOoZg7BiZZKA.png")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Halla Mechatronics")
                st.image("https://www.mtu.edu/enterprise/teams/ams/logos/halla-mechatronics-veh.png")
            with C2:
                st.write("Harman International")
                st.image("https://upload.wikimedia.org/wikipedia/commons/c/c2/Harman_International_logo.svg")
            with C3:
                st.write("Nexteer Automotive")
                st.image("data:image/png;base64,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")
            with C4:
                st.write("Jackson")
                st.image("https://www.kentinvictachamber.co.uk/wp-content/uploads/2019/02/Jackson20Logo20Blue-1000x384.jpg")
            with C5:
                st.write("Tesla")
                st.image("https://1000logos.net/wp-content/uploads/2021/04/Tesla-logo.png")                        
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Computer Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Computer Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$19.99", avgsal22 = "$20.33", avgsal23 = "$25.48", avgsal2123 = "$21.93", medsal21 = "$20.00", medsal22 = "$20.00", medsal23 = "$23.00", medsal2123 = "$21.00", count21 = "18", count22 = "18", count23 = "22", count2123 = "58")
    
    elif ms_intern == ["Computer Science"]:
        file_path = "LATLONG(Computer Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Delta Dental")
                st.image("https://www.kspdonline.com/wp-content/uploads/2019/11/delta-dental-of-michigan-log.png")
            with C2:
                st.write("Amazon")
                st.image("https://www.hatchwise.com/wp-content/uploads/2022/05/amazon-logo-1024x683.png")
            with C3:
                st.write("Ford Motor Company")
                st.image("https://download.logo.wine/logo/Ford_Motor_Company/Ford_Motor_Company-Logo.wine.png")
            with C4:
                st.write("Humana")
                st.image("https://logos-world.net/wp-content/uploads/2022/07/Humana-Symbol.png")
            with C5:
                st.write("Rocket Companies")
                st.image("data:image/png;base64,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")  
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Microsoft")
                st.image("data:image/png;base64,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")
            with C2:
                st.write("Auto-Owners Insurance Company")
                st.image("https://upload.wikimedia.org/wikipedia/commons/2/22/AutoOwnersLogo2015Pad.jpg")
            with C3:
                st.write("GE")
                st.image("https://upload.wikimedia.org/wikipedia/commons/f/ff/General_Electric_logo.svg")
            with C4:
                st.write("Autodesk")
                st.image("https://adsknews.autodesk.com/app/uploads/2021/09/autodesk-logo-primary-rgb-black-large-scaled.jpg")
            with C5:
                st.write("Google")
                st.image("https://cdn.vox-cdn.com/thumbor/2ECtQus43_-tjqtlxy0WE8peSEQ=/0x0:2012x1341/1400x1050/filters:focal(1006x670:1007x671)/cdn.vox-cdn.com/uploads/chorus_asset/file/15483559/google2.0.0.1441125613.jpg")                               
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Computer Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Computer Science) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$23.03", avgsal22 = "$26.84", avgsal23 = "$29.96", avgsal2123 = "$26.61", medsal21 = "$25.00", medsal22 = "$25.00", medsal23 = "$25.00", medsal2123 = "$23.67", count21 = "36", count22 = "92", count23 = "97", count2123 = "225")
    
    elif ms_intern == ["Electrical Engineering"]:
        file_path = "LATLONG(Electrical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("DTE Energy")
                st.image("https://www.detroitnews.com/gcdn/-mm-/d6c3b2e154dec7b878c3a925988ce89f7382da06/c=0-84-909-598/local/-/media/2017/10/16/DetroitNews/DetroitNews/636437400389592182-DTElogo4.jpg?width=660&height=374&fit=crop&format=pjpg&auto=webp")
            with C2:
                st.write("Lansing Board of Water and Light")
                st.image("https://res.cloudinary.com/micronetonline/image/upload/c_crop,h_1194,w_3000,x_0,y_0/f_auto/q_auto:best/v1664295825/tenants/b5f7c51e-b36e-4985-b65c-20bdb9fe3401/e2099576c1044364b24ca764a67540e7/bwl.png")
            with C3:
                st.write("Consumers Energy")
                st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYsAAACACAMAAADNjrXOAAAAxlBMVEX///8AXbl1vB4AWrgAVLYAUbUAWbgAVrdtuQAAVbYAUrYATbRptwAAT7VBfcbv8/lxuhEASrOju9+dzmr2+v3I2O3w+Ofi6/b9/vsAX7qk0XTV6sLZ7MjS3/Dx9vtUhsnc6PV9oNPI46+ZzGarweK/0ekARrL3+/K3yuZxmdGPrtqr1YGbtt0pbsCEpta+3p+z2JLo8904dcJci8uGxD2w14h8vyzP5reRyVTD4Kjk8dceab52m9G63JiUylyJxUgAQLBskMzKSjhJAAAYEUlEQVR4nO1dB1fiShROTJPE0AzSpArSQRFBirL8/z/15s7cKUGCrvtkV8139pyFJNNuvxOcq2kxYhxBoVDoUFxFgd4t/O15fkUUOlf3q9Xq+vq6vGguJ893j48DgtLlzcvTdjubzefzs7P0OcHFb4M0Sp/N57Pt08tNqTQYPN49T5oLMtTq/upncwuITijenDw/ElK/bGfzM4XA5wJpFWf/A2RvOAIf8my+fbksDR4nzTJhT+dvE+gTUbgipF9MCOFvnmbztErxg3ROv6LZh/BbbJSjMebMnkqDu8mi/B0407kngv88KL3Mzs457RXChAgtb5M7xJIQU/JExJTI6ePd3fPzhGC5XDYJFgRlhmsJdgHuwTPLJXn++fnujvCeaN0TmDc6IhtK4dNbvOFzm29vSo+T8vXXYktnBQy43M6RvmzJku7McJ+B4b4hckfIvFwsiFW4v6eu9jMtdwGc/P09OqPH0gtR0Tn4n4tzKQjHGQNsebocTBbXV/+sjykU7stNsrr5uWSAkELiM2dkAXeTJdhiIPk/tI4C8Od6QZgzAPNJWHPxBmPoyoignW0JU8qrf2cxhavr5uPl05nicMnHNBH7l9Id8YMkSrn6SnoNoRzhzF0J3Nr5xVGuIFPOZzeD5V/lSaFDmHAzE+YXGLB9GTwvifp+KepHA9jSnAxetiTIY1yJZArwZP5UOrmaEC4sS6AJLBoi9qc0aV7ffxMGHETnakV05Qac4BGeUJacz18GzVN4k85qMUAukNDi8o4M+u+YyxOAWLDrJuEJ1ZOjLDnblpbXn0eb5eWMxXdPpWX5/kfxYB8FIpTPl1vwkkc5Mn96XHxGGNwhFvHlbvEPxQ1/HdRnQux4jCMX6W2pufqfGfKdHcIfobMCjkTrCGXIbNC8j6X4NKARzSxaRYAhZ0935VigTwWiIqUtMCTCZJEobDZYXP3taf4cdFaTy/kxBTmfl2J+nBCd8uOW7v9EKch8ENurE6Jzffd01GBtJ/d/e44/CYXru+0xdpwNynF4dUJ0yoP0MX7cLGJrdUqsJkfV42URa8cp0Wm+HGPHZflvT/BnobA4yo7H2JWfFJ0mMVaHuXGWvpg1Y1t1Ulw9n10cUY44DTwtri+PKMfL6m9P74ehc5eO9BwX2+u/Pb2fhsUs0lTF3Dg5yke48fR7QVV9uJsWdaM43bWqnzTb06CVDWNYOdXI19uLSL8xeH86npt6pm0Yum4YtutmP3HCn42q55oh3LZPN3h5HuXFz9OLd/Yx9mxdQab1qTP+VOR8PQz/pGo+iXLiZxcv71KNBs4fFIP+v/7sKX8e+okwK4zRace/eok0VOl3+PA2ssJcr5EZbv7zJ/1JqNlhXjiNU8+gGa0ad282Rg5YQ/HR/7K8CLg6cHeR6Z58DlfbKK9xUXqjaddis5+Szw9MqswU3st3h+PGeNjl37UUA/lUyTYaw7roJchlx41Gv1UJ8Ds+GUR9pO1ZjLPXlZZqs774paoYNZVtjA+Ph6j4aJl4ODVMyVHJ/dyw0cgqksYXyC/hk1UILDcshoEmJLaUnVTlIpSpqShF2anzl+O8SDL6u+CwmV4YRXYnO/Jd03Ec0/VrbLLDjAvIBO2RT+6YHlIm37N9lzyZcH29T6/02ZO3OeKO2MdfFdH+V5DD9j1iIsNdae2ka5msrynjVdGHRt6DNiT/JeFKfWf7+Eyxry4max6wTD0P2vu61lpDK9fngWJryhaY4AtM4fqGWs83fZhRlzax7Hzrli0o0Ma4NOhlTafmF/do+hzJjJtjrMi7TKs94LhHP9o1ut6RZQiza/t1uMb0xkj2fbyVyVEW+Y4SuDyoHCbCM8VnA9F+lPXwmp8d8o8ZSvig5kuLb/sVOUOz1SNCnxjCeNar8RCo2G7IMjEJsx82YtZUjvMjXy7Q0eFam9kItzIlPLXI2vo4O+ehR3u2iShkXTEGqqH/Km6eRDJjcIQXLRe1GqbyywfcwnorTsgL2jQewS9FcSsBUjlkLHQcQxA1YMQCwxew9cEqtCJ7oihJaTihroK1w64aslGXzdB+gP8pgfzwePV9socD2ZSn741qAavybIF8KBNUaYyPPMD/TkprebxJsSgmifOxCAN6Dl/lPu4ifcaRRAMliWp1qsJAVhIg2Vwdpwf+vM6Dd5szA+ZWybDPmzGjBBUYxgBnLCJ+eDJv7bcnCxFdgQQk2eLWYz4tokwNnAG94lS1CiNQUR0PkccJFrm3ALVtu3xUrga0BVugMx0nDUFQrsIwFJHOFOeemC4wAJWH6GzAHvdyB+h6Gbl5G51ncJrvxRsNZnjdNpcVEEjUId184KEjua/VGEXI/W4mQZAh14ammDpG/L7S3n2o8VUmRFfwbJfR0ibCwOQQLOdIWBLDsKdiPKJ9LTEeosvJrkZRXNjtHRpOHQzumM4QzEHKZ/wnNloREYMoSoNN3Sju1njZq0rDlMewhyrvKxTmv22luKh74VAgxRbl9A6oJHXzSCDSrMrUwiS0qYz7BOMUp5dupUTETwRatM8KY6J2VeVXnQ2ZAWtlVaVwmuZouh4j6XSX0DPX5+MheoofEatCYTdzXI51m+i9L6aSF7yocL23jOm02MU56MUU1y2aBSPJSLDJeOsd3vEqR+6HRL1haimDKEC5Bt+pfMQwC56VEReqLLFyddlel71Kz8Gp7oQeCJjMgYSiOQNlwwUXA7Gr4fdZ+MplPzQeQqqQzqenBRiQEOlNsaUYD9IBp3iHBrk/xKTdZEYCo30wnsglaskxwjECZnJZpHMA24ic73wS0WCHUtsLX0ZZgrWgrFl57gTtB2H5oVmW2wXHGg0xTq/j7U1oFUgK2h672gkbD12hZzCStdpUGHG0cQ6PeTFsDY2HqO5tRtFVKf4KxcYcSs9Qq9UYA+FZVGGrG6INeMqujJ00DcUEZxahFpq2iFCMdFSSMZK2QgsQ3IRSqnFr4ogJmVmhTtCsLWINku1aLE5XbiPpYBUKKfjalK66wncRf45uFgiERt7joVHbfz0ev8VV1Ge4hVUp/go9B1HxqoxCcChYFV7j2QJzWTTCxJYeHY1fppSx1ZA6hE7k3zIf/lEC+gXqzbQp5D0kF6qqpKqyWYCKN8RSuLJ4tBlXDPoc2HF+GyQKhQs8hySF6Kouu8rLMEuAMBN3NZS4cWoqTzjqfg0O4IwrOQbgHwq7TSaQRMGTXJMgs1K0GVDHUB2UC9XIpjcoD4wk03hKgsOYRTmMw7zgc6KDoDJMQ6TKSaPJDVcg1InNrZdRXKaj6JIdFi5s78sHdI13BaadewLl5UNd2LixmHMQHm8nV4O09kNWwxW8DBhXwDPw7VwxkmsGahIH6ErlxgDLZmNNmT5s7L3h9/EUoRgXh3mBjpmGZZzqfbEoO1CF+bUT5PqZ37gWDwfBHecPOga+INI+YLEXuD3FHPLoua7OMCuCa4n63nicSchLW92jUvyVwlY0fE6IGKjCHmraWAokt65s84RqmpGkUnZsGzWKFxF6gQaCqmVfmhBdCJAS+xx2gohuDd0GaEBXTl0RLqW9omyKE1IIlK9TVEUumtnbfusm+XiSFziAEYr3FX+lJD2GfBKHCkLKCsCRfTkJthGEPBMePxJRgdTs8ONoTGnOyzwn0BKDb7snNoNArA46wdSmASCUrDNrpAg4cHUnV4ERI93FSIgHFCeE+0YQI6498L2wnViUcTQgf2g8BA7gbFJ5hCAcfSVTE8QNTCEWwS1185kqX6rNrQ7fUmuLHNViNxrSRLp7IhJCRLaXvjz8OBojpy9iU78rdnBAW3DcjFwKJMVo+cncchlw93RLk10Ef8+Dsy5PpA3wMdjeC6QNrIa8YlHMhVk2EAsl4qVoy/HYKK58IcwzeB5Geb80njNSXkrXlZKegeklcFQJWELduT63fZhJyHeHiWNvqjoRMe158/DzNR5Fjnu4hQfxCuqFvm732TQSQArpBBXLLxMl5CUx1mIrwfWUVQSKF/dFVyihdJmMuCCXjAx+KxQdUyDpyOND1FjpHPZe6dGnFH+F6SNIGHoWohdVpoxeOLaj2E/imfXQlAxHvug5hKjE+zxiQ6ovEidMsxzaO89fXSYBNkTciud77TlsW2fL81oi06P94ZyHkhSNqK6E89JNtg041cLBM+XF/nhyH62+l+mpm6puK5TI8AUmii5Trp685vL+urw/Z8T+93OqPMCyZHB3AKWIv7iMMFFEWUO7Bo7N1pz1Qlf1vJQG8HyK5a+GnjToG6G8SDjMqYwyFVIc3jnkG7Cckuuqthc8a3IDnI+nvElqqXkO73QjYzM1TOqGuqEvqHDfS9nSGNFpOl4LrYeH10VyYh/7jUmUibqI/OFa2zQ5NwzHf+Cd98SvdOAqNQMPpkFg0+2+BP2YgevZjDANtqUzKa2h4fGGfdegj1ZF+4xsD44vyT76dIiW5+yNmvJtuJ9QHLQ6XlHdXd7RASTo/Na0vQ2x0dqhH1lW3ZALTFhUvNsefdSSsWHQM0xHf6jwsJKnm3wL0Q29UtzH4DAvjr1MSvVHtgWezlk36gqPaoZLLlrkKmZOSQaw/PiRESjHniQOrsaNevBgkgs2WUWPPQmhSQ1bHelKq/eKJs6FjZqb0ttT5RdbfDxTr4X3+fkAAqTTYMQ+EhuUYl0lG6FuLHvUZylCFocKJYrs1b5iRwH8LYkeftcexuowK9Lz43+VUc1XKpX6vhsKDl49iHydPBlKelLkwrGZvtHX8VGD1+N9bKhKrlKPMjNBXYTFaFLFJiDaVevY7ys7EQHtefz3Sr8P9r7Zg1gY4zuaQnZ7jZryVjoKhYg87yL+S74PgAeItR6m4yyU21n8dwD+oTeriE4UK977q9oYKur4Fh/31A2PuSwZpB1x3Pfzg6xIn8da8THslF/sGK7O9iYxdSRh3hFWLA//ijM9j33FRzFc+66ZSJiu706HGIh06T6Zu+5F/1XH1dPh30Zd3MRHIvwB6t3ssJ9t5ZSwDmLOY2Fe5zFCKaJ2oWJ8EgrP6YNpRfriMlaKk+Lq8TAnzi5m8Z9PnhTXN+cROjGPI9lT4v5ufvjPWNMXs5gTJ8TVZHZYJeDPieOU4nRYPc8iziKMT8s5Ja4WpbNIRlw8xYd6nQid8mOUQgAjZpP4jJyT4GoxmEVWB4gZcSrA6cHpyMNqgREvy5gRn47OalmaRx8aDHw4e4yPRf1s3Jefb9IXkecLUj6cl5qxQnwqrq4ng9nFEW2gleTSpWYcvX4eCqvyc4lxIbpYH6jD9rEc68MnoXBfngye0kd1AStfzgbNVewfPgNXq8VdaZt+QxVY6Yt0zIbPQOH+evE8gMo8bzGBFbmeXz7HRul/xtV1eflYwjqbb9Q/phYpTbjwKbXEfigKHaIFEyz4+0YRXYUJT4/L67jg1/+BQqGzohx4kgV/j7MAC0+ezV4eoQDh317AVwdjALFCrOj4uzjA1IAVX580V/9uMekvgEIH6X/zpDDgHRxI85LAN4/LRcyDj4FIP3gAqPnOihC/VbJbZQArqQ5FmUvPzfIqdgi/C0J8EP7mBKR/C5W5Ofnfpv+ZLAs/nz3dDKAqeSeuhPp+EOJfAfGXdyD7sxD13y3+tBQwcQMvpbvl4nr1s2oyfxhAekZ7sDtE8s848d8n++kQ9edbQv7HZbN8fR8rwFtglC83l1Tsn1DuJe3fjP+R8oz26fls+3JTepw0F+UVUD8m/7tROKM0ZJD0PwJBd0H5ywElPRiemPZ/gtIN4jKEUuiLAkL35YIRvlCIKR8jRowYMf4MwT9e2+Yfn97/h+5D0XGcdeNvFCvIj/tjQehKv3/or/q601v/tnay0kF/Ebm1D6caGYbj/UG5hUqyFnmm4zFkM64uvmx868AxwrU1/DFyyz95YY6TI+sZCXM33qwT7NCrD6JvmR/ixc5WzhYbGYnXelGrae12N6cFxaOniXwDtDzdZwcJbRJ/UhOmZpsfquC1NuS5fymHngQURtvQ8re73XqtVX992Yov70Le10Vxi8Pn778T7t5hnu9EylPa5Xx5qK5AMqvlTZhdTusdPX3qyyNpOA/y88drcNV99by296Pt6oYgfz/x+siQwMxTXuRvK8SHf3R6XwFtTzeF4tcMQYpKa5g9cnoHQy47bHP6t0xj3+vmu8NsOyzm1fZ+t2NH0cWaLU5JzLWGLfpkYKWI8v76ZcMZ6fvVZL4VkrZyRunawooxQwMK6fg2hlVFhxdpGPr0QLVhxttoY9c3TYuGXg+eCUeKme5tXXTWHnmW61oZNCs7L9MKep5lmr6t2jKil9LwFPGUxNTOpxNwoHOjDnoxhGm2DtZq+Caoe+rhNfl8HsQ4mFq2axjkH2NB3qIngQIebOpoyX/ZacZ3oSQRnPrm0lMWE64rDtbTNp7t2oZp6z47X3tkmF0duGOI4lIUllJHpG6xYyTbnpMwyQR0Awrm7PrURo3IXJJD7fuCWIjXHmLtOHBUWq6IJqvrCtPl0BMT4Vjctd+o5CtTAwKfYJjtO7o9zGbFYW4b3zC6gZZP2ixOrvo66a5fybeLhjjmWaMHsMnShC2XnpJYyegWVOhoO3piDF9TqQzpytJytx877OxrYG28PkZ5l7CZBe+67LzrhsPPjs97eqJKYy+jSClYd1Gsc1ZI2ru+btMHCA/o6bVtS7eTAe+1Lh7MmoowbBw86NVkicTOpmef94v0rLZq+5SFYk8OQttX8TyRSjxxvGqxu1ODn3WLGkLIadbphZSNNm7s2MqR8UHRsLDJiPkDooBFJtREE3wp3gcyPVAV9r2XcKkvGXqNXKW9874zK8AovDq7V3rzwKZCX7XFWbcbhyaDDUccke+iK0kaaqY3dIW0k9CoQXvlxwYrFk8Dby3bpZgFHJo8stpNR4yjqX5yncx+ZwMFxwq/iufzMvcKTKoXcDYx3hwZ1CK9UhRNIwqmREcjmUtjnOSIXseOYhbze5keaMw4oZs/ZldWYvTaXQylAYeUvA5XuBYEGag7BDziFp+7EmJXTNkHmCHukIv0BGo4IxXFWjJSo9ZOlnvATC9L4qdi93srwWsEvv5qD2kq433wt1XIALl5IYJraJSwRUlY6rqzprp7QojKv5EhQLeyIhMMdNV1Nw5kelXH1g1L731r7/AKYBT29pCQdhRDJqdrg6cghMYQ5xBFwVOzwZVQBSARj7JVlLTFHiOqSM92+uKCTEJUzsNJ+kxj8knfMXTHL37hAvW/DYiHZKhfr1TylHbcmzM5JZmeFfALmOnxjW3hSopqPBYodSDhSHcN+MnvZ021opvCedjR4hpTGa99G496/yGA05SFXa56UFWW0I6LbWDQUm3EPXMz4rJMrygUhWsIbLbKeCwviUr4Bvwk9xMpfkF5QwFuRs305EslLZckXPxBPhyCfvEFcrAUhKt8z4cIPQS8G5HpEcEFDSGxj4OErWGk2g5lesTPiC1bl/KT3OcBgdQQjWqNbBdKNeh31bN8dzRUXtQoKR5sm0dWPZYFc/cMgouZngiEuYaQTE+Jx8hza34gqkvzNnk/5aoVkTeOsrlbpAHWcLdDNxHaHvn2UG1UxaIZXU243ZRJU+qqlM4HGzM9sSViYQo9DWV6LZnpTQ3YUSLOnJfxCWd6RBWE84CoDSo+JPC45/1tlW8OIrUiQyPkBArvHE6dHrNWFfGqjdisvUyvxV2JFYrHiOE3sBCsz7TAFVXnQpke4YXkDMkjwZHI4kIb52htpW8G4lLROwQ13LAdmrgZ1PIZ/bq4KaXlHFYaL/AFYTcy01Mr/MFXarrqNnt/Sy4gc0garmR6oJhYBZBMgNWeLxq4sZWzjpcc+27YJXRnlG13x4btFOnC8xnCnkqq0rN0ZisgbC1m261aZsTq/pAL3HRwV0LMi7HeyEOy14ZRbKfyQ8ewKF1JHMszPSPkj8loemLTJRPQHZzAztHdcT5VH/MJ/BQEaxeq5bqO7SXRo46Jrrim5Tg+89iBYZPY0rIyta5P6/4MLQetWMq02W94KreGbjjy9zztjGG4pktuM8eyS/DaPBXPMNQJDDMkqXPJBBw+gbzrkCumlXC8D/2s5Atj7Hi+5XtJGWcObc/yfbPH7UNl7RFOrFvacDoF6mzYf3BnNEVxz659z1Q2QXKjDFQlqWEakpyO8FNrOg1vgLWnGd8i49XEBPI1mJHv9n5ODCVQz+Uqwf6Vuvo9n8v9Nl3yr3qNQrWyN5wWvLoSI0aMo/gPPyyIf/QNsbkAAAAASUVORK5CYII=")
            with C4:
                st.write("General Motors")
                st.image("https://www.cnet.com/a/img/resize/881915eb938253a9d5e22f3d4ed0efb172186076/hub/2021/01/08/16573426-bb3b-4513-9451-a5e05f729f9a/gm.jpg?auto=webp&fit=crop&height=675&width=1200")
            with C5:
                st.write("Commonwealth Associates")
                st.image("https://educationusa.state.gov/sites/default/files/field_hei_logo/msu_logo.png")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("General Motors")
                st.image("https://image.cnbcfm.com/api/v1/image/106821423-1610125493528-Untitled-5.jpg?v=1610125520")
            with C2:
                st.write("Gentex Corporation")
                st.image("https://s19538.pcdn.co/wp-content/uploads/2015/04/Gentex-Logo.png")
            with C3:
                st.write("Michelin")
                st.image("data:image/png;base64,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")
            with C4:
                st.write("Nexteer Automotive")
                st.image("https://s19538.pcdn.co/wp-content/uploads/2016/04/Nexteer-Automotive-Logo.png")
            with C5:
                st.write("Northrop Grumman Corporation")
                st.image("https://upload.wikimedia.org/wikipedia/commons/3/36/Northrop_Grumman_logo_blue-on-clear_2020.svg")                        
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Electrical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Electrical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$19.86", avgsal22 = "$22.00", avgsal23 = "$23.13", avgsal2123 = "$21.66", medsal21 = "$19.75", medsal22 = "$22.00", medsal23 = "$22.25", medsal2123 = "$21.33", count21 = "48", count22 = "63", count23 = "58", count2123 = "169")
    
    elif ms_intern == ["Environmental Engineering"]:
        file_path = "LATLONG(Environmental Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("GEI Consultants")
                st.image("data:image/png;base64,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")
            with C2:
                st.write("Fishbeck")
                st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAllBMVEUAcIj///8CcYgAbIUAcIkAYXv8//8meo/r+fv4//8+hZXj8/UAYXkAaoNWlaTd7/EWdIlknKpOjp7M5OnC2+B1qrfm+vsAZ34vfI3z//8AZH+Vv8YAa4EAY3oAaYSEs7211NqoyNGRusJqoa3Z7vCdwMmKvcY2hJfP6e2rztZwprAAVG9LjJyhw8m83+Xs9fV2s78AUWsVjGfDAAAJW0lEQVR4nO2ciXbiuBKGjRZWi5gtBsXYbBkgF7pn3v/lRipJRl5wgKSnk7715SQBS5b0q7RUyRyCICB/LkpbgCAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgiAIgvxyGGO/uwm/DsaEjJMkiWVqLjR9tY1IFVfSdJIIPq+noC5V3EdLJGkwmw66i8VgmkVxs75A/PWi2NO6tI5O+kt8msKmum5HyeGbRcvRe+FNuVnAuzrbuK5W1ocSOPksiaauIf2gDVk8afkckkYrNiikoHDR2EV3wQdW4ceQ01aRaWMTf4fCj3zjlVpjZkZXd3qc9szLkWiq9Tco/MggJcES5mBvy2Usw5UZpyG73msNCoMvOUrpFkQNU6a/AI3DlOxFTbV+N4VmFq6keWfGWWOZ307hEhp80pNZ2TBIx4php6nW76aw09aNivP3lNKkcWb/UoWuYruj1ii8dVnNJdChLmPHKwlXLxQUllILCt9bABtWM3f3rTbUX6BYqi4v3Cw0k2U5f15LpRlOYV6il6NswzqRjcKJ+XVF1iq85qYWvjSSqR+igwm7G04lXIL7WSnGEKn6oZdrng2Zdoz96nOFhAqhk2rMxKj2zmudPpumaiP3KVSti33sfi5UMJEsQeEkTBKhpx8L9Isk10N59Pa6Xm9GhDt/2ikkNNxnKmkoL4GGVUhlMtrou+JleewI3nnTSVsSlj0VJni0VWmv2VBKUa8whkZX+411Cl4ZrCt01CpzVsWGz65M3TY5PLjEwywRDNx0q1BuB7a4jXSdahT+r7+yN7VX89T1uG4WjWc7V+BkLAsj3E9rT41bVVJI+Cskryo+F4MF812FrwWFWsyLn9zd0osNT8LzZrWvflHYO3s39bLQM9L+yS/wKL02xuNBoTE/ZFWhzEzfhNX18BGFKpydFdPPwlO481Mmkl0UljhzZykxbBeTpnkSk6W6lIyKQmncr0EcVHhMISM2alwsjEd+TrVljcKf6re7ej3ajs/SssJeXmVmTEXEySU9P1sX/+zGd/pWbkxVoYCNrdWNalapBxSqiqmpdbqP42i0WmiFJI+A9fhbylSGZuAswoLCp2wfdYZHW6uN0WNz43QYcE7sJO7b1s6t5Ek23p9G626NQtqHPL1+XeBjFPb6c0NHdxyJzGto4QTeRMpC3kojYD49cb1TqNVx016LS4zfelZriO5/biSaONwq3IRqo2BUzo2MKRhRmlUi49BeYcLuqYRhahz+1mLIU+VTUZHOFoeSQhqZETWsPSKyCgllhd1OvzZzbcK1Cp3gjdL0CG2A/VsZT5ARqDAKu8QeLZAltELb1yk82VkZUGJ6ow+uA5jg1bkDFKK2dgeynuz4c+ZhIv5bFBS6omb+6lRRaGOiwm4i7H6oc2lnxlcIK2l7LPPNEf6W/FKSgm0mULPdLXJ/TJipoCcwhYq6cd6/YgMmFao9sdldTsJrm1m3nUIWm5Xt5bIyNyg0bq11zZxCd3jkKTQuq46NKfE8iYvXxsAPMn7fE2fBxadxMhh/cokmSjt7k2iuL0DYJqHIFSdlHyiP8e0wXl1z6gsKbe32n2fDoDRK3exorQI99nNf0bOhns+mI56hhKJfqgZFCoZqCbfO7LnMCfWVge4OM7j9cKXktfEfLTOZrggs29DHVxiUFDI7uVvdN6/ocvR0XaFONDNsHwQRTMOJDyy10o2CRc02ZxXyNZQySKo5PqYwoHt3jnqY58e8dym0wtQ4m7fqIW5GHmoMZBSe7I7UgV36UxUSSvKj1Nz7ukshS9yZbp27A+ZlQQrb0rRmlTQKjcBWP70e/j6qUO9+mTPjKn5I4aJgw2mZiVIo3lE4Nkvt7vogfVyhPriJjm6kxrDg3qfQjNI9YxHMukSWYW5b0ucMZRu5eWi8/KfkarD/uEItUu7tUDWb/z0K7ULbUrugGa5v5SMgvQmZNixqTJSvpUbi4OoJ0ocUKveLz4yHCZfvsqFcQ8tCRpbQTRNes1TQMZS+rR7e5zv+0lqxzut+UKEOdvPSiDyBRIg871IYwyA9qrEozHrRLzSRMHhrJuuBV0+9cp/GdFDridRLfMyGdGjnvupaebbZyD0KGTdrxFgf2Jj4Zie9JjKRvOm30mTLCjOR+Qpzic/1Eh9TKHeTuWuPVSjZTTZkcLgcUG6i/R2c5FkZk1jvrPo8jaXLWfcg9Wu7ldi4Q8cEaRyRQmzhJA6iuidRjypstY8dLlQ4IzswjtbpLQp7hEt90sbdCjUUphHmXfctDFWy5NFm4Dx2a+vWtK9uTdNYpT3rM5NCBBwfnMSaU91HFerZkY3np40JUCEwflehflC33myO7pzjaEdtanfuVm+yfj2vTOw4ARtax0C3f/WyeYG0UUGhdvKtxOea5eYjCj12t+0WJS7u8nJVkyoh1KL9RTllVLahsqJpUbdTkfg5Chdz76ztZoWrmOXHTctjJTkz4RRL591SSmWUqmBNWInzssTbFTKrULuAdL/yj3cGe3tKe0Whnhud4icC1E2jwhbAZwVTtVdRfiZB43XxJG6kpkT5RJglO9fZxanYoJBufw4Ggx/uuQVZHtTbrnkqoRaY7GCbNNg4lymEHCdXK6PjrrpwkKaDOtl04FranW5jWnpEkGQ7m7zYbTryEiswJucvT3na+aTvlFDX8FIIS/SVwc9DpxhlNCgMkjiWsbjkh3N/akcWFZL0R7PZdh5fDoBU/tg9d4COgFsYPEzSHz0Skbolmw3niaxxslIZDVXqqE9k4XM3+mmK2iLGs9lstE+kMHuCiG1deVYJ7RXB7QqLEBjuru2APvsS/pMwOM8g3h2FF3rRo3BiVky+ZGKqQHot1IO0ax8/M6ccdU/l3lFIWFAsE85wWN5A5reF5X9c3nwEuVKIl9O/4K7mXVh0YKo3VKWUSrq8vtmGxoTNzy6/IvcoFIqU1Y6gL8wdCpO/M8X+lzfpk7ljpeHV+PA7cLtCVhMBfwfuGKWo8IuCCj1Q4Rfl/0fhDY7K91YYc0UYhvAn5KH5Z67Y6/yfz/ns+H+N/SzG0y20v6XCoPhpk/f5dgrpH6/wz7dh6bOJf6DCgIzuYtv0SfYvCr2P391cBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBPkY/wK1b6fkmy/2swAAAABJRU5ErkJggg==")
            with C3:
                st.write("MAHLE")
                st.image("https://1000logos.net/wp-content/uploads/2020/08/MAHLE-Logo.png")                       
            with C4:
                st.write("MI - Department of Environment, Great Lakes, and Energy")
                st.image("https://content.govdelivery.com/attachments/fancy_images/MIDEQ/2019/04/2522040/egle-logo_original.png")
            with C5:
                st.write("SME")
                st.image("https://mma.prnewswire.com/media/179413/sme_logo.jpg?p=facebook")
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Environmental Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Environmental Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$15.00", avgsal22 = "$17.53", avgsal23 = "$21.66", avgsal2123 = "$18.06", medsal21 = "$15.00", medsal22 = "$17.00", medsal23 = "$20.50", medsal2123 = "$17.50", count21 = "5", count22 = "15", count23 = "20", count2123 = "40")

    elif ms_intern == ["Materials Science & Engineering"]:
        file_path = "LATLONG(Materials Science and Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Apple")
                st.image("https://th.bing.com/th/id/R.df3fc521dc6d79da661c279326ef247e?rik=lZmjPTGg6qWtEw&pid=ImgRaw&r=0")
            with C2:
                st.write("MI - Department of Transportation")
                st.image("https://pavecampaign.org/wp-content/uploads/2020/08/Website-PSAC-Logo-template-25.jpg")
            with C3:
                st.write("3M")
                st.image("https://news.3m.com/image/Trifecta+3M+001+Logo+CMYK_thumb.jpg")
            with C4:
                st.write("Bosch")
                st.image("https://logos-world.net/wp-content/uploads/2020/08/Bosch-Emblem.png")
            with C5:
                st.write("Cleveland-Cliffs")
                st.image("https://d1io3yog0oux5.cloudfront.net/clevelandcliffs/files/pages/clevelandcliffs/db/1149/description/cc-foundation-logo.jpg")                        
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Materials Science and Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Materials Science and Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$26.66", avgsal22 = "$25.61", avgsal23 = "$21.06", avgsal2123 = "$24.44", medsal21 = "$24.25", medsal22 = "$21.88", medsal23 = "$19.00", medsal2123 = "$21.71", count21 = "8", count22 = "11", count23 = "10", count2123 = "29")
    
    elif ms_intern == ["Mechanical Engineering"]:
        file_path = "LATLONG(Mechanical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Tenneco")
                st.image("https://getlogo.net/wp-content/uploads/2020/06/new-tenneco-logo-vector.png")
            with C2:
                st.write("DTE Energy")
                st.image("https://www.detroitnews.com/gcdn/-mm-/d6c3b2e154dec7b878c3a925988ce89f7382da06/c=0-84-909-598/local/-/media/2017/10/16/DetroitNews/DetroitNews/636437400389592182-DTElogo4.jpg?width=660&height=374&fit=crop&format=pjpg&auto=webp")
            with C3:
                st.write("BorgWarner")
                st.image("data:image/png;base64,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")
            with C4:
                st.write("Stellantis")
                st.image("data:image/png;base64,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")
            with C5:
                st.write("General Motors")
                st.image("https://www.cnet.com/a/img/resize/881915eb938253a9d5e22f3d4ed0efb172186076/hub/2021/01/08/16573426-bb3b-4513-9451-a5e05f729f9a/gm.jpg?auto=webp&fit=crop&height=675&width=1200")  
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Trane Technologies")
                st.image("https://logovectorseek.com/wp-content/uploads/2020/09/trane-technologies-logo-vector.png")
            with C2:
                st.write("MSU - Facility for Rare Isotope Beams")
                st.image("https://pbs.twimg.com/profile_images/923281654231261190/ACZF7B2e_400x400.jpg")
            with C3:
                st.write("Bosch")
                st.image("https://logos-world.net/wp-content/uploads/2020/08/Bosch-Emblem.png")
            with C4:
                st.write("Ford Motor Company")
                st.image("https://download.logo.wine/logo/Ford_Motor_Company/Ford_Motor_Company-Logo.wine.png")
            with C5:
                st.write("First Solar")
                st.image("https://upload.wikimedia.org/wikipedia/en/b/bb/First_Solar_logo.svg")                                              
            st.header("Top Internship Destinations")
            fig = create_pie_chart(file_path)
            st.plotly_chart(fig)
        with T2:
            st.title("Interactive Map for Internship/Co-op Location Data: 2021 - 2023 College of Engineering")
            choropleth_file_path = "LATLONG(Mechanical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            fig = choropleth_state_map(choropleth_file_path)
            st.plotly_chart(fig)
            display_top_5_states(choropleth_file_path)
            st.title("Interactive City Visualization")
            file_path = "LATLONG(Mechanical Engineering) HS EGRX-1220 Merge Combo_2021-2023.csv"
            display_city_visualization(file_path)
            display_top_5_cities(file_path)
        with T3:
            report_salary(avgsal21 = "$20.68", avgsal22 = "$21.40", avgsal23 = "$22.96", avgsal2123 = "$21.68", medsal21 = "$20.00", medsal22 = "$20.30", medsal23 = "$22.00", medsal2123 = "$20.77", count21 = "76", count22 = "119", count23 = "100", count2123 = "295")

    # Enrollment Data Section
    st.divider()
    st.subheader("ENROLLMENT DATA")
    ms_ed = st.multiselect("Note: Only select one option per filter.", options=["Fall 2023", "Fall 2022", "Fall 2021"], placeholder = "Filter By Year", label_visibility="visible", default=["Fall 2023"])
    if ms_ed == ["Fall 2023"]:
        st.header("Fall 2023 Enrollment Data")
        T4, T1, T2, T3= st.tabs(["Major", "Class Level", "Ethnicity", "Gender"])
        with T4:
            data_major([], [2085, 1412, 484, 434, 299, 199, 376, 188, 84, 332, 181, 59], ["Computer Science","Mechanical Engineering", "Electrical Engineering","Civil Engineering","Applied Engineering Sciences", "Engineering - Exploratory", "Computer Engineering", "Biosystems Engineering", "Computational Data Science", "Chemical Engineering", "Environmental Engineering", "Materials Science & Engineering"])
            st.write("**Total Enrollment - 6133**")
        with T1:

            class_data = {
            'Class Level': ["First Year - 1847", "Sophomore - 1501", "Junior - 1249", "Senior - 1536"],
            'Count': [1847, 1501, 1249, 1536]}
        
            df = pd.DataFrame(class_data)

            category_order = ["First Year (1847)", "Sophomore (1501)", "Junior (1249)", "Senior (1536)"]
                                            
            major_fig = px.pie(df, values='Count', names ='Class Level', title = 'Distribution of Students by Year', color_discrete_sequence=['#BFD641', '#FFB84C', '#5D9AE9', '#FFDE59'], hover_name = ["First Year", "Sophomore", "Junior", "Senior"], category_orders={'Class Level': category_order},
                labels={'Class Level': 'Class Level'})
            
            st.plotly_chart(major_fig)
            st.write("**Total Enrollment - 6133**")

        with T2:
            EnrollEthnicity2023 = ['White - 3481', 'Asian - 790', 'International - 785', 'Hispanic/Latine - 337', 'Black/African American - 324', 'Two or More Races - 243', 'Not Specified - 158', 'American Indian/Alaskan Native - 14', 'Hawaiian/Pacific Islander - 1']
            data_ethnicity([3481,790,785,337,324,243,158,14,1], EnrollEthnicity2023)
            st.write("**Total Enrollment - 6133**")
            
        with T3:
            data_gender([4747, 1386], ['#0B1799', '#C70F0F'], ['Male - 4747', 'Female - 1386'])
            st.write("**Total Enrollment - 6133**")

    elif ms_ed == ["Fall 2022"]:
        st.header("Fall 2022 Enrollment Data")
        T1, T2, T3= st.tabs(["Class Level", "Ethnicity", "Gender"])
        with T1:

            class_data = {
            'Class Level': ["First Year - 1863", "Sophomore - 1287", "Junior - 1105", "Senior - 1691"],
            'Count': [1863, 1287, 1105, 1691]}
        
            df = pd.DataFrame(class_data)

            category_order = ["First Year (1863)", "Sophomore (1287)", "Junior (1105)", "Senior (1691)"]
                                            
            major_fig = px.pie(df, values='Count', names ='Class Level', title = 'Distribution of Students by Year', color_discrete_sequence=['#BFD641', '#FFB84C', '#5D9AE9', '#FFDE59'], hover_name = ["First Year", "Sophomore", "Junior", "Senior"], category_orders={'Class Level': category_order},
                labels={'Class Level': 'Class Level'})
            
            st.plotly_chart(major_fig)
            st.write("**Total Enrollment - 5946**")

        with T2:
            EnrollEthnicity2022 = ['White - 3483', 'Asian - 725', 'International - 732', 'Hispanic/Latine - 311', 'Black/African American - 309', 'Two or More Races - 212', 'Not Specified - 165', 'American Indian/Alaskan Native - 9']
            data_ethnicity([3483,725,732,311,309,212,165,9], EnrollEthnicity2022)
        with T3:
            data_gender([4590, 1356], ['#0B1799', '#C70F0F'], ['Male - 4590', 'Female - 1356'])

    elif ms_ed == ["Fall 2021"]:
        st.header("Fall 2021 Enrollment Data")
        T1, T2, T3= st.tabs(["Class Level", "Ethnicity", "Gender"])
        with T1:

            class_data = {
            'Class Level': ["First Year - 1522", "Sophomore - 1210", "Junior - 1328", "Senior - 1681"],
            'Count': [1522, 1210, 1328, 1681]}
        
            df = pd.DataFrame(class_data)

            category_order = ["First Year (1522)", "Sophomore (1210)", "Junior (1328)", "Senior (1681)"]
                                            
            major_fig = px.pie(df, values='Count', names ='Class Level', title = 'Distribution of Students by Year', color_discrete_sequence=['#BFD641', '#FFB84C', '#5D9AE9', '#FFDE59'], hover_name = ["First Year", "Sophomore", "Junior", "Senior"], category_orders={'Class Level': category_order},
                labels={'Class Level': 'Class Level'})
            
            st.plotly_chart(major_fig)
            st.write("**Total Enrollment - 5741**")

        with T2:
            EnrollEthnicity2021 = ['White - 3540', 'Asian - 675', 'International - 585', 'Hispanic/Latine - 306', 'Black/African American - 290', 'Two or More Races - 178', 'Not Specified - 161', 'American Indian/Alaskan Native - 6']
            data_ethnicity([3540,675,585,306,290,178,161,6], EnrollEthnicity2021)
        with T3:
            data_gender([4452, 1289], ['#0B1799', '#C70F0F'], ['Male - 4452', 'Female - 1289'])

    
    st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_f52727d1f5fd44fb865b6bff7b45b6ef.xlsx?dn=Diversity_graphs%20Combined_12_9_22.xlsx", label = ":green[**Diversity Enrollment Data 5 Year Overview for Engineering**]")

    J2, J1 = st.columns(2)
    with J2:
        st.page_link("https://careernetwork.msu.edu/outcomes/", label= ":green[**Destination Data for All Majors**]")
        st.image("CareerServices.png", "Contains MSU Wide - All Colleges Destination Survey (2023) by our Career Services Network")
    with J1:
        st.page_link("https://engineering.msu.edu/academics/undergraduate-studies/enrollment-data", label= ":green[**College of Engineering Enrollment Data**]")
        st.image("EnrollmentData.png", "Gives a year by year enrollment and graduation date breakdown for the last 10 years")


    #Annual Activity Report Section 
    st.divider()
    st.subheader("ANNUAL ACTIVITY REPORT")
    st.write("Annual overview of The Center's activities and student engagement")
    K1, K2, K3 = st.columns(3)
    with K1:
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_5553fe34db574893a98e7a8dbc12054d.pdf", label= ":green[**2022-2023 Activity Report**]")
        st.image("2023.png")
        
    with K2:
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_771032809d634849a706253122fdcf05.pdf", label= ":green[**2021-2022 Activity Report**]")
        st.image("2022.png")
    with K3:
        st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_4586c10b1b31439bbe69da616e0e3315.pdf", label= ":green[**2020-2021 Activity Report**]")
        st.image("2021.png")
    with st.expander("Activity Reports From Prior Years"):
        K1, K2, K3 = st.columns(3)
        with K1:
            st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_63a24da526604d86b872fef02fe33e18.pdf", label= ":green[**2019-2020 Activity Report**]")
            st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_e1d90f9b3daf445fb275bde81048dbb2.pdf", label= ":green[**2016-2017 Activity Report**]")
        with K2:
            st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_013d842090f14402855558e2ad91aac7.pdf", label= ":green[**2018-2019 Activity Report**]")
            
        with K3:
            st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_767f829043174861b77a83a2742a1096.pdf", label= ":green[**2017-2018 Activity Report**]")

    #Research and Readings Section 
    st.divider()
    st.subheader("RESEARCH AND READINGS")

    number = st.slider("Drag the slide bar to unlock a new level of information with our recommended research and readings!", 0, 80, 40, 20, format = "")

    if number == 0:
        research_readings([1,8.5,8], "https://www.careers.egr.msu.edu/_files/ugd/bc0367_faa49c899d6f44b3b8471d235776e681.pdf",':green[**The Co-Op Experience - A Lasting Impact by Dr. Phil Gardner and Garth Motschenbacher**]')
        with st.container(border=True):
            st.image("TheCoopExperience.png")

    elif number == 20:
        research_readings([1,11,2.65], "https://joinhandshake.com/wp-content/themes/handshake/dist/assets/downloads/network-trends/gen-z-career-goals-ai-economy.pdf?view=true", ':green[**Handshake Network Trends Report: The Class of 2024 sets their sights on the future**]')
        st.image("HandshakeFuture.png")
    elif number == 40:
        research_readings([1,24,10],"https://www.careers.egr.msu.edu/_files/ugd/bc0367_b684a1faf5c64d0eb711a136ce31f72f.pdf",':green[**Factors Relating to Faculty Engagement in Cooperative Education by Dr. Bernadette Friedrich**]')
        with st.container(border=True):
            st.image("CooperativeEd.png")
    elif number == 60:
        research_readings([1,3,2.65], "https://joinhandshake.com/blog/network-trends/how-gen-z-defines-flexibility/",':green[**Handshake Network Trends Report: How Gen Z defines “flexibility”**]')
        st.image("HandshakeGenZArticle.png")
    
    elif number == 80:
        research_readings([3,6.28,3], "https://ceri.msu.edu/_assets/pdfs/folder College%20Recruiting%20Outlook%202022-2023.pdf", ':green[**College Hiring Outlook 2023 - by Dr. Phil Gardner**]')
        st.image("CollegeHiringOutlook.png")


    
if __name__ == "__main__":

    main()