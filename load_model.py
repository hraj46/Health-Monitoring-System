import pickle
import numpy as np

# Load the trained model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Example input: Blood Pressure, Sugar, Cholesterol, Haemoglobin
input_data = np.array([[150, 220, 260, 13]])  # A new patient’s health data

# Apply scaling before prediction
input_data_scaled = scaler.transform(input_data)

# Make prediction
prediction = model.predict(input_data_scaled)
print("Prediction:", "High Risk" if prediction[0] == 1 else "Low Risk")
