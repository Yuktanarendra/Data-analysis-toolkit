import streamlit as st

st.header('6. Data Visualization Overview')
st.write("""
This page provides an overview of the various data visualization options available in this application.
Use the 'Data Visualization' page to create specific plots and gain insights into the data.
""")

st.markdown("""
**Available Visualizations:**

- **Correlation Heatmap:** Displays the correlation between different features in the dataset.
- **Pairplot:** Creates pairwise scatter plots for each feature in the dataset.
- **Bar Plot:** Displays a bar plot for a selected column.
- **Scatter Plot:** Displays a scatter plot for selected x and y axes.
- **Pie Chart:** Creates a pie chart for a selected column.
- **Histogram:** Displays a histogram for a selected column.
- **Box Plot:** Creates a box plot for a selected column.

You can access these visualizations in the 'Data Visualization' page.
""")
