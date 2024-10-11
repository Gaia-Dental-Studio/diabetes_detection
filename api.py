from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the RandomForestClassifier model
with open('Diabetes_clf.pkl', 'rb') as file:
    model = pickle.load(file)

# Route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json(force=True)
    
    # Convert data into a pandas DataFrame
    input_data = pd.DataFrame(data, index=[0])
    
    # Make a prediction
    prediction = model.predict(input_data)[0]
    
    # Return the result
    result = 'diabetic' if prediction == 1 else 'non-diabetic'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
