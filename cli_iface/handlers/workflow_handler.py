from data_store import get_data_store

def handle_workflow_command(sub_cmd, args):
    if sub_cmd == "create_workflow" or sub_cmd == "mkwf":
        return create_workflow(*args)
    elif sub_cmd == "select_workflow" or sub_cmd == "selwf":
        return select_workflow(*args)
    elif sub_cmd == "list_workflows" or sub_cmd == "lswf":
        return list_workflows()
    elif sub_cmd == "finish_workflow" or sub_cmd == "fnwf":
        return finish_workflow()
    elif sub_cmd == "remove_workflow" or sub_cmd == "rmwf":
        return remove_workflow(*args)
    return f"Unknown workflow command: {sub_cmd}"

def create_workflow(workflow_name):
    data_store = get_data_store()
    active_project = data_store["active_project"]
    active_user = data_store["active_user"]
    if not active_project or not active_user:
        return "No project selected."
    project = data_store["users"][active_user]["projects"][active_project]
    project[workflow_name] = {}
    data_store["active_workflow"] = workflow_name
    return f"Workflow {workflow_name} created."

def select_workflow(workflow_name):
    data_store = get_data_store()
    active_project = data_store["active_project"]
    active_user = data_store["active_user"]
    if not active_project or not active_user:
        return "No project selected."
    project = data_store["users"][active_user]["projects"][active_project]
    if workflow_name in project:
        data_store["active_workflow"] = workflow_name
        return f"Workflow {workflow_name} selected."
    return "Workflow does not exist."

def remove_workflow(workflow_name):
    data_store = get_data_store()
    active_user = data_store['active_user']
    active_project = data_store["active_project"]
    if active_project is None:
        return "No project selected."
    project = data_store['users'][active_user]["projects"][active_project]
    if workflow_name in project:
        del project[workflow_name]
        print( f"Workflow {workflow_name} removed.")
        return workflow_name
    print( "Workflow does not exist.")
    return None

def list_workflows():
    data_store = get_data_store()
    active_project = data_store["active_project"]
    active_user = data_store["active_user"]
    if not active_project or not active_user:
        return "No project selected."
    workflows = data_store["users"][active_user]["projects"][active_project]
    return "Workflows: " + ", ".join(workflows.keys())

def finish_workflow():
    return "Workflow finished."
