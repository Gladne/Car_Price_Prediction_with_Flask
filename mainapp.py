# Import Flask library to create web application
from flask import Flask, render_template, request

# Import numpy for numerical array handling
import numpy as np

# Import pickle to load the trained ML model
import pickle

# Create  Flask app object
app = Flask(__name__)

# Load the trained machine learning model
# 'rb' means read binary mode
model = pickle.load(open('lr_model.pkl', 'rb'))

# Route for Home Page
@app.route('/')
def home():
    # Render the input form page
    return render_template('index.html')

# Route for Prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form values entered by user
    kms = float(request.form['kms'])                # kilimeters driven
    age = float(request.form['age'])                # car age
    original_price = float(request.form['price'])   # original car price
    fuel_type = request.form['fuel']                # fuel type selected
    transmission =request.form['transmission']      # transmission type

    # Convert Fuel Type into Numerical format
    if fuel_type == 'Petrol':
        fuel = [0, 0, 1]
    elif fuel_type == 'Diesel':
        fuel = [0, 1, 0]
    elif fuel_type == 'CNG':
        fuel = [1, 0, 0]
    else:
        fuel = [0, 0, 0]

    # Convert Transmission into Numerical format
    if transmission == 'Automatic':
        transmission_val = [1, 0]
    else:
        transmission_val = [0, 1]         

    # Prepare input for ML model
    data = np.array([[
        original_price,
        kms,
        age,
        fuel[0],
        fuel[1],
        fuel[2],
        transmission_val[0],
        transmission_val[1]

    ]])    

    # Predict car price
    prediction = model.predict(data)

    # Round prediction value
    predicted_price = round(prediction[0], 2)

    # Send result to result.html page
    return render_template('result.html', 
                           price = predicted_price)

# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # debug=True reloads server automatically







