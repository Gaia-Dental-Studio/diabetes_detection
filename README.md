# Diabetes_detection
This repository code is adopted from https://github.com/DineshAnalyticsandAI/Diabetes-Detection with a modification in the user interface.

## Description
The application is built using a Random Forest model trained with the Pima Indians Diabetes dataset. The dataset, originally from the National Institute of Diabetes and Digestive and Kidney Diseases, contains information on 768 women from a population near Phoenix, Arizona, USA. 258 tested positive, and 500 tested negative. It consists of 2 classes and 8 attributes: pregnancies, OGTT(Oral Glucose Tolerance Test), blood pressure, skin thickness, insulin, BMI(Body Mass Index), age, and pedigree diabetes function.

### Independent Variables:
Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- BloodPressure: Diastolic blood pressure (mm Hg)
- SkinThickness: Triceps skin fold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age (years)

### Dependent Variable:
Outcome: Class variable: Non-diabetic (0) or Diabetic (1)

# Installation:
To set up the project, you can use the pip command to install the required packages specified in the requirements.txt file.
```
pip install -r requirements.txt
```
This will install all of the required packages for the project.

Run the application by executing the following two syntax in parallel:
```bash
python api.py
streamlit run app.py
```

#### API Endpoint

- **URL**: `/predict`
- **Method**: POST
