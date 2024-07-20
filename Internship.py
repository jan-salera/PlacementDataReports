import streamlit as st

#Initalize Functions Here
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
        st.header(avgsal21)
        st.write("2021 Average Internship Salary (" + count21 + " students)")
        st.header(medsal21)
        st.write("2021 Median Internship Salary (" + count21 + " students)")
    with C2: # second column 
        st.header(avgsal22)
        st.write("2022 Average Internship Salary (" + count22 + " students)")
        st.header(medsal22)
        st.write("2022 Median Internship Salary (" + count22 + " students)")
    with C3: # third column 
        st.header(avgsal23)
        st.write("2023 Average Internship Salary (" + count23 + " students)")
        st.header(medsal23)
        st.write("2023 Median Internship Salary (" + count23 + " students)")
    with C4: # fourth column 
        st.header(":green[" + avgsal2123 + "]")
        st.write("Three Year Cumulative Average Internship Salary (" +  count2123 + " students)")
        st.header(":green[" + medsal2123 + "]")
        st.write("Three Year Cumulative Median Internship Salary (" + count2123 + " students)") # turns the text into green

def main():
    st.header("Internship Data")

    options = ("All Engineering Majors", "Applied Engineering Sciences", "Biosystems Engineering", "Chemical Engineering", "Civil Engineering", "Computational Data Science", "Computer Engineering", "Computer Science", "Electrical Engineering", "Environmental Engineering", "Materials Science & Engineering", "Mechanical Engineering")
    ms_intern = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Major", label_visibility="visible", default=["All Engineering Majors"])

    if ms_intern == ["All Engineering Majors"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.header("Top Hiring Companies")
            C1, C2, C3, C4, C5 = st.columns(5)
            with C1:
                st.write("Amazon")
                st.image("https://th.bing.com/th/id/R.df3fc521dc6d79da661c279326ef247e?rik=lZmjPTGg6qWtEw&pid=ImgRaw&r=0")
            with C2:
                st.write("Ford")
                st.image("https://th.bing.com/th/id/OIP.rCier55RtLlFnTH9QIB4nwHaEK?rs=1&pid=ImgDetMainr=0")
            with C3:
                st.write("Google")
                st.image("https://logosmarcas.net/wp-content/uploads/2020/09/Google-Logo.png")
            with C4:
                st.write("Instagram")
                st.image("https://th.bing.com/th/id/OIP.izOOxDyHFwihHcQcKIExmQHaHa?rs=1&pid=ImgDetMain")
            with C5:
                st.write("Apple")
                st.image("https://logosmarcas.net/wp-content/uploads/2020/04/Apple-Logo.png")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()
    
    elif ms_intern == ["Applied Engineering Sciences"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()

    elif ms_intern == ["Biosystems Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()

    elif ms_intern == ["Chemical Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()
    
    elif ms_intern == ["Civil Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()

    elif ms_intern == ["Computational Data Science"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()
    
    elif ms_intern == ["Computer Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()
    
    elif ms_intern == ["Computer Science"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()
    
    elif ms_intern == ["Electrical Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()
    
    elif ms_intern == ["Environmental Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()

    elif ms_intern == ["Materials Science & Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()
    
    elif ms_intern == ["Mechanical Engineering"]:
        T1, T2, T3 = st.tabs(["By Employer", "By Geography", "By Salary"])
        with T1:
            st.write("Insert Top #? Companies")
            st.write("Insert By Company Circle Graph Here")
        with T2:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")
        with T3:
            st.write("Report Average and Median Salary Here")
            report_salary()

if __name__ == "__main__":
    main()