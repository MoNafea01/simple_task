from model import Model
from fit import Fit
from utils import load_model

class Predict:
    def __init__(self, fit, X):
        self.fit_payload = fit.payload
        self.X = X
        self.payload = {
            "message": "Model hadn't predicted yet",
            "model": None,
            'predictions': None,
            'model_id': self.fit_payload['model_id'],
            'model_name': self.fit_payload['model_name']
        }
        self.predict = self.predict_model()
    
    def predict_model(self):
        try:
            model = load_model(self.payload)
            prediction = model.predict(self.X)
            self.payload = {"message": "Model predicted", "model": model, 'prediction': prediction}
            return self.payload
        except Exception as e:
            raise ValueError(f"Error loading model: {e}")
    
    def __str__(self):
        return f'{self.payload}'


if __name__ == '__main__':
    model = Model('linear_regression', 'linear_models', 'regression', {})
    fit = Fit(model, [[1, 2], [2, 3]], [3, 4])
    pred = Predict(fit, [[3, 4], [4, 5]])
    print(pred.payload)