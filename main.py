import streamlit as st

st.title("**PLACEMENT DATA & REPORTS**")
st.header("DESTINATION DATA")

st.write("**Engineering 2023 Graduate Outcomes**")
st.write("Summary of placement, salary and geographic destinations for all undergraduate students in the College of Engineering")
options = ("Applied Engineering Sciences", "Biosystems Engineering", "Computational Data Science", "Civil Engineering", "Chemical Engineering", "Computer Engineering", "Computer Science", "Electrical Engineering", "Enviornmental Engineering", "Mechanical Engineering", "Material Science")

ms = st.multiselect("empty label name", options=options, placeholder = "Filter By Major", label_visibility="collapsed")

if ms == ["Applied Engineering Sciences"]:
    st.write("You chose to sort by :green[Applied Engineering Sciences]")
