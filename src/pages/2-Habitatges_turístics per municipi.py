import streamlit as st
import geopandas as gpd
from streamlit_folium import folium_static
import folium
import pandas as pd
from branca.colormap import LinearColormap


# Títol
st.title("Habitatges turístics per municipis de Mallorca")

# Càrrega habitatges turístics
df_habitatges = pd.read_csv("data/Habitatges.csv")
df_habitatges_municipi = df_habitatges.groupby('Municipi').size()

# Càrrega geojson municipis
df_geojson = gpd.read_file("../data/mallorca.json")
# Transformem camp per poder relacionar les dades
df_geojson['Municipi'] = df_geojson['neighbourhood'].str.upper()

df_habitatges_municipi = df_habitatges_municipi.reset_index()
df_habitatges_municipi.columns = ['Municipi', 'Count']

df_merged = pd.merge(df_geojson, df_habitatges_municipi, on='Municipi', how='inner')

m = folium.Map(location=[39.55263, 2.9],
               zoom_start=10,
               zoom_control=False,
               scrollWheelZoom=False,
               dragging=False)

colormap = LinearColormap(colors=['red', 'green'], vmin=df_merged['Count'].min(), vmax=df_merged['Count'].max())

folium.Choropleth(
    geo_data=df_merged,
    name="choropleth",
    data=df_merged,
    columns= ["Municipi", 'Count'],
    key_on="feature.properties.Municipi",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.1,
    ).add_to(m)

tooltip = folium.GeoJsonTooltip(
    fields=["Municipi", 'Count'],
    aliases=["", "Hab.Turístics:"],
    localize=True,
    sticky=False,
    labels=True
)

folium.GeoJson(df_merged, name="Mapa de municipis de Mallorca", tooltip=tooltip).add_to(m)

'''
En general, com podem observar, els municipis amb més oferta d'allotjaments turístics són els situats a la costa i que disposen de platges. Destaca especialment el municipi de Pollença.
'''


folium_static(m, width=1000, height=1000)

disable_dragging_js = """
<script>
document.addEventListener("DOMContentLoaded", function() {
alert('')
    var map = document.getElementsByClassName('folium-map')[0];
    map.style.cursor = 'default';
    map.style.pointerEvents = 'none';

    map.addEventListener('click', function(event) {
        event.preventDefault();
    });
});
</script>
"""

st.write(disable_dragging_js, unsafe_allow_html=True)
