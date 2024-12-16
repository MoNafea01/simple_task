# Data loading nodes
# backend/core/nodes/dataLoader.py
import pandas as pd
from sklearn.datasets import load_iris, load_diabetes

class DataLoader:
    def __init__(self, data_type=None, filepath=None):
        self.data_type = data_type
        self.filepath = filepath
        self.payload = self.load()
        self.X = self.payload['data'][0]
        self.y = self.payload['data'][1]
    def load(self):
        datasets = {
                'iris': load_iris,
                'diabetes': load_diabetes,
                'custom': self._load_custom_data
            }
        try:
            if self.data_type in datasets.keys():
                data =  datasets[self.data_type](return_X_y=True)
                payload = {"message": f"Data loaded: {self.data_type}",
                           "data" : data,
                           "node_name": self.data_type,
                            "node_type": "data_loader",
                            }
                return payload
            else:
                raise ValueError(f"Unsupported data type: {self.data_type}")
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def _load_custom_data(self, *args, **kwargs):
        data = pd.read_csv(self.filepath)
        import os
        self.data_type = os.path.basename(self.filepath).split('.')[0]
        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        return X, y
    
    def __str__(self):
        return f'{self.payload}'
    
    def __call__(self, *args):
        payload = self.payload.copy()
        for arg in args:
            if arg == '1':
                payload['data'] = self.X
            elif arg == '2':
                payload['data'] = self.y
        return payload
                

if __name__ == "__main__":
    # Example usage
    # loader = DataLoader(data_type='iris')
    # X, y = loader.load()

    # loader = DataLoader(data_type='diabetes')
    # X, y = loader('X'),loader('y')

    loader = DataLoader(data_type='custom', filepath=r"C:\Users\a1mme\OneDrive\Desktop\MO\test_grad\project\core\data.csv")
    X, y = loader('X'),loader('y')
    print(f"Loaded data: {X}, {y}")
    

