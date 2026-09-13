import json
from pathlib import Path


FILE_PATH = Path("tasks.json")


def load_tasks():
    tasks = []

    if not FILE_PATH.exists():
        FILE_PATH.touch()
        FILE_PATH.write_text("[]")
        return tasks

    try:
        with open(FILE_PATH, "r") as file:
            tasks = json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError("tasks.json contains invalid JSON") from error

    return tasks


def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)