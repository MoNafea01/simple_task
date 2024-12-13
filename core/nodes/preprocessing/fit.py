from transformer import Scaler
from utils import save_node, get_attributes


class Fit:
    def __init__(self, transformer, data):
        self.transfomer_payload = transformer()
        self.data = data
        self.payload = self.fit()

    def fit(self):
        if isinstance(self.transfomer_payload, dict):
            try:
                transformer = self.transfomer_payload['node']
                if hasattr(transformer, 'fit_transform'):
                    transformer = transformer.fit(self.data)
                    attributes = get_attributes(transformer)
                    self.payload = {"message": "Transformer Fitted", "node": transformer,
                                    'attributes': attributes, 'node_name':self.transfomer_payload['node_name'],
                                    'node_id': self.transfomer_payload['node_id']
                                    }
                    save_node(self.payload)
                    return self.payload
            except Exception as e:
                raise ValueError(f"Error transforming data: {e}")
        else:
            raise ValueError(f"Please provide transformer payload as dict")
        
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    

if __name__ == '__main__':
    scaler = Scaler("standard", {'with_mean': True, 'with_std': True})
    fit = Fit(scaler, [[1, 2], [2, 3]])
    print(fit)
    