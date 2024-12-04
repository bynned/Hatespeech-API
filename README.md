# Hate Speech Prediction API Documentation

## Overview
This API is designed to detect hate speech in a given text using a pre-trained TensorFlow model and a TF-IDF vectorizer. The model predicts whether a given text contains hate speech and provides the probability of the prediction.

---

## API Endpoints

### `POST /api/predict`
This endpoint takes a JSON payload containing text and returns whether the text contains hate speech, along with the prediction probability.

#### Request
- **Method**: `POST`
- **Content-Type**: `application/json`

##### Body Parameters
| Field | Type   | Description                |
|-------|--------|----------------------------|
| text  | string | The text to be analyzed.   |

##### Example Request Body
```json
{
    "text": "This is an example text to analyze."
}
```

#### Response
- **Content-Type**: `application/json`

##### Response Fields
| Field             | Type    | Description                               |
|--------------------|---------|-------------------------------------------|
| text              | string  | The original text provided.               |
| is_hate_speech    | boolean | Whether the text is classified as hate speech. |
| probability       | float   | The probability that the text is hate speech (value between 0 and 1). |
| error (optional)  | string  | Error message in case of a failure.       |
| trace (optional)  | string  | Detailed stack trace in case of a failure. |

##### Example Successful Response
```json
{
    "text": "This is an example text to analyze.",
    "is_hate_speech": false,
    "probability": 0.3
}
```

##### Example Error Response
```json
{
    "error": "Invalid input. Please provide text."
}
```

---

## Error Handling
The API handles errors gracefully and returns appropriate HTTP status codes and error messages in the response.

| HTTP Status Code | Description                                       |
|------------------|---------------------------------------------------|
| 200              | Request processed successfully.                  |
| 400              | Invalid request (e.g., missing `text` parameter).|
| 500              | Internal server error (e.g., prediction failure, model not loaded).|

---

## Setup and Deployment

### Requirements
- Python 3.7+
- Flask
- TensorFlow
- Joblib
- Pre-trained model file (`hatespeech_model.h5`)
- TF-IDF vectorizer file (`tfidf_vectorizer.pkl`)

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the `hatespeech_model.h5` and `tfidf_vectorizer.pkl` files in the project directory.

### Running the Server
Start the API server:
```bash
python app.py
```
The server will run on `http://localhost:5050`.

---

## Notes
1. Ensure that both the model (`hatespeech_model.h5`) and the vectorizer (`tfidf_vectorizer.pkl`) are properly trained and available in the project directory.
2. Update the model and vectorizer as needed to improve prediction accuracy.
3. The threshold for hate speech classification is set at 0.5; adjust it based on the requirements.
