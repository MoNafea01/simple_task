# ai_operations/utils/model/model_fit.py
from model import Model
import os
import joblib
from utils import save_model, get_attributes
class Fit:
    def __init__(self, model, X, y):
        self.model_payload = model.payload
        self.X = X
        self.y = y
        self.payload = {
            "message": "Model hadn't been fitted yet",
            "model": None,
            'attributes': None,
            'model_name': self.model_payload['model_name'],
            'model_id': self.model_payload['model_id']
        }
        self.fit = self.fit_model()
    
    def fit_model(self):
        if isinstance(self.model_payload, dict):
            try:
                model = self.model_payload['model']
                model = model.fit(self.X, self.y)
                attributes = get_attributes(model)
                self.payload = {"message": "Model fitted", "model": model, 
                                'attributes': attributes , 'model_id': self.payload['model_id'],
                                'model_name': self.payload['model_name']}
                save_model(self.payload)
                return self.payload
            except Exception as e:
                raise ValueError(f"Error fitting model: {e}")
        else:
            raise ValueError(f"Please provide model payload as dict")
    

    def __str__(self):
        return str(self.payload)
    
    
    
if __name__ == '__main__':
    model = Model('linear_regression', 'linear_models', 'regression', {})
    fit = Fit(model, [[1, 2], [2, 3]], [3, 4])
    print(fit)
