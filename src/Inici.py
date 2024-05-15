import streamlit as st
import geopandas as gpd
import pandas as pd


st.set_page_config(
    layout="wide",
    page_title="Inici"
)

# Títol
st.title("Habitatges turístics a Mallorca")

df_habitatges = pd.read_csv("../data/Habitatges.csv")


total_habitatges = df_habitatges.shape[0]

'''
Actualment a Mallorca hi ha un debat sobre les places turístiques.

A continuació es presentaran les dades corresponents als polèmics habitatges turístics de l'illa de Mallorca.

'''

st.write(f"Actualment hi ha un total de {total_habitatges} de d'habitatgres turístics")

"""
Font de dades:

Habitatges Turístics Mallorca
Govern de les Illes Balears. Catàleg de dades obertes Illes Balears

https://catalegdades.caib.cat/Turisme/Habitatges-Tur-stics-Mallorca/3q3t-usfm/about_data


GeoJSON de cadascuna de les illes que conformen l'arxipèlag balear

https://github.com/enmiquelangel/geojsonsillesbalears

PAC3 de Visualització de dades








"""

