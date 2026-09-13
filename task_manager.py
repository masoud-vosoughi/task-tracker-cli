from datetime import datetime

from storage import save_tasks


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
    for index, task in enumerate(tasks):
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
        "updatedAt": current_time,
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