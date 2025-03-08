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
    x=spring_data['Year'], y=spring_data['Retention Rate (%)'], 
    mode='lines', name='Spring', line=dict(color='red', dash='dash')
)

# Crear el diseño del gráfico
layout = go.Layout(
    title='Comparison of Retention Rate (%) by Term',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Retention Rate (%)')
)

# Crear la figura con ambas trazas
fig = go.Figure(data=[trace_fall, trace_spring], layout=layout)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)



##############################################################################################################################################


# Normalize the columns to create percentages
df['Engineering Enrolled (%)'] = df['Engineering Enrolled'] / df['Enrolled'] 
df['Business Enrolled (%)'] = df['Business Enrolled'] / df['Enrolled'] 
df['Arts Enrolled (%)'] = df['Arts Enrolled'] / df['Enrolled'] 
df['Science Enrolled (%)'] = df['Science Enrolled'] / df['Enrolled'] 



# Derretir el DataFrame para que las categorías (Engineering, Business, etc.) estén en una columna 'Category'
df_melted = df.melt(id_vars=['Year', 'Term'], 
                    value_vars=['Engineering Enrolled (%)', 'Business Enrolled (%)', 
                                'Arts Enrolled (%)', 'Science Enrolled (%)'],
                    var_name='Category', 
                    value_name='Percentage')

# Crear el gráfico de barras apiladas 100% por Year y Term
fig = px.bar(df_melted, 
             x='Year', 
             y='Percentage', 
             color='Category', 
             facet_row='Term', 
             title='100% Stacked Bar Chart by Year and Term for Enrollment Categories',
             labels={'Percentage': 'Percentage'},
             color_discrete_map={
                 'Engineering Enrolled (%)': 'blue', 
                 'Business Enrolled (%)': 'green', 
                 'Arts Enrolled (%)': 'red',
                 'Science Enrolled (%)': 'orange'
             },
             text='Percentage',
             category_orders={'Year': sorted(df['Year'].unique())}
            )

# Formatear el gráfico para mostrar porcentajes
fig.update_traces(texttemplate='%{text:.1%}', textposition='outside', textfont_size=12)
fig.update_layout(barmode='stack', 
                  yaxis=dict(tickformat='.0%', ticksuffix='%'),
                  xaxis_title='Year',
                  yaxis_title='Percentage'
                 )

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

###########################################################################################################################################################
trace_fall = go.Scatter(
    x=fall_data['Year'], y=fall_data['Student Satisfaction (%)'], 
    mode='lines', name='Fall', line=dict(color='blue')
)

trace_spring = go.Scatter(
    x=spring_data['Year'], y=spring_data['Student Satisfaction (%)'], 
    mode='lines', name='Spring', line=dict(color='red', dash='dash')
)

# Crear el diseño del gráfico
layout = go.Layout(
    title='Comparison of Student Satisfaction (%) by Term',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Student Satisfaction (%)')
)

# Crear la figura con ambas trazas
fig = go.Figure(data=[trace_fall, trace_spring], layout=layout)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)


