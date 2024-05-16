import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard")
def load_data():
    # Chargement des données
    return pd.read_excel('Data_visual_clean.xlsx')

from css import load_css
load_css()

def main():
    st.title('Dashboard - Analyse des Biens Immobiliers')

    df = load_data()

    # Calculs pour le résumé des données
    total_vente = len(df[df['Action commerciale'] == 'À vendre'])
    total_location = len(df[df['Action commerciale'] == 'À Louer'])
    prix_moyen_vente = df[df['Action commerciale'] == 'À vendre']['Prix de vente'].mean()
    prix_moyen_location = df[df['Action commerciale'] == 'À Louer']['Prix de location ( pu*superficie)'].mean()
    surface_moyenne = df['Surface'].mean()

    # Affichage des sections Statistiques Clés et Répartition des Biens par Zone côte à côte
    col1, col2 = st.columns(2)

    with col1:
        st.header('Statistiques Clés')
        st.markdown('<div class="st-emotion-cache-13ln4jf">', unsafe_allow_html=True)
        st.metric("Total Ventes", total_vente)
        st.metric("Total Locations", total_location)
        st.metric("Surface Moyenne (m²)", f"{surface_moyenne:.2f}")
        st.metric("Prix Moyen Vente (DH)", f"{prix_moyen_vente:,.2f}")
        st.metric("Prix Moyen Location (DH/m²)", f"{prix_moyen_location:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.header('Répartition des Biens par Zone')
        fig_zone = px.bar(df, x='Zone', color='Action commerciale', 
                          barmode='group', title='Répartition des Biens à Vendre et à Louer par Zone',
                          labels={'count': 'Nombre de Biens'})
        fig_zone.update_layout(height=400, margin=dict(t=30, b=30, l=0, r=0))
        st.plotly_chart(fig_zone, use_container_width=True)

    # Affichage des sections Visualisation des Prix et Détails des Propriétés côte à côte
    col3, col4 = st.columns(2)

    with col3:
        st.header('Visualisation des Prix')
        
        # Box plot pour les prix de vente
        fig_vente = px.box(df[df['Action commerciale'] == 'À vendre'], y='Prix de vente', title='Box Plot des Prix de Vente')
        fig_vente.update_layout(height=300, margin=dict(t=30, b=30, l=0, r=0))
        st.plotly_chart(fig_vente, use_container_width=True)
        
        # Scatter plot pour les prix de location en fonction de la surface
        fig_location = px.scatter(df[df['Action commerciale'] == 'À Louer'], x='Surface', y='Prix de location ( pu*superficie)', title='Prix de Location en fonction de la Surface')
        fig_location.update_layout(height=300, margin=dict(t=30, b=30, l=0, r=0))
        st.plotly_chart(fig_location, use_container_width=True)

    with col4:
        st.header('Détails des Propriétés')
        expensive_properties = df[df['Action commerciale'] == 'À vendre'].nlargest(5, 'Prix de vente')
        largest_properties = df.nlargest(5, 'Surface')
        st.subheader("Biens les Plus Chers à Vendre")
        st.dataframe(expensive_properties)
        st.subheader("Plus Grandes Propriétés Disponibles")
        st.dataframe(largest_properties)

if __name__ == '__main__':
    main()
