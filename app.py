# 빌트인
import logging

# 서드파티
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)


def preprocessing(json_payload):
    sentences = json_payload['message']
    tensor = tf.constant(sentences)
    return tensor


def postprocessing(json_payload, prediction_tensor):
    prediction = prediction_tensor.numpy()
    sentences = json_payload['message']
    response = {}
    d = {}
    for idx, sentence in enumerate(sentences):
        idx = np.argmax(prediction[idx])
        d[sentence] = 'ham' if idx == 1 else 'spam'
    response['request'] = sentences
    response['response'] = d
    return response


@app.route("/")
def home():
    html = "<h3>애저 파이프라인을 이용한 지속적 배포</h3>"
    return html.format(format)


@app.route("/predict", methods=['POST'])
def predict():
    model = tf.keras.models.load_model('./saved_model')
    app.logger.info(f"Model loaded.")
    
    json_payload = request.json
    app.logger.info(f"JSON payload: {json_payload}")

    preprocessed_payload = preprocessing(json_payload)
    prediction = model(preprocessed_payload)
    app.logger.info(f"Prediction: {prediction}")

    response = postprocessing(json_payload, prediction)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
