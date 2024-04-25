import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Load the data
data_url = "https://raw.githubusercontent.com/NAKIBINGEGIDEON/data-analysis-and-visualization-project/92354269f67066df75a9fb6e47cbdcc820cbfc78/data.csv"
df = pd.read_csv(data_url)

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

# Sidebar for selecting variables
st.sidebar.title('Dashboard Settings')
selected_variable_x = st.sidebar.selectbox('Select X Variable', variables)
selected_variable_y = st.sidebar.selectbox('Select Y Variable', variables)

# Create a cross-tabulation of the selected variables
cross_tab = pd.crosstab(df[selected_variable_x], df[selected_variable_y], normalize='columns') * 100

# Create an interactive heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(cross_tab, annot=True, fmt=".0f", cmap="BuPu")
plt.title(f"Heatmap: {selected_variable_x} vs {selected_variable_y}")
plt.xlabel(selected_variable_y)
plt.ylabel(selected_variable_x)

# Display the heatmap
st.pyplot(heatmap.figure)
