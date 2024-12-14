from .transformer import Scaler
from .utils import save_node, get_attributes, load_node, handle_name, _get_nodes_dir



class Fit:
    def __init__(self, data, transformer: dict|str = None):
        self.transformer_path = transformer
        self.transformer = transformer() if isinstance(transformer, Scaler) else (transformer if isinstance(transformer, dict)
                                      else load_node(transformer))
        self.data = data
        self.payload = self.fit()

    def fit(self):
        if isinstance(self.transformer, dict):
            try:
                import joblib
                nodes_dir = _get_nodes_dir()
                transformer = joblib.load(f'{nodes_dir}\\{self.transformer['node_name']}_{self.transformer['node_id']}.pkl')
                transformer = transformer.fit(self.data)
                if hasattr(transformer, 'fit_transform'):
                    transformer = transformer.fit(self.data)
                    attributes = get_attributes(transformer)
                    payload = {"message": "Transformer Fitted", "node": transformer,
                                    'attributes': attributes,
                                    'node_name':self.transformer['node_name'],
                                    'node_id': self.transformer['node_id']
                                    }
                    save_node(payload)
                    del payload['node']
                    return payload
            except Exception as e:
                raise ValueError(f"Error fitting transformer: {e}")
        try:
            node_name, node_id = handle_name(self.transformer_path)
            transformer = self.transformer.fit(self.data)
            attributes = get_attributes(transformer)
            payload = {"message": "Transformer Fitted",
                            'attributes': attributes,'node_id': node_id,
                            'node_name':node_name, "node": transformer
                            }
            save_node(payload)
            del payload['node']
            return payload
        except Exception as e:
            raise ValueError(f"Error fitting transformer: {e}")
    
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    

if __name__ == '__main__':
    # scaler = Scaler("standard", {'with_mean': True, 'with_std': True})
    scaler = r"C:\Users\a1mme\OneDrive\Desktop\MO\test_grad\backend\core\nodes\saved\preprocessors\standard_2054159895008.pkl"
    fit = Fit([[1, 2], [2, 3]], scaler)
    print(fit)
    
