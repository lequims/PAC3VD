import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
st.set_page_config(
    layout="wide",
    page_title="Evolució places turístiques de Mallorca"
)

# Títol
st.title("Evolució places turístiques de Mallorca")


'''
Com han evolucionat les places turístiques a Mallorca en els últims anys? 

'''

df_habitatges = pd.read_csv("data/Habitatges.csv")
df_allotjaments = pd.read_csv("data/Allotjaments.csv")


df_habitatges["Inici d'activitat"] = pd.to_datetime(df_habitatges["Inici d'activitat"])
df_allotjaments["Inici d'activitat"] = pd.to_datetime(df_allotjaments["Inici d'activitat"])

df_habitatges = df_habitatges[['Inici d\'activitat', 'Places']].copy()
df_allotjaments = df_allotjaments[['Inici d\'activitat', 'Places']].copy()

df_habitatges['Tipus'] = 'Habitatge turístic'
df_allotjaments['Tipus'] = 'Allotjament turístic'

df_combinat = pd.concat([df_habitatges, df_allotjaments])

df_combinat_grp = df_combinat.groupby([df_combinat["Inici d'activitat"].dt.year, 'Tipus'])["Places"].sum().reset_index(name='Places')

df_combined_recent = df_combinat_grp[df_combinat_grp["Inici d'activitat"] >= 2000]


fig = px.line(df_combined_recent, x="Inici d'activitat", y='Places', color='Tipus', markers=True)


fig.update_traces(hovertemplate='Any: %{x}<br>Places turístiques: %{y}')


fig.update_layout(
    title='Noves places en allotjaments i habitatges turístícs (A partir de l\'any 2000)',
    xaxis_title='Any',
    yaxis_title='Noves places'
)


st.plotly_chart(fig)

'''
Entre els anys 2015-2017 hi ha un creixement molt significatiu en les places ofertades per habitatges turístics motivat per l'entrada en vigor d'una nova [regulació, LLEI 6/2017](https://intranet.caib.es/sites/institutestudisautonomics/f/342256) que, modificant la llei del 2012 feia més restrictiu l'accès a llicències d'habitatges turístics.

'''


df_combinat_grp = df_combinat.groupby([df_combinat["Inici d'activitat"].dt.year, 'Tipus'])["Places"].sum().reset_index(name='Places')

df_combinat_grp.sort_values(by=["Inici d'activitat", 'Tipus'], inplace=True)  # Asegurar el orden correcto
df_combinat_grp['Places acumulades'] = df_combinat_grp.groupby('Tipus')['Places'].cumsum()

# Filtrar datos desde el año 2000
df_combined_recent = df_combinat_grp[df_combinat_grp["Inici d'activitat"] >= 2000]

# Crear gráfico
fig = px.line(df_combined_recent, x="Inici d'activitat", y='Places acumulades', color='Tipus', markers=True)

# Configuración del gráfico
fig.update_traces(hovertemplate='Año: %{x}<br>Evolució places turistiques: %{y}')
fig.update_layout(
    title='Evolució places turístiques (A partir de l\'any 2000)',
    xaxis_title='Any',
    yaxis_title='Total places'
)

# Mostrar gráfico
st.plotly_chart(fig)

'''
L'evolució d'ambdues tipologies de places turístiques, desmotra que aquestes han anat creixents ens els darrers 20 anys. Destaca el creixement l'any 2017 en les places turístiques d'habitatges, però també en les d'allotjaments turístics.



'''


df_total_per_year = df_combined_recent.groupby('Inici d\'activitat')['Places acumulades'].sum().reset_index()


df_combined_percent = pd.merge(df_combined_recent, df_total_per_year, on='Inici d\'activitat', suffixes=('', '_total'))


df_combined_percent['Percent'] = (df_combined_percent['Places acumulades'] / df_combined_percent['Places acumulades_total']) * 100


df_habitatge_percent = df_combined_percent[df_combined_percent['Tipus'] == 'Habitatge turístic']
df_allotjament_percent = df_combined_percent[df_combined_percent['Tipus'] == 'Allotjament turístic']


fig = go.Figure()
fig.add_trace(go.Bar(
    x=df_habitatge_percent["Inici d'activitat"],
    y=df_habitatge_percent['Percent'],
    name='Habitatge turístic',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=df_allotjament_percent["Inici d'activitat"],
    y=df_allotjament_percent['Percent'],
    name='Allotjament turístic',
    marker_color='red'
))


fig.update_layout(
    barmode='stack',
    title='Evolució percentual de cada tipus de places turístiques',
    xaxis_title='Any',
    yaxis_title='Percentatge del total (%)',
    yaxis=dict(tickformat=".0%"),  
    legend_title="Tipus"
)


st.plotly_chart(fig)

'''
El creixement de l'oferta de places en habitatges turístics ha estat especialment rellevant a partir del l'any 2015 representant un 25% a l'actualitat.
'''