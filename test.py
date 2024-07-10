import plotly.express as px
import pandas as pd

# Sample data (replace with your actual data)
data = {
    'Year': ['Freshman', 'Sophomore', 'Junior', 'Senior'],
    'Count': [25, 20, 15, 30]  # Example counts
}

df = pd.DataFrame(data)

# Specify the order of categories for the legend
category_order = ['Freshman', 'Sophomore', 'Junior', 'Senior']

# Create the pie chart using Plotly Express
fig = px.pie(df, values='Count', names='Year', 
             title='Distribution of Students by Year',
             category_orders={'Year': category_order},
             labels={'Year': 'Year'})

# Show the plot
fig.show()