from .transformer import Scaler
from .fit import Fit
from .utils import save_data, load_node, get_attributes, handle_name, _get_nodes_dir

class Transform:
    def __init__(self, data, transformer: dict|str = None):
        self.transformer_path = transformer
        self.transformer = transformer() if isinstance(transformer, Fit) else (transformer() 
                                            if isinstance(transformer, Scaler) else(transformer if isinstance(transformer, dict)
                                            else(load_node(transformer))))
        self.data = data
        self.payload = self.transform()

    def transform(self):
        if isinstance(self.transformer, dict):
            try:
                import joblib
                nodes_dir = _get_nodes_dir()
                transformer = joblib.load(f'{nodes_dir}\\{self.transformer['node_name']}_{self.transformer['node_id']}.pkl')
                transformed = transformer.transform(self.data)
                attributes = get_attributes(transformer)
                payload = {"message": "Data transformed", "node": transformer,
                                'node_name': self.transformer['node_name'],
                                'node_id': self.transformer['node_id'], 'attributes': attributes,
                                'transformed_data': transformed
                                }
                save_data(payload)
                del payload['node']
                return payload
            except Exception as e:
                raise ValueError(f"Error loading transformer: {e}")
        try:
            node_name, node_id = handle_name(self.transformer_path)
            transformer = self.transformer
            transformed = transformer.transform(self.data)
            attributes = get_attributes(transformer)
            payload = {"message": "Data transformed", "node": transformer,
                            'node_name': node_name, 'node_id': node_id, 'attributes': attributes,
                            'transformed_data': transformed
                            }
            save_data(payload)
            del payload['node']
            return payload
        except Exception as e:
            raise ValueError(f"Error transforming data: {e}")
        
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    

if __name__ == '__main__':
    # scaler = Scaler("standard", {'with_mean': True, 'with_std': True})
    # fit = Fit([[1, 2], [2, 3]], scaler)
    scaler = r"C:\Users\a1mme\OneDrive\Desktop\MO\test_grad\backend\core\nodes\saved\preprocessors\standard_3121037534288.pkl"
    transformed = Transform([[3, 4], [4, 5]], scaler)
    print(transformed)
