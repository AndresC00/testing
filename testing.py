import streamlit as st
import pandas as pd
import plotly.express as px

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



# Sección de Tendencias de Retención
st.subheader("Retention Rate Trends")
st.line_chart(df.set_index("Year")["Retention Rate (%)"])

