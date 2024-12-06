from data_store import get_data_store, set_data_store
from save_load import save_data_to_file
import os

path = os.path.dirname(os.path.abspath(__file__)) + '/../'
data_file_path = path + 'data_store.json'

def handle_user_command(sub_cmd, args):

    commands = {
        "create_user": create_user,
        "mkusr": create_user,
        "load_user": load_user,
        "selusr": load_user,
        "remove_user": remove_user,
        "rmusr": remove_user,
    }

    if sub_cmd in commands:
        return commands[sub_cmd](*args)
    return f"Unknown user command: {sub_cmd}"


def create_user(username, password):
    data_store = get_data_store()
    if username not in data_store["users"]:
        data_store["users"][username] = {"password": password, "projects": {}}
        data_store["active_user"] = username
        save_data_to_file(data_file_path)
        return f"User {username} created."
    data_store["active_user"] = username
    return f"User {username} already exists."


def load_user(username, password):

    data_store = get_data_store()
    if username in data_store["users"] and data_store["users"][username]["password"] == password:
        data_store["active_user"] = username
        return f"User {username} loaded."
    return "Invalid username or password."


def remove_user(username):
    
    data_store = get_data_store()
    if not is_sudo():
        return "You must be an admin to remove users."
    if username in data_store["users"]:
        del data_store["users"][username]
        save_data_to_file(data_file_path)
        return f"User {username} removed."
    return "User does not exist."

def is_sudo():
    data_store = get_data_store()
    active_user = data_store["active_user"]
    return (data_store["users"][active_user]["password"] == "admin" and active_user == "admin")