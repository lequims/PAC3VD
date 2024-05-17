import streamlit as st
import geopandas as gpd
import pandas as pd


st.set_page_config(
    layout="wide",
    page_title="Inici"
)

# Títol
st.title("Saturació de places turístiques a Mallorca")

df_habitatges = pd.read_csv("data/Habitatges.csv")
df_allotjaments = pd.read_csv("data/Allotjaments.csv")

total_habitatges = df_habitatges.shape[0]
total_allotjaments = df_allotjaments.shape[0]



'''
En aquesta pràctica de visualització de dades, ens centrarem en l'anàlisi de la saturació turística a Mallorca, una de les illes més visitades de l'arxipèlag balear.

Es un tema que actualment està en boca de tothom, ja que la saturació turística pot tenir un impacte negatiu en la qualitat de vida dels residents locals, així com en la sostenibilitat del medi ambient i dels recursos naturals de l'illa.


'''

st.write(f"Actualment hi ha un total de **{total_habitatges}** de d'habitatges turístics. i un total de **{total_allotjaments}** allotjaments turístics. Tots ells conformen l'actual oferta turística legal de l'illa.")

"""
**Font de dades:**

Habitatges Turístics Mallorca
Govern de les Illes Balears. Catàleg de dades obertes Illes Balears

https://catalegdades.caib.cat/Turisme/Habitatges-Tur-stics-Mallorca/3q3t-usfm/about_data


Allotjaments Turístics Mallorca
Govern de les Illes Balears. Catàleg de dades obertes Illes Balears

https://catalegdades.caib.cat/Turisme/Allotjaments-Tur-stics-Mallorca/j2yj-e83g/data_preview


GeoJSON de cadascuna de les illes que conformen l'arxipèlag balear

https://github.com/enmiquelangel/geojsonsillesbalears


Dades de població per municipi de Mallorca
Població per illa, municipi, sexe i grup d'edat.

https://intranet.caib.es/ibestat-jaxi/tabla.do?px=fe3be181-2d59-4205-a774-f703a3a671b9&pag=1&nodeId=%202acef6cf-175a-4826-b71e-8302b13c1262%20&pxName=pad_res01_22.px


PAC3 de Visualització de dades
Miquel Piulats

Repositori
https://github.com/lequims/PAC3VD




"""

