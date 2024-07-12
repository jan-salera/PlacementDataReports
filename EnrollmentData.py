import streamlit as st
import plotly.express as px
import pandas as pd

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

st.subheader("ENROLLMENT DATA")
st.header("Fall 2023 Enrollment Data")
T1, T2, T3 = st.tabs(["Class Level", "Ethnicity", "Gender"])
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
with T3:
    data_gender([4747, 1386], ['#0B1799', '#C70F0F'], ['Male - 4747', 'Female - 1386'])

st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_f52727d1f5fd44fb865b6bff7b45b6ef.xlsx?dn=Diversity_graphs%20Combined_12_9_22.xlsx", label = ":green[**Diversity Enrollment Data 5 Year Overview for Engineering**]")