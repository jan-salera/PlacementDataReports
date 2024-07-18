import streamlit as st
import plotly.express as px

#Initalize Functions Here
def report_salary(avgsal = "$10,000", medsal = "$10,000"):
    C1, C2 = st.columns(2) 

    with C1: 
        st.header(avgsal)
        st.write("Average Internship Salary")
    with C2:
        st.header(medsal)
        st.write("Median Internship Salary")


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


def main():
    st.header("Internship Data")

    options = ("Cumulative Data 2021 - 2023", "2023", "2022", "2021")
    ms_intern = st.multiselect("Note: Only select one option per filter.", options=options, placeholder = "Filter By Year", label_visibility="visible", default=["2021"])

    if ms_intern == ["Cumulative Data 2021 - 2023"]:
        T1, T2, T3 = st.tabs(["By Major", "By Employer", "By Geography"])
        with T1:
            st.write("Insert By Major Circle Graph Here")
            data_major()
            st.write("Report Average and Median Salary Here")
            report_salary()
        with T2:
            st.write("Insert By Company Circle Graph Here")
            data_major()
        with T3:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")

    elif ms_intern == ["2023"]:
        T1, T2, T3 = st.tabs(["By Major", "By Employer", "By Geography"])
        with T1:
            st.write("Insert By Major Circle Graph Here")
            data_major()
            st.write("Report Average and Median Salary Here")
            report_salary()
        with T2:
            st.write("Insert By Company Circle Graph Here")
            data_major()
        with T3:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")

    elif ms_intern == ["2022"]:
        T1, T2, T3 = st.tabs(["By Major", "By Employer", "By Geography"])
        with T1:
            st.write("Insert By Major Circle Graph Here")
            data_major()
            st.write("Report Average and Median Salary Here")
            report_salary()
        with T2:
            st.write("Insert By Company Circle Graph Here")
            data_major()
        with T3:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")

    elif ms_intern == ["2021"]:
        T1, T2, T3 = st.tabs(["By Major", "By Employer", "By Geography"])
        with T1:
            st.write("Insert By Major Circle Graph Here")
            data_major()
            st.write("Report Average and Median Salary Here")
            report_salary()
        with T2:
            st.write("Insert By Company Circle Graph Here")
            data_major()
        with T3:
            st.write("Insert Chloropleth State Maps Here")
            st.write("Insert Chloropleth City Maps Here")

if __name__ == "__main__":
    main()