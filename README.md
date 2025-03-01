# Health-Monitoring-System
📌 Project Overview

The Health Monitoring System is designed to analyze patient health data using Big Data Technologies (Apache Spark, Hadoop, MapReduce) and Machine Learning. This project generates health records for 10,000 patients and processes them to predict whether a patient is at risk based on parameters like Blood Pressure (BP), Sugar Level, Cholesterol, and Hemoglobin Levels.

🔥 Key Features

Big Data Processing: Uses Apache Spark & Hadoop MapReduce for handling large-scale health data.

Machine Learning Model: A Random Forest Classifier is trained to predict health risks.

Scalability: The system can handle large datasets efficiently.

Interactive Dashboard: Visualization of health statistics.

Frontend Application: Built with Flask, featuring a responsive and aesthetic UI for predictions.

📊 Dataset Generation

Since no real dataset was used, synthetic data was generated using NumPy and Pandas:

Blood Pressure (BP): 80-180 mmHg

Sugar Level: 70-250 mg/dL

Cholesterol: 100-300 mg/dL

Hemoglobin: 8-18 g/dL

Risk Classification: (1 = High Risk, 0 = Low Risk)

⚡ Technologies Used

Big Data: Apache Spark, Hadoop, MapReduce

Machine Learning: Scikit-learn (Random Forest Classifier)

Web Framework: Flask

Frontend: HTML, CSS (Responsive Design)

Storage: Pickle (.pkl files for model & scaler)

🏗️ Project Structure

health-monitoring-system/
models/               # Stores model.pkl & scaler.pkl
static/               # CSS & Images (Aesthetic Background)
templates/            # HTML Files (Flask Frontend)
app.py                # Flask App (Frontend for Prediction)
requirements.txt      # Required dependencies
README.md             # Project Report

🚀 Run the Application

Install Dependencies

pip install -r requirements.txt

Start Flask App

python app.py

Open in Browser

http://127.0.0.1:5000/

📈 Results & Dashboard

The system provides: ✅ Health Risk Prediction based on user input. ✅ Basic Statistics on health conditions (e.g., average BP, Cholesterol levels). ✅ Visualization of Patient Data using Matplotlib/Seaborn (if needed).

📜 Conclusion

This Health Monitoring System successfully predicts health risks using Machine Learning & Big Data Processing. The system can be extended by:

Adding more health parameters (BMI, Heart Rate, Age, Gender, etc.)

Integrating real-time patient monitoring via IoT sensors

Deploying the model on Cloud (AWS/GCP) for real-world scalability.

📩 Contact

🔹 GitHub: https://github.com/hraj46/ 🔹 Email: rajhimanshu7452@gmail.com

