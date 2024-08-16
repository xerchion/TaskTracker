import pytest

from Task import Task
from TodoList import TodoList

DATA = [
    {
        "id": 0,
        "description": "bibenenida",
        "status": "todo",
        "created_at": 1723482790.2585022,
        "updated_at": 1723484274.2685523,
    }
]
task = Task(
    int(DATA[0]["id"]),
    DATA[0]["description"],
    DATA[0]["status"],
    DATA[0]["created_at"],
    DATA[0]["updated_at"],
)


@pytest.fixture
def dtl():
    return TodoList(DATA)


def test_get_new_id(dtl):
    assert dtl.get_new_id() == 1
    dtl.add_task(DATA)
    assert dtl.get_new_id() == 2


def test_update(dtl):
    text = "test"
    dtl.update(0, text)
    assert dtl.tasks[0].get_description() == text


def test_delete(dtl):
    dtl.add_task(DATA)
    dtl.delete(0)
    assert dtl.get_new_id() - 1 == dtl.tasks[-1].get_id()


def test_mark(dtl):
    new_status = "done"
    old_status = dtl.tasks[0].get_status()
    dtl.mark(0, new_status)
    assert old_status != new_status


def test_filter_by(dtl):

    tasks = dtl.filter_by("all")
    assert len(tasks) == len(DATA)
    # tasks no existentes
    tasks = dtl.filter_by("in_progress")
    assert tasks == []

    # tasks con filtro especifico: estado: todo
    tasks = dtl.filter_by("todo")
    assert tasks[0].get_status() == "todo"


def test_to_dict(dtl):
    elements_dict = dtl.to_dict()
    assert len(elements_dict) == dtl.size()
    assert elements_dict[0]["description"] == dtl.tasks[0].get_description()
