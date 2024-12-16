# Model training nodes
# core/nodes/models.py
from .models import MODELS as models
from .utils import save_node


class Model:
    def __init__(self, model_name, model_type, task, params=None):
        self.model_name = model_name
        self.model_type = model_type
        self.task = task
        self.params = params if params else models.get(model_type).get(task).get(model_name).get('params')
        self.payload = self.create_model()

    def create_model(self):
        if self.model_type not in models:
            raise ValueError(f"""Unsupported model type: {self.model_type}
                             available types are: {list(models.keys())}""")
        
        if self.task not in models[self.model_type]:
            raise ValueError(f"Unsupported task type: {self.task}")
        
        if self.model_name not in models[self.model_type][self.task]:
            raise ValueError(f"Unsupported model type: {self.model_name}")
        
        model = models[self.model_type][self.task][self.model_name].get('node')(**self.params)
        payload = {"message": f"Model created {self.model_name}",
                   "params": self.params, 
                    "node_name": self.model_name, 
                    "node_type": self.model_type, 
                    "task": self.task,"node_id": id(model), 
                    "node": model
                    }
        save_node(payload)
        del payload['node']
        return payload
    
    def update_params(self, params):
        self.params = params
        self.payload = self.create_model()

    def __str__(self):
        return f'{self.payload}'
    
    def __call__(self, *args):
        return self.payload


if __name__ == '__main__':
    model = Model('ridge', 'linear_models', 'regression')
    print(model)
