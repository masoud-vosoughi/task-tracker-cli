import task_manager
from task_manager import (
    add_task,
    delete_task,
    find_task,
    update_task_status,
)


def test_find_task_existing_id():
    tasks = [
        {"id": 1, "description": "First task"},
        {"id": 2, "description": "Second task"},
    ]

    result = find_task(tasks, 2)

    assert result == {"id": 2, "description": "Second task"}


def test_find_task_missing_id():
    tasks = [
        {"id": 1, "description": "First task"},
    ]

    result = find_task(tasks, 99)

    assert result is None


def test_add_task(monkeypatch):
    monkeypatch.setattr(
        task_manager,
        "save_tasks",
        lambda tasks: None,
    )

    tasks = []

    new_id = add_task(tasks, "Learn testing")

    assert new_id == 1
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Learn testing"
    assert tasks[0]["status"] == "todo"


def test_update_task_status(monkeypatch):
    monkeypatch.setattr(
        task_manager,
        "save_tasks",
        lambda tasks: None,
    )

    tasks = [
        {
            "id": 1,
            "description": "Learn testing",
            "status": "todo",
        }
    ]

    result = update_task_status(tasks, 1, "done")

    assert result is True
    assert tasks[0]["status"] == "done"


def test_delete_task(monkeypatch):
    monkeypatch.setattr(
        task_manager,
        "save_tasks",
        lambda tasks: None,
    )

    tasks = [
        {"id": 1},
        {"id": 2},
    ]

    result = delete_task(tasks, 1)

    assert result is True
    assert tasks == [{"id": 2}]