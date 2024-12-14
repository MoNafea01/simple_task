# User-defined custom nodes
# core/nodes/custom.py

class CustomNode:
    def __init__(self, function):
        self.function = function  # Expecting a custom function passed in
    
    def execute(self, *args, **kwargs):
        return self.function(*args, **kwargs)
