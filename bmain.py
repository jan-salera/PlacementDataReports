import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Shows the entire graduating class breakdown by major
def data_major(colors = [], count = [78, 44, 14, 58, 95, 24, 227, 76, 17, 171, 16], majors = ["Applied Engineering Sciences", "Biosystems Engineering",        "Computational Data Science", "Civil Engineering","Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Mechanical Engineering", "Material Sciences and Engineering"]):
    class_data = {
    'Major': majors,
    'Count': count
    }
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
        title='',
        range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
        hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
    )
    return fig

AllEthnicity = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'Not Reported','American Indian/Alaskan Native']
Major2022 = [57, 50, 7, 51, 91, 42, 193, 60, 20, 164, 23]
InverseGender = ['#C70F0F', '#0B1799']
Major2021 = [72, 47, 44, 100, 42, 173, 67, 24, 155, 22]
MajorList2021 = ["Applied Engineering Sciences", "Biosystems Engineering", "Civil Engineering" , "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Mechanical Engineering", "Material Sciences and Engineering"]
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
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Material Sciences and Engineering", "Mechanical Engineering")
        else:
            options= ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Material Sciences and Engineering", "Mechanical Engineering")
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
            AllFig = choropleth_state_map("DestinationCumulativeDataset(All Majors).csv")
            st.header('Interactive Map for Destination Data: All Engineering Majors')
            st.plotly_chart(AllFig)

    elif ["Applied Engineering Sciences"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "100%", krinfo = "78/78", pr = "92.3%", prinfo = "72/78", avgsal = "$72,233", medsal = "$70,000", employ = "87%", grad = "5.1%")
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
            AESFig = choropleth_state_map("DestinationCumulativeDataset(Applied Engineering Sciences).csv")
            st.header('Interactive Map for Destination Data: AES Major')
            st.plotly_chart(AESFig)  
    
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
            BEFig = choropleth_state_map("DestinationCumulativeDataset(Biosystems Engineering).csv")
            st.header('Interactive Map for Destination Data: BE Major')
            st.plotly_chart(BEFig) 
                
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
            CDSFig = choropleth_state_map("DestinationCumulativeDataset(Computational Data Science).csv")
            st.header('Interactive Map for Destination Data: CDS Major')
            st.plotly_chart(CDSFig) 

    elif ["Civil Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "95%", krinfo = "55/58", pr = "96%", prinfo = "53/55", avgsal = "$65,895", medsal = "$65,000", employ = "84%", grad = "9%")
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
            CEFig = choropleth_state_map("DestinationCumulativeDataset(Civil Engineering).csv")
            st.header('Interactive Map for Destination Data: CE Major')
            st.plotly_chart(CEFig)
            
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
                ChemEGender2022 = [66, 34]
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
                ChemEGender2021 = [54, 41]
                data_gender(ChemEGender2021)
            
        elif ["Cumulative Data 21-23: Key Stats"] == ms1:
            c_key_stats('83%', '82%', '95%', '87%', '94%', '97%', '98%', '96%','69,604', '71,561', '77,315', '72,827', '70,000', '72,500', '76,000', '72,833')
            ChemEFig = choropleth_state_map("DestinationCumulativeDataset(Chemical Engineering).csv")
            st.header('Interactive Map for Destination Data: ChemE Major')
            st.plotly_chart(ChemEFig)
               
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
            CpEFig = choropleth_state_map("DestinationCumulativeDataset(Computer Engineering).csv")
            st.header('Interactive Map for Destination Data: CpE Major')
            st.plotly_chart(CpEFig)     

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
            CSEFig = choropleth_state_map("DestinationCumulativeDataset(Computer Science).csv")
            st.header('Interactive Map for Destination Data: CSE Major')
            st.plotly_chart(CSEFig)
    
    elif ["Electrical Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "93%", krinfo = "71/76", pr = "96%", prinfo = "68/71", avgsal = "$76,512", medsal = "$79,500", employ = "77%", grad = "16%")
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
            EEFig = choropleth_state_map("DestinationCumulativeDataset(Electrical Engineering).csv")
            st.header('Interactive Map for Destination Data: EE Major')
            st.plotly_chart(EEFig)
       
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
            ENEFig = choropleth_state_map("DestinationCumulativeDataset(Environmental Engineering).csv")
            st.header('Interactive Map for Destination Data: ENE Major')
            st.plotly_chart(ENEFig)

    elif ["Mechanical Engineering"] == ms:
        if ["2023"] == ms1:
            key_stats(year= "2023", kr = "92%", krinfo = "157/171", pr = "95%", prinfo = "149/157", avgsal = "$75,069", medsal = "$74,500", employ = "79%", grad = "15%")
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
            MEFig = choropleth_state_map("DestinationCumulativeDataset(Mechanical Engineering).csv")
            st.header('Interactive Map for Destination Data: ME Major')
            st.plotly_chart(MEFig)
    
    elif ["Material Sciences and Engineering"] == ms:
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
            MSFig = choropleth_state_map("DestinationCumulativeDataset(Materials Science and Eng).csv")
            st.header('Interactive Map for Destination Data: MS Major')
            st.plotly_chart(MSFig) 

    # Enrollment Data Section
    st.divider()
    st.subheader("ENROLLMENT DATA")
    st.header("Fall 2023 Enrollment Data")
    T1, T2, T3 = st.tabs(["Class Level", "Ethnicity", "Gender"])
    with T1:
        class_data = {
        'Class Level': ["First Year", "Sophomore", "Junior", "Senior"],
        'Count': [1847, 1501, 1249, 1536]}
        df = pd.DataFrame(class_data)
                                           
        major_fig = px.pie(df, values='Count', names='Class Level', title='Major Distribution', color_discrete_sequence=['#BFD641', '#FFB84C', '#5D9AE9', '#FFDE59'])
        
        major_fig.update_layout(
            legend=dict(
                traceorder='normal',  itemsizing='constant'
            ))
        
        st.plotly_chart(major_fig)

    with T2:
        EnrollEthnicity2023 = ['White', 'Asian', 'International', 'Hispanic/Latine', 'Black/African American', 'Two or More Races', 'Not Specified', 'American Indian/Alaskan Native', 'Hawaiian/Pacific Islander']
        data_ethnicity([3481,790,785,337,324,243,158,14,1], EnrollEthnicity2023)
    with T3:
        data_gender([4747, 1386])

    st.page_link("https://www.careers.egr.msu.edu/_files/ugd/bc0367_f52727d1f5fd44fb865b6bff7b45b6ef.xlsx?dn=Diversity_graphs%20Combined_12_9_22.xlsx", label = ":green[**Diversity Enrollment Data 5 Year Overview for Engineering**]")

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


    # Additional Links Section
    st.divider()
    st.subheader("ADDITIONAL LINKS")
    J2, J1 = st.columns(2)
    with J2:
        st.page_link("https://careernetwork.msu.edu/outcomes/", label= ":green[**Destination Data for All Majors**]")
        st.image("CareerServices.png", "Contains MSU Wide - All Colleges Destination Survey (2023) by our Career Services Network")
    with J1:
        st.page_link("https://engineering.msu.edu/academics/undergraduate-studies/enrollment-data", label= ":green[**College of Engineering Enrollment Data**]")
        st.image("EnrollmentData.png", "Gives a year by year enrollment and graduation date breakdown for the last 10 years")
    



if __name__ == "__main__":

    main()