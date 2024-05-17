import streamlit as st
import pandas as pd
import plotly.express as px



# Títol
st.title("Habitatges turístics per municipis de Mallorca")

# Càrrega habitatges turístics
df_habitatges = pd.read_csv("data/Habitatges.csv")

# Agrupem inici d'activitat per anys
df_habitatges["Inici d'activitat"] = pd.to_datetime(df_habitatges["Inici d'activitat"])
df_habitatges_grp = df_habitatges.groupby(df_habitatges["Inici d'activitat"].dt.year).size().reset_index(name='Habitatges')


fig = px.line(df_habitatges_grp, x="Inici d'activitat", y='Habitatges', markers=True)

# Configurar la visualizació interactiva
fig.update_traces(hovertemplate='Any: %{x}<br>Inici d\'activitat: %{y}')


fig.update_layout(
    title='Nombre d\'habitatges turístics por any d\'inici d\'activitat',
    xaxis_title='Any d\'inici d\'activitat',
    yaxis_title='Nombre d\'habitatges turístics'
)


st.plotly_chart(fig)


# Calcular la suma acumulativa
df_habitatges_grp['Habitatges acumulats'] = df_habitatges_grp['Habitatges'].cumsum()


fig = px.line(df_habitatges_grp, x="Inici d'activitat", y='Habitatges acumulats', markers=True)


fig.update_traces(hovertemplate='Any: %{x}<br>Total: %{y}', line=dict(width=3))


fig.update_layout(
    title='Nombre total d\'habitatges turístics per any',
    xaxis_title='Any',
    yaxis_title='Nombre total d\'habitatges turístics'
)


st.plotly_chart(fig)


