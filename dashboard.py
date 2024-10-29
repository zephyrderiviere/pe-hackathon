from common_test import *
from visuals_with_geopandas import *

import streamlit as st
import streamlit_folium as st_f


def main_page():
    """ Main page of the website """
    
    st.title("Earthquake analysis - Hackathon")
    st.subheader("By Armand, Romain, Zéphyr et Mathis")


def general():
    """ Page with all general information on the database """

    st.title("General information : ")
    st.subheader("Get to know the database we experimented with !")

    with open("./data/earthquake.csv") as f:
        st.download_button("Download the database to try it out for yourself", f, file_name="earthquakes_db.csv")
    
    st.markdown(
        f"""This open-source database can be found [](here).
            The database consists in **{len(df)}** different earthquakes,
            ranging from **{df.Date.min().date()}** to **{df.Date.max().date()}** ! """
    )


    st.text("Visualisation of all earthquakes :")
    st.image("./map.png")
    
    st.text("It is not fully complete though, here are all the missing values :")
    missing_values = df.isna().sum()
    st.dataframe(df.isna().sum())
    
    st.text("Finally, here is a small overview of the actual database : ")
    st.dataframe(df.iloc[:10])

def interactive_map():
    """ Interactive map page """

    st.title("Interactive map to look around")
    st_f.st_folium(earth_map)
    

page_names_to_funcs = {
    "Introduction": main_page,
    "General information": general,
    "Inteactive map" : interactive_map
}

page_selection = st.sidebar.selectbox("Choose your page : ", page_names_to_funcs.keys())
page_names_to_funcs[page_selection]()

# @st.cache_resource
# def initialization():
#     main_page()
# initialization()
