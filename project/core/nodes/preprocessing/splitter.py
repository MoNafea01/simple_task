from sklearn.model_selection import train_test_split

# class TrainTestSplit:
#     def __init__(self, *data, test_size : float = 0.25, random_state : int = None) -> dict[str, list]:
#         self.data = [d for d in data]
#         self.test_size = test_size
#         self.random_state = random_state
#         self.payload = self.split()

#     def split(self):
#         try:
#             len_data = len(self.data)
#             Xy = len_data * 2
#             arr = [0]*Xy
#             self.data = [d for d in self.data]
            
#             arr = train_test_split(
#                 *self.data,
#                 test_size=self.test_size,
#                 random_state=self.random_state
#             )
#             train = arr[::2]
#             test = arr[1::2]
#             return {"train_data": train, "test_data": test}
#         except Exception as e:
#             raise ValueError(f"Error splitting data: {e}")

#     def __str__(self):
#         return f"Train data: {self.payload.get('train_data')}, Test data: {self.payload.get('test_data')}"

#     def __call__(self):
#         return self.payload

class TrainTestSplit:
    def __init__(self, data, test_size: float = 0.25, random_state: int = None) -> dict:
        self.data = data  # Expecting data in a list of lists or similar format
        self.test_size = test_size
        self.random_state = random_state
        self.payload = self.split()

    def split(self):
        try:
            # Assuming 'data' is a dictionary with input features and labels, e.g. {'X': X_data, 'y': y_data}
            if isinstance(self.data, dict) and 'X' in self.data and 'y' in self.data:
                X = self.data['X']
                y = self.data['y']
            else:
                raise ValueError("Data must be a dictionary with 'X' and 'y' keys for features and labels.")

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=self.test_size, random_state=self.random_state
            )

            return {
                "train_data": {"X": X_train, "y": y_train},
                "test_data": {"X": X_test, "y": y_test},
            }
        except Exception as e:
            raise ValueError(f"Error splitting data: {e}")

    def __str__(self):
        return f"Train data: {self.payload.get('train_data')}, Test data: {self.payload.get('test_data')}"

    def __call__(self):
        return self.payload

if __name__ == "__main__":
    import numpy as np
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 2)
    y = np.array([0, 1, 0, 1, 0])
    data = {'X': X, 'y': y}
    splitter = TrainTestSplit(data, test_size=0.2, random_state=42)
    train, test= splitter().items()
    print(train)
    print(test)

