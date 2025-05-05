import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

# Shows the entire graduating class breakdown by major
def data_major(colors = [], count = [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16], majors = ["Applied Engineering Sciences", "Biosystems Engineering",        "Computational Data Science", "Civil Engineering","Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Mechanical Engineering", "Materials Science & Engineering"]):
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

def choropleth_state_map(file_path, selected_major, selected_year="All"):
    all_majors_data = pd.read_csv(file_path)

    # Detect correct state column
    if 'Employer State' in all_majors_data.columns:
        state_column = 'Employer State'
    elif 'State' in all_majors_data.columns:
        state_column = 'State'
    else:
        st.error("No Employer State or State column found in the dataset.")
        return None

    # Filter by major if needed
    if selected_major != "All Engineering Majors":
        if 'Major' in all_majors_data.columns:
            filtered_data = all_majors_data[all_majors_data['Major'] == selected_major]
        else:
            st.error("Major column not found in the dataset.")
            return None
    else:
        filtered_data = all_majors_data

    # --- New: Filter by graduation year if provided ---
    if selected_year != "All":
        if 'Graduation Term' in filtered_data.columns:
            # Extract year from Graduation Term (e.g., "December 2023 - UG")
            filtered_data['Graduation Year'] = filtered_data['Graduation Term'].str.extract(r'(\d{4})')
            filtered_data = filtered_data[filtered_data['Graduation Year'] == selected_year]
        else:
            st.warning("Graduation Term column not found. Skipping year filter.")

    # Create state counts
    state_counts = filtered_data[state_column].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']

    # State full name to abbreviation
    state_abbrev = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
        'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY',
        'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
        'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
        'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND',
        'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA',
        'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }

    # Map to abbreviations
    state_counts['StateAbbrev'] = state_counts['State'].map(state_abbrev)
    state_counts = state_counts.dropna(subset=['StateAbbrev'])

    # Calculate log of counts for smoother coloring
    state_counts['LogCount'] = np.log1p(state_counts['Count'])

    # Plot
    fig = px.choropleth(
        state_counts,
        locations='StateAbbrev',
        locationmode='USA-states',
        color='LogCount',
        color_continuous_scale='Greens',
        labels={'LogCount': 'Log Count'},
        scope='usa',
        range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),
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

def display_city_visualization(file_path, selected_year=None):
    data = pd.read_csv(file_path)
    
    # Determine Year column
    if 'Start Date' in data.columns:
        data['Year'] = pd.to_datetime(data['Start Date'], errors='coerce').dt.year
    elif 'Graduation Term' in data.columns:
        data['Year'] = data['Graduation Term'].str.extract(r'(\d{4})').astype(float)
    else:
        st.error("Neither 'Start Date' nor 'Graduation Term' column found.")
        return

    # Filter data based on selected year
    if selected_year:
        if selected_year in ["2021", "2022", "2023", "2024"]:
            data = data[data['Year'] == int(selected_year)]
        elif selected_year in ["Cumulative Data 21-23: Key Stats", "Cumulative Data 21-24: Key Stats"]:
            data = data[data['Year'].isin([2021, 2022, 2023, 2024])]
        else:
            st.error("Invalid year selection.")
            return
    # else: No filtering — keep ALL data (cumulative over all years)

    if data.empty:
        st.warning("No data available for the selected year.")
        return

    if 'Employer Latitude' not in data.columns or 'Employer Longitude' not in data.columns:
        st.warning("Latitude and Longitude columns not found. Creating columns... This may take a moment.")
        add_lat_long_to_dataframe(data)  # Make sure you have this function
        data.to_csv(file_path, index=False)
        st.info("Updated CSV file with Latitude and Longitude columns. Please reload the app to visualize.")
        return

    if 'Employer City' not in data.columns:
        if 'City' in data.columns:
            data['Employer City'] = data['City']
        else:
            st.error("Employer City or City column not found.")
            return

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
            'Employer City': False,
            'Graduate Count': False,
            'Employer Latitude': False,
            'Employer Longitude': False
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

    title_text = f"City Visualization ({selected_year})" if selected_year else "City Visualization (All Years)"

    fig.update_layout(
        height=300,
        width=600,
        title=title_text,
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=True,
            lakecolor='#9ec1cf',
            showocean=True,
            oceancolor='#9ec1cf'
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    st.plotly_chart(fig)


def top_5_employer_states(year, selected_major):
    states = []
    if year == "2024":
        if selected_major == "All Engineering Majors":
            states = ["Michigan: 252 positions", "Illinois: 35 positions", "Ohio: 15 positions", "California: 12 positions", "North Carolina: 11 positions"]
        elif selected_major == "Applied Engineering Sciences":
            states = ["Michigan: 11 positions", "Illinois: 9 positions", "North Carolina: 3 positions", "Ohio: 2 positions"]
        elif selected_major == "Biosystems Engineering":
            states = ["Michigan: 8 positions"]
        elif selected_major == "Chemical Engineering":
            states = ["Michigan: 22 positions", "Wisconsin: 3 positions", "Tennessee: 2 positions"]
        elif selected_major == "Civil Engineering":
            states = ["Michigan: 19 positions", "New York: 3 positions"]
        elif selected_major == "Computational Data Science":
            states = ["Michigan: 2 positions"]
        elif selected_major == "Computer Engineering":
            states = ["Michigan: 8 positions", "Maryland: 2 positions"]
        elif selected_major == "Computer Science":
            states = ["Michigan: 71 positions", "Illinois: 17 positions", "Washington: 6 positions", "California: 5 positions", "Ohio: 4 positions"]
        elif selected_major == "Electrical Engineering":
            states = ["Michigan: 20 positions", "Illinois: 2 positions", "Minnesota: 2 positions"]
        elif selected_major == "Environmental Engineering":
            states = ["Michigan: 14 positions", "North Carolina: 2"]
        elif selected_major == "Materials Science & Engineering":
            states = ["Michigan: 4 positions"]
        elif selected_major == "Mechanical Engineering":
            states = ["Michigan: 73 positions", "Ohio: 7 positions", "Virginia: 5 positions", "Indiana: 4 positions", "Texas: 4 positions"]
        else:
            states = []
    elif year == "2023":
        if selected_major == "All Engineering Majors":
            states = ["Michigan: 370 positions", "Illinois: 44 positions", "Ohio: 22 positions", "Texas: 19 positions", "California: 16 positions"]
        elif selected_major == "Applied Engineering Sciences":
            states = ["Michigan: 30 positions", "Illinois: 13 positions", "Ohio: 5 positions", "Arizona: 2 positions", "California: 2 positions"]
        elif selected_major == "Biosystems Engineering":
            states = ["Michigan: 19 positions", "Iowa: 3 positions", "Arizona: 2 positions", "California: 2 positions", "Illinois: 2 positions"]
        elif selected_major == "Chemical Engineering":
            states = ["Michigan: 37 positions", "Illinois: 9 positions", "Ohio: 6 positions", "Georgia: 3 positions", "Indiana: 3 positions"]
        elif selected_major == "Civil Engineering":
            states = ["Michigan: 34 positions", "Texas: 3 positions", "Colorado: 2 positions", "New York: 2 positions"]
        elif selected_major == "Computational Data Science":
            states = ["Michigan: 6 positions"]
        elif selected_major == "Computer Engineering":
            states = ["Michigan: 13 positions"]
        elif selected_major == "Computer Science":
            states = ["Michigan: 80 positions", "Illinois: 9 positions", "Washington: 6 positions", "Texas: 5 positions", "California: 4 positions"]
        elif selected_major == "Electrical Engineering":
            states = ["Michigan: 40 positions", "Illinois: 3 positions", "Texas: 3 positions", "Georgia: 2 positions", "New York: 2 positions"]
        elif selected_major == "Environmental Engineering":
            states = ["Michigan: 10 positions"]
        elif selected_major == "Materials Science & Engineering":
            states = ["Michigan: 4 positions", "Ohio: 2 positions", "Pennsylvania: 2 positions"]
        elif selected_major == "Mechanical Engineering":
            states = ["Michigan: 97 positions", "Illinois: 6 positions", "California: 4 positions", "Florida: 4 positions", "Indiana: 4 positions"]
        else:
            states = []
    if year == "2022":
        if selected_major == "All Engineering Majors":
            states = ["Michigan: 347 positions", "Illinois: 37 positions", "Texas: 33 positions", "California: 25 positions", "Wisconsin: 19 positions"]
        elif selected_major == "Applied Engineering Sciences":
            states = ["Michigan: 19 positions", "Illinois: 6 positions", "Texas: 6 positions", "California: 3 positions", "Arizona: 2 positions"]
        elif selected_major == "Biosystems Engineering":
            states = ["Michigan: 28 positions", "Colorado: 3 positions", "California: 2 positions", "Massachusetts: 2 positions", "Washington: 2 positions"]
        elif selected_major == "Chemical Engineering":
            states = ["Michigan: 40 positions", "Wisconsin: 4 positions", "California: 4 positions", "Illinois: 3 positions", "Iowa: 3 positions"]
        elif selected_major == "Civil Engineering":
            states = ["Michigan: 21 positions", "Illinois: 6 positions", "California: 3 positions", "Maryland: 2 positions", "Texas: 2 positions"]
        elif selected_major == "Computational Data Science":
            states = ["Michigan: 3 positions"]
        elif selected_major == "Computer Engineering":
            states = ["Michigan: 14 positions", "Texas: 3 positions", "Wisconsin: 3 positions", "Florida: 2 positions", "Washington: 2 positions"]
        elif selected_major == "Computer Science":
            states = ["Michigan: 85 positions", "California: 9 positions", "Minnesota: 7 positions", "Texas: 7 positions", "Illinois: 6 positions"]
        elif selected_major == "Electrical Engineering":
            states = ["Michigan: 33 positions", "Illinois: 5 positions", "Indiana: 3 positions", "Texas: 3 positions", "Wisconsin: 3 positions"]
        elif selected_major == "Environmental Engineering":
            states = ["Michigan: 9 positions", "California: 2 positions"]
        elif selected_major == "Materials Science & Engineering":
            states = ["Michigan: 11 positions", "Ohio: 2 positions"]
        elif selected_major == "Mechanical Engineering":
            states = ["Michigan: 84 positions", "Illinois: 10 positions", "Texas: 7 positions", "Ohio: 4 positions", "Indiana: 3 positions"]
        else:
            states = []
    if year == "2021":
        if selected_major == "All Engineering Majors":
            states = ["Michigan: 293 positions", "Illinois: 37 positions", "Wisconsin: 21 positions", "Indiana: 17 positions", "California: 14 positions"]
        elif selected_major == "Applied Engineering Sciences":
            states = ["Michigan: 19 positions", "Illinois: 12 positions", "New York: 3 positions", "Ohio: 3 positions", "California: 2 positions"]
        elif selected_major == "Biosystems Engineering":
            states = ["Michigan: 19 positions", "Wisconsin: 4 positions", "Oregon: 2 positions", "Pennsylvania: 2 positions"]
        elif selected_major == "Chemical Engineering":
            states = ["Michigan: 31 positions", "Wisconsin: 9 positions", "Indiana: 5 positions", "Illinois: 3 positions", "California: 2 positions"]
        elif selected_major == "Civil Engineering":
            states = ["Michigan: 25 positions"]
        elif selected_major == "Computer Engineering":
            states = ["Michigan: 16 positions", "California: 2 positions"]
        elif selected_major == "Computer Science":
            states = ["Michigan: 63 positions", "Illinois: 15 positions", "Washington: 7 positions", "Minnesota: 3 positions", "Texas: 3 positions"]
        elif selected_major == "Electrical Engineering":
            states = ["Michigan: 28 positions", "Ohio: 3 positions", "California: 2 positions", "Illinois: 2 positions", "Indiana: 2 positions"]
        elif selected_major == "Environmental Engineering":
            states = ["Michigan: 13 positions"]
        elif selected_major == "Materials Science & Engineering":
            states = ["Michigan: 8 positions"]
        elif selected_major == "Mechanical Engineering":
            states = ["Michigan: 71 positions", "Indiana: 5 positions", "Wisconsin: 5 positions", "California: 3 positions", "Alabama: 2 positions"]
        else:
            states = []
    if year == "Cumulative Data 21-23: Key Stats":
        if selected_major == "All Engineering Majors":
            states = ["Michigan: 1319 positions", "Illinois: 156 positions", "Texas: 78 positions", "California: 67 positions", "Ohio: 64 positions"]
        elif selected_major == "Applied Engineering Sciences":
            states = ["Michigan: 81 positions", "Illinois: 40 positions", "Texas: 11 positions", "Ohio: 10 positions", "California: 8 positions"]
        elif selected_major == "Biosystems Engineering":
            states = ["Michigan: 82 positions", "Wisconsin: 8 positions", "California: 5 positions", "Illinois: 5 positions", "Iowa: 4 positions"]
        elif selected_major == "Chemical Engineering":
            states = ["Michigan: 132 positions", "Wisconsin: 19 positions", "Indiana: 14 positions", "Illinois: 11 positions", "Ohio: 11 positions"]
        elif selected_major == "Civil Engineering":
            states = ["Michigan: 109 positions", "Illinois: 9 positions", "Texas: 7 positions", "New York: 6 positions", "California: 3 positions"]
        elif selected_major == "Computational Data Science":
            states = ["Michigan: 11 positions", "Texas: 3 positions", "Ohio: 2 positions"]
        elif selected_major == "Computer Engineering":
            states = ["Michigan: 56 positions", "California: 4 positions", "Illinois: 4 positions", "Texas: 4 positions", "Wisconsin: 4 positions"]
        elif selected_major == "Computer Science":
            states = ["Michigan: 311 positions", "Illinois: 47 positions", "Washington: 23 positions", "California: 20 positions", "Texas: 20 positions"]
        elif selected_major == "Electrical Engineering":
            states = ["Michigan: 126 positions", "Illinois: 12 positions", "Texas: 8 positions", "Indiana: 6 positions", "Wisconsin: 6 positions"]
        elif selected_major == "Environmental Engineering":
            states = ["Michigan: 50 positions", "California: 3 positions", "North Carolina: 2 positions", "Ohio: 2 positions", "Texas: 2 positions"]
        elif selected_major == "Materials Science & Engineering":
            states = ["Michigan: 28 positions", "Ohio: 5 positions", "Illinois: 2 positions", "Pennsylvania: 2 positions", "Texas: 2 positions"]
        elif selected_major == "Mechanical Engineering":
            states = ["Michigan: 333 positions", "Illinois: 21 positions", "Indiana: 18 positions", "Ohio: 15 positions", "Texas: 15 positions"]
        else:
            states = []

    if not states:
        states = ["No data available for the selected year and major."]
    
    st.subheader("Top 5 States")
    for i, state in enumerate(states, start=1):
        st.write(f"{i}. {state}")

def display_top_5_cities(year, selected_major):
    if year == "2023":
        if selected_major == "All Engineering Majors":
            michigan_cities = ["Detroit: 57 positions", "Lansing: 13 positions", "Ann Arbor: 10 positions", "Grand Rapids: 8 positions", "Jackson: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 6 positions", "Indianapolis, IN: 4 positions", "Boston, MA: 3 positions", "Orlando, FL: 3 positions", "Berkeley, CA: 2 positions"]
        elif selected_major == "Applied Engineering Sciences":
            michigan_cities = ["Detroit: 18 positions", "Grand Rapids: 5 positions", "Lansing: 4 positions", "Ann Arbor: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 13 positions", "Phoenix, AZ: 2 positions", "Toledo, OH: 2 positions"]
        elif selected_major == "Biosystems Engineering":
            michigan_cities = ["Detroit: 9 positions", "Grand Rapids: 4 positions", "Lansing: 4 positions"]
            non_michigan_cities = ["Madison, WI: 2 positions", "Minneapolis, MN: 2 positions", "Modesto, CA: 2 positions"]
        elif selected_major == "Chemical Engineering":
            michigan_cities = ["Detroit: 15 positions", "Ann Arbor: 7 positions", "Lansing: 7 positions", "Grand Rapids: 4 positions", "Saginaw: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 8 positions", "Atlanta, GA: 2 positions", "Boston, MA: 2 positions", "Cleveland, OH: 2 positions", "Indianapolis, IN: 2 positions"]
        elif selected_major == "Civil Engineering":
            michigan_cities = ["Detroit: 14 positions", "Lansing: 12 positions", "Grand Rapids: 6 positions"]
            non_michigan_cities = ["Dallas, TX: 3 positions", "Denver, CO: 2 positions", "New York, NY: 2 positions"]
        elif selected_major == "Computational Data Science":
            michigan_cities = ["Detroit: 4 positions", "Lansing: 2 positions"]
            non_michigan_cities = []
        elif selected_major == "Computer Engineering":
            michigan_cities = ["Detroit: 9 positions", "Lansing: 3 positions"]
            non_michigan_cities = []
        elif selected_major == "Computer Science":
            michigan_cities = ["Lansing: 42 positions", "Detroit: 33 positions", "Ann Arbor: 2 positions", "Grand Rapids: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 8 positions", "Seattle, WA: 6 positions", "New York, NY: 4 positions", "Washington, DC: 4 positions", "Madison, WI: 3 positions"]
        elif selected_major == "Electrical Engineering":
            michigan_cities = ["Detroit: 16 positions", "Lansing: 8 positions", "Grand Rapids: 6 positions", "Jackson: 2 positions", "Saginaw: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 3 positions", "Atlanta, GA: 2 positions", "Austin, TX: 2 positions"]
        elif selected_major == "Environmental Engineering":
            michigan_cities = ["Detroit: 4 positions", "Lansing: 4 positions"]
            non_michigan_cities = []
        elif selected_major == "Materials Science & Engineering":
            michigan_cities = ["Detroit: 3 positions"]
            non_michigan_cities = []
        elif selected_major == "Mechanical Engineering":
            michigan_cities = ["Detroit: 57 positions", "Lansing: 13 positions", "Ann Arbor: 10 positions", "Grand Rapids: 8 positions", "Jackson: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 6 positions", "Indianapolis, IN: 4 positions", "Boston, MA: 3 positions", "Orlando, FL: 3 positions", "Berkeley, CA: 2 positions"]
        else:
            michigan_cities = []
            non_michigan_cities = []
    if year == "2022":
        if selected_major == "All Engineering Majors":
            michigan_cities = ["Detroit: 164 positions", "Lansing: 75 positions", "Grand Rapids: 36 positions", "Ann Arbor: 31 positions", "Kalamazoo: 18 positions"]
            non_michigan_cities = ["Chicago, IL: 29 positions", "Dallas, TX: 12 positions", "Madison, WI: 10 positions", "Minneapolis, MN: 10 positions", "Austin, TX: 8 positions"]
        elif selected_major == "Applied Engineering Sciences":
            michigan_cities = ["Detroit: 13 positions", "Lansing: 3 positions"]
            non_michigan_cities = ["Chicago, IL: 5 positions", "Dallas, TX: 3 positions", "Fort Worth, TX: 2 positions", "Nashville, TX: 2 positions", "Phoenix, AZ: 2 positions"]
        elif selected_major == "Biosystems Engineering":
            michigan_cities = ["Lansing: 8 positions", "Detroit: 7 positions", "Kalamazoo: 5 positions", "Grand Rapids: 3 positions", "Benton Harbor: 2 positions"]
            non_michigan_cities = ["Denver, CO: 3 positions", "Boston, MA: 2 positions"]
        elif selected_major == "Chemical Engineering":
            michigan_cities = ["Detroit: 12 positions", "Kalamazoo: 8 positions", "Lansing: 7 positions", "Midland: 4 positions", "Jackson: 3 positions"]
            non_michigan_cities = ["Cleveland, OH: 2 positions", "Indianapolis, IN: 2 positions", "Madison, WI: 2 positions"]
        elif selected_major == "Civil Engineering":
            michigan_cities = ["Detroit: 8 positions", "Lansing: 7 positions", "Grand Rapids: 3 positions", "Ann Arbor: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 5 positions"]
        elif selected_major == "Computational Data Science":
            michigan_cities = ["Detroit: 3 positions"]
            non_michigan_cities = []
        elif selected_major == "Computer Engineering":
            michigan_cities = ["Detroit: 6 positions", "Lansing: 5 positions", "Grand Rapids: 2 positions"]
            non_michigan_cities = ["Austin, TX: 2 positions", "Madison, WI: 2 positions", "Seattle, WA: 2 positions"]
        elif selected_major == "Computer Science":
            michigan_cities = ["Detroit: 40 positions", "Lansing: 21 positions", "Grand Rapids: 12 positions", "Ann Arbor: 9 positions"]
            non_michigan_cities = ["Minneapolis, MN: 7 positions", "New York, NY: 6 positions", "Chicago, IL: 5 positions", "San Francisco, CA: 4 positions", "Seattle, WA: 4 positions"]
        elif selected_major == "Electrical Engineering":
            michigan_cities = ["Detroit: 15 positions", "Ann Arbor: 7 positions", "Lansing: 5 positions", "Kalamazoo: 3 positions", "Grand Rapids: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 4 positions", "Indianapolis, IN: 3 positions", "Dallas, TX: 2 positions", "Milwaukee, WI: 2 positions"]
        elif selected_major == "Environmental Engineering":
            michigan_cities = ["Detroit: 4 positions", "Lansing: 3 positions", "Grand Rapids: 2 positions"]
            non_michigan_cities = []
        elif selected_major == "Materials Science & Engineering":
            michigan_cities = ["Detroit: 4 positions", "Lansing: 3 positions", "Grand Rapids: 2 positions"]
            non_michigan_cities = []
        elif selected_major == "Mechanical Engineering":
            michigan_cities = ["Detroit: 52 positions", "Lansing: 13 positions", "Ann Arbor: 9 positions", "Grand Rapids: 7 positions"]
            non_michigan_cities = ["Chicago, IL: 7 positions", "Cincinnati, OH: 3 positions", "Peoria, IL: 3 positions", "Atlanta, GA: 2 positions", "Indianapolis, IN: 2 positions"]
        else:
            michigan_cities = []
            non_michigan_cities = []
    if year == "2021":
        if selected_major == "All Engineering Majors":
            michigan_cities = ["Detroit: 143 positions", "Lansing: 75 positions", "Grand Rapids: 25 positions", "Ann Arbor: 14 positions", "Kalamazoo: 11 positions"]
            non_michigan_cities = ["Chicago, CA: 36 positions", "Madison, WI: 16 positions", "Minneapolis, MN: 8 positions", "Portland, OR: 8 positions", "Seattle, WA: 7 positions"]
        elif selected_major == "Applied Engineering Sciences":
            michigan_cities = ["Detroit: 9 positions", "Grand Rapids: 4 positions", "Lansing: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 12 positions", "Charlotte, NC: 2 positions", "Columbus, OH: 2 positions", "Portland, OR: 2 positions"]
        elif selected_major == "Biosystems Engineering":
            michigan_cities = ["Lansing: 10 positions", "Detroit: 3 positions", "Kalamazoo: 3 positions", "Grand Rapids: 2 positions"]
            non_michigan_cities = ["Madison, WI: 3 positions", "Philadelphia, PA: 2 positions"]
        elif selected_major == "Chemical Engineering":
            michigan_cities = ["Detroit: 13 positions", "Ann Arbor: 4 positions", "Grand Rapids: 4 positions", "Kalamazoo: 3 positions", "Lansing: 2 positions"]
            non_michigan_cities = ["Madison, WI: 8 positions", "Indianapolis, IN: 3 positions", "Chicago, IL: 2 positions"]
        elif selected_major == "Civil Engineering":
            michigan_cities = ["Detroit: 12 positions", "Lansing: 8 positions", "Jackson: 2 positions"]
        elif selected_major == "Computer Engineering":
            michigan_cities = ["Lansing: 8 positions", "Detroit: 7 positions"]
            non_michigan_cities = ["San Francisco, CA: 2 positions"]
        elif selected_major == "Computer Science":
            michigan_cities = ["Detroit: 37 positions", "Lansing: 17 positions", "Grand Rapids: 6 positions", "Ann Arbor: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 14 positions", "Seattle, WA: 6 positions", "Austin, TX: 3 positions", "Minneapolis, MN: 3 positions", "Los Angeles, CA: 2 positions"]
        elif selected_major == "Electrical Engineering":
            michigan_cities = ["Detroit: 14 positions", "Lansing: 9 positions", "Jackson: 3 positions"]
            non_michigan_cities = ["Chicago, IL: 3 positions", "Alexandria, VA: 2 positions"]
        elif selected_major == "Environmental Engineering":
            michigan_cities = ["Detroit: 6 positions", "Lansing: 3 positions", "Grand Rapids: 2 positions"]
            non_michigan_cities = []
        elif selected_major == "Materials Science & Engineering":
            michigan_cities = ["Detroit: 5 positions"]
            non_michigan_cities = []
        elif selected_major == "Mechanical Engineering":
            michigan_cities = ["Detroit: 37 positions", "Lansing: 15 positions", "Grand Rapids: 5 positions", "Ann Arbor: 4 positions", "Kalamazoo: 3 positions"]
            non_michigan_cities = ["Chicago, IL: 3 positions", "Madison, WI: 3 positions", "Indianapolis, IN: 2 positions", "Minneapolis, MN: 2 positions"]
        else:
            michigan_cities = []
            non_michigan_cities = []
    if year == "Cumulative Data 21-23: Key Stats":
        if selected_major == "All Engineering Majors":
            michigan_cities = ["Detroit: 633 positions", "Lansing: 347 positions", "Grand Rapids: 106 positions", "Ann Arbor: 96 positions", "Kalamazoo: 31 positions"]
            non_michigan_cities = ["Chicago, IL: 142 positions", "Madison, WI: 39 positions", "Seattle, WA: 30 positions", "Minneapolis, MN: 28 positions", "Dallas, TX: 26 positions"]
        elif selected_major == "Applied Engineering Sciences":
            michigan_cities = ["Detroit: 51 positions", "Grand Rapids: 10 positions", "Lansing: 9 positions", "Ann Arbor: 5 positions"]
            non_michigan_cities = ["Chicago, IL: 39 positions", "Dallas, TX: 4 positions", "Phoenix, AZ: 4 positions", "Los Angeles, CA: 4 positions", "Cincinnati, OH: 3 positions"]
        elif selected_major == "Biosystems Engineering":
            michigan_cities = ["Detroit: 30 positions", "Lansing: 25 positions", "Grand Rapids: 9 positions", "Kalamazoo: 8 positions", "Ann Arbor: 2 positions"]
            non_michigan_cities = ["Madison, WI: 6 positions", "Chicago, IL: 4 positions", "Denver, CO: 3 positions", "Minneapolis, MN: 3 positions", "Boston, MA: 2 positions"]
        elif selected_major == "Chemical Engineering":
            michigan_cities = ["Detroit: 49 positions", "Lansing: 20 positions", "Kalamazoo: 14 positions", "Ann Arbor: 12 positions", "Grand Rapids: 11 positions"]
            non_michigan_cities = ["Madison, WI: 13 positions", "Chicago, IL: 12 positions", "Indianapolis, IN: 7 positions", "Cleveland, OH: 4 positions", "Atlanta, GA: 4 positions"]
        elif selected_major == "Civil Engineering":
            michigan_cities = ["Detroit: 44 positions", "Lansing: 39 positions", "Grand Rapids: 11 positions", "Ann Arbor: 5 positions", "Jackson: 3 positions"]
            non_michigan_cities = ["Chicago, IL: 8 positions", "Dallas, TX: 5 positions", "New York, NY: 4 positions"]
        elif selected_major == "Computational Data Science":
            michigan_cities = ["Detroit: 7 positions", "Lansing: 4 positions"]
            non_michigan_cities = ["Columbus, OH: 2 positions", "Austin, TX: 2 positions"]
        elif selected_major == "Computer Engineering":
            michigan_cities = ["Detroit: 25 positions", "Lansing: 24 positions", "Grand Rapids: 3 positions"]
            non_michigan_cities = ["San Francisco, CA: 4 positions", "Baltimore, MD: 3 positions", "Chicago, IL: 3 positions", "Madison, WI: 3 positions", "Austin, TX: 2 positions"]
        elif selected_major == "Computer Science":
            michigan_cities = ["Detroit: 145 positions", "Lansing: 114 positions", "Grand Rapids: 23 positions", "Ann Arbor: 21 positions", "Kalamazoo: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 43 positions", "Seattle, WA: 22 positions", "Minneapolis, MN: 12 positions", "New York, NY: 12 positions", "Austin, TX: 8 positions"]
        elif selected_major == "Electrical Engineering":
            michigan_cities = ["Detroit: 55 positions", "Lansing: 29 positions", "Ann Arbor: 16 positions", "Grand Rapids: 9 positions", "Jackson: 7 positions"]
            non_michigan_cities = ["Chicago, IL: 12 positions", "Dallas, TX: 4 positions", "Milwaukee, WI: 4 positions", "Indianapolis, IN: 3 positions", "Minneapolis, MN: 3 positions"]
        elif selected_major == "Environmental Engineering":
            michigan_cities = ["Detroit: 23 positions", "Lansing: 16 positions", "Grand Rapids: 6 positions", "Ann Arbor: 2 positions"]
            non_michigan_cities = ["Charlotte, NC: 2 positions"]
        elif selected_major == "Materials Science & Engineering":
            michigan_cities = ["Detroit: 13 positions", "Lansing: 7 positons", "Grand Rapids: 3 positions"]
            non_michigan_cities = ["Cleveland, OH: 2 positions"]
        elif selected_major == "Mechanical Engineering":
            michigan_cities = ["Detroit: 196 positions", "Lansing: 54 positions", "Ann Arbor: 30 positions", "Grand Rapids: 21 positions", "Kalamazoo: 6 positions"]
            non_michigan_cities = ["Chicago, IL: 18 positions", "Indianapolis, IN: 10 positions", "Madison, WI: 7 positions", "Cincinnati, OH: 7 positions", "Boston, MA: 6 positions"]
        else:
            michigan_cities = []
            non_michigan_cities = []

    st.subheader("Top 5 Michigan Cities")
    for i, city in enumerate(michigan_cities, start=1):
        st.write(f"{i}. {city}")

    st.subheader("Top 5 Non-Michigan Cities")
    for i, city in enumerate(non_michigan_cities, start=1):
        st.write(f"{i}. {city}")
        
AllEthnicity = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'Not Reported','American Indian/Alaskan Native']
Major2024 = [52,32,8,46,58,27,207,48,28,158,14]
Major2022 = [57, 50, 7, 51, 91, 42, 193, 60, 20, 164, 23]
InverseGender = ['#C70F0F', '#0B1799']
Major2021 = [72, 47, 44, 100, 42, 173, 67, 24, 155, 22]
MajorList2021 = ["Applied Engineering Sciences", "Biosystems Engineering", "Civil Engineering" , "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Mechanical Engineering", "Materials Science & Engineering"]
Major2123 = [207, 141, 21, 153, 286, 108, 593, 203, 61, 490, 61]

def main():  
    col1, col2 = st.columns([2,3]) 
    with col1:
        options = ("Cumulative Data 21-23: Key Stats", "2024", "2023", "2022", "2021")
        ms1 = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Year", default=["2023"], label_visibility="visible")

    with col2:
        if ms1 == ["2021"]:
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
        else:
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
        ms = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major",  default=["All Engineering Majors"], label_visibility="hidden")

    if ["All Engineering Majors"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "86.9%", krinfo = "589/678", pr = "77.1%", prinfo = "454/589", avgsal = "$78,032", medsal = "$75,500", employ = "77.1%", grad = "13%", vol = "Less than 1%", other = 0)
                st.caption("Note: 0.1% of graduates indicate “other intentions” - placed and not seeking")
                st.header("Spring 2024 Graduating Class Composition: All Engineering Majors")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    data_major([],Major2024)
                with t2:
                    AllEthnicity2024 = ['White', 'Asian', 'International', 'Not Specified', 'Black/African American','Hispanic/Latine', 'Two or More Races']
                    AllCount2024 = [455, 73, 51, 30, 25, 22, 22]
                    data_ethnicity(AllCount2024, AllEthnicity2024)
                with t3:
                    AllGender2024 = [493, 185]
                    data_gender(AllGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "All Engineering Majors", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "All Engineering Majors")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "2024")
                    display_top_5_cities("2024", "All Engineering Majors")

        elif ["2023"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats()
                st.caption("Note: 0.8% of graduates indicate “other intentions” - placed and not seeking")
                st.header("Spring 2023 Graduating Class Composition: All Engineering Majors")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    data_major()
                with t2:
                    AllEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'American Indian/Alaskan Native']
                    AllCount2023 = [552, 89, 86, 35, 29, 18, 10, 1]
                    data_ethnicity(AllCount2023, AllEthnicity2023)
                with t3:
                    AllGender2023 = [625, 195]
                    data_gender(AllGender2023)
            with tab2:
                st.image("2023 (1).jpg")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "All Engineering Majors")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2023", "All Engineering Majors")
                with t2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(All Majors).csv", "2023")
                    display_top_5_cities("2023", "All Engineering Majors")
        elif ["2022"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats("2022", "82.5%", "625/758", "98%", "612/625", "$73,922", "$72,500", "82.9%", "14.6%", "0.2%")
                st.caption("Note: 0.3% of graduates indicate “other intentions” - placed and not seeking")
                st.header("Spring 2022 Graduating Class Composition: All Engineering Majors")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    data_major([], Major2022)
                with t2:
                    AllCount2022 = [532, 72, 77, 23, 14, 25, 12, 1, 2]
                    data_ethnicity(AllCount2022, AllEthnicity)
                with t3:
                    AllGender2022 = [541, 217]
                    data_gender(AllGender2022)
            with tab2:
                st.image("2022 (1).jpg")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "All Engineering Majors")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "All Engineering Majors")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "2022")
                    display_top_5_cities("2022", "All Engineering Majors")
        elif ["2021"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2021", kr = "80.3%", krinfo = "599/746", pr = "96%", prinfo = "575/599", avgsal = "$69,838", medsal = "$70,000", employ = "82%", grad = "13.5%", vol = "0.5%")
                st.header("Spring 2021 Graduating Class Composition: All Engineering Majors")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    data_major([], Major2021, MajorList2021)
                with t2:
                    AllCount2021 = [523, 73, 19, 1, 19, 83, 2, 1, 25]
                    AllEthnicity2021 = ["White", "Asian", "Black/African American", "Hawaiian/Pacific Islander", "Hispanic/Latine", "International", "Not Reported", "Not Specified", "Two or More Races"]
                    data_ethnicity(AllCount2021, AllEthnicity2021)
                with t3:
                    AllGender2021 = [556, 190]
                    data_gender(AllGender2021)
            with tab2:
                st.image("2021 (1).jpg")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv","All Engineering Majors")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig)   
                    top_5_employer_states("2021", "All Engineering Majors")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "2021")
                    display_top_5_cities("2021", "All Engineering Majors")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('80.3%', '82.5%', '90.5%', '84.4%', '96.0%', '98.0%','94.3%', '96.1%', '69,838', '73,922', '76,806', '73,522', '70,000','72,500', '75,000', '72,500')
            with t2:
                st.image("FT (1).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "All Engineering Majors")
                    st.header('Interactive Map for Destination Data: College of Engineering')
                    st.plotly_chart(fig) 
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "All Engineering Majors")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024.csv")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "All Engineering Majors")

    elif ["Applied Engineering Sciences"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "81%", krinfo = "42/52", pr = "90%", prinfo = "38/42", avgsal = "$75,042", medsal = "$78,750", employ = "81%", grad = "7%", vol = 0, other = 0)
                st.caption("Note: 2% of graduates indicate “other intentions” - placed and not seeking")
                st.header("Spring 2024 Graduating Class Composition: AES Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    AESColors = ['#CECECE', '#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                    data_major(AESColors,Major2024)
                with t2:
                    AESEthnicity2024 = ['White', 'Asian', 'Black/African American', 'Two or More Races']
                    AESCount2024 = [42,5,3,2]
                    data_ethnicity(AESCount2024, AESEthnicity2024)
                with t3:
                    AllGender2024 = [36, 16]
                    data_gender(AllGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv(Applied Engineering Sciences)", "Applied Engineering Sciences", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Applied Engineering Sciences")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Applied Engineering Sciences).csv", "2024")
                    display_top_5_cities("2024", "Applied Engineering Sciences")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (2).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Applied Engineering Sciences")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Applied Engineering Sciences")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Applied Engineering Sciences).csv", "2023")
                    display_top_5_cities("2023", "Applied Engineering Sciences")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (2).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Applied Engineering Sciences")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Applied Engineering Sciences")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Applied Engineering Sciences).csv", "2022")
                    display_top_5_cities("2022", "Applied Engineering Sciences")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (2).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Applied Engineering Sciences")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2021", "Applied Engineering Sciences")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Applied Engineering Sciences).csv", "2021")
                    display_top_5_cities("2021", "Applied Engineering Sciences")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('88%', '81%', '100%', '90%', '100%', '100%', '92%','97%', '66,697', '67,579', '72,233', '68,836', '65,000', '70,000','70,000', '68,333')
            with t2:
                st.image("FT (2).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "All Engineering Majors")
                    st.header('Interactive Map for Destination Data: College of Engineering')
                    st.plotly_chart(fig) 
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "All Engineering Majors")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024.csv")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "All Engineering Majors")
    
    elif ["Biosystems Engineering"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "86.9%", krinfo = "29/32", pr = "83%", prinfo = "24/29", avgsal = "$72,545", medsal = "$70,000", employ = "52%", grad = "28%", vol = "3%", other = 0)
                st.header("Spring 2024 Graduating Class Composition: BE Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    BEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#18453B', '#CECECE','#CECECE','#CECECE','#CECECE']
                    data_major(BEColors,Major2024)
                with t2:
                    BEEthnicity2024 = ['White','Two or More Races','Asian', 'Not Specified','Black/African American','Hispanic/Latine']
                    BEECount2024 = [26,2,1,1,1,1]
                    data_ethnicity(BEECount2024,BEEthnicity2024)
                with t3:
                    BEGender2024 = [12,20]
                    data_gender(BEGender2024, InverseGender)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Biosystems Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Biosystems Engineering")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Biosystems Engineering).csv", "2024")
                    display_top_5_cities("2024", "All Engineering Majors")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (3).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Biosystems Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Biosystems Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Biosystems Engineering).csv", "2023")
                    display_top_5_cities("2023", "Biosystems Engineering")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (3).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Biosystems Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Biosystems Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Biosystems Engineering).csv", "2022")
                    display_top_5_cities("2022", "Biosystems Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (3).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Biosystems Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2021", "Biosystems Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Biosystems Engineering).csv", "2021") 
                    display_top_5_cities("2021", "Biosystems Engineering")          
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('87%', '100%', '93%', '93%', '87%', '94%', '93%', '91%',
                            '58,792', '64,547', '68,768', '64,036', '56,160', '64,500', '72,500', '64,387')
            with t2:
                st.image("FT (3).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Biosystems Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig) 
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Biosystems Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: BE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Biosystems Engineering).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Biosystems Engineering")

    elif ["Chemical Engineering"] == ms:
        if ["2024"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                key_stats("2024", "88%", "51/58", "86%", prinfo = "44/51", avgsal = "$75,907", medsal = "$78,000", employ = "80%", grad = "6%")
                st.header("Spring 2024 Graduating Class Composition: ChemE Major")
                tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with tab1:
                    ChemEColors = ['#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                    data_major(ChemEColors, Major2024)
                with tab2:
                    ChemEEthnicity2024 = ['White', "Black/African American",'Asian', 'Hispanic/Latine', 'Not Specified', "International"]
                    ChemECount2024 = [46,4,2,3,2,1]
                    data_ethnicity(ChemECount2024, ChemEEthnicity2024)
                with tab3:
                    ChemEGender2024 = [35, 23]
                    data_gender(ChemEGender2024)
            with t2:
                st.write("insert graphic")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Chemical Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Chemical Engineering")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Chemical Engineering).csv", "2024")
                    display_top_5_cities("2024", "Chemical Engineering")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (4).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Chemical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2021", "Chemical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Chemical Engineering).csv", "2023")
                    display_top_5_cities("2021", "Chemical Engineering")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (4).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Chemical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Chemical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Chemical Engineering).csv", "2022")
                    display_top_5_cities("2022", "Chemical Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (4).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Chemical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2021", "Chemical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Chemical Engineering).csv", "2021") 
                    display_top_5_cities("2021", "Chemical Engineering")            
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('83%', '82%', '95%', '87%', '94%', '97%', '98%', '96%','69,604', '71,561', '77,315', '72,827', '70,000', '72,500', '76,000', '72,833')
            with t2:
                st.image("FT (4).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Chemical Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Chemical Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: ChemE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Chemical Engineering).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Chemical Engineering")
                 
    elif ["Civil Engineering"] == ms:
        if ["2024"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                key_stats("2024", "91%", "42/46", "100%", prinfo = "42/42", avgsal = "$69,441", medsal = "$70,000", employ = "76%", grad = "24%")
                st.header("Spring 2024 Graduating Class Composition: CE Major")
                tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with tab1:
                    CEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                    data_major(CEColors, Major2024)
                with tab2:
                    CEEthnicity2024 = ['White', "Black/African American",'Asian', 'Not Specified', "Two or More Races", 'Hispanic/Latine']
                    CECount2024 = [35,4,2,2,2,1]
                    data_ethnicity(CECount2024, CEEthnicity2024)
                with tab3:
                    CEGender2024 = [29, 17]
                    data_gender(CEGender2024)
            with t2:
                st.write("insert graphic")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Civil Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Civil Engineering")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Civil Engineering).csv", "2024")
                    display_top_5_cities("2024", "Civil Engineering")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (5).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Civil Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Civil Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Civil Engineering).csv", "2023")
                    display_top_5_cities("2023", "Civil Engineering")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (5).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Civil Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Civil Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Civil Engineering).csv", "2022")
                    display_top_5_cities("2022", "Civil Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (5).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Civil Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2021", "Civil Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Civil Engineering).csv", "2021")
                    display_top_5_cities("2021", "Civil Engineering")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('75%', '76%', '95%', '82%', '97%', '95%', '96%', '96%','58,612', '66,729', '65,895', '63,745', '55,640', '67,800', '65,000', '62,813')
            with t2:
                st.image("FT (5).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Civil Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("LATLONGDestinationCumulativeDataset(Civil Engineering).csv", "Civil Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: CE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Civil Engineering).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Civil Engineering")

    elif ["Computational Data Science"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "88%", krinfo = "7/8", pr = "100%", prinfo = "7/7", avgsal = "$78,000", medsal = "$70,000", employ = "100%", grad = 0)
                st.header("Spring 2024 Graduating Class Composition: CDS Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    CDSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE',
                    '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#18453B']  
                    data_major(CDSColors, Major2024)
                with t2:
                    CDSEthnicity2024 = ['White', 'Asian', 'Hispanic/Latine', 'International', 'Not Specified', 'Two or More Races']
                    CDSCount2024 = [3,1,1,1,1,1]
                    data_ethnicity(CDSCount2024, CDSEthnicity2024)
                with t3:
                    CDSGender2024 = [4, 4]
                    data_gender(CDSGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Computational Data Science", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Computational Data Science")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Computational Data Science).csv", "2024")
                    display_top_5_cities("2024", "Computational Data Science")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (6).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Computational Data Science")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Computational Data Science")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computational Data Science).csv", "2023")
                    display_top_5_cities("2023", "Computational Data Science")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (6).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Computational Data Science")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Computational Data Science")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computational Data Science).csv", "2022")
                    display_top_5_cities("2022", "Computational Data Science")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats(0, '86%', '93%', '90%', 0, '100%', '92%', '96%', 0, '70,333', '91,357', '80,845', 0, '75,000', '95,000', '85,000', "Two") 
            with t2:
                st.image("FT (6).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Computational Data Science")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig) 
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Computational Data Science")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: CDS Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computational Data Science).csv", "Computational Data Science")

    elif ["Computer Engineering"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "93%", krinfo = "25/27", pr = "88%", prinfo = "22/25", avgsal = "$89,686", medsal = "$88,000", employ = "64%", grad = "24%")
                st.header("Spring 2024 Graduating Class Composition: CpE Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    CpEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#18453B','#CECECE','#CECECE']  
                    data_major(CpEColors, Major2024)
                with t2:
                    CpEEthnicity2024 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Not Specified']
                    CpECount2024 = [14,7,4,1,1]
                    data_ethnicity(CpECount2024, CpEEthnicity2024)
                with t3:
                    CpEGender2024 = [22, 5]
                    data_gender(CpEGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Computer Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Computer Engineering")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Computer Engineering).csv", "2024")
                    display_top_5_cities("2024", "Computer Engineering")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (7).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Computer Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Computer Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Engineering).csv", "2023")
                    display_top_5_cities("2023", "Computer Engineering")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (7).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Computer Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Computer Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Engineering).csv", "2022")
                    display_top_5_cities("2022", "Computer Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (7).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Computer Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2021", "Computer Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Engineering).csv", "2021")
                    display_top_5_cities("2021", "Computer Engineering")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('79%', '76%', '92%', '82%', '97%', '97%', '100%',	'98%', '81,500', '83,698', '80,112', '81,770','77,500',	'80,500',	'79,040', '79,013')      
            with t2:
                st.image("FT (7).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Computer Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)  
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Computer Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: CpE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Engineering).csv", "Cumulative Data 21-23: Key Stats")       
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Computer Engineering")                

    elif ["Computer Science"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "80%", krinfo = "166/207", pr = "89%", prinfo = "147/166", avgsal = "$87,721", medsal = "$85,000", employ = "79%", grad = "10%")
                st.header("Spring 2024 Graduating Class Composition: CSE Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    CSEColors = ['#18453B', '#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                    data_major(CSEColors, Major2024)
                with t2:
                    CSEEthnicity2024 = ['White', 'Asian', 'International','Not Specified', "Two or More Races", 'Hispanic/Latine', "Black/African American"]
                    CSECount2024 = [109,39,27,9,9,8,6]
                    data_ethnicity(CSECount2024, CSEEthnicity2024)
                with t3:
                    CSEGender2024 = [168, 39]
                    data_gender(CSEGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Computer Science", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Computer Science")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Computer Science).csv", "2024")
                    display_top_5_cities("2024", "Computer Science")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (8).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Computer Science")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Computer Science")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Science).csv", "2023")
                    display_top_5_cities("2023", "Computer Science")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (8).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Computer Science")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Computer Science")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Science).csv", "2022")
                    display_top_5_cities("2022", "Computer Science")   
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (8).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Computer Science")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2021", "Computer Science")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Science).csv", "2021")
                    display_top_5_cities("2021", "Computer Science")  
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('71%', '79%', '81%', '77%', '98%', '98%', '92%', '96%','76,365', '85,220', '89,826', '83,804', '75,000', '80,000', '85,000', '80,000') 
            with t2:
                st.image("FT (8).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Computer Science")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig) 
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Computer Science")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: CSE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computer Science).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Computer Science")
    
    elif ["Electrical Engineering"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "90%", krinfo = "43/48", pr = "89%", prinfo = "38/43", avgsal = "$76,890", medsal = "$80,000", employ = "70%", grad = "19%")
                st.header("Spring 2024 Graduating Class Composition: EE Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    EEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE', '#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                    data_major(EEColors, Major2024)
                with t2:
                    EEEthnicity2024 = ['White', 'Asian', 'Not Specified', 'International', 'Hispanic/Latine', "Black/African American", "Two or More Races"]
                    EECount2024 = [33,5,3,2,2,2,1]
                    data_ethnicity(EECount2024, EEEthnicity2024)
                with t3:
                    EEGender2024 = [39, 9]
                    data_gender(EEGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Electrical Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Electrical Engineering")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Electrical Engineering).csv", "2024")
                    display_top_5_cities("2024", "Electrical Engineering")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (9).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Electrical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Electrical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Electrical Engineering).csv", "2023")
                    display_top_5_cities("2023", "Electrical Engineering")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (9).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Electrical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Electrical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Electrical Engineering).csv", "2022")
                    display_top_5_cities("2022", "Electrical Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (9).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Electrical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2021", "Electrical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Electrical Engineering).csv", "2021")
                    display_top_5_cities("2021", "Electrical Engineering")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('85%', '83%', '93%', '87%', '95%', '100%', '96%', '97%', '73,322', '79,650', '76,512', '76,495', '75,000', '77,500', '79,500', '77,333')
            with t2:
                st.image("FT (9).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Electrical Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Electrical Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: EE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Electrical Engineering).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Electrical Engineering")
       
    elif ["Environmental Engineering"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "86%", krinfo = "24/28", pr = "100%", prinfo = "24/24", avgsal = "$68,060", medsal = "$68,000", employ = "83%", grad = "17%")
                st.header("Spring 2024 Graduating Class Composition: ENE Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    ENEColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE']
                    data_major(ENEColors, Major2024)
                with t2:
                    ENEEthnicity2024 = ['White',  "Black/African American", 'International', 'Not Specified', 'Hispanic/Latine', "Two or More Races"]
                    ENECount2024 = [20,2,2,2,1,1]
                    data_ethnicity(ENECount2024, ENEEthnicity2024)
                with t3:
                    ENEGender2024 = [8, 20]
                    data_gender(ENEGender2024, InverseGender)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Environmental Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Environmental Engineering")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Environmental Engineering).csv", "2024")
                    display_top_5_cities("2024", "Environmental Engineering")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (10).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Environmental Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Environmental Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Environmental Engineering).csv", "2023")
                    display_top_5_cities("2023", "Environmental Engineering")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (10).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Environmental Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Environmental Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Environmental Engineering).csv", "2022")
                    display_top_5_cities("2022", "Environmental Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (10).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Electrical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2021", "Environmental Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Environmental Engineering).csv", "2021")
                    display_top_5_cities("2021", "Environmental Engineering")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('71%', '90%', '94%', '85%', '94%', '100%', '94%', '96%','60,560', '63,697', '58,102', '60,786 ', '60,000', '62,400', '61,950', '61,450')
            with t2:
                st.image("FT (10).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Environmental Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Environmental Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: ENE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Environmental Engineering).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Environmental Engineering")
    
    elif ["Materials Science & Engineering"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "86%", krinfo = "12/14", pr = "100%", prinfo = "12/12", avgsal = "$69,333", medsal = "$72,500", employ = "75%", grad = "25%")
                st.header("Spring 2024 Graduating Class Composition: MS Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    MSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#CECECE', '#18453B', '#CECECE']
                    data_major(MSColors, Major2024)
                with t2:
                    MSEthnicity2024 = ['White', 'International',"Two or More Races"]
                    MSCount2024 = [12,1,1]
                    data_ethnicity(MSCount2024, MSEthnicity2024)
                with t3:
                    MSGender2024 = [10, 4]
                    data_gender(MSGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Materials Science & Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "All Engineering Majors")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Materials Science and Eng).csv", "2024")
                    display_top_5_cities("2024", "All Engineering Majors")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (11).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Materials Science and Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Materials Science & Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Materials Science and Eng).csv", "2023")
                    display_top_5_cities("2023", "Materials Science & Engineering")
        elif ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (11).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Materials Science and Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Materials Science & Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Materials Science and Eng).csv", "2022")
                    display_top_5_cities("2022", "Materials Science & Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (11).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Materials Science and Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2021", "Materials Science & Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Materials Science and Eng).csv", "2021")
                    display_top_5_cities("2021", "Materials Science & Engineering")  
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('82%', '87%', '94%', '88%', '94%', '95%', '93%', '94%', '63,581', '72,147', '70,447', '68,725', '60,320', '75,000', '72,500', '69,273')
            with t2:
                st.image("FT (11).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Materials Science and Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Materials Science & Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: MS Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Materials Science and Eng).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Materials Science & Engineering")
    
    elif ["Mechanical Engineering"] == ms:
        if ["2024"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats(year= "2024", kr = "94%", krinfo = "148/158", pr = "91%", prinfo = "136/148", avgsal = "$76,907", medsal = "$75,500", employ = "80%", grad = "10%")
                st.caption("Note: 1% of graduates indicate “other intentions” - placed and not seeking")
                st.header("Spring 2024 Graduating Class Composition: ME Major")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    MEColors = ['#CECECE', '#18453B', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
                    data_major(MEColors, Major2024)
                with t2:
                    MEEthnicity2024 = ['White', 'International','Asian', 'Not Specified', 'Black/African American', 'Hispanic/Latine', 'Two or More Races']
                    MECount2024 = [115,13,11,9,3,4,1]
                    data_ethnicity(MECount2024, MEEthnicity2024)
                with t3:
                    MEGender2024 = [130, 28]
                    data_gender(MEGender2024)
            with tab2:
                st.write("insert visualization")
            with tab3:
                t1, t2= st.tabs(["By State", "By City"])
                with t1:
                    fig = choropleth_state_map("LATLONGAnnual Cumulative Data Set_2021-2024.csv", "Mechanical Engineering", selected_year='2024')
                    st.header('Interactive Map for Destination Data: Spring 2024 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2024", "Mechanical Engineering")
                with t2:
                    display_city_visualization("LATLONGAnnual Cumulative Data Set_2021-2024(Mechanical Engineering).csv", "2024")
                    display_top_5_cities("2024", "Mechanical Engineering")
        elif ["2023"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2023 (12).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv", "Mechanical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2023", "Mechanical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Mechanical Engineering).csv", "2023")
                    display_top_5_cities("2023", "Mechanical Engineering")
        if ["2022"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2022 (12).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv", "Mechanical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2022", "Mechanical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Mechanical Engineering).csv", "2022")
                    display_top_5_cities("2022", "Mechanical Engineering")
        elif ["2021"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
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
            with t2:
                st.image("2021 (12).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "Mechanical Engineering")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                    top_5_employer_states("2021", "Mechanical Engineering")
                with tab2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Mechanical Engineering).csv", "2022")
                    display_top_5_cities("2021", "Mechanical Engineering")  
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('85%', '84%', '92%', '87%', '97%', '98%', '95%', '97%','69,674', '70,685', '75,069', '71,809', '71,000', '72,000', '74,500', '72,500')
            with t2:
                st.image("FT (12).jpg")
            with t3:
                tab1, tab2 = st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Mechanical Engineering")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Mechanical Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: ME Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Mechanical Engineering).csv", "Cumulative Data 21-23: Key Stats")    
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Mechanical Engineering")  
    


if __name__ == "__main__":

    main()
