# Import the libraies
import numpy as np
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import joblib

model = joblib.load('model.pkl')

# Define the '/' root route to display the content from index.html
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = [float(x) for x in request.form.values()]
    features = [np.array(form_data)]
    prediction = model.predict(features)
    print(prediction)
    # Format prediction text for display in "index.html"
    return render_template('index.html', Red_Wine_Quality_Prediction='Red wine quality value should be {}'.format(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
