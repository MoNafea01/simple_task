from .transformers import SCALERS
from .utils import save_node


class Scaler:
    def __init__(self, scaler_name, params):
        self.scaler_name = scaler_name
        self.params = params
        self.payload = self.create_scaler()

    def create_scaler(self):
        if self.scaler_name not in SCALERS:
            raise ValueError(f"Unsupported scaler: {self.scaler_name}")
        scaler = SCALERS[self.scaler_name]['scaler'](**self.params)
        payload = {
            "message": f"Scaler created {self.scaler_name}", "params": self.params,
            "node": scaler, "node_name": self.scaler_name, "node_id": id(scaler)
        }
        save_node(payload)
        del payload['node']
        return payload
    
    
    def update_params(self, params):
        self.params = params
        self.payload = self.create_scaler()

    def __str__(self):
        return str(self.payload)
    
    def __call__(self):
        return self.payload

    

if __name__ == "__main__":
    scaler = Scaler("standard_scaler",{})
    print(scaler)
    