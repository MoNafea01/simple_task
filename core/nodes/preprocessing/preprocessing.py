# Preprocessing nodes
# core/nodes/preprocessing.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, MaxAbsScaler, RobustScaler, QuantileTransformer, PowerTransformer
import pandas as pd

class Preprocessor:
    def __init__(self, scaling=True, test_size=0.2, random_state=42, scaler_type=None,split_data=True):
        self.test_size = test_size
        self.random_state = random_state
        self.scaler_type = scaler_type
        self.split_data = split_data
    def preprocess(self, X, y):
        scalers = {
            'standard': StandardScaler,
            'minmax': MinMaxScaler,
            'maxabs': MaxAbsScaler,
            'robust': RobustScaler,
            'quantile': QuantileTransformer,
            'power': PowerTransformer,
            'normalizer': Normalizer
        }
        # Optionally scale data
        if self.split_data:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
            if self.scaler_type == None:
                return X_train, X_test, y_train, y_test
            
        if self.scaler_type is not None:
            if self.scaler_type not in scalers.keys():
                raise ValueError(f"Unsupported scaler: {self.scaler_type}")
            
            scaler = scalers[self.scaler_type]()
            if self.split_data:
                X_train = scaler.fit_transform(X_train)
                X_test = scaler.transform(X_test)
                return X_train, X_test, y_train, y_test
            
            X = scaler.fit_transform(X)
            return X, y
        else:
            return X, y

if __name__ == "__main__":
    # Example usage
    import numpy as np
    X = np.random.rand(100, 10)
    y = np.random.rand(100)
    
    preprocessor = Preprocessor(scaling=True, test_size=0.3, random_state=42, 
                                scaler_type='standard',split_data=True)
    X_train, X_test, y_train, y_test = preprocessor.preprocess(X, y)
    print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")


