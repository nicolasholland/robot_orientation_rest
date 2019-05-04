"""
Server application, rest api that accepts images and returns probabilities.

curl (example, use the request.py instead):

$ curl -d '{"img": [1, 2, 3], "x": 10, "y": 10}' -X POST http://localhost:5000/api
"""
import numpy as np
from flask import Flask, request, jsonify
import pickle

from model import cluster_image

server = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@server.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    image = np.array(data)

    feature = np.array([cluster_image(image)])

    prediction = model.predict(feature).flatten()

    retval = prediction.tolist()

    return jsonify(retval)

if __name__ == '__main__':
    server.run(port=5000, debug=True)

