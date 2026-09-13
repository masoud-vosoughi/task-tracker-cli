import json
from pathlib import Path


FILE_PATH = Path("tasks.json")


def load_tasks():
    tasks = []

    if not FILE_PATH.exists():
        FILE_PATH.touch()
        FILE_PATH.write_text("[]")
        return tasks

    else:
        with open(FILE_PATH, "r") as file:
            tasks = json.load(file)

    return tasks


def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)
