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

### **Option 1: Using Docker**

If you prefer to use Docker, you can quickly run the application by pulling the pre-built Docker image from Docker Hub.

1. **Pull the Docker Image**:
   You can pull the pre-built Docker image for this API:
   ```bash
   docker pull bynned/hatespeech-api
   ```

2. **Run the Docker Container**:
   After pulling the image, run the container using the following command:
   ```bash
   docker run -p 5050:5050 bynned/hatespeech-api
   ```
   This will start the Flask API inside the container, accessible on `http://localhost:5050`.

---

### **Option 2: Running the Application Manually**

If you prefer to run the API manually without Docker, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hatespeech-api.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the `hatespeech_model.h5` and `tfidf_vectorizer.pkl` files in the project directory.

4. Start the API server:
   ```bash
   python toxic_check_service.py
   ```
   The server will run on `http://localhost:5050`.

---
