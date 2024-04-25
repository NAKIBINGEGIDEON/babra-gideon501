

import streamlit as st
import pandas as pd

# Define countries with latitude and longitude data
countries = {
    'Nigeria': {'lat': 9.082, 'lon': 8.675},
    'Ivory Coast': {'lat': 7.54, 'lon': -5.5471},
    'Kenya': {'lat': 1.2921, 'lon': 36.8219},
    'Mozambique': {'lat': -18.665695, 'lon': 35.529562},
    'South Africa': {'lat': -30.5595, 'lon': 22.9375}  # Adding South Africa
}

# Function to load data from GitHub
def load_data_from_github(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return None

# Function to plot static map with markers
def plot_static_map():
    st.subheader("Countries with Data Collection")
    for country in countries.keys():
        st.markdown(f"- {country}")

    st.subheader("Map of Data Collection Countries")
    st.map(countries.values())

# Main function for Streamlit app
def main():
    # Set page configuration
    st.set_page_config(
        page_title="Impact of COVID-19 in Sub-Saharan Africa",
        page_icon="🌍"
    )

    # Design Home Page
    st.title("Impact of COVID-19 in Sub-Saharan Africa")
    st.markdown("## Welcome to the Dashboard!")

    # Display static map with markers
    plot_static_map()

    # Get URL of the dataset on GitHub
    github_url = "https://raw.githubusercontent.com/NAKIBINGEGIDEON/data-analysis-and-visualization-project/92354269f67066df75a9fb6e47cbdcc820cbfc78/data.csv"

    # Load the dataset
    data = load_data_from_github(github_url)

    if data is not None:
        st.header("Dataset Preview:")
        st.write(data.head())

# Entry point of the Streamlit app
if __name__ == "__main__":
    main()
