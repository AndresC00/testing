import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
@st.cache_data
def load_data():
    return pd.read_csv('university_student_dashboard_data.csv')

# Cargar los datos
df = load_data()

# Título del dashboard
st.title("University Student Dashboard")

# Mostrar un resumen de los datos
st.subheader("Data Overview")
st.write(df)

# Gráfico de Total Applications, Admissions, and Enrollments per Term and Year
st.subheader("Total Applications, Admissions, and Enrollments by Year and Term")

# Crear gráfico de barras usando Plotly
fig = px.bar(df,
             x='Term',
             y=['Applications', 'Admitted', 'Enrolled'],
             color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96'],
             barmode='group',
             title='Total Applications, Admissions, and Enrollments by Year and Term',
             labels={'value': 'Count', 'variable': 'Category'},
             facet_col='Year')

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)

##############################################################################################################################################################

import plotly.graph_objs as go

# Asumimos que los datos ya están cargados en df
# Filtrar los datos para las estaciones 'Fall' y 'Spring'
fall_data = df[df['Term'] == 'Fall']
spring_data = df[df['Term'] == 'Spring']

# Asegurarse de que los datos estén ordenados por el mismo eje (por ejemplo, por 'Date' o algún otro índice relevante)
fall_data = fall_data.sort_values('Year')
spring_data = spring_data.sort_values('Year')

# Crear las trazas para los dos conjuntos de datos
trace_fall = go.Scatter(
    x=fall_data['Year'], y=fall_data['Retention Rate (%)'], 
    mode='lines', name='Fall', line=dict(color='blue')
)

trace_spring = go.Scatter(
    x=fall_data['Year'], y=fall_data['Retention Rate (%)'], 
    mode='lines', name='Spring', line=dict(color='red', dash='dash')
)

# Crear el diseño del gráfico
layout = go.Layout(
    title='Comparison of Fall and Spring Data',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Retention Rate (%)')
)

# Crear la figura con ambas trazas
fig = go.Figure(data=[trace_fall, trace_spring], layout=layout)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
