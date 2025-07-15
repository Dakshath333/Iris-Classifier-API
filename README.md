# Iris-Classifier-API
A lightweight Flask-based REST API that serves a machine learning model trained on the Iris dataset for real-time predictions.

# Iris Classifier API 🌸

This project is a simple Flask-based REST API that loads a trained machine learning model (Random Forest) to classify iris flower species using sepal and petal measurements.

---

## 🚀 Features

- Trained using scikit-learn's famous Iris dataset
- Uses a `RandomForestClassifier` for prediction
- Provides a `/predict` endpoint for real-time classification
- JSON-based request/response for easy integration

---

## 🧠 Model Details

The model is trained using `RandomForestClassifier` on the Iris dataset and saved using `joblib`.

---

## 📁 Project Structure

```bash
.
├── app.py               # Flask API server
├── train_model.py       # Script to train and save the model
├── iris_model.pkl       # Serialized trained model
├── requirements.txt     # List of Python dependencies
└── README.md            # Documentation
