# Data loading nodes
# backend/core/nodes/dataLoader.py
import pandas as pd
from sklearn.datasets import load_iris, load_diabetes

class DataLoader:
    def __init__(self, data_type='iris', filepath=None):
        self.data_type = data_type
        self.filepath = filepath

    def load(self):
        datasets = {
                'iris': load_iris,
                'diabetes': load_diabetes,
                'custom': self._load_custom_data
            }
        try:
            if self.data_type in datasets.keys():
                return datasets[self.data_type](return_X_y=True)
            else:
                raise ValueError(f"Unsupported data type: {self.data_type}")
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def _load_custom_data(self, *args, **kwargs):
        # Load custom dataset from a CSV file
        data = pd.read_csv(self.filepath)
        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        return X, y


if __name__ == "__main__":
    # Example usage
    loader = DataLoader(data_type='iris')
    X, y = loader.load()
    print(f"Loaded data: {X.shape}, {y.shape}")

    loader = DataLoader(data_type='diabetes')
    X, y = loader.load()
    print(f"Loaded data: {X.shape}, {y.shape}")

    loader = DataLoader(data_type='custom', filepath='backend/core/data.csv')
    X, y = loader.load()
    print(f"Loaded data: {X.shape}, {y.shape}")
    