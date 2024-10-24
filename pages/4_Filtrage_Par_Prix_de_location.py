import streamlit as st
import pandas as pd
import plotly.express as px
from read_file import read_excel_file

st.set_page_config(page_title="filtering by rental price")

@st.cache_data
def load_data(file_path):
    return read_excel_file(file_path)

from css import load_css
load_css()

st.title('Tanger Real Estate Data Analysis')
file_path = 'Data_visual_clean.xlsx'

df = load_data(file_path)
if 'Zone' in df.columns and 'Surface' in df.columns and 'Prix de location ( pu*superficie)' in df.columns:
    # Widget pour sélectionner la zone
    unique_zones = df['Zone'].unique()
    selected_zone = st.selectbox('Select an area:', unique_zones)

    # Sliders pour surface et prix de vente
    min_surface, max_surface = int(df['Surface'].min()), int(df['Surface'].max())
    surface_threshold = st.slider('Filter properties with a surface area less than (m²):', 
                                    min_value=min_surface, max_value=max_surface, 
                                    value=min_surface, key='surface_sale')
    min_price, max_price = int(df['Prix de location ( pu*superficie)'].min()), int(df['Prix de location ( pu*superficie)'].max())
    price_threshold = st.slider('Filter properties with a rental price lower than (DH):', 
                                min_value=min_price, max_value=max_price, 
                                value=min_price, key='price_sale')

    # Application des filtres
    filtered_data = df[(df['Zone'] == selected_zone) & 
                        (df['Surface'] < surface_threshold) & 
                        (df['Prix de location ( pu*superficie)'] < price_threshold)]
    
    st.write(f"Number of properties after filtering: {len(filtered_data)}")
    if st.checkbox('Show filtered data'):
        st.write(filtered_data)

    # Visualisation optionnelle
    if st.button('View the distribution of filtered rental prices'):
        fig = px.histogram(filtered_data, x='Prix de location ( pu*superficie)', 
                            title='Distribution des Prix de location Après Filtrage',
                            labels={'Prix de location ( pu*superficie)': 'Prix (DH)'},
                            color_discrete_sequence=['#636EFA'])
        st.plotly_chart(fig)
else:
    missing_cols = [col for col in ['Zone', 'Surface', 'Prix de location ( pu*superficie)'] if col not in df.columns]
    st.error(f"The necessary columns are not present in the file: {', '.join(missing_cols)}")
