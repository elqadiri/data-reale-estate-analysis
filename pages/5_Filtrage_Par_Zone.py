import streamlit as st
import pandas as pd
import plotly.express as px
from read_file import read_excel_file

st.set_page_config(page_title="filtering by area")

@st.cache_data
def load_data(file_path):
    return read_excel_file(file_path)

from css import load_css
load_css()

file_path = 'Data_visual_clean.xlsx'

def main():
    st.title('Analysis of Real Estate by Area')

    df = load_data(file_path)

    grouped_df = df.groupby(['Zone', 'Action commerciale']).size().reset_index(name='Nombre')

    zone_options = df['Zone'].unique()
    selected_zone = st.selectbox('Select an area:', zone_options)

    filtered_data = grouped_df[grouped_df['Zone'] == selected_zone]

    if not filtered_data.empty:
        st.write(f"Résultats pour la zone {selected_zone}:")
        st.write(filtered_data)

        fig = px.bar(filtered_data, x='Action commerciale', y='Nombre', color='Action commerciale',
                     title=f'Number of goods per commercial action for {selected_zone}',
                     labels={'Nombre': 'Nombre de biens', 'Action commerciale': 'Type d\'action'})
        st.plotly_chart(fig)

        detailed_data = df[df['Zone'] == selected_zone]
        st.write("Details of properties in selected area:")
        st.dataframe(detailed_data) 
    else:
        st.error("No data available for selected area.")

if __name__ == '__main__':
    main()
