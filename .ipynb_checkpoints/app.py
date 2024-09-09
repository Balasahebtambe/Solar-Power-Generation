from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the model from the pickle file
with open('GB.pkl', 'rb') as file:
    model = pickle.load(file)


# Define a route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.json

    # Convert data to a NumPy array for prediction
    # Assuming the data is sent as a JSON array of features
    features = np.array([data['features']])

    # Make prediction using the model
    prediction = model.predict(features)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction.tolist()})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
