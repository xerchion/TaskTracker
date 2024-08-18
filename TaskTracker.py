import sys
from typing import List

from Action import Action
from constants import NAME_FILE
from File import File
from TodoList import TodoList

file = File(NAME_FILE)


def catch_intro() -> List[str]:
    """Capture parameters of user in CLI and return them as a list."""
    return sys.argv[1:] if len(sys.argv) > 1 else []


def run_user_action(action, todo_list):
    if action.get_name() == "add":
        if action.has_valid_arguments():
            description = action.get_args()[1]
            if not todo_list.task_exists(description):
                todo_list.add_task(description)
                file.save_data(todo_list.to_dict())
            else:
                print("\nYa hay una tarea con esa descripción. ")
                print("Se muestra a continuación: ")
                todo_list.view(todo_list.get_task(action.get_name()))
        else:
            print("Para añadir una tarea es necesaria su descripcion")
    elif action.get_name() == "update":
        if action.get_n_args() > 1:
            task_id = int(arguments[1])
            task_new_name = arguments[2]
            todo_list.update_task(task_id, task_new_name)
            file.save_data(todo_list.to_dict())
        else:
            print("Para añadir una tarea es necesaria su descripcion")
    elif action.get_name() == "delete":
        if action.get_n_args() > 1:
            task_id = int(arguments[1])
            if todo_list.delete_task(task_id):
                file.save_data(todo_list.to_dict())
                print("Tarea borrada, correctamente, de la lista")

            else:
                print("No existe ninguna tarea con ese identificador")
    elif action.get_name()[:4] == "mark":
        if action.get_n_args() > 1:
            task_id = int(arguments[1])
            if task_id < todo_list.size():
                todo_list.mark_task(task_id, action[5:])
                file.save_data(todo_list.to_dict())
            else:
                print("No existe una tarea con ese identificador")
    elif action == "list":
        filter = arguments[1]
        # opcion de listado completo, sin mas argumentos
        if action.get_n_args() == 1:
            tasks = todo_list.filter_by("all")
        else:  # listar por tipo
            tasks = todo_list.filter_by(filter)
        if len(tasks) != 0:
            print("\nMostrando tareas por filtro:     " + filter + "\n")
            todo_list.view(tasks)
        else:
            print("No hay ninguna tarea en estado: " + filter)


# Main
arguments = catch_intro()  # call to capture user intro

# comprobar si existe archivo json ya creado
if not file.exists():
    file.create([])
else:
    todo_list = TodoList(file.extract_data())
todo_list = TodoList(file.extract_data())
action = Action(arguments)

if action.is_valid():
    run_user_action(action, todo_list)
else:
    print(action.show_error())
