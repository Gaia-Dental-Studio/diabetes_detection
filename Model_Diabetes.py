# Diabetes Detector
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image


df = pd.read_csv('diabetes.csv')

y = df['Outcome']
X = df.drop(['Outcome'],axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)


RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train,y_train)

import pickle
pickle.dump(RandomForestClassifier, open('Diabetes_clf.pkl', 'wb'))