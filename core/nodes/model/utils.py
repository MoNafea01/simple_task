import os
import joblib

def _make_dirs(directory):
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory: {e}")
    
def save_node(payload):
    if isinstance(payload, dict):
        node_name = payload['node_name']
        node = payload['node']
        node_id = payload['node_id']
        nodes_dir = _get_nodes_dir()

        _make_dirs(nodes_dir)
        node_path = f'{nodes_dir}\\{node_name}_{node_id}.pkl'
        joblib.dump(node, node_path)

def load_node(payload):
    if isinstance(payload, dict):
        try:
            node_name = payload['node_name']
            node_id = payload['node_id']
            nodes_dir = _get_nodes_dir()
            model_path = f'{nodes_dir}\\{node_name}_{node_id}.pkl'
            transfomer = joblib.load(model_path)
            return transfomer
        except Exception as e:
            raise ValueError(f"Error loading model: {e}")
        
    else:
        raise ValueError(f"Please provide model payload as dict")
    
def get_attributes(model):
    fitted_params = {}
    if hasattr(model, 'coef_'):
        fitted_params['coef_'] = model.coef_
    if hasattr(model, 'intercept_'):
        fitted_params['intercept_'] = model.intercept_
    if hasattr(model, 'classes_'):
        fitted_params['classes_'] = model.classes_
    if hasattr(model, 'support_vectors_'):
        fitted_params['support_vectors_'] = model.support_vectors_
    if hasattr(model, 'feature_importances_'):
        fitted_params['feature_importances_'] = model.feature_importances_
    if hasattr(model, 'tree_'):
        fitted_params['tree_'] = model.tree_
    if hasattr(model, 'n_iter_'):
        fitted_params['n_iter_'] = model.n_iter_
    return fitted_params

def _get_nodes_dir(directory='saved\\models'):
    nodes_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    nodes_dir = os.path.join(nodes_path, directory)
    return nodes_dir
