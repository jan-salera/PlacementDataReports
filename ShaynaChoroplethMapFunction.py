def choropleth_state_map(file_path, name_of_major_category = "All"):
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
        title='Number of Employed ", name_of_major_category, " Spartan Graduates in the United States (Log-Scaled)',
        range_color=(state_counts['LogCount'].min(), state_counts['LogCount'].max()),  # Set the color scale range
        hover_data={'State': True, 'Count': True, 'StateAbbrev': False, 'LogCount': False}
    )
    return fig
