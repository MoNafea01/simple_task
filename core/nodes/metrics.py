# Evaluation metric nodes
# core/nodes/metrics.py
from sklearn.metrics import accuracy_score, precision_score, recall_score

class Evaluator:
    def __init__(self, metric='accuracy'):
        self.metric = metric

    def evaluate(self, y_true, y_pred):
        if self.metric == 'accuracy':
            return accuracy_score(y_true, y_pred)
        elif self.metric == 'precision':
            return precision_score(y_true, y_pred)
        elif self.metric == 'recall':
            return recall_score(y_true, y_pred)
        else:
            raise ValueError(f"Unsupported evaluation metric: {self.metric}")

if __name__ == "__main__":
    # Example usage
    import numpy as np
    y_true = np.random.randint(0, 2, 100)
    y_pred = np.random.randint(0, 2, 100)

    evaluator = Evaluator(metric='accuracy')
    score = evaluator.evaluate(y_true, y_pred)
    print(f"Score: {score}")