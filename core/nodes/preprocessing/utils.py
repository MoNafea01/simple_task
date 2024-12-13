import os
import joblib

def _make_dirs(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory: {e}")

def save_node(payload):
    if isinstance(payload, dict):
        node_name = payload.get('node_name')
        node = payload.get('node')
        node_id = payload.get('node_id')
        nodes_dir = _get_nodes_dir()

        _make_dirs(nodes_dir)
        node_path = f'{nodes_dir}\\{node_name}_{node_id}.pkl'
        joblib.dump(node, node_path)


def save_data(payload):
    if isinstance(payload, dict):
        node_name = payload.get('node_name')
        node = payload.get('node')
        node_id = payload.get('node_id')
        nodes_dir = _get_nodes_dir('saved\\data')
        _make_dirs(nodes_dir)
        node_path = f'{nodes_dir}\\{node_name}_{node_id}.pkl'
        joblib.dump(node, node_path)


def load_node(path: str):
    if isinstance(path, str):
        try:
            return joblib.load(path)
        except Exception as e:
            raise ValueError(f"Error loading model: {e}")
    else:
        raise ValueError(f"Please provide model payload as string")



def _get_nodes_dir(directory='saved\\preprocessors'):
    nodes_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    nodes_dir = os.path.join(nodes_path, directory)
    return nodes_dir

def get_attributes(transformer):

    excluded_attributes = {
        "n_samples_seen_",
        "n_features_in_",
        "feature_names_in_",
        "dtype_",
        "sparse_input_"
    }
    attributes = {
        attr: getattr(transformer, attr)
        for attr in dir(transformer)
        if attr.endswith("_") and not attr.startswith("_") and attr not in excluded_attributes
    }
    return attributes


def handle_name(path = None):
    name = path.split("\\")[-1].split(".")[0]
    # remove numbers using re
    import re
    _name = re.sub(r'\d+', '', name)
    _id = re.sub(r'\D', '', name)
    _name = _name.rsplit("_", 1)[0]
    return _name,int(_id)

