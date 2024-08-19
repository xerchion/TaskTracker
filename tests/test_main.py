# tests/test_cli.py
import sys
from unittest.mock import patch

import pytest

from Action import Action
from constants import NAME_FILE
from File import File
from TaskTracker import catch_intro, run_user_action
from TodoList import TodoList


# / probar con esto a usarlo en add y luego cuando vaya, las demas....
@pytest.fixture
def setup():
    # Configuración del entorno de pruebas
    file = File(NAME_FILE)
    if not file.exists():
        file.create([])  # Crea el archivo si no existe
    todo_list = TodoList(file.extract_data())

    return todo_list, file


def test_catch_intro_with_arguments():
    # Simula argumentos de línea de comandos
    test_args = ["TaskTracker.py", "add", "task1"]
    with patch.object(sys, "argv", test_args):
        result = catch_intro()
        assert result == ["add", "task1"]


def test_catch_intro_without_arguments():
    # Simula la ejecución sin argumentos de línea de comandos
    test_args = ["TaskTracker.py"]
    with patch.object(sys, "argv", test_args):
        result = catch_intro()
        assert result == []


def test_user_arguments_add_action(setup):
    # Test para la accion ADD
    # Comprueba que añade una tarea con su descriptcion
    # Comprueba que hay un registro más en el almacenamiento

    task_name = "probando ADD"
    action = Action(["add", task_name])
    todo_list, file = setup
    last_size = todo_list.size()

    run_user_action(action, todo_list, file)
    task = todo_list.get_task_by_description(task_name)
    assert task.get_description() == task_name
    assert todo_list.size() == last_size + 1

    # borrando la tarea de prueba
    todo_list, file = setup
    action = Action(["delete", task.get_id()])
    run_user_action(action, todo_list, file)


def test_user_arguments_delete_action(setup):
    # Test para la accion DELETE

    # Comprueba que borra correctamente un registro
    # Comprueba que hay un registro menos en el almacenamiento
    todo_list, file = setup

    # Añadir tarea para posteriormente borrarla
    task_name = "prueba de borrado"
    action = Action(["add", task_name])
    run_user_action(action, todo_list, file)
    task_id = todo_list.get_task_by_description(task_name).get_id()

    # Accion de borrado
    action = Action(["delete", task_id])
    todo_list, file = setup
    last_size = todo_list.size()
    run_user_action(action, todo_list, file)
    todo_list, file = setup

    assert todo_list.id_exists(task_id) is False
    # assert todo_list.get_task(task_name).get_description() == task_name
    assert todo_list.size() == last_size - 1


def test_user_arguments_update_action(setup):
    # Test para la accion UPDATE
    # el Test comprueba:
    #   - El registro existe.
    #   - El registro se actualiza correctamente
    #   - El numero de elementos no varía

    todo_list, file = setup
    last_size = todo_list.size()
    id = todo_list.tasks[0].get_id()
    # Añadir tarea para posteriormente borrarla
    task_new_name = "MODIFICADO"
    action = Action(
        [
            "update",
            id,
            task_new_name,
        ]
    )
    run_user_action(action, todo_list, file)
    task_id = todo_list.get_task_by_description(task_new_name).get_id()

    assert todo_list.id_exists(task_id) is True
    assert todo_list.get_task_by_id(task_id).get_description() == task_new_name
    assert todo_list.size() == last_size


def test_user_arguments_mark_action(setup):
    # Test para la accion MARK
    # el Test comprueba:
    #   - El registro existe.
    #   - El registro se actualiza correctamente
    #   - El numero de elementos no varía

    todo_list, file = setup
    last_size = todo_list.size()
    id = todo_list.tasks[0].get_id()
    # Añadir tarea para posteriormente borrarla
    action = Action(["mark-done", id])
    run_user_action(action, todo_list, file)

    assert todo_list.id_exists(id) is True
    assert todo_list.get_task_by_id(id).get_status() == "done"
    assert todo_list.size() == last_size


def test_user_arguments_list_action(setup, capsys):
    # Test para la accion LIST
    # el Test comprueba:
    #   - La salida es correcta.
    #   -
    #   -

    # añadimos una tarea con un estado especial:  LISTING
    # Test para la accion ADD
    # Comprueba que añade una tarea con su descriptcion
    # Comprueba que hay un registro más en el almacenamiento
    # Añadir tarea para posteriormente borrarla
    task_name = "Listar por status"
    action = Action(["add", task_name])
    todo_list, file = setup
    run_user_action(action, todo_list, file)
    todo_list, file = setup

    task = todo_list.get_task_by_description(task_name)

    action = Action(["mark-done", task.get_id()])
    run_user_action(action, todo_list, file)
    task = todo_list.get_task_by_description(task_name)

    status = "done"
    action = Action(["list", status])
    run_user_action(action, todo_list, file)
    todo_list, file = setup
    task = todo_list.get_task_by_description(task_name)

    # borrando la tarea de prueba
    todo_list, file = setup
    action = Action(["delete", task.get_id()])
    run_user_action(action, todo_list, file)
    todo_list, file = setup

    # Capturamos la salida
    salida = capsys.readouterr()
    exit = " Listar por status                       done"
    assert exit in salida.out
