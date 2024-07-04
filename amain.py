import streamlit as st
import plotly.express as px
import pandas as pd

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



st.markdown("""<h1 style="font-weight: normal; text-align:center;">Spartan Engineering Key Statistics </h1>""", unsafe_allow_html=True)

# year = ['2021', '2022','2023']
# percentage = [96.0, 98.0, 94.3]
# colors = ['#18453B', '#008208', "#7BBD00"]
# kr_fig = px.bar(x=year, y=percentage, labels={'x':'Year', 'y':'Placement Rate (%)'}, color=year, 
# color_discrete_sequence=colors, width=200, height=300)

# df = pd.DataFrame(dict(
#     x = [2021, 2022, 2023],
#     y = [1, 2, 3]
# ))
# fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
# fig.show()

# st.plotly_chart(kr_fig)


C1, C2, C3, C4 = st.columns(4)
with C1:
    st.header(":green[84.4%]")
    st.write("Three Year Average Knowledge Rate")

    # st.subheader("2021")
    # st.header("80.3%")
    # st.write("Knowledge Rate")
    # st.header("96.0%")
    # st.write("Placement Rate")
    # st.header("$69,838")
    # st.write("Average Salary")
    # st.header("$70,000")
    # st.write("Median Salary")

with C2:
    st.header(":green[96.1%]")
    st.write("Three Year Average Placement Rate")
    # st.subheader("2022")
    # st.header("82.5%")
    # st.write("Knowledge Rate")
    # st.header("98.0%")
    # st.write("Placement Rate")
    # st.header("$73,922")
    # st.write("Average Salary")
    # st.header("$72,500")
    # st.write("Median Salary")

with C3:
    st.header(":green[$73,522]")
    st.write("Three Year Average Average Salary")
    # st.subheader("2023")
    # st.header("90.5%")
    # st.write("Knowledge Rate")
    # st.header("94.3%")
    # st.write("Placement Rate")
    # st.header("$76,806")
    # st.write("Average Salary")
    # st.header("$75,000")
    # st.write("Median Salary")

with C4:
    st.header(":green[$72,500]")
    st.write("Three Year Average Median Salary")
    # st.subheader("3 Yr Average")
    # st.header(":green[84.4%]")
    # st.write("Knowledge Rate")
    # st.header(":green[96.1%]")
    # st.write("Placement Rate")
    # st.header(":green[$73,522]")
    # st.write("Average Salary")
    # st.header(":green[$72,500]")
    # st.write("Median Salary")

D1, D2 = st.columns(2)

with D1:
    data = {
        'Year': [2021, 2022, 2023],
        'Knowledge Rate (%)': [80.3, 82.5, 90.5]
    }
    df = pd.DataFrame(data)

    # Create line plot using plotly.express
    fig = px.line(df, x='Year', y='Knowledge Rate (%)', title='Knowledge Rate Trend from 2021 to 2023', range_x= [2021, 2023], range_y = [80,95], height= 300, width= 300)

    # Customize axes labels (optional)
    fig.update_layout(
        xaxis=dict(
        tickmode='linear',  # Set tick mode to linear
        tick0=2021,
        dtick=1)
    )

    # Show the graph
    st.plotly_chart(fig)

    saldata = {
        'Year': [2021, 2022, 2023],
        'Average Salary ($)': [69838, 73922, 76806]
    }
    df = pd.DataFrame(saldata)

    # Create line plot using plotly.express
    fig1 = px.line(df, x='Year', y='Average Salary ($)', title='Average Salary Trend from 2021 to 2023', range_x= [2021, 2023], range_y = [69000,78000], height= 300, width= 300)

    # Customize axes labels (optional)
    fig1.update_layout(
        xaxis=dict(
        tickmode='linear', # Set tick mode to linear
        tick0=2021,
        dtick=1)
    )

    # Show the graph
    st.plotly_chart(fig1)

with D2:

    data = {
        'Year': [2021, 2022, 2023],
        'Placement Rate (%)': [96.0, 98.0, 94.3]
    }

    df = pd.DataFrame(data)

    # Create line plot using plotly.express
    fig = px.line(df, x='Year', y='Placement Rate (%)', title='Placement Rate Trend from 2021 to 2023', range_x= [2021, 2023], range_y = [90,100], height= 300, width= 300)

    # Customize axes labels (optional)
    fig.update_layout(
        xaxis=dict(
        tickmode='linear',  # Set tick mode to linear
        tick0=2021,
        dtick=1)
    )

    # Show the graph
    st.plotly_chart(fig)

    saldata = {
        'Year': [2021, 2022, 2023],
        'Median Salary ($)': [70000, 72500, 75000]
    }
    df = pd.DataFrame(saldata)

    # Create line plot using plotly.express
    fig1 = px.line(df, x='Year', y='Median Salary ($)', title='Median Salary Trend from 2021 to 2023', range_x= [2021, 2023], range_y = [70000,75000], height= 300, width= 300)

    # Customize axes labels (optional)
    fig1.update_layout(
        xaxis=dict(
        tickmode='linear', # Set tick mode to linear
        tick0=2021,
        dtick=1)
    )

    # Show the graph
    st.plotly_chart(fig1)



C1, C2, C3, C4 = st.columns(4)
with C1:
    st.subheader("2021")
    st.header("80.3%")
    st.write("Knowledge Rate")
    st.header("96.0%")
    st.write("Placement Rate")
    st.header("$69,838")
    st.write("Average Salary")
    st.header("$70,000")
    st.write("Median Salary")

with C2:
    st.subheader("2022")
    st.header("82.5%")
    st.write("Knowledge Rate")
    st.header("98.0%")
    st.write("Placement Rate")
    st.header("$73,922")
    st.write("Average Salary")
    st.header("$72,500")
    st.write("Median Salary")

with C3:
    st.subheader("2023")
    st.header("90.5%")
    st.write("Knowledge Rate")
    st.header("94.3%")
    st.write("Placement Rate")
    st.header("$76,806")
    st.write("Average Salary")
    st.header("$75,000")
    st.write("Median Salary")

with C4:
    st.subheader("3 Yr Average")
    st.header(":green[84.4%]")
    st.write("Knowledge Rate")
    st.header(":green[96.1%]")
    st.write("Placement Rate")
    st.header(":green[$73,522]")
    st.write("Average Salary")
    st.header(":green[$72,500]")
    st.write("Median Salary")
    