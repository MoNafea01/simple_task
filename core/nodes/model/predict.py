from model import Model
from fit import Fit
from utils import load_node

class Predict:
    def __init__(self, model, X):
        self.model_payload = model()
        self.X = X
        self.payload = self.predict_model()
    
    def predict_model(self):
        try:
            model = load_node(self.model_payload)
            prediction = model.predict(self.X)
            self.payload = {"message": "Model predicted", "node": model, 'prediction': prediction,
                            "node_id": self.model_payload['node_id'], 
                            "node_name": self.model_payload['node_name']
                            }
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