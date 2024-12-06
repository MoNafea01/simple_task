from handlers.user_handler import handle_user_command
from handlers.project_handler import handle_project_command
from handlers.workflow_handler import handle_workflow_command
from handlers.block_handler import handle_block_command

def cmd_handler(command,mode=False):
    try:
        if mode:
            command = "aino " + command

        args = command.split()
        if not args:
            return "No command entered."

        cmd = args[0]
        if cmd == 'nomode':
            return "Mode deactivated."

        elif cmd == "aino":
            sub_cmd = args[1]
            if len(args) == 1:
                return handle_sub_command(sub_cmd)
            return handle_sub_command(sub_cmd, args[2:])
        
        return f"Unknown command: {cmd}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_sub_command(sub_cmd, args):
    commands = {
        "create_user": handle_user_command, "mkusr": handle_user_command,
        "load_user": handle_user_command, "selusr": handle_user_command,
        "remove_user": handle_user_command, "rmusr": handle_user_command,
        "create_project": handle_project_command, "mkprj": handle_project_command,
        "select_project": handle_project_command, "selprj": handle_project_command,
        "deselect_project": handle_project_command, "dselprj": handle_project_command,
        "list_projects": handle_project_command, "lsprj": handle_project_command,
        "remove_project": handle_project_command, "rmprj": handle_project_command,
        "create_workflow": handle_workflow_command, "mkwf": handle_workflow_command,
        "select_workflow": handle_workflow_command, "selwf": handle_workflow_command,
        "deselect_workflow": handle_workflow_command, "dselwf": handle_workflow_command,
        "list_workflows": handle_workflow_command, "lswf": handle_workflow_command,
        "finish_workflow": handle_workflow_command, "fnwf": handle_workflow_command,
        "remove_workflow": handle_workflow_command, "rmwf": handle_workflow_command,
        "make": handle_block_command, "mkblk": handle_block_command, 
        "edit": handle_block_command, "edblk": handle_block_command,
        "remove": handle_block_command, "rmblk": handle_block_command,
        "list_blocks": handle_block_command, "lsblk": handle_block_command,
        "list_commands": help_commands, "help": help_commands,
        "aino": activate_mode
    }

    if sub_cmd in commands:
        return commands[sub_cmd](sub_cmd,args)
    else:
        return f"Unknown sub-command: {sub_cmd}"

def help_commands():
    """
    Provides a list of available commands.
    """
    return """
    Available commands:
    User commands:
        create_user | mkusr <user_name> <password>
        load_user | selusr <user_name> <password>
        remove_user | rmusr <user_name>
    Project commands:
        create_project | mkprj <project_name>
        select_project | selprj <project_name>
        remove_project | rmprj <project_name>
        deselect_project | dselprj
        list_projects | lsprj
    Workflow commands:
        create_workflow | mkwf <workflow_name>
        select_workflow | selwf <workflow_name>
        remove_workflow | rmwf <workflow_name>
        list_workflows | lswf
        finish_workflow | fnwf
    Block commands:
        make | mkblk <block_name> <ports_in,ports_out> <params_names,params_values>
        edit | edblk <block_name> <ports_in,ports_out> <params_names,params_values>
        remove | rmblk <block_name>
        list_blocks | lsblk
    General commands:
        list_commands | help
    """
def activate_mode(*args):
    return "Mode activated."
