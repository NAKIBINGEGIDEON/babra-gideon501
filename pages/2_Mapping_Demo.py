import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px  # Import plotly express

# Load the data
data_url = "https://raw.githubusercontent.com/NAKIBINGEGIDEON/data-analysis-and-visualization-project/92354269f67066df75a9fb6e47cbdcc820cbfc78/data.csv"
df = pd.read_csv(data_url)

# Define countries with latitude and longitude data
countries = {
    "Ivory Coast (Cote D'Ivoire)": {'lat': 7.54, 'lon': -5.5471},
    'Kenya': {'lat': 1.2921, 'lon': 36.8219},
    'Mozambique': {'lat': -18.665695, 'lon': 35.529562},
    'Nigeria': {'lat': 9.082, 'lon': 8.675},
    'South Africa': {'lat': -30.5595, 'lon': 22.9375}
}

# Get unique variables
variables = df.columns

# Streamlit app
st.set_page_config(layout="wide")  # Set layout to wide

# Add general title
st.markdown(
    """
    <div style="text-align:center">
        <h1>African Countries Dashboard</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar for selecting variable
st.sidebar.title('Dashboard Settings')
selected_variable = st.sidebar.selectbox('Select Variable to Visualize', variables)

# Create a layout for the map and radial column chart
col1, col2 = st.columns((2, 1))  # Divide page into two columns

# Create a section for the map
col1.subheader('Interactive Map')

# Create figure for the map
fig_map = go.Figure()

# Add scattergeo for each country
for country, coords in countries.items():
    # Filter data for the selected country and remove NaN values
    country_data = df[df['Country'] == country][selected_variable].dropna()
    if not country_data.empty:
        # Calculate percentage for the selected variable
        total_responses = country_data.count()
        variable_counts = country_data.value_counts()
        percentages = (variable_counts / total_responses) * 100

        # Add country marker to the map with percentage text
        text = f"<b>{country}</b><br>{selected_variable}<br>"
        for value, percentage in percentages.items():
            text += f"{value}: {percentage:.0f}%<br>"
            # Add big ol' number annotations
            fig_map.add_annotation(
                x=coords['lon'],
                y=coords['lat'],
                text=str(round(float(percentage))),
                font=dict(size=20),
                showarrow=False
            )
        fig_map.add_trace(
            go.Scattergeo(
                lon=[coords['lon']],
                lat=[coords['lat']],
                text=text,
                mode='markers',
                marker=dict(size=percentages.values, color=percentages.values, colorscale='Reds',
                            cmin=0, cmax=100, colorbar=dict(title='Percentage')),
                hoverinfo='text',
                showlegend=False
            )
        )

# Set layout for map
fig_map.update_geos(projection_type="natural earth", showcoastlines=True, showcountries=True)
fig_map.update_layout(title_text=f'Map of African Countries with {selected_variable} Distribution', 
                  geo=dict(showframe=False, showcoastlines=True, coastlinecolor="Black",
                           showocean=True, oceancolor='LightBlue'),
                  margin=dict(l=0, r=0, t=30, b=0))

# Display the map
col1.plotly_chart(fig_map)

# Create a section for the radial column chart
col2.subheader(f'Overall Distribution of {selected_variable}')

# Filter out NaN values
variable_counts = df[selected_variable].dropna().value_counts()
variable_counts_percentage = (variable_counts / variable_counts.sum()) * 100

fig_radial = go.Figure()

# Add separate trace for each category
for value, percentage in variable_counts_percentage.items():
    fig_radial.add_trace(go.Barpolar(
        r=[percentage],
        theta=[value],
        name=value,  # Assign label for legend
        marker_color=px.colors.qualitative.Plotly[len(fig_radial.data)],  # Assign custom color
        hoverinfo='text',
        hovertext=f'{value}: {percentage:.0f}%',  # Add hover text
        width=0.5
    ))

fig_radial.update_layout(
    title=f'Overall Distribution of {selected_variable}',
    font=dict(size=12, color='black'),  # Customize text font and color
    polar=dict(radialaxis=dict(visible=True, showticklabels=False), angularaxis=dict(direction='clockwise')),
    height=600,  # Increase the height of the chart
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)  # Position the legend
)

# Display the radial column chart
col2.plotly_chart(fig_radial)
