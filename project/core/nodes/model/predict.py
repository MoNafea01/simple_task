from .model import Model
from .fit import Fit
from .utils import load_node, handle_name, get_attributes, _get_nodes_dir


class Predict:
    def __init__(self, X, model: dict|str = None):
        self.model_path = model
        self.model = model() if isinstance(model, Fit) else (model() if isinstance(model,Model) 
                                else(model if isinstance(model, dict)
                                else(load_node(model))))
        self.X = X
        self.payload = self.predict_model()
    
    def predict_model(self):
        if isinstance(self.model, dict):
            try:
                import joblib
                nodes_dir = _get_nodes_dir()
                model = joblib.load(f'{nodes_dir}\\{self.model['node_name']}_{self.model['node_id']}.pkl')
                predictions = model.predict(self.X)
                attributes = get_attributes(model)
                payload = {"message": "Model predicted", 'predictions': predictions,
                                "node_id": self.model['node_id'], "attributes": attributes,
                                "node_name": self.model['node_name']
                                }
                return payload
            except Exception as e:
                raise ValueError(f"Error loading model: {e}")
        try:
            node_name, node_id = handle_name(self.model_path)
            model = self.model
            predictions = model.predict(self.X)
            attributes = get_attributes(model)
            payload = {"message": "Model predicted", 'predictions': predictions,
                            "node_id": node_id, "attributes": attributes,
                            "node_name": node_name
                            }
            return payload
        except Exception as e:
            raise ValueError(f"Error loading model: {e}")
    
    def __str__(self):
        return f'{self.payload}'
    
    def __call__(self):
        return self.payload

if __name__ == '__main__':
    # model = Model('logistic_regression', 'linear_models', 'classification', {'penalty': 'l2','C': 0.5,})
    # fit = Fit([[1, 2], [2, 3]], [3, 4], model)
    model = r"C:\Users\a1mme\OneDrive\Desktop\MO\test_grad\backend\core\nodes\saved\models\logistic_regression_2782831042800.pkl"
    pred = Predict([[3, 4], [4, 5]], model)
    print(pred)