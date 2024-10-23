import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from streamlit_option_menu import option_menu
from sklearn.datasets import load_iris
import io



# Custom CSS to increase the font size in the sidebar and adjust styles
st.markdown("""
    <style>
    /* Increase the size of the sidebar */
    .css-1d391kg {
        width: 25% !important;
        min-width: 300px !important;
    }

    /* Customize the sidebar content */
    .css-18e3th9 {
        font-size: 20px !important;
        font-weight: bold;
        color: #4b4b4b;
    }

    /* Customize the main text area */
    .css-1d391kg .stMarkdown p {
        font-size: 18px;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }

    /* Add some padding around the sidebar */
    .css-1d391kg .stSidebar {
        padding: 20px;
    }

    /* Custom h1 tag styling */
    .custom-h1 {
        font-size: 2em;
        font-weight: bold;
        color: #2E86C1;
        margin-top: 0;
        margin-bottom: 0.5em;
    }

    /* Responsive sidebar */
    @media (max-width: 600px) {
        .css-1d391kg {
            width: 100% !important;
            min-width: auto !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation using option menu
with st.sidebar:
    st.sidebar.markdown("<h1 style='text-align: center;'>Data Analysis</h1>", unsafe_allow_html=True)
    page = option_menu(
        "Features",
        ["Dashboard", "Data Collection", "Data Preprocessing", "Data Visualization", "Model Training",
         "Download Preprocessed Data", "Data Visualization Overview"],
        icons=["house", "cloud-upload", "gear", "bar-chart", "book", "download", "eye"],
        menu_icon="cast",
        default_index=0,
    )

if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"


def set_page(selected_page):
    st.session_state.page = selected_page


set_page(page)


# Functions for different pages
def load_data(file):
    if file is not None:
        data = pd.read_csv(file)
        st.session_state.df = data
        return data
    return None


def preprocess_data(df, handle_missing):
    if handle_missing == "Fill with Mean":
        numeric_columns = df.select_dtypes(include=['number']).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    elif handle_missing == "Fill with Mode":
        df = df.apply(lambda x: x.fillna(x.mode()[0]) if x.dtype == "object" else x.fillna(x.mean()))
    elif handle_missing == "Drop Missing":
        df.dropna(inplace=True)
    return df


def load_sample_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    st.session_state.df = df
    return df


# Dashboard
if st.session_state.page == "Dashboard":
    st.markdown('<h1 class="custom-h1">Dashboard</h1>', unsafe_allow_html=True)

    if 'df' in st.session_state and st.session_state.df is not None:
        st.write("### Dataset Overview")
        st.dataframe(st.session_state.df.head())

        st.write("### Basic Statistics")
        st.dataframe(st.session_state.df.describe())

        st.write("### Missing Values")
        st.write(st.session_state.df.isnull().sum())

        st.write("### Correlation Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(st.session_state.df.corr(), ax=ax, annot=True, cmap="coolwarm")
        st.pyplot(fig)

        st.write("### Pair Plot")
        pair_plot = sns.pairplot(st.session_state.df)
        st.pyplot(pair_plot)

        st.write("### Interactive Plotly Visualization")
        fig = px.scatter_matrix(st.session_state.df)
        st.plotly_chart(fig)
    else:
        st.write("Upload a dataset to view the dashboard.")



if st.session_state.page == "Data Collection":
    exec(open("data_collection.py").read())
elif st.session_state.page == "Data Preprocessing":
    exec(open("data_preprocessing.py").read())
elif st.session_state.page == "Data Visualization":
    exec(open("data_visualization.py").read())
elif st.session_state.page == "Model Training":
    exec(open("model_training.py").read())
elif st.session_state.page == "Download Preprocessed Data":
    exec(open("download_data.py").read())
elif st.session_state.page == "Data Visualization Overview":
    exec(open("visualization_overview.py").read())