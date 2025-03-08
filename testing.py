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

# Sección de Tendencias de Retención por Año y Término
st.subheader("Retention Rate Trends by Year and Term")

# Crear gráfico de líneas con agrupación por término
fig_retention = px.line(df.sort_values(['Year', 'Term']),
                        x='Year',
                        y='Retention Rate (%)',
                        color='Term',
                        line_dash='Term',
                        markers=True,
                        title='Retention Rate Evolution by Academic Term',
                        labels={'Retention Rate (%)': 'Retention Rate'},
                        trendline="lowess",
                        facet_col='Term',
                        height=500)

# Personalizar diseño
fig_retention.update_layout(
    hovermode='x unified',
    xaxis_title='Academic Year',
    yaxis_title='Retention Rate (%)',
    legend_title='Academic Term',
    xaxis=dict(tickmode='linear', dtick=1),
    template='plotly_white'
)

# Añadir anotaciones de tendencia
for term in df['Term'].unique():
    trend_data = px.get_trendline_results(fig_retention).query(f"Term == '{term}'").iloc[0]["px_fit_results"]
    slope = trend_data.params[1] * 100  # Convertir pendiente a porcentaje
    annotation_text = f'{term} Trend: {"+" if slope > 0 else ""}{slope:.1f}% anual'
    
    fig_retention.add_annotation(
        xref='paper',
        yref='paper',
        x=0.95,
        y=0.85 - (0.1 * list(df['Term'].unique()).index(term)),
        text=annotation_text,
        showarrow=False,
        font=dict(color='green' if slope > 0 else 'red')
    )

st.plotly_chart(fig_retention, use_container_width=True)

