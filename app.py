import streamlit as st
import pandas as pd
import plotly.express as px

# leer nuestra base de datos
car_data = pd.read_csv('vehicles_us.csv')

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
# codigo para variable Y
selected_y_variable = st.selectbox(
    'Select the y-variable for comparison:', options)
# codigo para seleccionar si deseamos un histograma o un cuadro de dispersion
build_histogram = st.checkbox('Build a histogram')
build_scatter = st.checkbox('Build a scatter plot')

if selected_options:
    for selected_option in selected_options:
        st.write(
            f'Creation of a graphic for column {selected_option}( and Y-axis: {selected_y_variable})')

        if build_histogram:
            # Si seleccionaron la opcion histograma
            fig = px.histogram(car_data, x=selected_option,
                               y=selected_y_variable)
            st.plotly_chart(fig, use_container_width=True)

        if build_scatter:
            # si seleccionaron el grafico de dispersion
            st.write(
                f'Creation of a scatter plot for the column {selected_option}( and Y-axis: {selected_y_variable})')
            # se puede cambiar la variable price por cualquier otra opcion
            fig = px.scatter(car_data, x=selected_option,
                             y=selected_y_variable)
            st.plotly_chart(fig, use_container_width=True)
