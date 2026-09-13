import sys
from datetime import datetime

from storage import load_tasks, save_tasks


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def update_task_status(tasks, task_id, new_status):
    task = find_task(tasks, task_id)
    if task:
        task["status"] = new_status
        update_timestamp(task)
        save_tasks(tasks)
        return True
    return False

def parse_task_id(value):
    try:
        return int(value)
    except ValueError:
        return None

def delete_task(tasks, task_id):
    for index,task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            save_tasks(tasks)
            return True
    return False

def update_timestamp(task):
    task["updatedAt"] = datetime.now().isoformat()

def add_task(tasks, description):
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1
    status = "todo"
    current_time = datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": description,
        "status": status,
        "createdAt": current_time,
        "updatedAt": current_time
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_id

def update_task_description(tasks, task_id, new_description):
    task = find_task(tasks, task_id)

    if task:
        task["description"] = new_description
        update_timestamp(task)
        save_tasks(tasks)
        return True

    return False

def get_tasks(tasks, status=None):
    if status is None:
        return tasks
    return [task for task in tasks if task["status"] == status]

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
    valid_commands = ["add", "update", "delete" ,"mark-in-progress", "mark-done", "list"]
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
        "Task marked in progress successfully"
    )
        elif command == "mark-done":
             handle_mark_status(
        tasks,
        args,
        "done",
        "Task marked done successfully"
    )
             
        elif command == "list":
            handle_list(tasks, args, valid_statuses)
    else:
        print("No command provided")

if __name__ == "__main__":
    main()