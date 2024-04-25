import streamlit as st
import pandas as pd

# Function to load data from GitHub
def load_data_from_github(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"An error occurred while loading the data: {str(e)}")
        return None

# Main function for Streamlit app
def main():
    # Set page configuration
    st.set_page_config(
        page_title="Impact of COVID-19 in Sub-Saharan Africa",
        page_icon="🌍",
        layout="wide"
    )

    # Add CSS for styling
    st.markdown(
        """
        <style>
        body {
            background-color: white;
        }
        .css-1yqjytt {
            text-align: center;
            font-size: 24px;
        }
        .css-1l02zno.e1lsy6010 {
            background: url("https://raw.githubusercontent.com/NAKIBINGEGIDEON/newdataviz/b5bf27fb269868001d44e10e81b69c7c88f63f76/banner_icons_community2.jpg") no-repeat center center;
            background-size: cover;
            padding: 20px;
        }
        .css-1dbjc4n.r-ku1wi2.r-1ylenci.r-1phboty.r-1d2f490.r-1udh08x.r-u8s1d.r-zchlnj.r-ipm5af {
            text-align: justify;
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Design Home Page
    st.title("Impact of COVID-19 in Sub-Saharan Africa")
    # Justify the abstract
    st.markdown("<div style='text-align: justify;'>"
                "<h4>Index Terms—Sub-Saharan, Economic impact, Data Analysis, Data Visualization, COVID-19</h4>"
                "</div>", unsafe_allow_html=True)

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
