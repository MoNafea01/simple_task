from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import pandas as pd


def perform_train_test_split(data, test_size, random_state=None):
    X = pd.DataFrame(data["X"])
    y = pd.Series(data["y"])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return {
        "X_train": X_train.values.tolist(),
        "X_test": X_test.values.tolist(),
        "y_train": y_train.tolist(),
        "y_test": y_test.tolist()
    }

def perform_standard_scaler(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(pd.DataFrame(data))
    return {"scaled_data": scaled_data.tolist()}

def perform_logistic_regression(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return {"model_params": model.get_params(), "model_coefficients": model.coef_.tolist()}

def calculate_accuracy_score(y_true, y_pred):
    return {"accuracy": accuracy_score(y_true, y_pred)}

def perform_model_predict(model, X):
    predictions = model.predict(X)
    return {"predictions": predictions.tolist()}

def perform_model_fit(model_params, X_train, y_train):
    model = LogisticRegression(**model_params)
    model.fit(X_train, y_train)
    return {"model_coefficients": model.coef_.tolist()}

def perform_scaler_fit_transform(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(pd.DataFrame(data))
    return {"scaled_data": scaled_data.tolist(), "scaler": scaler}

def perform_scaler_transform(scaler, data):
    scaled_data = scaler.transform(pd.DataFrame(data))
    return {"scaled_data": scaled_data.tolist()}

def load_iris_data():
    iris = load_iris()
    return {
        "data": iris.data.tolist(),
        "target": iris.target.tolist(),
        "target_names": iris.target_names.tolist(),
        "feature_names": iris.feature_names
    }

def perform_print(message):
    print(message)
    return {"message": message}