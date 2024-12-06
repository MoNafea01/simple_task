from handlers.user_handler import handle_user_command
from handlers.project_handler import handle_project_command
from handlers.workflow_handler import handle_workflow_command
from handlers.block_handler import handle_block_command

def cmd_handler(command,mode=False):
    try:
        if mode:
            command = "aino "+command
        args = command.split()
        
        if not args:
            return "No command entered."

        cmd = args[0]
        if cmd == 'nomode':
            return "Mode deactivated."

        elif cmd == "aino":
            sub_cmd = args[1]
            # Delegate to specific handlers
            if sub_cmd in {"create_user", "load_user", "remove_user","mkusr","selusr","rmusr"}:
                return handle_user_command(sub_cmd, args[2:])
            elif sub_cmd in {"create_project", "select_project", "deselect_project", "list_projects","remove_project",
                             "mkprj","selprj","dselprj","lsprj","rmprj"}:
                return handle_project_command(sub_cmd, args[2:])
            elif sub_cmd in {"create_workflow", "select_workflow", "list_workflows", "finish_workflow", 
            "remove_workflow","mkwf","selwf","lswf","fnwf","rmwf"}:
                return handle_workflow_command(sub_cmd, args[2:])
            elif sub_cmd in {"make", "edit", "list_blocks", "remove","mkblk","edblk","lsblk","rmblk"}:
                return handle_block_command(sub_cmd, args[2:])
            elif sub_cmd in {"list_commands","help"}:
                helper = f"""Available commands:\n\nUser commands:\n\tcreate_user | mkusr\t<user_name> <password>\n\tload_user   | selusr\t<user_name> <password>\n\tremove_user | rmusr\t<user_name>
                \nProject commands:\n\tcreate_project    | mkprj\t<project_name>\n\tselect_project    | selprj\t<project_name>\n\tremove_project    | rmprj\t<project_name>\n\tdeselect_project  | dselprj\n\tlist_projects     | lsprj
                \nWorkflow commands:\n\tcreate_workflow | mkwf\t<workflow_name>\n\tselect_workflow | selwf\t<workflow_name>\n\tremove_workflow | rmwf\t<workflow_name>\n\tlist_workflows  | lswf\n\tfinish_workflow | fnwf
                \nBlock commands:\n\tmake        | mkblk\t<block_name> <ports_in,ports_out> <params_names,params_values>\n\tedit        | edblk\t<block_name> <ports_in,ports_out> <params_names,params_values>\n\tremove      | rmblk\t<block_name>\n\tlist_blocks | lsblk
                \n\nGeneral commands:\n\tlist_commands | thelp"""
                return helper
            elif args[1] == 'aino' and mode==True:
                return "Mode activated."

            else:
                return f"Unknown sub-command: {sub_cmd}"

        else:
            return f"Unknown command: {cmd}"
    except Exception as e:
        return f"Error: {str(e)}"
