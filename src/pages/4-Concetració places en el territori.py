import streamlit as st
import pandas as pd
import re
from streamlit_folium import folium_static
import folium
from folium.plugins import HeatMap

st.set_page_config(
    layout="wide",
    page_title="Concentració places en el territori"
)

# Títol
st.title("Concentració places en el territori")

'''
Finalment, podem observar la distribució de places turístiques en el territori.
El mapa és interactiu i permet l'observació en detall de cada índret de l'illa.
'''

df_habitatges = pd.read_csv("data/Habitatges.csv")
df_allotjaments = pd.read_csv("data/Allotjaments.csv")

df_habitatges['Tipus'] = 'Habitatge'  
df_allotjaments['Tipus'] = 'Allotjament' 

df_habitatges = df_habitatges[['Places', 'Tipus', 'Coordenades']]
df_allotjaments = df_allotjaments[['Places', 'Tipus', 'Columna amb nova georeferència']]


df_habitatges = df_habitatges.dropna(subset=['Coordenades'])
df_habitatges = df_habitatges.dropna(subset=['Places'])

df_allotjaments = df_allotjaments.dropna(subset=['Columna amb nova georeferència'])
df_allotjaments.rename(columns={'Columna amb nova georeferència': 'Coordenades'}, inplace=True)

df_combined = pd.concat([df_habitatges, df_allotjaments], ignore_index=True)

def wkt_to_latlon(wkt_point):
    match = re.match(r'POINT \(([^ ]+) ([^ ]+)\)', wkt_point)
    if match:
        return float(match.group(2)), float(match.group(1))  # Retorna (lat, lon)


df_combined['Coordinates'] = df_combined['Coordenades'].apply(wkt_to_latlon)
df_combined[['Latitude', 'Longitude']] = pd.DataFrame(df_combined['Coordinates'].tolist(), index=df_combined.index)

m = folium.Map(location=[39.55263, 2.9],
               zoom_start=10)

heat_data = [[row['Latitude'], row['Longitude'], row['Places']] for index, row in df_combined.iterrows()]

HeatMap(heat_data).add_to(m)

folium_static(m, width=850, height=850)
