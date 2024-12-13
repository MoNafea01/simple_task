from model import Model
from fit import Fit
from utils import load_node, handle_name, get_attributes


class Predict:
    def __init__(self, X, model: dict|str = None):
        self.model_path = model
        self.model = model() if isinstance(model, Fit) else (model() if isinstance(model,Model) 
                                                             else(load_node(model)))
        self.X = X
        self.payload = self.predict_model()
    
    def predict_model(self):
        if isinstance(self.model, dict):
            try:
                model = self.model['node']
                prediction = model.predict(self.X)
                attributes = get_attributes(model)
                self.payload = {"message": "Model predicted", "node": model, 'prediction': prediction,
                                "node_id": self.model['node_id'], "attributes": attributes,
                                "node_name": self.model['node_name']
                                }
                return self.payload
            except Exception as e:
                raise ValueError(f"Error loading model: {e}")
        try:
            node_name, node_id = handle_name(self.model_path)
            model = self.model
            prediction = model.predict(self.X)
            attributes = get_attributes(model)
            self.payload = {"message": "Model predicted", "node": model, 'prediction': prediction,
                            "node_id": node_id, "attributes": attributes,
                            "node_name": node_name
                            }
            return self.payload
        except Exception as e:
            raise ValueError(f"Error loading model: {e}")
    
    def __str__(self):
        return f'{self.payload}'
    
    def __call__(self):
        return self.payload

if __name__ == '__main__':
    model = Model('linear_regression', 'linear_models', 'regression', {})
    fit = Fit([[1, 2], [2, 3]], [3, 4], model)
    pred = Predict([[3, 4], [4, 5]], model)
    print(pred)