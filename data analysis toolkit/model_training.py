import streamlit as st
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import plotly.figure_factory as ff


def train_model(X_train, y_train, model_type, params):
    if model_type == "Random Forest":
        model = RandomForestClassifier()
    elif model_type == "SVM":
        model = SVC()
    elif model_type == "Logistic Regression":
        model = LogisticRegression()
    elif model_type == "Gradient Boosting":
        model = GradientBoostingClassifier()
    elif model_type == "Decision Tree":
        model = DecisionTreeClassifier()

    grid_search = GridSearchCV(model, params, cv=5)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_


st.header('4. Model Training')
if 'df' in st.session_state and st.session_state.df is not None:
    target = st.selectbox('Select target variable', st.session_state.df.columns)
    X = st.session_state.df.drop(columns=[target])
    y = st.session_state.df[target]

    test_size = st.slider('Test size (percentage)', 10, 50, 20) / 100.0
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    st.write(f"Training set size: {X_train.shape[0]}")
    st.write(f"Testing set size: {X_test.shape[0]}")

    model_type = st.selectbox("Choose model",
                              ["Random Forest", "SVM", "Logistic Regression", "Gradient Boosting", "Decision Tree"])
    if model_type == "Random Forest":
        params = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20, 30]
        }
    elif model_type == "SVM":
        params = {
            'C': [0.1, 1, 10],
            'kernel': ['linear', 'rbf']
        }
    elif model_type == "Logistic Regression":
        params = {
            'C': [0.1, 1, 10],
            'solver': ['lbfgs', 'liblinear']
        }
    elif model_type == "Gradient Boosting":
        params = {
            'n_estimators': [50, 100, 200],
            'learning_rate': [0.01, 0.1, 0.2],
            'max_depth': [3, 5, 7]
        }
    elif model_type == "Decision Tree":
        params = {
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10]
        }

    if st.button("Train Model"):
        model = train_model(X_train, y_train, model_type, params)
        y_pred = model.predict(X_test)
        st.write("Classification Report:")
        st.text(classification_report(y_test, y_pred))

        if st.checkbox("Show confusion matrix"):
            cm = confusion_matrix(y_test, y_pred)
            fig = ff.create_annotated_heatmap(z=cm, x=['Predicted 0', 'Predicted 1'], y=['Actual 0', 'Actual 1'],
                                              colorscale='Viridis')
            st.plotly_chart(fig)

        if st.checkbox("Show feature importances (for applicable models)"):
            if model_type in ["Random Forest", "Gradient Boosting", "Decision Tree"]:
                feature_importances = pd.DataFrame(model.feature_importances_, index=X.columns,
                                                   columns=['Importance']).sort_values('Importance', ascending=False)
                st.bar_chart(feature_importances)
            else:
                st.warning("Feature importances are not available for the selected model.")
else:
    st.warning("Please complete the Data Collection and Data Preprocessing steps first.")
