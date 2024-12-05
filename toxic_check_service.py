from flask import Flask, request, jsonify
import traceback
import tensorflow as tf
import joblib
from flask_cors import CORS


app = Flask(__name__)

#Enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Load the model and vectorizer
try:
    model = tf.keras.models.load_model("hatespeech_model.h5")  # Load the trained model
    print("Model loaded successfully.")

    tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")  # Load the vectorizer
    print("TF-IDF Vectorizer loaded successfully.")
except Exception as e:
    print(f"Error loading model or vectorizer: {str(e)}")
    model = None
    tfidf_vectorizer = None

@app.route("/")
def hello():
    return "Welcome to HatespeechAPI!"


@app.route('/api/predict', methods=['POST'])
def predict():
    """Predict hate speech based on input text."""
    if model and tfidf_vectorizer:
        try:
            # Parse input JSON
            json_ = request.json
            if not json_ or 'text' not in json_:
                return jsonify({'error': 'Invalid input. Please provide text.'}), 400

            input_text = json_['text']

            input_vectorized = tfidf_vectorizer.transform([input_text])

            input_dense = input_vectorized.toarray()

            # Predict
            prediction = model.predict(input_dense)
            hate_speech_probability = float(prediction[0][0])
            is_hate_speech = hate_speech_probability > 0.5

            # Return the prediction
            return jsonify({
                'text': input_text,
                'is_hate_speech': is_hate_speech,
                'probability': hate_speech_probability
            })

        except Exception as e:
            return jsonify({'error': 'Prediction failed', 'trace': traceback.format_exc()}), 500
    else:
        return jsonify({'error': 'Model or vectorizer not loaded. Please check your setup.'}), 500

if __name__ == '__main__':
    try:
        port = 5050
        app.run(debug=True, host='0.0.0.0', port=port)
    except Exception as e:
        print(f"Error starting the server: {str(e)}")
