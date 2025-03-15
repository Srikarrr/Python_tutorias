from flask import Flask,jsonify, request
import numpy as np
import joblit

app =Flask(__name__)

#dummy prediction endpoint
@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Simulate a random prediction
    prediction = np.random.rand() # Replace 
    return jsonify ({'prediction':prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)   