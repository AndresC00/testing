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
st.subheader("Retention Rate Trends Over Time")

# Crear columna combinada Year-Term para el eje temporal
df['Period'] = df['Year'].astype(str) + " " + df['Term']

# Gráfico de líneas con tendencia
fig_retention = px.line(df,
                        x='Period',
                        y='Retention Rate (%)',
                        color='Year',
                        markers=True,
                        title='Retention Rate Trend by Academic Period',
                        labels={'Retention Rate (%)': 'Retention Rate', 'Period': 'Academic Period'},
                        trendline="lowess")  # Suavizado de tendencia

# Personalizar diseño
fig_retention.update_layout(
    hovermode='x unified',
    xaxis_title='Academic Period',
    yaxis_title='Retention Rate (%)',
    showlegend=True
)

# Mostrar gráfico
st.plotly_chart(fig_retention, use_container_width=True)
