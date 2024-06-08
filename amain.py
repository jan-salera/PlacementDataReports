import streamlit as st
import plotly.express as px
import numpy as np

def Key_Stats_KR():
    year = ['2022', '2023','2024']
    percentage = [93, 89, 90]
    colors = ['#18453B', '#008208', "#7BBD00"]
    kr_fig = px.bar(x=year, y=percentage, labels={'x':'Year', 'y':'Placement Rate (%)'}, color=year, 
    color_discrete_sequence=colors, width=180, height=300)

    st.plotly_chart(kr_fig)


col1, col2, col3 = st.columns(3)
with col1:
    kr_check = st.checkbox("See more", key=0)
    if kr_check:
        Key_Stats_KR()
with col2:
    pr_check = st.checkbox("See more", key=1)
    if pr_check:
        Key_Stats_KR()
with col3:
    kr_check = st.checkbox("See more", key=2)
    if kr_check:
        Key_Stats_KR()