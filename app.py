import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    input_values = {}

    if request.method == 'POST':
        try:
            input_values = {key: request.form[key] for key in request.form}
            features = np.array([float(val) for val in input_values.values()]).reshape(1, -1)
            prediction = model.predict(features)[0]
        except:
            prediction = "Invalid input!"

    return render_template('index.html', prediction=prediction, input_values=input_values)

if __name__ == '__main__':
    app.run(debug=True)
