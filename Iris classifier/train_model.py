from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, 'iris_model.pkl')

print("Model saved as iris_model.pkl")
