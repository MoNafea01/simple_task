from data_store import get_data_store

def handle_project_command(sub_cmd, args):
    if sub_cmd == "create_project" or sub_cmd == "mkprj":
        return create_project(*args)
    elif sub_cmd == "select_project" or sub_cmd == "selprj":
        return select_project(*args)
    elif sub_cmd == "deselect_project" or sub_cmd == "dselprj":
        return deselect_project()
    elif sub_cmd == "list_projects" or sub_cmd == "lsprj":
        return list_projects()
    elif sub_cmd == "remove_project" or sub_cmd == "rmprj":
        return remove_project(*args)
    return f"Unknown project command: {sub_cmd}"

def create_project(project_name):
    data_store = get_data_store()
    active_user = data_store["active_user"]
    if not active_user:
        return "No user selected."
    data_store["users"][active_user]["projects"][project_name] = {}
    data_store["active_project"] = project_name
    return f"Project {project_name} created."

def select_project(project_name):
    data_store = get_data_store()
    active_user = data_store["active_user"]
    if not active_user:
        return "No user selected."
    if project_name in data_store["users"][active_user]["projects"]:
        data_store["active_project"] = project_name
        return f"Project {project_name} selected."
    return "Project does not exist."

def deselect_project():
    data_store = get_data_store()
    data_store["active_project"] = None
    return "Project deselected."

def list_projects():
    data_store = get_data_store()
    active_user = data_store["active_user"]
    if not active_user:
        return "No user selected."
    projects = data_store["users"][active_user]["projects"]
    return "Projects: " + ", ".join(projects.keys())

def remove_project(project_name):
    data_store = get_data_store()
    active_user = data_store['active_user']
    if active_user is None:
        return "No user selected."
    if project_name in data_store['users'][active_user]["projects"]:
        del data_store['users'][active_user]["projects"][project_name]
        print( f"Project {project_name} removed.")
        return project_name
    print( "Project does not exist.")
    return None