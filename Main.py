import streamlit as st
from css import load_css


st.set_page_config(page_title="Main page")
st.image("analyst.jpg", use_column_width=True)
load_css()
st.header("Bienvenue sur CapAlliance Data Analysis!")
st.write("""
         Bienvenue sur notre plateforme d'analyse de données immobilières. Ici, vous pouvez charger, visualiser, 
         et analyser des données immobilières pour prendre des décisions éclairées basées sur des analyses de marché approfondies. 
         Utilisez les onglets à gauche pour naviguer entre différentes fonctionnalités telles que la visualisation de données, 
         le filtrage des données pour les ventes ou la location, et plus encore.
         """)

st.subheader("Comment utiliser cette application")
st.write("""
          - **Charger des Données**: Commencez par charger vos données immobilières via le bouton de téléchargement.
          - **Visualisation des Données**: Accédez à l'onglet de visualisation pour voir les distributions et tendances des données.
          - **Filtrage des Données**: Utilisez les options de filtrage sous les onglets de vente et de location pour affiner les données affichées.
          - **Analyse**: Observez les résultats des filtres et analysez les données à l'aide des graphiques et des statistiques fournies.
          """)


