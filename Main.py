import streamlit as st
from css import load_css


st.set_page_config(page_title="Main page")
st.image("analyst.jpg", use_column_width=True)
load_css()
st.header("Welcome to Tanger Real Estate Data Analysis!")
st.write("""
         Welcome to our real estate data analysis platform. Here, you can upload, visualize, 
         and analyze real estate data to make informed decisions based on in-depth market analysis. 
         Use the tabs on the left to navigate between different features such as data visualization, 
         filtering data for sales or rentals, and more.
         """)

st.subheader("How to use this application")
st.write("""
          - **Upload Data**: Start by uploading your real estate data using the upload button.
          - **Data Visualization**: Go to the visualization tab to see data distributions and trends.
          - **Data Filtering**: Use the filtering options under the sales and rental tabs to refine the displayed data.
          - **Analysis**: Observe the filtered results and analyze the data using the provided charts and statistics.
          """)


