import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar datos
df = pd.read_csv("university_student_dashboard_data.csv")

st.title("University Student Dashboard")

# 1. Total applications, admissions, and enrollments per term
fig = px.bar(df,
             x=['Term','Year'],
             y=['Applications', 'Admitted', 'Enrolled'],
             color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96'],
             barmode='group',
             title='Total Applications, Admissions, and Enrollments by Year and Term',
             labels={'value': 'Count', 'variable': 'Category'},
             facet_col='Year')

# Display the figure in Streamlit
st.plotly_chart(fig, use_container_width=True)

# 2. Retention rate trends over time
st.subheader("Retention Rate Trends")
st.line_chart(df.set_index("Year")["Retention Rate (%)"])

# 3. Student satisfaction scores over the years
st.subheader("Student Satisfaction Over Time")
st.line_chart(df.set_index("Year")["Student Satisfaction (%)"])

# 4. Enrollment breakdown by department
st.subheader("Enrollment Breakdown by Department")
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
st.bar_chart(df.set_index("Year")[departments])

# 5. Comparison between Spring vs. Fall term trends
st.subheader("Spring vs. Fall Term Trends")
spring_data = df[df["Term"] == "Spring"]
fall_data = df[df["Term"] == "Fall"]
st.line_chart(spring_data.set_index("Year")[['Applications', 'Admitted', 'Enrolled']], use_container_width=True)
st.line_chart(fall_data.set_index("Year")[['Applications', 'Admitted', 'Enrolled']], use_container_width=True)

# 6. Compare trends between departments, retention rates, and satisfaction levels
st.subheader("Comparison of Trends")
st.line_chart(df.set_index("Year")[['Retention Rate (%)', 'Student Satisfaction (%)']])
