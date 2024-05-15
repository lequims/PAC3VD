import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    layout="wide",
    page_title="Comercialització"
)

# Títol
st.title("Comercialització d'allotjaments turístics a Mallorca")

df_habitatges = pd.read_csv("data/Habitatges.csv")

df_count_explotadors = df_habitatges['Explotador/s'].value_counts()
count_unique = df_count_explotadors[df_count_explotadors == 1].sum()
count_multiple = df_count_explotadors[df_count_explotadors > 1].count()

# Primer gràfic de pastís

sizes = [count_unique, count_multiple]
labels = ['Únic allotjament', '> 1 allotjament']
colors = ['lightblue', 'lightgreen']

fig, ax = plt.subplots(figsize=(3, 3))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=210)
ax.axis('equal')
st.pyplot(fig)



df_multiple = df_count_explotadors[df_count_explotadors > 5]

# Definir los intervalos para los contenedores (bins)
bins = np.arange(df_multiple.min(), df_multiple.max() + 1, 1)

# Crear el histograma
fig, ax = plt.subplots()
ax.hist(df_multiple, bins=bins, color='skyblue', edgecolor='black')

# Añadir etiquetas y título
ax.set_xlabel('Número de apariciones')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de comercialitzadors amb cinc o més propietats')

# Mostrar el histograma usando Streamlit
st.pyplot(fig)


