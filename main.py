import streamlit as st
import plotly.express as px

# Graphs for the entire 2023 Graduating Class Dataset
def All_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Enviornmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution')
    st.plotly_chart(major_fig)

def All_Data_Gender():
    gender_data = {'Gender': ['Male', 'Female'], 'Count': [625, 195]}
    colors = ['#0B1799', '#C70F0F']
    gender_fig = px.pie(gender_data, values='Count', names='Gender', title='Gender Distribution', color_discrete_sequence=colors)
    st.plotly_chart(gender_fig)

def All_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'American Indian/Alaskan Native'],
    'Count': [552, 89, 86, 35, 29, 18, 10, 1]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934', "#C3C3C3"]
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

def Key_Stats_KR():
    year = ['2022', '2023','2024']
    percentage = [93, 89, 90]
    colors = ['#18453B', '#008208', "#7BBD00"]
    kr_fig = px.bar(x=year, y=percentage, labels={'x':'Year', 'y':'Placement Rate (%)'}, color=year, 
    color_discrete_sequence=colors, width=180, height=300)

    st.plotly_chart(kr_fig)
    

def AES_Data():

    gender_data = {
    'Gender': ['Male', 'Female', 'Other'],
    'Count': [45, 35, 5] }
    gender_fig = px.pie(gender_data, values='Count', names='Gender', title='Gender Distribution')
    st.plotly_chart(gender_fig)

    ethnicity_data = {
    'Ethnicity': ['White', 'Black', 'Hispanic', 'Asian', 'Other'],
    'Count': [60, 20, 10, 5, 5]}
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution')
    st.plotly_chart(ethnicfig)

def main():
    st.title("**PLACEMENT DATA & REPORTS**")
    st.header("DESTINATION DATA")

    st.write("**Engineering 2023 Graduate Outcomes**")
    st.write("Summary of placement, salary and geographic destinations for all undergraduate students in the College of Engineering")
    options = ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", 
    "Civil Engineering", "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", 
    "Enviornmental Engineering", "Mechanical Engineering", "Material Science")
    ms = st.multiselect("empty label name", options=options, placeholder = "Filter By Major", label_visibility="collapsed")

    if "All Engineering Majors" in ms:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title("")
            st.title("")
            st.title("")
            st.header("90.5% Knowledge Rate")
            kr_check = st.checkbox("See more", key=0)
            if kr_check:
                Key_Stats_KR()
        with col2:
            st.title(":gray[**Key Stats**]")
            st.header("94.3% Placement Rate")
            pr_check = st.checkbox("See more", key=1)
            if pr_check:
                Key_Stats_KR()
        with col3:
            st.title("")
            st.title("")
            st.title("")
            st.header("$76,806 Average Starting Salary")
            kr_check = st.checkbox("See more", key=2)
            if kr_check:
                Key_Stats_KR()
        
        
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            All_Data_Major()
        with tab2:
            All_Data_Ethnicity()
        with tab3:
            All_Data_Gender()

    elif "Applied Engineering Sciences" in ms:
        st.write("You chose to sort by :green[Applied Engineering Sciences]")
        AES_Data()

    elif "Biosystems Engineering" in ms:
        st.write("You chose to sort by :green[Biosystems Engineering]")

    elif "Computational Data Science" in ms:
        st.write("You chose to sort by :green[Computational Data Science]")

    elif "Civil Engineering" in ms:
        st.write("You chose to sort by :green[Civil Engineering]")

    elif "Chemical Engineering" in ms:
        st.write("You chose to sort by :green[Chemical Engineering]")

    elif "Computer Science" in ms:
        st.write("You chose to sort by :green[Computer Science]")

    elif "Computer Engineering" in ms:
        st.write("You chose to sort by :green[Computer Engineering]")
        
    elif "Electrical Engineering" in ms:
        st.write("You chose to sort by :green[Electrical Engineering]")

    elif "Enviornmental Engineering" in ms:
        st.write("You chose to sort by :green[Enviornmental Engineering]")  

    elif "Mechanical Engineering" in ms:
        st.write("You chose to sort by :green[Mechanical Engineering]") 

    elif "Material Science" in ms:
        st.write("You chose to sort by :green[Material Science]") 
    

if __name__ == "__main__":
    main()