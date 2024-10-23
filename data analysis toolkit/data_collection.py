import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None

st.header('1. Data Collection')
data_source = st.radio("Select data source", ("Upload CSV", "Use Sample Data"))

if data_source == "Upload CSV":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file:
        st.session_state.df = pd.read_csv(uploaded_file)
else:
    # Use sample data
    data = load_iris(as_frame=True)
    st.session_state.df = data.frame

if st.session_state.df is not None:
    st.write("Data preview:")
    st.dataframe(st.session_state.df.head(10))
