import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Generate dummy health data for 10,000 patients
np.random.seed(42)
data = pd.DataFrame({
    'bp': np.random.randint(80, 180, 10000),   # Blood Pressure
    'sugar': np.random.randint(70, 250, 10000),  # Sugar Level
    'cholesterol': np.random.randint(100, 300, 10000),  # Cholesterol
    'haemoglobin': np.random.uniform(8, 18, 10000)  # Haemoglobin
})

# Generate a dummy target variable (1 = High Risk, 0 = Low Risk)
data['risk'] = np.where((data['bp'] > 140) | (data['sugar'] > 200) | (data['cholesterol'] > 250), 1, 0)

# Split dataset
X = data.drop(columns=['risk'])
y = data['risk']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save the model and scaler
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Model and Scaler saved successfully as 'model.pkl' and 'scaler.pkl'.")
