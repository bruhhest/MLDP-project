import streamlit as st
import pandas as pd

st.write("""
# Simple Red Wine Quality Prediction App
This app predicts the **Red Wine Quality** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    fixed_acidity = st.sidebar.slider('fixed_acidity', 5.0, 7.0, 9.0)
    volatile_acidity = st.sidebar.slider('volatile_acidity', 0.2, 0.5, 0.8)
    residual_sugar = st.sidebar.slider('residual_sugar', 1.0, 2.0, 3.0)
    citric_acid = st.sidebar.slider('citric_acid', 0.0, 0.2, 0.4)
    chlorides = st.sidebar.slider('chlorides', 0.0, 0.1, 0.2)
    free_sulfur_dioxide = st.sidebar.slider('free_sulfur_dioxide', 10.0, 20.0, 30.0)
    total_sulfur_dioxide = st.sidebar.slider('total_sulfur_dioxide', 40.0, 50.0, 60.0)
    density = st.sidebar.slider('density', 0.8, 0.9, 1.0)
    pH = st.sidebar.slider('pH', 2.0, 3.0, 4.0)
    citric_acid = st.sidebar.slider('sulphates', 0.5, 0.6, 0.7)
    citric_acid = st.sidebar.slider('alcohol', 9.0, 9.5, 10.0)
    data = {'fixed_acidity': fixed_acidity,
            'volatile_acidity': volatile_acidity,
            'residual_sugar': residual_sugar,
            'citric_acid': citric_acid,
            'chlorides': chlorides,
            'free_sulfur_dioxide': free_sulfur_dioxide,
            'total_sulfur_dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

Red_Wine_Quality = datasets.load_Red_Wine_Quality()
X = Red_Wine_Quality.data
Y = Red_Wine_Quality.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(dataset)
prediction_proba = clf.predict_proba(dataset)

st.subheader('Class labels and their corresponding index number')
st.write(Red_Wine_Quality.target_names)

st.subheader('Prediction')
st.write(Red_Wine_Quality.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
