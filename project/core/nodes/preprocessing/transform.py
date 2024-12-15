from .preprocessor import Preprocessor
from .fit import Fit
from .utils import save_data, load_node, get_attributes, handle_name, _get_nodes_dir

class Transform:
    def __init__(self, data, preprocessor: dict|str = None):
        self.preprocessor_path = preprocessor
        self.preprocessor = preprocessor() if isinstance(preprocessor, Fit) else (preprocessor() 
                                            if isinstance(preprocessor, Preprocessor) else(preprocessor if isinstance(preprocessor, dict)
                                            else(load_node(preprocessor))))
        self.data = data.get('data') if isinstance(data, dict) else data
        self.payload = self.transform()

    def transform(self):
        if isinstance(self.preprocessor, dict):
            try:
                import joblib
                nodes_dir = _get_nodes_dir()
                preprocessor = joblib.load(f'{nodes_dir}\\{self.preprocessor.get('node_name')}_{self.preprocessor.get('node_id')}.pkl')
                transformed = preprocessor.transform(self.data)
                attributes = get_attributes(preprocessor)
                payload = {"message": "Data transformed", 
                           'data': transformed,
                           "node": preprocessor,
                           'node_name': self.preprocessor.get('node_name'),
                           'node_id': self.preprocessor.get('node_id'), 
                           'attributes': attributes,
                           }
                save_data(payload)
                del payload['node']
                return payload
            except Exception as e:
                raise ValueError(f"Error loading preprocessor: {e}")
        try:
            node_name, node_id = handle_name(self.preprocessor_path)
            preprocessor = self.preprocessor
            transformed = preprocessor.transform(self.data)
            attributes = get_attributes(preprocessor)
            payload = {"message": "Data transformed", 
                       'data': transformed, 
                       "node": preprocessor,
                       'node_name': node_name, 
                       'node_id': node_id, 
                       'attributes': attributes,
                       }
            save_data(payload)
            del payload['node']
            return payload
        except Exception as e:
            raise ValueError(f"Error transforming data: {e}")
        
    def __str__(self):
        return str(self.payload)
    
    def __call__(self,*args):
        return self.payload
    

if __name__ == '__main__':
    scaler = Preprocessor("standard_scaler", "scaler", {'with_mean': True, 'with_std': True})
    fit = Fit([[1, 2], [2, 3]], scaler)
    # # scaler = r"C:\Users\a1mme\OneDrive\Desktop\MO\test_grad\backend\core\nodes\saved\preprocessors\standard_3121037534288.pkl"
    transformed = Transform([[3, 4], [4, 5]], scaler)
    print(transformed)
