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

##############################################################################################################################################################

fall_data = df[df['Term'] == 'Fall']
spring_data = df[df['Term'] == 'Spring']

# Crear gráfico de líneas para el término "Fall"
fig_fall = px.line(fall_data,
                   x='Year',
                   y='Retention Rate (%)',
                   markers=True,
                   trendline="lowess",
                   line_shape='linear',
                   name='Fall')

# Crear gráfico de líneas para el término "Spring"
fig_spring = px.line(spring_data,
                     x='Year',
                     y='Retention Rate (%)',
                     markers=True,
                     trendline="lowess",
                     line_shape='linear',
                     name='Spring')

# Crear una figura combinada
fig_combined = go.Figure()

# Añadir trazas de Fall y Spring a la figura combinada
for trace in fig_fall.data:
    fig_combined.add_trace(trace)

for trace in fig_spring.data:
    fig_combined.add_trace(trace)

# Personalizar diseño del gráfico combinado
fig_combined.update_layout(
    title='Retention Rate Trends for Fall and Spring Terms',
    xaxis_title='Academic Year',
    yaxis_title='Retention Rate (%)',
    hovermode='x unified',
    template='plotly_white'
)

# Mostrar gráfico en Streamlit
st.plotly_chart(fig_combined, use_container_width=True)


