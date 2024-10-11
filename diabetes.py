# Diabetes Detector
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

#!pip install -q streamlit

import streamlit as st
st.set_page_config(layout="wide")
st.write("""
# Welcome to Diabetes Detection Webpage
""")
st.write('*******')
image = Image.open('Capture.JPG')

#image

# st.image(image,caption='ML',use_column_width=True)

df = pd.read_csv('diabetes.csv')

#df

# st.subheader('Data Information :')
# st.dataframe(df)
# st.write(df.describe())

# chart = st.bar_chart(df)

y = df['Outcome']

X = df.drop(['Outcome'],axis=1)

#X

#y

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

# Get the feature input from users

# X.columns

# X['Insulin'].max()

def get_user_input():
  Pregnancies = st.sidebar.slider('Pregnancies',0,17,3)
  Glucose = st.sidebar.slider('Glucose',0,199,117)
  BloodPressure = st.sidebar.slider('BloodPressure',0,160,72)
  SkinThickness = st.sidebar.slider('SkinThickness',0,99,23)
  Insulin = st.sidebar.slider('Insulin',0.0,846.0,30.0)
  BMI = st.sidebar.slider('BMI',0.0,67.1,32.0)
  DiabetesPedigreeFunction = st.sidebar.slider('Diab. Pedigree Func',0.078,2.42,0.3725)
  Age = st.sidebar.slider('Age',20,100,30)

  user_data = {'Pregnancies': Pregnancies,
               'Glucose' : Glucose,
               'BloodPressure' : BloodPressure,
               'SkinThickness' : SkinThickness,
               'Insulin': Insulin,
               'BMI': BMI,
               'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
               'Age': Age
               }
  features = pd.DataFrame(user_data,index =[0])
  return features

user_input = get_user_input()

st.subheader('Patient entered medical data (as selected via slider on the left) : ')

st.write(user_input)

RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train,y_train)

prediction = RandomForestClassifier.predict(user_input)

# st.subheader('Machine Learning Model Prediction: Patient is - ')
# st.write(prediction)

if prediction == 1:
  st.subheader('Machine Learning Model Prediction : Member is diabetic')
else:
 st.subheader('Machine Learning Model Prediction :  Member is non-diabetic')

st.subheader('Machine Learning Model Confidence level(Test Accuracy Score) is :')
st.write(str(accuracy_score(y_test,RandomForestClassifier.predict(X_test)) *100) +'%')
