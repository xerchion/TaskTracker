import sys

from constants import ACTION_POS, ACTIONS, NAME_FILE
from File import File
from TodoList import TodoList

file = File(NAME_FILE)


def catch_intro():
    # Capture parameters of user in CLI
    # return:  user´s action and text of task
    arguments = sys.argv
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
    else:
        arguments = "   "

        # if len(sys.argv) == 1:            # debuggeo
        #    arguments = default_args

    return arguments


def validate_action(action):
    # desestructurar la instrucción
    # Valida si el usuario introduce una accion correcta
    if action in ACTIONS:
        # validada
        return True
    else:
        # ninguna accion
        if action == " ":
            print("Indique una acción")
        # accion no válida
        else:
            print("Invalid sentence")
    return False


def action_works():
    # leer datos desde el archivo
    # Añadir tareas
    if action == "add":
        if n_args > 1:
            task_name = arguments[1]
            if not todo_list.task_exists(task_name):
                todo_list.add_task(task_name)
                file.save_data(todo_list.to_dict())
            else:
                print(
                    "\nYa hay una tarea con esa descripción, se muestra a continuación: "
                )
                task = []
                task.append(todo_list.get_task(task_name))
                todo_list.view(task)

        else:
            print("Para añadir una tarea es necesaria su descripcion")
    elif action == "update":
        if n_args > 1:
            task_id = int(arguments[1])
            task_new_name = arguments[2]
            todo_list.update(task_id, task_new_name)
            file.save_data(todo_list.to_dict())
        else:
            print("Para añadir una tarea es necesaria su descripcion")
    elif action == "delete":
        if n_args > 1:
            task_id = int(arguments[1])
            if todo_list.delete(task_id):
                file.save_data(todo_list.to_dict())
                print("Tarea borrada, correctamente, de la lista")

            else:
                print("No existe ninguna tarea con ese identificador")
    elif action[:4] == "mark":
        if n_args > 1:
            task_id = int(arguments[1])
            if task_id < todo_list.size():
                todo_list.mark(task_id, action[5:])
                file.save_data(todo_list.to_dict())
            else:
                print("No existe una tarea con ese identificador")
    elif action == "list":
        filter = arguments[1]
        if n_args == 1:  # opcion de listado completo, sin mas argumentos
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

action = arguments[ACTION_POS]
n_args = len(arguments)

if validate_action(action):
    action_works()
