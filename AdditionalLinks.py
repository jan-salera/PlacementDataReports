import streamlit as st

J2, J1 = st.columns(2)
with J2:
    st.page_link("https://careernetwork.msu.edu/outcomes/", label= ":green[**Destination Data for All Majors**]")
    st.image("CareerServices.png", "Contains MSU Wide - All Colleges Destination Survey (2023) by our Career Services Network")
with J1:
    st.page_link("https://engineering.msu.edu/academics/undergraduate-studies/enrollment-data", label= ":green[**College of Engineering Enrollment Data**]")
    st.image("EnrollmentData.png", "Gives a year by year enrollment and graduation date breakdown for the last 10 years")
