import streamlit as st
import plotly.express as px

# Shows the entire graduating class breakdown by major
def data_major(colors = [], count = [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16]):
    class_data = {
    'Major': ["Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", 
    "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", 
    "Mechanical Engineering", "Material Science"],
    'Count': count}
    major_fig = px.pie(class_data, values='Count', names='Major', title='Major Distribution', color_discrete_sequence=colors)
    st.plotly_chart(major_fig)

# Shows the entire graduating class breakdown by gender
def data_gender(count = [], color = ['#0B1799', '#C70F0F']):
    gender_data = {'Gender': ['Male', 'Female'], 'Count': count}
    colors = color
    gender_fig = px.pie(gender_data, values='Count', names='Gender', title='Gender Distribution', color_discrete_sequence=colors)
    st.plotly_chart(gender_fig)

# Shows the entire graduating class breakdown by ethnicity
def data_ethnicity(count = [], ethnicity = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Two or More Races', 'Not Specified', "Black/African American"]):
    ethnicity_data = {
    'Ethnicity': ethnicity,
    'Count': count}
    msu_colors = ['#18453B', '#008208', '#7BBD00', '#61BF67', '#49764C', '#0B9A6D', '#008934', "#C3C3C3"]
    ethnicfig = px.pie(ethnicity_data, values='Count', names='Ethnicity', title='Ethnicity Distribution', color_discrete_sequence=msu_colors)
    st.plotly_chart(ethnicfig)

AllEthnicity = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'American Indian/Alaskan Native']
Major2022 = [57, 50, 7, 51, 91, 42, 193, 60, 20, 164, 23]
InverseGender = ['#C70F0F', '#0B1799']

def main():        
    col1, col2 = st.columns([2,3]) 
    with col1:
        options = ("Cummulative Data 21-23", "2023", "2022", "2021")
        ms1 = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Year", label_visibility="visible")

    with col2:
        options = ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", 
        "Civil Engineering", "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", 
        "Environmental Engineering", "Mechanical Engineering", "Material Science")
        ms = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major",  label_visibility="hidden")

    if ["All Engineering Majors"] == ms:
        if ["2023"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                data_major()
            with tab2:
                AllCount2023 = [552, 89, 86, 35, 29, 18, 10, 1]
                data_ethnicity(AllCount2023, AllEthnicity)
            with tab3:
                AllGender2023 = [625, 195]
                data_gender(AllGender2023)
        elif ["2022"] == ms1:
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                data_major([], Major2022)
            with tab2:
                AllCount2022 = [532, 72, 77, 23, 14, 25, 13, 2]
                data_ethnicity(AllCount2022, AllEthnicity)
            with tab3:
                AllGender2022 = [541, 217]
                data_gender(AllGender2022)

    elif ["Applied Engineering Sciences"] == ms:
        if ["2023"] == ms1:
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
        if ["2022"] == ms1:
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

    elif ["Biosystems Engineering"] == ms:
        if ["2023"] == ms1:
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
                
    elif ["Computational Data Science"] == ms:
        if ["2023"] == ms1:
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
            st.header("Spring 2022 Graduating Class Composition: CDS Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CDSColors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE', '#18453B']
                data_major(CDSColors, Major2022)
            with tab2:
                CDSEthnicity2022 = ['White', 'Asian', 'International', 'Not Specified']
                CDSCount2022 = [4, 1, 1, 1]
                data_ethnicity(CDSCount2022, CDSEthnicity2022)
            with tab3:
                BEGender2022 = [4, 3]
                data_gender(BEGender2022)           

    elif ["Civil Engineering"] == ms:
        if ["2023"] == ms1:
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

    elif ["Chemical Engineering"] == ms:
        if ["2023"] == ms1:
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
               
    elif ["Computer Engineering"] == ms:
        if ["2023"] == ms1:
            st.header("Spring 2023 Graduating Class Composition: CpE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CpE_Colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE']
                data_major(CpE_Colors)
            with tab2:
                CpEEthnicity2023 = ['White', 'International']
                CpECount2023 = [22, 2]
                data_ethnicity(CpECount2023, CpEEthnicity2023)
            with tab3:
                CpEGender2023 = [21, 3]
                data_gender(CpEGender2023)
        elif ["2022"] == ms1:
            st.header("Spring 2022 Graduating Class Composition: CpE Major")
            tab1, tab2, tab3 = st.tabs(["Major", "Ethnicity", "Gender"])
            with tab1:
                CpE_Colors = ['#CECECE', '#CECECE', '#CECECE','#CECECE','#CECECE','#CECECE','#CECECE','#18453B','#CECECE','#CECECE','#CECECE']
                data_major(CpE_Colors, Major2022)
            with tab2:
                CpEEthnicity2022 = ['White', 'Asian', 'International', 'Hispanic/Latine', "Black/African American"]
                CpECount2022 = [28, 4, 5, 1, 4 ]
                data_ethnicity(CpECount2022, CpEEthnicity2022)
            with tab3:
                CpEGender2022 = [34, 8]
                data_gender(CpEGender2022)

    elif ["Computer Science"] == ms:
        if ["2023"] == ms1:
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
    
    elif ["Electrical Engineering"] == ms:
        if ["2023"] == ms1:
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
       
    elif ["Environmental Engineering"] == ms:
        if ["2023"] == ms1:
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

    elif ["Mechanical Engineering"] == ms:
        if ["2023"] == ms1:
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

    elif ["Material Science"] == ms:
        if ["2023"] == ms1:
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
        

if __name__ == "__main__":
    main()