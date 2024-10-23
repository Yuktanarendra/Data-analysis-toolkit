import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

st.header('3. Data Visualization')
if 'df' in st.session_state and st.session_state.df is not None:
    if st.checkbox("Show correlation heatmap"):
        fig = plt.figure(figsize=(10, 8))
        sns.heatmap(st.session_state.df.corr(), annot=True, cmap='coolwarm')
        st.pyplot(fig)

    if st.checkbox("Show pairplot"):
        fig = sns.pairplot(st.session_state.df)
        st.pyplot(fig)

    if st.checkbox("Show bar plot"):
        column = st.selectbox("Select column for bar plot", st.session_state.df.columns)
        fig = px.bar(st.session_state.df, x=column)
        st.plotly_chart(fig)

    if st.checkbox("Show scatter plot"):
        x_axis = st.selectbox("X axis", st.session_state.df.columns)
        y_axis = st.selectbox("Y axis", st.session_state.df.columns)
        fig = px.scatter(st.session_state.df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)

    if st.checkbox("Show pie chart"):
        column = st.selectbox("Select column for pie chart", st.session_state.df.columns)
        fig = px.pie(st.session_state.df, names=column)
        st.plotly_chart(fig)

    if st.checkbox("Show histogram"):
        column = st.selectbox("Select column for histogram", st.session_state.df.columns)
        fig = px.histogram(st.session_state.df, x=column)
        st.plotly_chart(fig)

    if st.checkbox("Show box plot"):
        column = st.selectbox("Select column for box plot", st.session_state.df.columns)
        fig = px.box(st.session_state.df, y=column)
        st.plotly_chart(fig)
else:
    st.warning("Please complete the Data Collection and Data Preprocessing steps first.")
