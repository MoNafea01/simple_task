from sklearn.model_selection import train_test_split

class TrainTestSplit:
    def __init__(self, data, **params):
        self.data = data.get('data') if isinstance(data, dict) else data
        self.params = params
        self.payload = self.split()
        self.out1 = self.payload['data'][0]
        self.out2 = self.payload['data'][1]

    def split(self):
        try:
            output = train_test_split(self.data,**self.params)
            output = [output[0], output[1]]
            payload = {"message": "Data split successful", 
                       "data": output,
                       "params": self.params, 
                       "node_name": "TrainTestSplit", 
                       "node_type": "preprocessing", 
                       "node_id": id(self), 
                       }
            return payload
        except Exception as e:
            raise ValueError(f"Error splitting data: {e}")

    def __str__(self):
        return f"data: {self.payload}"

    def __call__(self, *args):
        payload = self.payload.copy()
        for arg in args:
            if arg == '1':
                payload['data'] = self.out1
            elif arg == '2':
                payload['data'] = self.out2
        return payload


if __name__ == "__main__":
    import numpy as np
    data = [[1,2,3,4,5], [6,7,8,9,10]]
    y = np.array([0, 1, 0, 1, 0])
    data = {
        "data":[[0, 1, 0, 1, 0]]
    }
    splitter = TrainTestSplit(data, test_size=0.2, random_state=42)
    print(splitter('1'))
