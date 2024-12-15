class Splitter:
    """
    This Class is responsible for splitting the data into two parts.\n
    to get the first part of the data, call the instance with 'out1' as an argument\n
    to get the second part of the data, call the instance with 'out2' as an argument\n
    it also accept a dictionary as an argument\n
    Note that the dictionary must have a key named "data" that has a list of two elements\n
    """

    def __init__(self, data):
        self.data = data.get('data') if isinstance(data, dict) else data
        self.payload = self.split()
        self.out1 = self.payload['data'][0]
        self.out2 = self.payload['data'][1]
    
    def split(self):
        try:
            d1, d2 = self.data[0], self.data[1]
            payload = {"message": "Data split successful", 
                   "data": [d1,d2],
                   "node_name": "Splitter", 
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
    data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    splitter = Splitter(data)
    print(splitter(''))