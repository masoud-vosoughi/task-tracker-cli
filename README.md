# Task Tracker CLI

A simple command-line task tracker built with Python.

The application allows users to create, update, delete, list, and change the status of tasks directly from the terminal. Task data is persisted locally in a JSON file.

## Features

- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in progress
- Mark tasks as done
- List all tasks
- Filter tasks by status
- Persist tasks in a JSON file
- Handle invalid task IDs
- Handle malformed JSON data
- Unit and integration tests with `pytest`

## Project Structure

```text
task-tracker-cli/
├── task_cli.py
├── task_manager.py
├── storage.py
├── tasks.json
└── tests/
    ├── test_task_manager.py
    └── test_integration.py
```

### `task_cli.py`

Handles command-line input, validates commands and arguments, and delegates operations to the task manager.

### `task_manager.py`

Contains the core business logic for creating, updating, deleting, filtering, and changing task status.

### `storage.py`

Handles loading task data from and saving task data to `tasks.json`.

### `tests/`

Contains unit and integration tests for the application.

## Requirements

- Python 3.11 or newer
- `pytest` for running the test suite

> Developed and tested with Python 3.14.3.

## Usage

Run commands from the project directory.

### Add a task

```bash
python task_cli.py add "Learn Python"
```

Example output:

```text
Task added successfully (ID: 1)
```

### Update a task

```bash
python task_cli.py update 1 "Learn FastAPI"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as in progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark a task as done

```bash
python task_cli.py mark-done 1
```

### List all tasks

```bash
python task_cli.py list
```

### List tasks by status

```bash
python task_cli.py list todo
```

```bash
python task_cli.py list in-progress
```

```bash
python task_cli.py list done
```

You can also list all unfinished tasks with:

```bash
python task_cli.py list not-done
```

`not-done` is a filtering option and is not stored as an actual task status.

## Task Statuses

Tasks can have one of the following statuses:

- `todo`
- `in-progress`
- `done`

New tasks are created with the `todo` status by default.

## Data Storage

Tasks are stored locally in:

```text
tasks.json
```

If the file does not exist, the application automatically creates an empty JSON task list.

Each task contains data in the following format:

```json
{
  "id": 1,
  "description": "Learn Python",
  "status": "todo",
  "createdAt": "2026-09-30T10:00:00+00:00",
  "updatedAt": "2026-09-30T10:00:00+00:00"
}
```

The local `tasks.json` file is ignored by Git so personal task data is not committed to the repository.

## Running Tests

Run the full test suite with:

```bash
python -m pytest -q
```

The project includes:

- Unit tests for task-management logic
- Integration tests for JSON persistence

## Concepts Practiced

This project was built to practice:

- Python functions and modules
- Command-line arguments with `sys.argv`
- Lists and dictionaries
- File handling
- JSON persistence
- Exception handling
- Input validation
- Datetime handling
- List comprehensions
- Generator expressions
- Separation of concerns
- Unit testing
- Integration testing
- Git and GitHub workflow