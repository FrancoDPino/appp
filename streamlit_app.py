import streamlit as st
import pandas as pd

# Load the Excel file
file_path = 'July 2024 Inspections .xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Streamlit app
st.title("July 2024 Inspections Report")

# Filters
department = st.multiselect("Select Department", options=df["Department"].unique(), default=df["Department"].unique())
inspector = st.multiselect("Select Inspector", options=df["Inspector"].unique(), default=df["Inspector"].unique())
completion_status = st.selectbox("Completion Status", options=["All", "Completed", "Not Completed"])

# Filter data
filtered_df = df[(df["Department"].isin(department)) & (df["Inspector"].isin(inspector))]

if completion_status == "Completed":
    filtered_df = filtered_df[filtered_df["Completed"].notnull()]
elif completion_status == "Not Completed":
    filtered_df = filtered_df[filtered_df["Completed"].isnull()]

# Display filtered data
st.dataframe(filtered_df)

# Visualizations
st.bar_chart(filtered_df["Department"].value_counts())
st.write("Completion Status Distribution")
st.pie_chart(filtered_df["Completed"].notnull().value_counts())

# Save filtered data
st.download_button(
    label="Download data as CSV",
    data=filtered_df.to_csv().encode('utf-8'),
    file_name='filtered_inspection_data.csv',
    mime='text/csv',
)

