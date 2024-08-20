ACTION_POS = 0
TEXT_POS = 1
ACTIONS = ["add", "update", "delete", "mark-in-progress", "mark-done", "list"]
N_ARGUMENTS = [1, 2, 1, 1, 1, [0, 1]]
NAME_FILE = "tasks.json"

USER_MSG = {
    "HELP": "You can view the help in the README.md file",
    "NO_TASK_IN_STATUS": "There are no tasks in status: ",
    "FILTERED_TASKS": "Showing tasks by filter:     ",
    "HEADER_LIST": "Id            Description                    Status \
            Created             Updated",
    "TASK_ALREADY_EXISTS": "There is already a task with that description.",
    "TASK_ADDED_OK": "Task saved successfully",
    "TASK_DELETED_OK": "Task deleted successfully",
    "TASK_UPDATED_OK": "Task updated successfully",
    "ID_NO_EXISTS": "There is no task with that identifier.",
    "ARGS_NO_VALID": "The arguments are not valid.",
    "N_ARGS_NO_VALID": "The number of arguments is not valid for this action",
    "NO_ACTION": "You did not specify an action, please provide one.",
    "NO_VALID_ACTION": "Please provide a valid action.",
}

# TodoList Constants
LAST = -1
INC = 1
