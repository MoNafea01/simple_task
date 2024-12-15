from .preprocessors import PREPROCESSORS as preprocessors
from .utils import save_node


class Preprocessor:
    def __init__(self, preprocessor_name, preprocessor_type, params):
        self.preprocessor_name = preprocessor_name
        self.preprocessor_type = preprocessor_type
        self.params = params
        self.payload = self.create_preprocessor()


    def create_preprocessor(self):
        if self.preprocessor_type not in preprocessors:
            raise ValueError(f"""Unsupported preprocessor type: {self.preprocessor_type}
                            available types are: {list(preprocessors.keys())}""")

        if self.preprocessor_name not in preprocessors[self.preprocessor_type]:
            raise ValueError(f"Unsupported preprocessor: {self.preprocessor_name}")
        
        preprocessor = preprocessors[self.preprocessor_type][self.preprocessor_name].get('node')(**self.params)
        payload = {"message":f"{self.preprocessor_type} created {self.preprocessor_name}", 
                   "params": self.params,
                   "node_name": self.preprocessor_name, 
                   "node_type": self.preprocessor_type, 
                   "node_id": id(preprocessor), 
                   "node": preprocessor
                   }
        save_node(payload)
        del payload['node']
        return payload
    
    def update_params(self, params):
        self.params = params
        self.payload = self.create_preprocessor()
    
    def __str__(self):
        return str(self.payload)
    
    def __call__(self,*args):
        return self.payload

    

if __name__ == "__main__":
    scaler = Preprocessor('standard_scaler', 'scaler', {})
    print(scaler)
    
