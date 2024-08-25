import streamlit as st
import plotly.express as px
import pandas as pd

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