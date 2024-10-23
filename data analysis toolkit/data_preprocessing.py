import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df, handle_missing):
    if handle_missing == "Fill with Mean":
        numeric_columns = df.select_dtypes(include=['number']).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    elif handle_missing == "Fill with Mode":
        df = df.apply(lambda x: x.fillna(x.mode()[0]) if x.dtype == "object" else x.fillna(x.mean()))
    elif handle_missing == "Drop Missing":
        df.dropna(inplace=True)
    return df


st.markdown('<h1 class="custom-h1">2. Data Preprocessing</h1>', unsafe_allow_html=True)

if 'df' in st.session_state and st.session_state.df is not None:
    st.write("### Step 1: Handling Missing Values")
    if st.checkbox("Show data info"):
        st.write(st.session_state.df.info())

    missing_values = st.session_state.df.isnull().sum().sum()
    st.write(f"Total missing values: {missing_values}")

    if missing_values > 0:
        handle_missing = st.radio("How do you want to handle missing values?",
                                  ["Fill with Mean", "Fill with Mode", "Drop Missing"])
        st.session_state.df = preprocess_data(st.session_state.df, handle_missing)
        st.write("Data after handling missing values:")
        st.dataframe(st.session_state.df.head())
    else:
        st.write("No missing values found.")

    st.write("### Step 2: Encoding Categorical Variables")

    # Identify categorical columns
    categorical_cols = st.session_state.df.select_dtypes(include=['object']).columns.tolist()

    encoding_type = st.radio("Select Encoding Type", ["Label Encoding", "One-Hot Encoding"])

    if encoding_type == "Label Encoding":
        label_encoder = LabelEncoder()
        for col in categorical_cols:
            st.session_state.df[col] = label_encoder.fit_transform(st.session_state.df[col])
        st.write("Data after label encoding:")
        st.dataframe(st.session_state.df.head())
    elif encoding_type == "One-Hot Encoding":
        st.session_state.df = pd.get_dummies(st.session_state.df, columns=categorical_cols, drop_first=True)
        st.write("Data after one-hot encoding:")
        st.dataframe(st.session_state.df.head())

    st.write("### Data Description")
    st.dataframe(st.session_state.df.describe())
else:
    st.warning("Please complete the Data Collection step first.")
