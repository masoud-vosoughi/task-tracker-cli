import storage
from task_manager import (
    add_task,
    delete_task,
    update_task_description,
    update_task_status,
)


def test_add_task_is_saved_and_loaded(monkeypatch, tmp_path):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    tasks = []

    add_task(tasks, "Learn testing")
    loaded_tasks = storage.load_tasks()

    assert len(loaded_tasks) == 1
    assert loaded_tasks[0]["description"] == "Learn testing"
    assert loaded_tasks[0]["status"] == "todo"


def test_description_update_is_persisted(monkeypatch, tmp_path):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    tasks = []

    task_id = add_task(tasks, "Old description")
    update_task_description(tasks, task_id, "New description")

    loaded_tasks = storage.load_tasks()

    assert loaded_tasks[0]["description"] == "New description"


def test_status_update_is_persisted(monkeypatch, tmp_path):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    tasks = []

    task_id = add_task(tasks, "Learn pytest")
    update_task_status(tasks, task_id, "done")

    loaded_tasks = storage.load_tasks()

    assert loaded_tasks[0]["status"] == "done"


def test_delete_task_is_persisted(monkeypatch, tmp_path):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    tasks = []

    task_id = add_task(tasks, "Temporary task")
    delete_task(tasks, task_id)

    loaded_tasks = storage.load_tasks()

    assert loaded_tasks == []


def test_full_task_lifecycle(monkeypatch, tmp_path):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    tasks = []

    task_id = add_task(tasks, "Original task")

    update_task_description(
        tasks,
        task_id,
        "Updated task",
    )

    update_task_status(
        tasks,
        task_id,
        "done",
    )

    loaded_tasks = storage.load_tasks()

    assert loaded_tasks[0]["description"] == "Updated task"
    assert loaded_tasks[0]["status"] == "done"

    delete_task(tasks, task_id)

    loaded_tasks = storage.load_tasks()

    assert loaded_tasks == []