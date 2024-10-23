import streamlit as st
import pandas as pd

st.header('5. Download Preprocessed Data')
if 'df' in st.session_state and st.session_state.df is not None:
    st.write("Preprocessed data preview:")
    st.dataframe(st.session_state.df.head())

    @st.cache
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(st.session_state.df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='preprocessed_data.csv',
        mime='text/csv',
    )
else:
    st.warning("Please complete the Data Collection and Data Preprocessing steps first.")
