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

def hex_colors(position = 0, size = 0):
    if size == 0:
        Colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    else:
        Colors = ['#CECECE', '#CECECE','#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    
    Colors [position] = '#18453B'
    return Colors

Colors =  {"HEX1" : hex_colors(), "HEX2" : hex_colors(1), "HEX3": hex_colors(2), "HEX4" : hex_colors(3), "HEX5" : hex_colors(4), "HEX6" : hex_colors(5), "HEX7" : hex_colors(6), "HEX8" : hex_colors(7), "HEX9" : hex_colors(8), "HEX10" : hex_colors(9), "HEX11" : hex_colors(-1)}

AllEthnicity = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'Not Reported','American Indian/Alaskan Native']
Major2022 = [57, 50, 7, 51, 91, 42, 193, 60, 20, 164, 23]
InverseGender = ['#C70F0F', '#0B1799']
Major2021 = [72, 47, 44, 100, 42, 173, 67, 24, 155, 22]

MajorList = ["All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering"]
MajorList2021 = MajorList.copy()
MajorList2021.remove("Computational Data Science")
Major2123 = [207, 141, 21, 153, 286, 108, 593, 203, 61, 490, 61]


def main():  
    col1, col2 = st.columns([2,3]) 
    with col1:
        options = ("Cumulative Data 21-23: Key Stats", "2023", "2022", "2021")
        ms1 = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Year", default=["2023"], label_visibility="visible")

    with col2:
        if ms1 == ["2021"]:
            options= (MajorList2021)
        else:
            options= (MajorList)
        ms = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major",  default=["All Engineering Majors"], label_visibility="hidden")

    if ["All Engineering Majors"] == ms:
        if ["2023"] == ms1:
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
                    fig = choropleth_state_map("CSV_Spring 2023_3-7-24.csv")
                    st.header('Interactive Map for Destination Data: Spring 2023 College of Engineering Graduating Class')
                    st.plotly_chart(fig) 
                with t2:
                    st.write("BY CITY")
        elif ["2022"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with tab1:
                key_stats("2022", "82.5%", "625/758", "98%", "612/625", "$73,922", "$72,500", "82.9%", "14.6%", "0.2%")
                st.caption("Note: 0.3% of graduates indicate “other intentions” - placed and not seeking")
                st.header("Spring 2022 Graduating Class Composition: All Engineering Majors")
                t1, t2, t3 = st.tabs(["Major", "Ethnicity", "Gender"])
                with t1:
                    data_major(Major2022)
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
                    fig = choropleth_state_map("CSV_Spring 2022_2-21-24.csv")
                    st.header('Interactive Map for Destination Data: Spring 2022 College of Engineering Graduating Class')
                    st.plotly_chart(fig)
                with t2:
                    st.write("BY CITY")
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
                    st.header("INSERT MAPS HERE")
                with tab2:
                    st.header("INSERT MAPS HERE")    
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            t1, t2, t3 = st.tabs(["Key Statistics", "By Employer", "By Geography"])
            with t1:
                c_key_stats('80.3%', '82.5%', '90.5%', '84.4%', '96.0%', '98.0%','94.3%', '96.1%', '69,838', '73,922', '76,806', '73,522', '70,000','72,500', '75,000', '72,500')
            with t2:
                st.image("FT (1).jpg")
            with t3:
                tab1, tab2= st.tabs(["By State", "By City"])
                with tab1:
                    AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv")
                    st.header('College of Engineering Spring 21-23 Destination Locations - By State')
                    st.plotly_chart(AllFig)
                    top_5_employer_states("LATLONGDestinationCumulativeDataset(All Majors).csv")
                with tab2:
                    st.header('College of Engineering Spring 21-23 Destination Locations - By City')
                    display_city_visualization("LATLONGDestinationCumulativeDataset(All Majors).csv")


if __name__ == "__main__":

    main()