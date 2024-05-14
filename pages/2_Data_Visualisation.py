import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from openpyxl import load_workbook 
import seaborn as sns
import statsmodels.api as sm
from read_file import read_excel_file

st.set_page_config(page_title="Data visualisation")

@st.cache_data
def load_data(file_path):
    return read_excel_file(file_path)

from css import load_css
load_css()

def main():
    st.title('CapAlliance Data Analysis')
    file_path = 'data_visualisation.xlsx'

    df = load_data(file_path)
    nb_rows = st.slider("Choose number of rows you want to display", min_value=5, max_value=len(df), step=20)
    st.write(df.iloc[:nb_rows])

    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    tab_categorial, tab_numerical = st.tabs(["Categorical Variables", "Numerical Variables"])

    with tab_categorial:
        cat_col = st.selectbox('Select a categorical column for visualization', categorical_columns, key='cat_visual')

        tab_hist, tab_pie, tab_heatmap, analyse_cond = st.tabs(['Histogram', 'Pie Chart', 'Heatmap', 'Analyse Conditionel'])

        with tab_hist:
            if cat_col:
                type_counts = df[cat_col].value_counts().reset_index()
                type_counts.columns = [cat_col, 'Count']
                fig = px.bar(type_counts, x=cat_col, y='Count', title=f'Count of {cat_col}',
                             labels={cat_col: cat_col, 'Count': 'Count'},
                             color='Count',
                             color_continuous_scale=px.colors.sequential.Viridis)
                st.plotly_chart(fig)

        with tab_pie:
            if cat_col:
                type_counts = df[cat_col].value_counts().reset_index()
                type_counts.columns = [cat_col, 'Count']
                type_counts['Percentage'] = 100 * type_counts['Count'] / type_counts['Count'].sum()
                type_counts[cat_col] = type_counts[cat_col] + ' (' + type_counts['Percentage'].round(1).astype(str) + '%)'
                fig = px.pie(type_counts, names=cat_col, values='Count',
                             title=f'Distribution of {cat_col}',
                             color_discrete_sequence=px.colors.sequential.Viridis)
                st.plotly_chart(fig)

        with tab_heatmap:
            cat_col2 = st.selectbox('Select another categorical column', categorical_columns, key='cat2')
            if cat_col and cat_col2:
                if cat_col != cat_col2:
                    pivot_table = pd.crosstab(df[cat_col], df[cat_col2])
                    plt.figure(figsize=(12, 8))
                    sns.heatmap(pivot_table, annot=True, fmt="d", cmap='viridis')
                    plt.title(f'Frequency of {cat_col} by {cat_col2}')
                    plt.xlabel(cat_col2)
                    plt.ylabel(cat_col)
                    st.pyplot(plt)
                else:
                    st.error("Please select different columns for the heatmap.")
        with analyse_cond:
            numeric_col = st.selectbox("Choisir une colonne numérique:", numerical_columns)

            if st.button("Générer le graphique"):
                grouped_data = df.groupby(cat_col)[numeric_col].mean().reset_index()
                
                fig = px.bar(grouped_data, x=cat_col, y=numeric_col,
                             title=f'Moyenne de {numeric_col} par {cat_col}',
                             labels={numeric_col: f'Moyenne de {numeric_col}', cat_col: cat_col})
                st.plotly_chart(fig)

    with tab_numerical:
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Destribution de Surface', 'Destribution de Prix de vente', 'Destribution de Prix de location', 'Dependances entre les variables', 'Scatter', 'Correlation'])
        with tab1:
            if 'Surface' in df.columns:
                fig = px.histogram(df, x='Surface',
                                   nbins=int((20000 - 0) / 50), 
                                   title='Distribution des Surfaces',
                                   labels={'Surface': 'Surface (m²)'},
                                   color_discrete_sequence=['blue'])
                fig.update_layout(
                    xaxis_title='Surface (m²)',
                    yaxis_title='Fréquence',
                    bargap=0.1,  
                    xaxis=dict(
                        range=[0, 20000]
                    )
                )
                st.plotly_chart(fig)
        with tab2:
            if 'Prix de vente' in df.columns:
                fig = px.histogram(df, x='Prix de vente',
                                   nbins=int((1500000 - 0) / 50), 
                                   title='Distribution des Prix de vente',
                                   labels={'Prix de vente': 'Prix (Dh)'},
                                   color_discrete_sequence=['blue'])
                fig.update_layout(
                    xaxis_title='Prix de vente (DH)',
                    yaxis_title='Fréquence',
                    bargap=0.1,  
                    xaxis=dict(
                        range=[0, 1500000]
                    )
                )
                st.plotly_chart(fig)
        with tab3:
            fig = px.box(df, y='Prix de location ( pu*superficie)',
                         title='Box Plot of Rental Prices',
                         labels={'Prix de location ( pu*superficie)': 'Rental Price (Currency)'})
            fig.update_layout(yaxis_title='Prix de location ( pu*superficie)',
                              xaxis_title=' ')
            st.plotly_chart(fig)
        with tab4:
            data_type = st.selectbox("Select the type of data to display:", ['Surface', 'Prix de vente', 'Prix de location ( pu*superficie)'])
            category = st.selectbox("Select a category for grouping:", ['Zone', 'Type de bien'])

            if data_type in df.columns and category in df.columns:
                fig = px.violin(df, y=data_type, x=category, color=category, box=True, points="all",
                                title=f"Distribution of {data_type} by {category}")
                st.plotly_chart(fig)
            else:
                st.error("Selected columns do not exist in the DataFrame.")
        with tab5:
            var1 = st.selectbox("Choose the first variable:", numerical_columns)
            var2 = st.selectbox("Choose the second variable:", numerical_columns)
            if var1 and var2:
                fig = px.scatter(df, x=var1, y=var2, trendline="ols",
                                 title=f'Relationship between {var1} and {var2}')
                fig.update_layout(xaxis_title=var1, yaxis_title=var2)
                st.plotly_chart(fig)
        with tab6:
            if numerical_columns:
                corr_matrix = df[numerical_columns].corr()
                fig = px.imshow(corr_matrix,
                                labels=dict(x="Variables", y="Variables", color="Correlation"),
                                x=numerical_columns,
                                y=numerical_columns,
                                title="Correlation Matrix of Numerical Variables",
                                color_continuous_scale=px.colors.diverging.RdBu,
                                zmin=-1, zmax=1)  

                fig.update_xaxes(side="bottom")

                fig.update_layout(
                    xaxis_showgrid=False,
                    yaxis_showgrid=False,
                    xaxis_zeroline=False,
                    yaxis_zeroline=False,
                    width=600, height=600 
                )
                st.plotly_chart(fig)

if __name__ == '__main__':
    main()
