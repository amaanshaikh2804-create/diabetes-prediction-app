from flask import Flask, render_template, request
import numpy as np


app=Flask(__name__)

import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

with open(os.path.join(MODEL_DIR, "rf_model.pkl"), "rb") as f:
    rf_model = pickle.load(f)

with open(os.path.join(MODEL_DIR, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)

with open(os.path.join(MODEL_DIR, "imputer.pkl"), "rb") as f:
    fill_zeros = pickle.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
   try:
       # Define input field names
       field_names = ['num_preg', 'glucose_conc', 'diastolic_bp', 'insulin',
                      'bmi', 'diab_pred', 'age', 'skin']

       # Get data from form and keep it in a dictionary
       form_data = {field: request.form[field] for field in field_names}

       # Convert to float list
       features = [float(form_data[field]) for field in field_names]
       input_array = np.asarray(features).reshape(1, -1)

       # Preprocess
       input_array = fill_zeros.transform(input_array)
       input_array = scaler.transform(input_array)

       # Predict
       prediction = rf_model.predict(input_array)
       result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

       return render_template('index.html', prediction_text=f'Prediction: {result}', form_data=form_data)

   except Exception as e:
       return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__=="__main__":
    app.run(debug=False)