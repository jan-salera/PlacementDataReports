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

def choropleth_state_map(file_path, selected_major):
    all_majors_data = pd.read_csv(file_path)
    
    if selected_major != "All Engineering Majors":
        filtered_data = all_majors_data[all_majors_data['Major'] == selected_major]
    else:
        filtered_data = all_majors_data
    
    state_counts = filtered_data['Employer State'].value_counts().reset_index()
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
    state_counts['LogCount'] = np.log1p(state_counts['Count'])
    
    fig = px.choropleth(
        state_counts,
        locations='StateAbbrev',
        locationmode='USA-states',
        color='LogCount',
        color_continuous_scale='Greens',
        labels={'LogCount': 'Log Count'},
        scope='usa',
        range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),
        hover_data={'State': True, 'Count': False, 'StateAbbrev': False, 'LogCount': False}
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

def display_city_visualization(file_path, selected_year):
    data = pd.read_csv(file_path)

    if 'Start Date' not in data.columns:
        st.error("Start Date column not found.")
        return
    
    # Convert 'Start Date' to datetime format and extract the year
    data['Year'] = pd.to_datetime(data['Start Date'], errors='coerce').dt.year

    # Filter data based on the selected year
    if selected_year in ["2021", "2022", "2023"]:
        data = data[data['Year'] == int(selected_year)]
    elif selected_year == "Cumulative Data 21-23: Key Stats":
        data = data[data['Year'].isin([2021, 2022, 2023])]
    else:
        st.error("Invalid year selection.")
        return

    if data.empty:
        st.warning("No data available for the selected year.")
        return

    if 'Employer Latitude' not in data.columns or 'Employer Longitude' not in data.columns:
        st.warning("Latitude and Longitude columns not found. Creating columns... This may take a moment.")
        add_lat_long_to_dataframe(data)
        data.to_csv(file_path, index=False)
        st.info("Updated CSV file with Latitude and Longitude columns. Please reload the app to visualize.")

    if 'Employer Latitude' in data.columns and 'Employer Longitude' in data.columns:
        city_counts = data.groupby('Employer City').size().reset_index(name='Graduate Count')
        data_merged = pd.merge(data, city_counts, on='Employer City', how='left')

        fig = px.scatter_geo(
            data_merged,
            lat='Employer Latitude',
            lon='Employer Longitude',
            hover_name='Employer City',
            hover_data={
                    'Employer City': True,
                    'Graduate Count': False,
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
            title=f"City Visualization ({selected_year})",
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
    else:
        st.error("Failed to create Latitude and Longitude columns. Please check your CSV file.")


def top_5_employer_states(year, selected_major):
    states = []
    if year == "2023":
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
            states = ["Michigan: 838 positions", "Illinois: 106 positions", "Texas: 62 positions", "Wisconsin: 51 positions", "Ohio: 47 positions"]
        elif selected_major == "Applied Engineering Sciences":
            states = ["Michigan: 64 positions", "Illinois: 30 positions", "Texas: 10 positions", "Ohio: 8 positions", "California: 7 positions"]
        elif selected_major == "Biosystems Engineering":
            states = ["Michigan: 47 positions", "Wisconsin: 7 positions", "California: 5 positions", "Illinois: 4 positions", "Arizona: 2 positions"]
        elif selected_major == "Chemical Engineering":
            states = ["Michigan: 97 positions", "Wisconsin: 16 positions", "Indiana: 11 positions", "Ohio: 11 positions", "Illinois: 10 positions"]
        elif selected_major == "Civil Engineering":
            states = ["Michigan: 69 positions", "Illinois: 8 positions", "Texas: 6 positions", "California: 3 positions", "Colorado: 2 positions"]
        elif selected_major == "Computational Data Science":
            states = ["Michigan: 8 positions", "Ohio: 2 positions"]
        elif selected_major == "Computer Engineering":
            states = ["Michigan: 31 positions", "Texas: 4 positions", "Arizona: 3 positions", "California: 3 positions", "Ohio: 3 positions"]
        elif selected_major == "Computer Science":
            states = ["Michigan: 186 positions", "Illinois: 26 positions", "Washington: 17 positions", "Texas: 15 positions", "Minnesota: 13 positions"]
        elif selected_major == "Electrical Engineering":
            states = ["Michigan: 77 positions", "Illinois: 8 positions", "Texas: 6 positions", "Indiana: 5 positions", "Wisconsin: 5 positions"]
        elif selected_major == "Environmental Engineering":
            states = ["Michigan: 28 positions", "California: 2 positions", "Ohio: 2 positions", "Texas: 2 positions"]
        elif selected_major == "Materials Science & Engineering":
            states = ["Michigan: 19 positions", "Ohio: 4 positions", "Pennsylvania: 2 positions", "Texas: 2 positions"]
        elif selected_major == "Mechanical Engineering":
            states = ["Michigan: 212 positions", "Illinois: 16 positions", "Indiana: 11 positions", "Wisconsin: 11 positions", "Texas: 10 positions"]
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
            michigan_cities = ["Detroit: 478 positions", "Lansing: 119 positions", "Grand Rapids: 92 positions", "Ann Arbor: 51 positions", "Kalamazoo: 30 positions"]
            non_michigan_cities = ["Chicago, IL: 98 positions", "Madison, WI: 34 positions", "Minneapolis, MN: 23 positions", "Seattle, WA: 22 positions", "Dallas, TX: 20 positions"]
        elif selected_major == "Applied Engineering Sciences":
            michigan_cities = ["Detroit: 39 positions", "Grand Rapids: 10 positions", "Lansing: 6 positions", "Ann Arbor: 4 positions"]
            non_michigan_cities = ["Chicago, IL: 29 positions", "Dallas, TX: 4 positions", "Phoenix, AZ: 4 positions", "Los Angeles, CA: 3 positions", "Minneapolis, MN: 3 positions"]
        elif selected_major == "Biosystems Engineering":
            michigan_cities = ["Detroit: 19 positions", "Grand Rapids: 8 positions", "Kalamazoo: 7 positions", "Lansing: 6 positions", "Ann Arbor: 2 positions"]
            non_michigan_cities = ["Madison, WI: 6 positions", "Chicago, IL: 3 positions", "Boston, MA: 2 positions", "Denver, CO: 2 positions", "Minneapolis, MN: 2 positions"]
        elif selected_major == "Chemical Engineering":
            michigan_cities = ["Detroit: 38 positions", "Kalamazoo: 11 positions", "Lansing: 10 positions", "Ann Arbor: 9 positions", "Midland: 6 positions"]
            non_michigan_cities = ["Madison, WI: 12 positions", "Chicago, IL: 9 positions", "Indianapolis, IN: 7 positions", "Cleveland, OH: 4 positions", "San Francisco, CA: 3 positions"]
        elif selected_major == "Civil Engineering":
            michigan_cities = ["Detroit: 33 positions", "Lansing: 17 positions", "Grand Rapids: 9 positions", "Ann Arbor: 3 positions", "Jackson: 3 positions"]
            non_michigan_cities = ["Chicago, IL: 7 positions", "Dallas, TX: 4 positions", "Denver, CO: 2 positions"]
        elif selected_major == "Computational Data Science":
            michigan_cities = ["Detroit: 6 positions", "Lansing: 2 positions"]
            non_michigan_cities = ["Columbus, OH: 2 positions"]
        elif selected_major == "Computer Engineering":
            michigan_cities = ["Detroit: 21 positions", "Lansing: 7 positions", "Grand Rapids: 3 positions"]
            non_michigan_cities = ["San Francisco, CA: 3 positions", "Austin, TX: 2 positions", "Minneapolis, MN: 2 positions", "Seattle, WA: 2 positions"]
        elif selected_major == "Computer Science":
            michigan_cities = ["Detroit: 109 positions", "Lansing: 43 positions", "Grand Rapids: 19 positions", "Ann Arbor: 10 positions", "Kalamazoo: 2 positions"]
            non_michigan_cities = ["Chicago, IL: 26 positions", "Seattle, WA: 16 positions", "Minneapolis, MN: 12 positions", "New York, NY: 9 positions", "Austin, TX: 7 positions"]
        elif selected_major == "Electrical Engineering":
            michigan_cities = ["Detroit: 43 positions", "Ann Arbor: 9 positions", "Lansing: 7 positions", "Grand Rapids: 6 positions", "Jackson: 5 positions"]
            non_michigan_cities = ["Chicago, IL: 8 positions", "Dallas, TX: 4 positions", "Indianapolis, IN: 3 positions", "Milwaukee, WI: 3 positions", "Alexandria, VA: 2 positions"]
        elif selected_major == "Environmental Engineering":
            michigan_cities = ["Detroit: 14 positions", "Lansing: 6 positions", "Grand Rapids: 5 positions"]
            non_michigan_cities = []
        elif selected_major == "Materials Science & Engineering":
            michigan_cities = ["Detroit: 12 positions", "Grand Rapids: 3 positions"]
            non_michigan_cities = []
        elif selected_major == "Mechanical Engineering":
            michigan_cities = ["Detroit: 144 positions", "Grand Rapids: 19 positions", "Lansing: 15 positions", "Ann Arbor: 12 positions", "Kalamazoo: 5 positions"]
            non_michigan_cities = ["Chicago, IL: 14 positions", "Indianapolis, IN: 8 positions", "Madison, WI: 6 positions", "Cincinnati, OH: 5 positions", "Boston, MA: 4 positions"]
        else:
            michigan_cities = []
            non_michigan_cities = []

    st.subheader("Top 5 Michigan Cities")
    for i, city in enumerate(michigan_cities, start=1):
        st.write(f"{i}. {city}")

    st.subheader("Top 5 Non-Michigan Cities")
    for i, city in enumerate(non_michigan_cities, start=1):
        st.write(f"{i}. {city}")

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
        ms1 = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Year", default=["2021"], label_visibility="visible")

    with col2:
        if ms1 == ["2021"]:
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
        else:
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
        ms = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major",  label_visibility="hidden")

    if ["All Engineering Majors"] == ms:
        if ["2023"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats()
                st.caption("Note: 0.8% of graduates indicate “other intentions” - placed and not seeking")
                st.write("Insert Class Composition")
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
                    display_city_visualization("LATLONGDestinationCumulativeDataset(All Majors).csv", "2022")
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
                    fig = choropleth_state_map("CSV_Spring 2021_2-21-24.csv", "All Engineering Majors")
                    st.header('Interactive Map for Destination Data: Spring 2021 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                    top_5_employer_states("2021", "All Engineering Majors")   
                with t2:
                    display_city_visualization("LATLONGDestinationCumulativeDataset(All Majors).csv", "2021")
                    display_top_5_cities("2021", "All Engineering Majors")
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('80.3%', '82.5%', '90.5%', '84.4%', '96.0%', '98.0%','94.3%', '96.1%', '69,838', '73,922', '76,806', '73,522', '70,000','72,500', '75,000', '72,500')
            with t2:
                st.image("FT (1).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "All Engineering Majors")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "All Engineering Majors")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(All Majors).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "All Engineering Majors")

    elif ["Applied Engineering Sciences"] == ms:
        if ["2023"] == ms1:
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
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv", "Applied Engineering Sciences")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig) 
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Applied Engineering Sciences")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: AES Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Applied Engineering Sciences).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Applied Engineering Sciences")
    
    elif ["Biosystems Engineering"] == ms:
        if ["2023"] == ms1:
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
        if ["2023"] == ms1:
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
        if ["2023"] == ms1:
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
                    top_5_employer_states("Cumulative Data 21-23: Key Stats", "Civil Engineering")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City: CE Major')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Civil Engineering).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Civil Engineering")

    elif ["Computational Data Science"] == ms:
        if ["2023"] == ms1:
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
                    display_city_visualization("LATLONGDestinationCumulativeDataset(Computational Data Science).csv", "Cumulative Data 21-23: Key Stats")
                    display_top_5_cities("Cumulative Data 21-23: Key Stats", "Computational Data Science")

    elif ["Computer Engineering"] == ms:
        if ["2023"] == ms1:
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
        if ["2023"] == ms1:
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
        if ["2023"] == ms1:
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
                    display_city_visualization("LATLONGDestinationCumulativeDataset(ELectrical Engineering).csv", "2022")
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
        if ["2023"] == ms1:
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
        if ["2023"] == ms1:
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
        if ["2023"] == ms1:
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
