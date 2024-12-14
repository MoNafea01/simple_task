from .transformer import Scaler
from .utils import save_node, get_attributes, load_node, handle_name



class Fit:
    def __init__(self, data, transformer: dict|str = None):
        self.transfomer_path = transformer
        self.transfomer = transformer() if isinstance(transformer, Scaler) else load_node(transformer)
        self.data = data
        self.payload = self.fit()

    def fit(self):
        if isinstance(self.transfomer, dict):
            try:
                transformer = self.transfomer['node']
                if hasattr(transformer, 'fit_transform'):
                    transformer = transformer.fit(self.data)
                    attributes = get_attributes(transformer)
                    self.payload = {"message": "Transformer Fitted", "node": transformer,
                                    'attributes': attributes,
                                    'node_name':self.transfomer['node_name'],
                                    'node_id': self.transfomer['node_id']
                                    }
                    save_node(self.payload)
                    return self.payload
            except Exception as e:
                raise ValueError(f"Error fitting transformer: {e}")
        try:
            node_name, node_id = handle_name(self.transfomer_path)
            transformer = self.transfomer.fit(self.data)
            attributes = get_attributes(transformer)
            self.payload = {"message": "Transformer Fitted", "node": transformer,
                            'attributes': attributes,'node_id': node_id,
                            'node_name':node_name
                            }
            save_node(self.payload)
            return self.payload
        except Exception as e:
            raise ValueError(f"Error fitting transformer: {e}")
    
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    

if __name__ == '__main__':
    scaler = Scaler("standard", {'with_mean': True, 'with_std': True})
    fit = Fit([[1, 2], [2, 3]], scaler)
    print(fit)
    
