import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(
    layout="wide",
    page_title="Oferta turística a Mallorca"
)

# Títol
st.title("Oferta de places turístiques a Mallorca")

'''
L'actual oferta de places turístiques a Mallorca es divideix en habitatges turístics i allotjaments turístics. 
En aquesta visualització, hem creuat les dades dels dos tipus d'allotjaments per a tenir una visió més globalitzada de les places turístiques.
'''

# Carrega les dades
df_habitatges = pd.read_csv("data/Habitatges.csv")
df_allotjaments = pd.read_csv("data/Allotjaments.csv")


total_habitatges = df_habitatges['Places'].sum()
total_allotjaments = df_allotjaments['Places'].sum()


labels = ['Habitatges', 'Allotjaments']
values = [total_habitatges, total_allotjaments]
custom_labels = [f"{label}: {value:,}" for label, value in zip(labels, values)]  # Formato con números y nombre

# Crear el gráfico de pastel
fig = go.Figure(data=[go.Pie(labels=custom_labels, values=values, hole=.3)])

# Añadir estilos al gráfico
fig.update_traces(hoverinfo='label+percent', textinfo='percent', textfont_size=20,
                  marker=dict(colors=['#0078AA', '#FF6347'], line=dict(color='#000000', width=2)))

# Actualizar el layout para añadir título y mejorar la presentación
fig.update_layout(
    title_text="Distribució de places turístiques: Habitatges vs Allotjaments",
    annotations=[dict(text='Places', x=0.5, y=0.5, font_size=20, showarrow=False)]
)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)


'''
Entenem per habitatges els establiments de tipus vivenda que ofereixen places turístiques. Per altra banda, dins els establiments englobariem Hotels, Agroturismes, etc....

'''