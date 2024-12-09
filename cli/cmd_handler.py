from handlers.user_handler import handle_user_command
from handlers.project_handler import handle_project_command
from handlers.workflow_handler import handle_workflow_command
from handlers.block_handler import handle_block_command
import re

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
        "make_admin": handle_user_command, "mkadm": handle_user_command,

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
        "explore": handle_block_command, "exblk": handle_block_command,
        
        "list_commands": help_commands, "help": help_commands,
        "aino": activate_mode
    }
    if len(args) == 0:
        arg = []
    elif len(args) == 1:
        arg = args
    else:
        arg = [args[0]] 
        if args[1].startswith("("):
            arg.extend(re.findall(r'\(.*?\)', ' '.join(args[1:])))
        else:
            arg.extend(args[1:])

    if sub_cmd in commands:
        return commands[sub_cmd](sub_cmd,arg)
    else:
        return f"Unknown sub-command: {sub_cmd}"

def help_commands():
    """
    Provides a list of available commands.
    """
    return """
    Available commands:
    User commands:
        mkusr  | create_user <user_name> <password>
        selusr | load_user <user_name> <password>
        rmusr  | remove_user <user_name>

    Project commands:
        mkprj   | create_project <project_name>
        selprj  | select_project <project_name>
        rmprj   | remove_project <project_name>
        dselprj | deselect_project
        lsprj   | list_projects

    Workflow commands:
        mkwf  | create_workflow <workflow_name>
        selwf | select_workflow <workflow_name>
        rmwf  | remove_workflow <workflow_name>
        lswf  | list_workflows
        fnwf  | finish_workflow
        dselwf| deselect_workflow
    Block commands:
        make   | mkblk <block_name> <ports_in,ports_out> <params_names,params_values>
        edit   | edblk <block_name> <ports_in,ports_out> <params_names,params_values>
        remove | rmblk <block_name>
        lsblk  | list_blocks
    General commands:
        help    | list_commands
    """
def activate_mode(*args):
    return "Mode activated."
