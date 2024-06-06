import streamlit as st
import plotly.express as px

# Graphs for the entire 2023 Graduating Class Dataset
def All_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
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

# Graphs for the AES 2023 Graduating Class Dataset
def AES_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def AES_Data_Gender():
    gender_data = {'Gender': ['Male', 'Female'], 'Count': [51, 27]}
    colors = ['#0B1799', '#C70F0F']
    gender_fig = px.pie(gender_data, values='Count', names='Gender', title='Gender Distribution', color_discrete_sequence=colors)
    st.plotly_chart(gender_fig)

def AES_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', 'Not Specified', "Black/African American"],
    'Count': [58, 6, 2, 6, 2, 3, 1]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the BE 2023 Graduating Class Dataset
def BE_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#18453B', '#CECECE','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def BE_Data_Gender():
    gender_data = {'Gender': ['Male', 'Female'], 'Count': [22, 22]}
    colors = ['#0B1799', '#C70F0F']
    gender_fig = px.pie(gender_data, values='Count', names='Gender', title='Gender Distribution', color_discrete_sequence=colors)
    st.plotly_chart(gender_fig)

def BE_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races'],
    'Count': [36, 3, 3, 1, 1]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the CDS 2023 Graduating Class Dataset
def CDS_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#18453B']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def CDS_Data_Gender():
    st.write("No Data Yet")

def CDS_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'Hispanic/Latine', 'Two or More Races'],
    'Count': [8, 3, 1, 2]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the CE 2023 Graduating Class Dataset
def CE_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def CE_Data_Gender():
    st.write("No Data Yet")

def CE_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races'],
    'Count': [41, 1, 4, 6, 4, 2]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the ChemE 2023 Graduating Class Dataset
def ChemE_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE','#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def ChemE_Data_Gender():
    st.write("No Data Yet")

def ChemE_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', 'Not Specified', "Black/African American"],
    'Count': [74, 6, 4, 3, 2, 2, 4]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the CpeE 2023 Graduating Class Dataset
def CpE_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def CpE_Data_Gender():
    st.write("No Data Yet")

def CpE_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'International'],
    'Count': [21, 2]}
    msu_colors = ['#18453B', '#008208']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the CSE 2023 Graduating Class Dataset
def CSE_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#18453B', '#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def CSE_Data_Gender():
    st.write("No Data Yet")

def CSE_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', "Black/African American"],
    'Count': [125, 43, 42, 4, 5, 8]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the EE 2023 Graduating Class Dataset
def EE_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE', '#18453B','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def EE_Data_Gender():
    st.write("No Data Yet")

def EE_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', 'Not Specified', "Black/African American"],
    'Count': [48, 8, 6, 4, 2, 2, 7]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the ENE 2023 Graduating Class Dataset
def ENE_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def ENE_Data_Gender():
    st.write("No Data Yet")

def ENE_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races'],
    'Count': [11, 3, 1, 1, 1]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934']
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the ME 2023 Graduating Class Dataset
def ME_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#18453B', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def ME_Data_Gender():
    st.write("No Data Yet")

def ME_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'American Indian/Alaskan Native'],
    'Count': [117, 15, 20, 9, 5, 1, 3, 1]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934', "#C3C3C3"]
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

# Graphs for the MSE 2023 Graduating Class Dataset
def MS_Data_Major():
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16] }
    colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#CECECE', '#18453B','#CECECE', '#CECECE']
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

def MS_Data_Gender():
    st.write("No Data Yet")

def MS_Data_Ethnicity():
    ethnicity_data = {
    'Ethnicity': ['White', 'Asian', 'International'],
    'Count': [13, 1, 2]}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934', "#C3C3C3"]
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

def main():
    st.title("**PLACEMENT DATA & REPORTS**")
    st.header("DESTINATION DATA")

    st.write("**Engineering 2023 Graduate Outcomes**")
    st.write("Summary of placement, salary and geographic destinations for all undergraduate students in the College of Engineering")
    options = ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", 
    "Civil Engineering", "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", 
    "Environmental Engineering", "Mechanical Engineering", "Material Science")
    ms = st.multiselect("Note: Make sure only one major is in the filter.", options=options, placeholder = "Filter By Major", label_visibility="visible")

    if ["All Engineering Majors"] == ms:
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

    elif ["Applied Engineering Sciences"] == ms:
        st.header("Spring 2023 Graduating Class Composition: AES Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            AES_Data_Major()
        with tab2:
            AES_Data_Ethnicity()
        with tab3:
            AES_Data_Gender()

    elif ["Biosystems Engineering"] == ms:
        st.header("Spring 2023 Graduating Class Composition: BE Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            BE_Data_Major()
        with tab2:
            BE_Data_Ethnicity()
        with tab3:
            BE_Data_Gender()

    elif ["Computational Data Science"] == ms:
        st.header("Spring 2023 Graduating Class Composition: CDS Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            CDS_Data_Major()
        with tab2:
            CDS_Data_Ethnicity()
        with tab3:
            CDS_Data_Gender()

    elif ["Civil Engineering"] == ms:
        st.header("Spring 2023 Graduating Class Composition: CE Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            CE_Data_Major()
        with tab2:
            CE_Data_Ethnicity()
        with tab3:
            CE_Data_Gender()

    elif ["Chemical Engineering"] == ms:
        st.header("Spring 2023 Graduating Class Composition: ChemE Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            ChemE_Data_Major()
        with tab2:
            ChemE_Data_Ethnicity()
        with tab3:
            ChemE_Data_Gender()

    elif ["Computer Science"] == ms:
        st.header("Spring 2023 Graduating Class Composition: CSE Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            CSE_Data_Major()
        with tab2:
            CSE_Data_Ethnicity()
        with tab3:
            CSE_Data_Gender()

    elif ["Computer Engineering"] == ms:
        st.header("Spring 2023 Graduating Class Composition: CpE Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            CpE_Data_Major()
        with tab2:
            CpE_Data_Ethnicity()
        with tab3:
            CpE_Data_Gender()
        
    elif ["Electrical Engineering"] == ms:
        st.header("Spring 2023 Graduating Class Composition: EE Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            EE_Data_Major()
        with tab2:
            EE_Data_Ethnicity()
        with tab3:
            EE_Data_Gender()

    elif ["Environmental Engineering"] == ms:
        st.header("Spring 2023 Graduating Class Composition: ENE Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            ENE_Data_Major()
        with tab2:
            ENE_Data_Ethnicity()
        with tab3:
            ENE_Data_Gender()

    elif ["Mechanical Engineering"] == ms:
        st.header("Spring 2023 Graduating Class Composition: ME Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            ME_Data_Major()
        with tab2:
            ME_Data_Ethnicity()
        with tab3:
            ME_Data_Gender()

    elif ["Material Science"] == ms:
        st.header("Spring 2023 Graduating Class Composition: MS Major")
        tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
        with tab1:
            MS_Data_Major()
        with tab2:
            MS_Data_Ethnicity()
        with tab3:
            MS_Data_Gender()
    

if __name__ == "__main__":
    main()