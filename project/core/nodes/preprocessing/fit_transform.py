from .transformer import Scaler
from .utils import save_data, save_node, load_node, get_attributes, handle_name, _get_nodes_dir

class FitTransform:
    def __init__(self, data, transformer: dict | str = None):
        self.transformer_path = transformer
        self.transformer = transformer() if isinstance(transformer, Scaler) else (transformer if isinstance(transformer, dict)
                                      else load_node(transformer))
        self.data = data
        self.payload = self.fit_transform()

    def fit_transform(self):
        if isinstance(self.transformer, dict):
            try:
                import joblib
                nodes_dir = _get_nodes_dir()
                transformer = joblib.load(f'{nodes_dir}\\{self.transformer['node_name']}_{self.transformer['node_id']}.pkl')
                if hasattr(transformer, 'fit_transform'):
                    transformed_data = transformer.fit_transform(self.data)
                    attributes = get_attributes(transformer)
                    payload = {
                        "message": "Data fitted and transformed",
                        "node": transformer,
                        'node_name': self.transformer['node_name'],
                        'node_id': self.transformer['node_id'],
                        'attributes': attributes,
                        'transformed_data': transformed_data
                    }
                    save_node(payload)
                    save_data(payload)
                    del payload['node']
                    return payload
            except Exception as e:
                raise ValueError(f"Error fitting and transforming transformer: {e}")
        try:
            node_name, node_id = handle_name(self.transformer_path)
            transformed_data = self.transformer.fit_transform(self.data)
            attributes = get_attributes(self.transformer)
            payload = {
                "message": "Data fitted and transformed",
                "node": self.transformer,
                'node_name': node_name,
                'node_id': node_id,
                'attributes': attributes,
                'transformed_data': transformed_data
            }
            save_node(payload)
            save_data(payload)
            del payload['node']
            return payload
        except Exception as e:
            raise ValueError(f"Error fitting and transforming data: {e}")

    def __str__(self):
        return str(self.payload)

    def __call__(self):
        return self.payload


if __name__ == '__main__':
    import numpy as np
    data = np.array([[1, 2], [2, 3]])
    # scaler = Scaler("standard", {'with_mean': True, 'with_std': True})
    scaler = r"C:\Users\a1mme\OneDrive\Desktop\MO\test_grad\backend\core\nodes\saved\preprocessors\standard_2186793224480.pkl"
    fit_transform = FitTransform(data, scaler)
    print(fit_transform)