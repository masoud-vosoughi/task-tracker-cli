import sys

from storage import load_tasks
from task_manager import (
    add_task,
    delete_task,
    get_tasks,
    parse_task_id,
    update_task_description,
    update_task_status,
)


def print_tasks(tasks):
    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(task)


def handle_add(tasks, args):
    if len(args) == 1:
        description = args[0]
        new_id = add_task(tasks, description)
        print(f"Task added successfully (ID: {new_id})")
    else:
        print("Missing required arguments")


def handle_update(tasks, args):
    if len(args) == 2:
        task_id = parse_task_id(args[0])
        new_description = args[1]

        if task_id is None:
            print("Task ID must be a number")
        else:
            if update_task_description(tasks, task_id, new_description):
                print("Task updated successfully")
            else:
                print("Task not found")
    else:
        print("Missing required arguments")


def handle_delete(tasks, args):
    if len(args) == 1:
        task_id = parse_task_id(args[0])

        if task_id is None:
            print("Task ID must be a number")
        else:
            if delete_task(tasks, task_id):
                print("Task deleted successfully")
            else:
                print("Task not found")
    else:
        print("Missing required arguments")


def handle_mark_status(tasks, args, new_status, success_message):
    if len(args) == 1:
        task_id = parse_task_id(args[0])

        if task_id is None:
            print("Task ID must be a number")
        else:
            if update_task_status(tasks, task_id, new_status):
                print(success_message)
            else:
                print("Task not found")
    else:
        print("Missing required arguments")


def handle_list(tasks, args, valid_statuses):
    if len(args) == 0:
        selected_tasks = get_tasks(tasks)
        print_tasks(selected_tasks)

    elif len(args) == 1:
        status = args[0]

        if status in valid_statuses:
            selected_tasks = get_tasks(tasks, status)
            print_tasks(selected_tasks)
        else:
            print("Invalid status")

    else:
        print("Missing required arguments")


def main():
    tasks = load_tasks()

    valid_commands = [
        "add",
        "update",
        "delete",
        "mark-in-progress",
        "mark-done",
        "list",
    ]
    valid_statuses = ["todo", "in-progress", "done"]

    if len(sys.argv) > 1:
        command = sys.argv[1]
        args = sys.argv[2:]

        if command not in valid_commands:
            print("Invalid command")

        elif command == "add":
            handle_add(tasks, args)

        elif command == "update":
            handle_update(tasks, args)

        elif command == "delete":
            handle_delete(tasks, args)

        elif command == "mark-in-progress":
            handle_mark_status(
                tasks,
                args,
                "in-progress",
                "Task marked in progress successfully",
            )

        elif command == "mark-done":
            handle_mark_status(
                tasks,
                args,
                "done",
                "Task marked done successfully",
            )

        elif command == "list":
            handle_list(tasks, args, valid_statuses)

    else:
        print("No command provided")


if __name__ == "__main__":
    main()