# ai_operations/utils/model/model_fit.py
from model import Model
from utils import save_node, get_attributes, load_node, handle_name

class Fit:
    def __init__(self, X, y, model: dict|str = None):
        self.model_path = model
        self.model = model() if isinstance(model, Model) else load_node(model)
        self.X = X
        self.y = y
        self.payload = self.fit()
    
    def fit(self):
        if isinstance(self.model, dict):
            try:
                model = self.model['node']
                model = model.fit(self.X, self.y)
                attributes = get_attributes(model)
                self.payload = {"message": "Model fitted", "node": model, 
                                'attributes': attributes , 'node_id': self.model['node_id'],
                                'node_name': self.model['node_name']}
                save_node(self.payload)
                return self.payload
            except Exception as e:
                raise ValueError(f"Error fitting model: {e}")
        try:
            node_name, node_id = handle_name(self.model_path)
            model = self.model.fit(self.X, self.y)
            attributes = get_attributes(model)
            self.payload = {"message": "Model fitted", "node": model, 
                            'attributes': attributes , 'node_id': node_id,
                            'node_name':node_name}
            save_node(self.payload)
            return self.payload
        except Exception as e:
            raise ValueError(f"Error fitting model: {e}")
    
    
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    

if __name__ == '__main__':
    # model = "C:\\Users\\a1mme\\OneDrive\\Desktop\\MO\\test_grad\\backend\\core\\nodes\\saved\\models\\linear_regression_2446545222544.pkl"
    model = Model('linear_regression', 'linear_models', 'regression', {})
    fit = Fit([[1, 2], [2, 3]], [3, 4], model)
    print(fit)