import pytest

from Task import Task
from TodoList import TodoList

DATA = [
    {
        "id": "0",
        "description": "testing todolist",
        "status": "todo",
        "created_at": 1723482790.2585022,
        "updated_at": 1723484274.2685523,
    }
]
task = Task(
    DATA[0]["id"],
    DATA[0]["description"],
    DATA[0]["status"],
    DATA[0]["created_at"],
    DATA[0]["updated_at"],
)


@pytest.fixture
def todo_list():
    return TodoList(DATA)


def test_get_new_id(todo_list):
    assert todo_list.get_new_id() == 1
    todo_list.add_task(DATA)
    assert todo_list.get_new_id() == 2


def test_update(todo_list):
    text = "new description update"
    todo_list.update_task(0, text)
    assert todo_list.tasks[0].get_description() == text


def test_delete(todo_list):
    todo_list.add_task(DATA)
    todo_list.delete_task(0)
    assert todo_list.get_new_id() - 1 == todo_list.tasks[-1].get_id()


def test_mark(todo_list):
    new_status = "done"
    old_status = todo_list.tasks[0].get_status()
    todo_list.mark_task(0, new_status)
    assert old_status != new_status


def test_filter_by(todo_list):
    tasks = todo_list.filter_by("all")
    assert len(tasks) == len(DATA)

    # Testing with a filter that matches no task
    tasks = todo_list.filter_by("in_progress")
    assert tasks == []

    tasks = todo_list.filter_by("todo")
    assert tasks[0].get_status() == "todo"


def test_to_dict(todo_list):
    elements_dict = todo_list.to_dict()
    assert len(elements_dict) == todo_list.size()
    assert elements_dict[0]["description"] == todo_list.tasks[0].get_description()
