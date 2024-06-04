import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import folium
from streamlit_folium import st_folium
import numpy as np
import json
# Load the dataset
dest21 = pd.read_csv("Spring 2021_2-21-24(Post-graduate Outcomes (Undergr).csv")

# Process state data
state_counts = dest21['Employer State'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']
state_counts = state_counts.drop([11, 32])
state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
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
# Example mapping of cities to counties in Michigan
city_to_county = {
    'Detroit - MI': 'Wayne County',
    'Lansing - MI': 'Ingham County',
    'Grand Rapids - MI': 'Kent County',
    'Ann Arbor - MI': 'Washtenaw County',
    'Kalamazoo - MI': 'Kalamazoo County',
    'Jackson - MI': 'Jackson County',
    'Flint - MI': 'Genesee County',
    'Jackson - MI': 'Jackson County',
    'Midland - MI': 'Midland County',
    'Traverse City - MI': 'Grand Traverse County',
    'Bay City - MI': 'Bay County',
    'Saginaw - MI': 'Saginaw County',
    'Adrian - MI': 'Lenawee County',
    'Battle Creek - MI': 'Calhoun County',
    'Cadillac - MI': 'Wexford County',
    'Benton Harbor - MI': 'Berrien County',
    'Coloma - MI': 'Berrien County',
    'Litchfield - MI': 'Hillsdale County',
    'Beaverton - MI': 'Gladwin County',
    'West Branch - MI': 'Ogemaw County',
    'Reed City - MI': 'Osceola County'
    # Add other mappings as needed
}

# Process city data
city_counts = dest21['Employer City'].value_counts().reset_index()
city_counts.columns = ['City', 'Count']
city_counts['County'] = city_counts['City'].map(city_to_county)
city_counts_mi = city_counts.dropna(subset=['County'])

# Aggregate counts by county
county_counts = city_counts_mi.groupby('County')['Count'].sum().reset_index()

# Load GeoJSON data for counties
geojson_url = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
response = requests.get(geojson_url)
geojson_data = response.json()

# Filter GeoJSON for Michigan counties only
michigan_counties = [feature for feature in geojson_data['features'] if feature['properties']['STATE'] == '26']

# Create a new GeoJSON object with only Michigan counties
michigan_geojson = {
    "type": "FeatureCollection",
    "features": michigan_counties
}

# Group by 'Job Source' and count occurrences
job_source_counts = dest21['Job Source'].value_counts().reset_index()
job_source_counts.columns = ['Job Source', 'Count']

# Group by 'Program Level' and count occurrences
job_levels_counts = dest21['Program Level'].value_counts().reset_index()
job_levels_counts.columns = ['Job Level', 'Count']

# Making 'salaries' data
dest21['Salary'] = pd.to_numeric(dest21['Salary'], errors='coerce')
salaries_data = dest21.dropna(subset=['Salary'])
bucket_ranges = [0, 50000, 75000, 100000, 125000, 150000, 175000, 200000, float('inf')]
bucket_labels = ['<$50k', '$50k-$75k', '$75k-$100k', '$100k-$125k', '$125k-$150k', '$150k-$175k', '$175k-$200k', '>$200k']
salaries_data['Salary Bucket'] = pd.cut(salaries_data['Salary'], bins=bucket_ranges, labels=bucket_labels, right=False)
salary_distribution = salaries_data['Salary Bucket'].value_counts().sort_index(ascending=False)

# Making 'Job Offers' data
offer_rec_date = dest21.dropna(subset=['Offer Received Date'])
offer_rec_date['Offer Received Date'] = pd.to_datetime(offer_rec_date['Offer Received Date'])
job_offers_trend = offer_rec_date.groupby(offer_rec_date['Offer Received Date'].dt.date).size().reset_index(name='Job Offers')#cutoff_date = pd.Timestamp('2022-01-31')
#job_offers_trend = job_offers_trend[pd.to_datetime(job_offers_trend['Reported Date']) <= cutoff_date]

state_counts['LogCount'] = np.log1p(state_counts['Count'])

# Create choropleth figure for states
fig = px.choropleth(
    state_counts,
    locations='StateAbbrev',
    locationmode='USA-states',
    color='LogCount',  # Use the log-transformed count
    color_continuous_scale='Greens',
    labels={'LogCount': 'Log Count'},
    scope='usa',
    title='Count of Employed Spartan Engineers by State (Log Scale)',
    range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
)

# Adjust colorbar to show the original scale
fig.update_coloraxes(
    colorbar=dict(
        tickvals=[np.log1p(x) for x in [1, 10, 100, 1000, 10000]],  # Customize tick values as needed
        ticktext=['1', '10', '100', '1000', '10000']  # Corresponding labels
    )
)

state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()

# Load the GeoJSON data
#state_geo = pd.read_csv("C:/Users/Shayna/OneDrive - Michigan State University/Documents/MSU The Center - Shayna Laptop/us_states.geojson.txt")
foliumstatemap = folium.Map(location=[37.8, -96], zoom_start=3.8)

folium.Choropleth(
    geo_data=state_geo,  # new geojson data
    name="choropleth",
    data=state_counts,
    columns=["State", "LogCount"],
    key_on="feature.properties.name",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.1,
    legend_name="Number of Employed Spartan Graduates",
).add_to(foliumstatemap)

folium.LayerControl().add_to(foliumstatemap)


# Create choropleth figure for Michigan counties
fig2 = px.choropleth(
    county_counts,
    geojson=michigan_geojson,
    locations='County',
    featureidkey="properties.NAME",
    color='Count',
    color_continuous_scale='Greens',
    labels={'Count': 'Count'},
    title='Count of Employed Spartan Engineers by County in Michigan'
)

# Optional: fit bounds to the locations and set visible to True
fig2.update_geos(fitbounds="locations", visible=True)

# Create a bar chart
fig3 = px.bar(
    job_source_counts,
    x='Job Source',
    y='Count',
    title='Counts of Jobs Found by Job Source Category',
    labels={'Job Source': 'Job Source Category', 'Count': 'Number of Jobs'},
    color='Count', 
    color_continuous_scale='Greens', 
)

# Customize the layout for better readability
fig3.update_layout(
    xaxis_title='Job Source Category',
    yaxis_title='Number of Jobs',
    xaxis_tickangle=-45,  # Rotate x-axis labels for better readability
    height=600,
)

# Create a pie chart
fig_pie = px.pie(
    job_levels_counts,
    values='Count',
    names='Job Level',
    title='Distribution of Education Levels',
)

# Create a histogram
fig_bar = px.bar(
    x=salary_distribution.index,
    y=salary_distribution.values,
    labels={'x': 'Salary Buckets', 'y': 'Number of Salaries'},
    title='Distribution of Salaries by Buckets (Descending)',
    color_discrete_sequence=['green'],  # Set color for bars
)

fig_bar.update_layout(
    xaxis={'categoryorder': 'total descending'},  # Sort x-axis categories in descending order
    xaxis_title='Salary Buckets',
    yaxis_title='Number of Salaries',
    yaxis_tickvals=list(range(0, salary_distribution.max()+1)),  # Set y-axis tick values
    yaxis_ticktext=[f"{val:.0f}" for val in range(0, salary_distribution.max()+1)],  # Set y-axis tick labels
)

# Create a line graph
fig_dot = px.scatter(
    job_offers_trend,
    x='Offer Received Date',
    y='Job Offers',
    title='Trend of Job Offers Received Over Time',
    labels={'Offer Received Date': 'Date', 'Job Offers': 'Number of Job Offers'},
    color_discrete_sequence=['green'],  # Set dot color to green
)
fig_dot.update_traces(mode='markers', marker=dict(size=10))
fig_dot.update_layout(
    xaxis_title='Date',
    yaxis_title='Number of Job Offers',
    yaxis=dict(
        tickmode='linear',
        dtick=1  # Set the tick step to 1
    ),
    height=300  # Adjust the height of the figure
)


# Display the Streamlit app
st.markdown(
    """
    <h1 style='text-align: center;'>Spring 2021 Destination Data - Initial Visualizations</h1>
    """, 
    unsafe_allow_html=True
)

import pandas

state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()
state_data = pandas.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv"
)

m = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(m)

folium.LayerControl().add_to(m)
st.write("This visualization is using dummy code to test the package itself on my computer. This visual is NOT related to the Data and Reports webpage.")
st_folium(m, width=700, height=500)


st.write(state_counts)
st.write("Here are some of the visualizations that I have made so far :)")
st.subheader('Interactive Choropleth Map for States using Folium')
st_folium(foliumstatemap, width=700, height=500)
st.subheader('Interactive Choropleth Map for States using Folium')
st.plotly_chart(fig)
st.subheader('Interactive Choropleth Map for Counties in Michigan')
st.plotly_chart(fig2)
st.write('### Bar Graph of Counts of Jobs found by each Job Source Category')
st.plotly_chart(fig3)
st.write("### Distribution of Levels of Continuing Education Sought")
st.plotly_chart(fig_pie)
st.write("### Distribution of Salaries")
st.plotly_chart(fig_bar)
st.write("### Trend of Job Offers Received Over Time")
st.plotly_chart(fig_dot)
