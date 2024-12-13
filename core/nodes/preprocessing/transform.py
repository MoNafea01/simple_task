from transformer import Scaler
from fit import Fit
from utils import save_data, load_node

class Transform:
    def __init__(self, transformer, data):
        self.transformer_payload = transformer()
        self.data = data
        self.payload = self.transform()

    def transform(self):
        try:
            transformer = load_node(self.transformer_payload)
            transformed = transformer.transform(self.data)
            self.payload = {"message": "Data transformed", "node": transformer,
                            'node_name': self.transformer_payload['node_name'],
                            'node_id': self.transformer_payload['node_id'],
                            'transformed_data': transformed
                            }
            save_data(self.payload)
            return self.payload
        
        except Exception as e:
            raise ValueError(f"Error transforming data: {e}")
        
    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload
    

if __name__ == '__main__':
    scaler = Scaler("standard", {'with_mean': True, 'with_std': True})
    fit_transform = Fit(scaler, [[1, 2], [2, 3]])
    transform = Transform(fit_transform, [[3, 4], [4, 5]])
    print(transform)
