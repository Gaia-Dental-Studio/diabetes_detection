import streamlit as st
import requests
import pandas as pd

# Streamlit app
st.set_page_config(layout="wide")
st.title('Diabetes Detection application')
st.write('This application uses Random Forest Algorithm to do prediction')
st.write('*******')

# Sidebar for input information
st.sidebar.header('Parameter Information:')

parameter_list = [
    '**Pregnancies:** Number of times pregnant ',
    '**Glucose:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test',
    '**BloodPressure:** Diastolic blood pressure (mm Hg)',
    '**SkinThickness:** Triceps skin fold thickness (mm)',
    '**Insulin:** 2-Hour serum insulin (mu U/ml)',
    '**BMI:** Body mass index (weight in kg/(height in m)^2)',
    '**DiabetesPedigreeFunction:** Diabetes pedigree function',
    '**Age:** Age (years)'
] 

for item in parameter_list:
    st.sidebar.markdown(item)

def get_user_input():
    st.subheader('Select Input Parameters')
    Pregnancies = st.slider('Pregnancies', 0, 17, 3)
    Glucose = st.slider('Glucose', 0, 199, 117)
    BloodPressure = st.slider('BloodPressure', 0, 160, 72)
    SkinThickness = st.slider('SkinThickness', 0, 99, 23)
    Insulin = st.slider('Insulin', 0.0, 846.0, 30.0)
    BMI = st.slider('BMI', 0.0, 67.1, 32.0)
    DiabetesPedigreeFunction = st.slider('Diab. Pedigree Func', 0.078, 2.42, 0.3725)
    Age = st.slider('Age', 20, 100, 40)

    user_data = {
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    }
    features = pd.DataFrame(user_data, index=[0])
    return features

user_input = get_user_input()

# Show input data on the Streamlit app
st.write('**Patient entered medical data (as selected via slider):** ')
st.write(user_input)

# API URL (Flask endpoint)
api_url = "http://127.0.0.1:5000/predict"

# Button for prediction
if st.button('Submit'):
    # Send user input to Flask API via POST request
    response = requests.post(api_url, json=user_input.to_dict(orient='records')[0])
    
    # Parse response from Flask
    if response.status_code == 200:
        result = response.json()['prediction']
        st.subheader(f'Machine Learning Model Prediction: {result.capitalize()}')
    else:
        st.error('Error in API request')
