import sys
from typing import List

from Action import Action
from constants import NAME_FILE, USER_MSG
from File import File
from TodoList import TodoList
from View import View


# Capture parameters of user in CLI and return them as a list.
def catch_intro() -> List[str]:
    return sys.argv[1:] if len(sys.argv) > 1 else []


def run_user_action(action, todo_list, file):
    if action.get_name() == "add":
        if action.has_valid_arguments():
            description = action.get_args()[1]
            if not todo_list.task_exists(description):
                todo_list.add_task(description)
                file.save_data(todo_list.to_dict())
                view.ok(USER_MSG["ADD_OK"])
            else:
                view.alert(USER_MSG["TASK_ALREADY_EXISTS"])
                todo_list.prepare_view(todo_list.get_task_by_description(description))
        else:
            view.alert(USER_MSG["TASK_WITHOUT_DESCRIPTION"])

    elif action.get_name() == "delete":
        if action.has_valid_arguments():
            task_id = int(action.get_args()[1])
            if todo_list.delete_task(task_id):
                file.save_data(todo_list.to_dict())
                view.ok(USER_MSG["TASK_DELETED"])
            else:
                view.alert(USER_MSG["ID_NO_EXISTS"] + ":", task_id)
        else:
            view.alert(USER_MSG["ARGS_NO_VALID"])

    elif action.get_name() == "update":
        if action.has_valid_arguments():
            task_id = int(action.get_args()[1])
            if todo_list.get_task_by_id(task_id):
                task_new_name = action.get_args()[2]
                todo_list.update_task(task_id, task_new_name)
                file.save_data(todo_list.to_dict())
                view.ok(USER_MSG["UPDATED_OK"])
            else:
                view.alert(USER_MSG["ID_NO_EXISTS"] + ":", task_id)
        else:
            view.alert(USER_MSG["TASK_WITHOUT_DESCRIPTION"])

    elif action.get_name()[:4] == "mark":
        if action.has_valid_arguments():
            task_id = int(action.get_args()[1])
            if todo_list.get_task_by_id(task_id):
                todo_list.mark_task(task_id, action.get_name()[5:])
                file.save_data(todo_list.to_dict())
                view.ok(USER_MSG["UPDATED_OK"])

            else:
                view.alert(USER_MSG["ID_NO_EXISTS"] + ":", task_id)

    elif action.get_name() == "list":
        filter = "all"
        # opcion de listado completo, sin mas argumentos
        if action.get_n_args() == 1:
            # listar por tipo
            filter = action.get_args()[1]
        tasks = todo_list.filter_by(filter)
        if len(tasks) != 0:
            view.info(USER_MSG["FILTERED_TASKS"] + filter + "\n")
            view.info(todo_list.prepare_view(tasks))

        else:
            view.alert(USER_MSG["NO_TASK_IN_STATUS"] + filter)


view = View()

# Load data
file = File(NAME_FILE)
if not file.exists():
    file.save_data([])
todo_list = TodoList(file.extract_data())

# Load user action
arguments = catch_intro()
action = Action(arguments)


if action.is_valid():
    run_user_action(action, todo_list, file)
else:
    view.alert(action.get_error_message())
    view.info(USER_MSG["HELP"])
