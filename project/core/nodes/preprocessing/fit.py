from .preprocessor import Preprocessor
from .utils import save_node, get_attributes, load_node, handle_name, _get_nodes_dir



class Fit:
    def __init__(self, data, preprocessor: dict|str = None):
        self.preprocessor_path = preprocessor
        self.preprocessor = preprocessor() if isinstance(preprocessor, Preprocessor) else (preprocessor if isinstance(preprocessor, dict)
                                      else load_node(preprocessor))
        self.data = data
        self.payload = self.fit()

    def fit(self):
        if isinstance(self.preprocessor, dict):
            try:
                import joblib
                nodes_dir = _get_nodes_dir()
                preprocessor = joblib.load(f'{nodes_dir}\\{self.preprocessor['node_name']}_{self.preprocessor['node_id']}.pkl')
                preprocessor = preprocessor.fit(self.data)
                if hasattr(preprocessor, 'fit_transform'):
                    preprocessor = preprocessor.fit(self.data)
                    attributes = get_attributes(preprocessor)
                    payload = {"message": "preprocessor Fitted", "node": preprocessor,
                                    'attributes': attributes,
                                    'node_name':self.preprocessor['node_name'],
                                    'node_id': self.preprocessor['node_id']
                                    }
                    save_node(payload)
                    del payload['node']
                    return payload
            except Exception as e:
                raise ValueError(f"Error fitting preprocessor: {e}")
        try:
            node_name, node_id = handle_name(self.preprocessor_path)
            preprocessor = self.preprocessor.fit(self.data)
            attributes = get_attributes(preprocessor)
            payload = {"message": "preprocessor Fitted",
                            'attributes': attributes,'node_id': node_id,
                            'node_name':node_name, "node": preprocessor
                            }
            save_node(payload)
            del payload['node']
            return payload
        except Exception as e:
            raise ValueError(f"Error fitting preprocessor: {e}")
    
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    

if __name__ == '__main__':
    scaler = Preprocessor('standard_scaler', 'scaler', {})
    # scaler = r"C:\Users\a1mme\OneDrive\Desktop\MO\test_grad\backend\core\nodes\saved\preprocessors\standard_2054159895008.pkl"
    fit = Fit([[1, 2], [2, 3]], scaler)
    print(fit)
    
