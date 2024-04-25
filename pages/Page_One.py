import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from GitHub
@st.cache_data()
def load_data_from_github(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return None

# Function to plot stacked bar chart with percentages for "Decreased a lot" category of IncomeChange and filtered variable
@st.cache_data()
def plot_stacked_bar_chart(data, x_column, y_column):
    # Filter out missing values for x_column and y_column
    filtered_data = data.dropna(subset=[x_column, y_column])

    # Convert the column to string to ensure compatibility for plotting
    filtered_data[x_column] = filtered_data[x_column].astype(str)

    # Filter data for "Decreased a lot" category of IncomeChange
    filtered_data = filtered_data[filtered_data["IncomeChange"] == "Decreased a lot"]

    # Calculate percentage for each category
    totals = filtered_data.groupby([x_column]).size()
    percentages = (totals / totals.sum()) * 100

    # Plot stacked bar chart
    fig = px.bar(filtered_data, x=x_column, color="IncomeChange",
                 title=f"Relationship between {x_column} and Income Change",
                 category_orders={y_column: sorted(filtered_data[y_column].astype(str).unique())},
                 color_discrete_map={"Decreased a lot": "#FF5733"})

    # Add percentage text annotations to the plot
    for index, value in percentages.items():
        fig.add_annotation(x=index, y=value, text=f"{value:.0f}%", showarrow=False)

    return fig

# Main function for Streamlit app
def main():
    # Set page configuration
    st.set_page_config(
        page_title="Power BI-like Dashboard",
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

        # Filter for only Yes and No for JobLoss
        filtered_data = data[data["JobLoss"].isin(["Yes", "No"])]

        # Plotting stacked bar chart
        if st.button("Analyze Ability to Work"):
            fig = plot_stacked_bar_chart(filtered_data, selected_variable, "JobLoss")
            st.subheader("Relationship between Job Loss (Yes) and Another Variable")
            st.plotly_chart(fig)

    elif analysis_type == "Income Change":
        # Select another variable
        selected_variable = st.sidebar.selectbox("Select another variable", data.columns)

        # Plotting income change
        if st.button("Analyze Income Change"):
            fig = plot_stacked_bar_chart(data, selected_variable, "IncomeChange")
            st.subheader("Relationship between Income Change (Decreased a lot) and Another Variable")
            st.plotly_chart(fig)

# Entry point of the Streamlit app
if __name__ == "__main__":
    main()
