from data_store import get_data_store

def handle_block_command(sub_cmd, args):
    if sub_cmd == "make" or sub_cmd == "mkblk":
        return create_block(*args)
    elif sub_cmd == "edit" or sub_cmd == "edblk":
        return edit_block(*args)
    elif sub_cmd == "list_blocks" or sub_cmd == "lsblk":
        return list_blocks()
    elif sub_cmd == "remove" or sub_cmd == "rmblk":
        return remove_block(*args)
    return f"Unknown block command: {sub_cmd}"

def create_block(block_name, ports, params):
    data_store = get_data_store()
    active_user = data_store["active_user"]
    active_project = data_store["active_project"]
    active_workflow = data_store["active_workflow"]

    if not active_user or not active_project or not active_workflow:
        return "No workflow selected."

    project = data_store["users"][active_user]["projects"][active_project]
    workflow = project[active_workflow]

    workflow[block_name] = {
        "ports": ports,
        "params": params
    }
    return f"Block {block_name} created with ports {ports} and params {params}."

def edit_block(block_name, ports, params):
    data_store = get_data_store()
    active_user = data_store["active_user"]
    active_project = data_store["active_project"]
    active_workflow = data_store["active_workflow"]

    if not active_user or not active_project or not active_workflow:
        return "No workflow selected."

    project = data_store["users"][active_user]["projects"][active_project]
    workflow = project[active_workflow]

    if block_name in workflow:
        workflow[block_name]["ports"] = ports
        workflow[block_name]["params"] = params
        return f"Block {block_name} updated with new ports {ports} and params {params}."
    return f"Block {block_name} does not exist."

def remove_block(block_name):
    data_store = get_data_store()
    active_user = data_store['active_user']
    active_project = data_store["active_project"]
    active_workflow = data_store["active_workflow"]
    if active_project is None or active_workflow is None:
        return "No workflow selected."
    project = data_store['users'][active_user]["projects"][active_project]
    workflow = project[active_workflow]
    if block_name in workflow:
        del workflow[block_name]
        print( f"Block {block_name} removed.")
        return block_name
    print( "Block does not exist.")
    return None

def list_blocks():
    data_store = get_data_store()
    active_user = data_store["active_user"]
    active_project = data_store["active_project"]
    active_workflow = data_store["active_workflow"]

    if not active_user or not active_project or not active_workflow:
        return "No workflow selected."

    blocks = data_store["users"][active_user]["projects"][active_project][active_workflow].keys()
    return "Blocks: " + ", ".join(blocks)
