import plotly.graph_objects as go

# Define your custom color palette
custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Create a Plotly color template using the custom colors
color_template = go.layout.Template(
    layout=go.Layout(
        colorway=custom_colors
    )
)

# Register the custom color template with Plotly
go.layout.Template.layout_templates['custom_template'] = color_template
go.layout.Template.defaults['layout']['template'] = 'custom_template'
