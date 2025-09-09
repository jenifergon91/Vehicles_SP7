import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Anuncios de Venta de Coches')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma de Odómetro')

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión de Precio vs. Odómetro')

# Lógica para mostrar el histograma si la casilla de verificación está seleccionada
if build_histogram:
    st.write('Creando un histograma para la distribución del odómetro')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig, use_container_width=True)

# Lógica para mostrar el gráfico de dispersión si la casilla de verificación está seleccionada
if build_scatter:
    st.write('Creando un gráfico de dispersión de Precio vs. Odómetro')

    fig = px.scatter(car_data, x="odometer", y="price", title='Precio vs. Odómetro')

    st.plotly_chart(fig, use_container_width=True)