# tests/test_cli.py
import sys
from unittest.mock import patch

import pytest

from Action import Action
from constants import NAME_FILE
from File import File
from TaskTracker import catch_intro, run_user_action
from TodoList import TodoList


# / probar con esto a usarlo en add y luego cuando valla, las demas....
def setup_todo_list():
    # Configuración del entorno de pruebas
    file = File(NAME_FILE)
    if file.exists():
        file.create([])  # Crea el archivo si no existe
    todo_list = TodoList(file.extract_data())
    return file, todo_list


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


def test_user_arguments_add_action():
    task_name = "probando lo que va"
    action = Action(["add", task_name])
    file = File(NAME_FILE)
    todo_list = TodoList(file.extract_data())
    run_user_action(action, todo_list)
    # // ahora la comprobacion de si lo ha añadido bien
    assert todo_list.get_task(task_name).get_description() == task_name
