# tests/test_cli.py
import sys
from unittest.mock import patch

import pytest

from Action import Action
from constants import NAME_FILE
from File import File
from TaskTracker import catch_intro, run_user_action
from TodoList import TodoList


@pytest.fixture
def setup():
    file = File(NAME_FILE)
    if not file.exists():
        file.create([])
    todo_list = TodoList(file.extract_data())
    return todo_list, file


def test_catch_intro_with_arguments():
    test_args = ["TaskTracker.py", "add", "task1"]
    with patch.object(sys, "argv", test_args):
        result = catch_intro()
        assert result == ["add", "task1"]


def test_catch_intro_without_arguments():
    test_args = ["TaskTracker.py"]
    with patch.object(sys, "argv", test_args):
        result = catch_intro()
        assert result == []


def test_user_arguments_add_action(setup):

    # Verifies that a task is added with the correct description.
    # Verifies that there is one more record in the storage.

    task_name = "testing ADD"
    action = Action(["add", task_name])
    todo_list, file = setup
    last_size = todo_list.size()

    run_user_action(action, todo_list, file)
    task = todo_list.get_task_by_description(task_name)
    assert task.get_description() == task_name
    assert todo_list.size() == last_size + 1

    # Clean up: Delete the test task
    action = Action(["delete", task.get_id()])
    run_user_action(action, todo_list, file)


def test_user_arguments_delete_action(setup):
    # Verifies that a task is deleted correctly.
    # Verifies that there is one less record in the storage after deletion.
    todo_list, file = setup

    # Add a task to later delete it
    task_name = "delete test task"
    action = Action(["add", task_name])
    run_user_action(action, todo_list, file)
    task_id = todo_list.get_task_by_description(task_name).get_id()

    # Perform the DELETE action
    action = Action(["delete", task_id])
    last_size = todo_list.size()
    run_user_action(action, todo_list, file)

    # Refresh the todo list to reflect the deletion
    todo_list, file = setup

    # Verify the task no longer exists
    assert not todo_list.id_exists(task_id)
    assert todo_list.size() == last_size - 1


def test_user_arguments_update_action(setup):
    # The test verifies:
    # - The record exists.
    # - The record is updated correctly.
    # - The number of items does not change.

    todo_list, file = setup
    last_size = todo_list.size()
    task_id = todo_list.tasks[0].get_id()

    # Update the task
    updated_task_name = "UPDATED"
    action = Action(["update", task_id, updated_task_name])
    run_user_action(action, todo_list, file)

    # Verify the task was updated correctly
    assert todo_list.id_exists(task_id) is True
    assert todo_list.get_task_by_id(task_id).get_description() == updated_task_name
    assert todo_list.size() == last_size


def test_user_arguments_mark_action(setup):
    # The test verifies:
    # - The record exists.
    # - The record is updated correctly.
    # - The number of items does not change.

    todo_list, file = setup
    last_size = todo_list.size()
    task_id = todo_list.tasks[0].get_id()

    # Mark the task as done
    action = Action(["mark-done", task_id])
    run_user_action(action, todo_list, file)

    # Verify the task status is updated to "done"
    assert todo_list.id_exists(task_id) is True
    assert todo_list.get_task_by_id(task_id).get_status() == "done"
    assert todo_list.size() == last_size


def test_user_arguments_list_action(setup, capsys):

    todo_list, file = setup

    # Add a task with a special status: LISTING
    task_name = "Listar por status"
    action = Action(["add", task_name])
    run_user_action(action, todo_list, file)

    # Mark the task as done
    task = todo_list.get_task_by_description(task_name)
    action = Action(["mark-done", task.get_id()])
    run_user_action(action, todo_list, file)

    # List tasks with the 'done' status
    status = "done"
    action = Action(["list", status])
    run_user_action(action, todo_list, file)

    # Capture the output
    captured_output = capsys.readouterr()
    expected_output = f" {task_name}                       done"
    assert expected_output in captured_output.out

    # Clean up: Delete the test task
    action = Action(["delete", task.get_id()])
    run_user_action(action, todo_list, file)
