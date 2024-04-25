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
                "<h3>In response to the worldwide COVID-19 outbreak, many countries in Sub-Saharan Africa followed the same strategy as high-income countries and implemented strict lockdown measures to contain the spread of the virus. Some countries had imposed business or workplace closures, others severely restricted public and private transport or had closed their borders. Using the data from a study conducted by GeoPoll in five countries in sub-Saharan Africa: A majority, 60%, of those who were employed from January – March 2020 say that COVID-19 has stopped them from being able to work, with Nigeria having the highest number of job loss of 24.0% and Mozambique having the least number of job loss of 16.8% moreover 51.2% of the total populations are informal workers and 19.0% of them don’t have any hope of job regain after the pandemic. While the impact of the economic crisis on developing countries is the subject of a growing number of studies, there is limited work on the direct and immediate economic effect of containment measures of coronavirus in developing countries. This project is an attempt to quantify the economic impact of Coronavirus on the five Sub-Saharan African countries by using descriptive analysis and various visualization approaches.</h3>"
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
