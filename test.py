import plotly.express as px
import pandas as pd
import streamlit as st

def top_5_employer_states(file_path):
    # Read data from CSV into a DataFrame
    all_majors_data = pd.read_csv(file_path)
    
    # Count occurrences of each state in 'Employer State' column
    state_counts = all_majors_data['Employer State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']
    
    # Select top 5 states based on count
    top_5_states = state_counts.head(5)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display top 5 employer states (only names)
    with col1:
        if len(top_5_states) > 0:
            st.write('1st')
            st.write(top_5_states.iloc[0]['State'])

    with col2:
        if len(top_5_states) > 1:
            st.write('**2.**', top_5_states.iloc[1]['State'])

    with col3:
        if len(top_5_states) > 2:
            st.write('3rd')
            st.write(top_5_states.iloc[2]['State'])

    with col4:
        if len(top_5_states) > 3:
            st.write('4th')
            st.write(top_5_states.iloc[3]['State'])

    with col5:
        if len(top_5_states) > 4:
            st.write('5th')
            st.write(top_5_states.iloc[4]['State'])


# Example usage:
csv_file = "LATLONGDestinationCumulativeDataset(All Majors).csv"
top_5_employer_states(csv_file)
