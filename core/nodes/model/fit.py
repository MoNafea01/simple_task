# ai_operations/utils/model/model_fit.py
from model import Model
from utils import save_node, get_attributes


class Fit:
    def __init__(self, model, X, y):
        self.model_payload = model()
        self.X = X
        self.y = y
        self.payload = self.fit_model()
    
    def fit_model(self):
        if isinstance(self.model_payload, dict):
            try:
                model = self.model_payload['node']
                model = model.fit(self.X, self.y)
                attributes = get_attributes(model)
                self.payload = {"message": "Model fitted", "node": model, 
                                'attributes': attributes , 'node_id': self.model_payload['node_id'],
                                'node_name': self.model_payload['node_name']}
                save_node(self.payload)
                return self.payload
            except Exception as e:
                raise ValueError(f"Error fitting model: {e}")
        else:
            raise ValueError(f"Please provide model payload as dict")
    
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    
    
if __name__ == '__main__':
    model = Model('linear_regression', 'linear_models', 'regression', {})
    fit = Fit(model, [[1, 2], [2, 3]], [3, 4])
    print(fit)
