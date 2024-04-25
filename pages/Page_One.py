import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Suppress warnings
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load data from GitHub
@st.cache_data
def load_data_from_github(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return None

# Function to plot stacked bar chart with percentages for a specific category and another variable
@st.cache_data
def plot_stacked_bar_chart(data, x_column, y_column, category):
    # Filter out missing values for x_column and y_column
    filtered_data = data.dropna(subset=[x_column, y_column])

    # Convert the column to string to ensure compatibility for plotting
    filtered_data[x_column] = filtered_data[x_column].astype(str)

    # Filter data based on the selected category
    filtered_data = filtered_data[filtered_data[y_column] == category]

    # Calculate percentage for each category in x_column
    totals = filtered_data.groupby([x_column]).size()
    percentages = (totals / totals.sum()) * 100

    # Get unique categories for x_column
    categories = filtered_data[x_column].unique()

    # Define a custom color palette
    custom_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    # Create a color map for categories
    color_map = {category: custom_palette[i % len(custom_palette)] for i, category in enumerate(categories)}

    # Plot stacked bar chart
    fig = px.bar(filtered_data, x=x_column, color=y_column,
                 title=f"Relationship between {x_column} and {y_column} ({category})",
                 color_discrete_map=color_map)

    # Add percentage text annotations to the plot
    for i, (index, value) in enumerate(percentages.items()):
        fig.add_annotation(x=index, y=value, text=f"{value:.0f}%", showarrow=False, yshift=10, font=dict(color=color_map[index]))

    return fig

# Main function for Streamlit app
def main():
    # Set page configuration
    st.set_page_config(
        page_title="Ability to work & Income Change",
        page_icon="📊"
    )

    # Design Home Page
    st.title("Power BI-like Dashboard")
    st.markdown("## Welcome to the Dashboard!")

    # Get URL of the dataset on GitHub
    github_url = "https://raw.githubusercontent.com/NAKIBINGEGIDEON/data-analysis-and-visualization-project/92354269f67066df75a9fb6e47cbdcc820cbfc78/data.csv"

    # Load the dataset
    data = load_data_from_github(github_url)

    # Sidebar for navigation
    st.sidebar.header("Analysis Type")
    analysis_type = st.sidebar.radio("Select Analysis Type", ["Ability to Work", "Income Change"])

    if analysis_type == "Ability to Work":
        # Select another variable
        selected_variable = st.sidebar.selectbox("Select another variable", data.columns)

        # Plotting stacked bar chart for Ability to Work
        if st.button("Analyze Ability to Work"):
            fig = plot_stacked_bar_chart(data, selected_variable, "JobLoss", "Yes")
            st.subheader("Relationship between Job Loss (Yes) and Another Variable (Ability to Work)")
            st.plotly_chart(fig)
    
    elif analysis_type == "Income Change":
        # Select another variable
        selected_variable = st.sidebar.selectbox("Select another variable", data.columns)

        # Plotting stacked bar chart for Income Change
        if st.button("Analyze Income Change"):
            fig = plot_stacked_bar_chart(data, selected_variable, "IncomeChange", "Decreased a lot")
            st.subheader("Relationship between Income Change (Decreased a lot) and Another Variable")
            st.plotly_chart(fig)

# Entry point of the Streamlit app
if __name__ == "__main__":
    main()
