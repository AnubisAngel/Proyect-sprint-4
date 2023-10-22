import streamlit as st
import pandas as pd
import plotly.express as px

# leer nuestra base de datos y asegurarnos que cumple con nuestro standard para tener datos limpios y utilizables
car_data = pd.read_csv('vehicles_us.csv')
df['column_name'] = df['column_name'].str.strip().str.lower()
df = df.drop_duplicates()

# Encabezado
st.header('Analisis of vehicles in the US')

# determinando las opciones de acuerdo a lo disponible en nuestra base de datos
options = [
    "price", "model_year", "model", "condition", "cylinders", "fuel",
    "odometer", "transmission", "type", "paint_color", "is_4wd",
    "date_posted", "days_listed"
]
# codigo para poder seleccionar las opciones
selected_options = st.multiselect('Select options to plot:', options)
# codigo para seleccionar si deseamos un histograma o un cuadro de dispersion
build_histogram = st.checkbox('Build a histogram')
build_scatter = st.checkbox('Build a scatter plot')

if selected_options:
    for selected_option in selected_options:
        st.write(f'Creation of a graphic for column {selected_option}')

        if build_histogram:
            # Si seleccionaron la opcion histograma
            fig = px.histogram(car_data, x=selected_option)
            st.plotly_chart(fig, use_container_width=True)

        if build_scatter:
            # si seleccionaron el grafico de dispersion
            st.write(
                f'Creation of a scatter plot for the column {selected_option}')
            # se puede cambiar la variable price por cualquier otra opcion
            fig = px.scatter(car_data, x=selected_option, y="price")
            st.plotly_chart(fig, use_container_width=True)
