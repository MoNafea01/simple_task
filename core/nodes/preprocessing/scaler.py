from preprocessors import SCALERS as scalers
import pandas as pd

class Scaler:
    def __init__(self, scaler: str):
        self.scaler = scaler

    def fit(self, X: pd.DataFrame):
        if self.scaler in scalers:
            self.scaler = scalers[self.scaler]['scaler'](**scalers[self.scaler]['params'])
        else:
            raise ValueError("Invalid scaler")

        self.scaler.fit(X)

    def transform(self, X: pd.DataFrame):
        return self.scaler.transform(X)

    def inverse_transform(self, X: pd.DataFrame):
        return self.scaler.inverse_transform(X)
    
if __name__ == "__main__":
    # Example usage
    import numpy as np
    X = np.random.rand(100, 10)
    X = pd.DataFrame(X)
    scaler = Scaler(scaler='standard')
    scaler.fit(X)
    X_scaled = scaler.transform(X)
    X_inverse = scaler.inverse_transform(X_scaled)
    print(X_inverse)
    print(X_scaled)
    print(X)