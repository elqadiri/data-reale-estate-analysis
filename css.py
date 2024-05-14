import streamlit as st

def load_css():
    css = """
<style>

    [data-testid="stSidebar"], [data-testid="stHeader"] {
        background-color: #2C3E50;  /* Dark blue shade */
        color: white !important;
    }
    [data-testid="stSidebar"] {
        font-weight: bold;
        box-shadow: 2px 6px 8px rgba(0, 0, 0, 0.5);
    }

    [data-testid="stSidebarNavLink"] {
        padding: 8px 16px;
        font-family: 'Roboto', sans-serif;
        border-radius: 5px;
        transition: background-color 0.3s, color 0.3s;
    }
    [data-testid="stSidebarNavLink"]:hover {
        background-color: #34495E;  /* Slightly lighter blue for hover */
        color: #ECF0F1;
    }
    [data-testid="stHeader"] {
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    .st-emotion-cache-1m6wrpk {
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow: auto;
        background-color: transparent; /* Use transparent for more adaptive styling */
    }
    .st-emotion-cache-1v0mbdj.e115fcil1 img {
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Smooth transition for transformations */
        border: 2px solid #2a9d8f; /* Example border color */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.6); /* Shadow for depth */
    }

    .st-emotion-cache-1v0mbdj.e115fcil1 img:hover {
        transform: scale(1.05); /* Scale up on hover */
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.8); /* Darker shadow on hover */
    }
    [data-testid="StyledLinkIconContainer"],p,li{
    color : black;
    }
    .st-emotion-cache-bm2z3a {
        background-color: white;
    }
    .st-emotion-cache-4d1onx p {
    color: white;
    }
    [data-testid="stSidebarNavLink"]:hover{
    padding : 15px;
    box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);
    }

    .st-emotion-cache-1wivap2 {
        overflow-wrap: normal;
        text-overflow: ellipsis;
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        font-family: "Source Sans Pro", sans-serif;
        line-height: normal;
        vertical-align: middle;
        font-size: 18px;
        color: black;
    }
    .st-emotion-cache-13ln4jf {
    width: 100%;
    padding: 2rem 1rem 1rem;
    max-width: 75rem;
   }
   
/* Styles pour les labels des métriques */
.st-emotion-cache-1tpl0xr p {
    font-size: 1.1rem; /* Taille de police personnalisée pour les labels */
    font-weight: 800;
    color: #666; /* Couleur du texte pour les labels */
}

/* Styles pour les valeurs des métriques */
.st-emotion-cache-1wivap2 {
    font-size: 1.5rem; /* Taille de police personnalisée pour les valeurs */
    font-weight: bold;
    color: #333; /* Couleur du texte pour les valeurs */
    text-align: center; /* Alignement du texte */
}





</style>
    """
    st.markdown(css, unsafe_allow_html=True)
