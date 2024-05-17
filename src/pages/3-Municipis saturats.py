import streamlit as st
import geopandas as gpd
from streamlit_folium import folium_static
import folium
import pandas as pd
from branca.colormap import LinearColormap

st.set_page_config(
    layout="wide",
    page_title="Saturació turística per a la gestió municipal"
)


# Títol
st.title("Saturació turística per a la gestió municipal")


'''
Quins ajuntaments estan més afectats per la saturació turística?

S'ha calculat un un índex de saturació turística per municipi, hem tingut en compte la relació entre la població resident i el nombre de places totals ofertades. 

Aquest índex ens permet identificar els municipis amb més intensitat de turisme i per tant més pressió sobre els recursos locals.

'''

# Carrega les dades
df_habitatges = pd.read_csv("data/Habitatges.csv")
df_allotjaments = pd.read_csv("data/Allotjaments.csv")

# Agrupar por 'Municipi' i sumar les places turístiques
df_habitatges_grp_places = df_habitatges.groupby('Municipi')['Places'].sum().reset_index()
df_allotjaments_grp_places = df_allotjaments.groupby('Municipi')['Places'].sum().reset_index()


df_places_total_municipis = pd.merge(df_habitatges_grp_places, df_allotjaments_grp_places, on='Municipi', suffixes=('_habitatges', '_allotjaments'))
df_places_total_municipis['Places'] = df_places_total_municipis['Places_habitatges'] + df_places_total_municipis['Places_allotjaments']

# Dades de població
df_poblacio = pd.read_csv("data/Poblacio.csv")
# Reduim columnes
df_poblacio = df_poblacio[['Municipi', 'Total']]
df_poblacio.rename(columns={'Total': 'Població'}, inplace=True)
# Format del municipi a majuscules
df_poblacio['Municipi'] = df_poblacio['Municipi'].str.upper()

df_final = pd.merge(df_places_total_municipis, df_poblacio, on='Municipi', how='left')

# Calculem índex de places turístiques per habitants del municipi.
df_final['Índex saturació'] = (df_final['Places'] / df_final['Població']).round(2)

# Càrrega geojson municipis
df_geojson = gpd.read_file("data/mallorca.json")
# Transformem camp per poder relacionar les dades
df_geojson['Municipi'] = df_geojson['neighbourhood'].str.upper()

df_final = df_final.reset_index()
df_merged = pd.merge(df_geojson, df_final, on='Municipi', how='inner')

m = folium.Map(location=[39.55263, 2.9],
               zoom_start=10,
               zoom_control=False,
               scrollWheelZoom=False,
               dragging=False)

colormap = LinearColormap(colors=['red', 'green'], vmin=df_merged['Índex saturació'].min(), vmax=df_merged['Índex saturació'].max())

folium.Choropleth(
    geo_data=df_merged,
    name="choropleth",
    data=df_merged,
    columns= ["Municipi", 'Índex saturació'],
    key_on="feature.properties.Municipi",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.1,
    ).add_to(m)

tooltip = folium.GeoJsonTooltip(
    fields=["Municipi", 'Places', 'Població', 'Índex saturació'],
    aliases=["", "Places", 'Població', "Índex calculat:"],
    localize=True,
    sticky=False,
    labels=True
)

folium.GeoJson(df_merged, name="Mapa de municipis de Mallorca", tooltip=tooltip).add_to(m)




folium_static(m, width=850, height=850)

'''
La lectura de l'índex és equivalent al nombre de places turístiques per  habitant del municipi.

La saturació turística està especialment present en municipis de la costa i afecta especialment als que tenen una població petita.
'''