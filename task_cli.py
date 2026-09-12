import sys
import json
from pathlib import Path
from datetime import datetime

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
        json.dump(tasks, file)

tasks = load_tasks()


valid_commands = ["add", "update", "delete" ,"mark-in-progress", "mark-done", "list"]
valid_statuses = ["todo", "in-progress", "done"]

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command not in valid_commands:
        print("Invalid command")
    elif command == "add":
        if len(sys.argv) == 3:
            description = sys.argv[2]
            if len(tasks) == 0:
                new_id = 1
            else:
                new_id = max(task["id"] for task in tasks)+1
            status = "todo"
            current_time = datetime.now().isoformat()
            new_task = {"id" : new_id, "description" : description, "status" : status, "createdAt" : current_time, "updatedAt" : current_time }
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Task added successfully (ID: {new_id})")
        else:
            print("not enough input")
    elif command == "update":
        if len(sys.argv) == 4:
            pass
        else:
            print("not enough input")
    
    elif command == "delete":
        if len(sys.argv) == 3:
            pass
        else:
            print("not enough input")
    elif command == "mark-in-progress":
        if len(sys.argv) == 3:
            pass
        else:
            print("not enough input")
    elif command == "mark-done":
        if len(sys.argv) == 3:
            pass
        else:
            print("not enough input")
    elif command == "list":
        if len(sys.argv) == 2:
            print("list")
        elif len(sys.argv) == 3:
            status = sys.argv[2]
            if status in valid_statuses:
                print(status)
            else:
                print("status is not valid")
        else:
            print("not valid input")
        
    
else:
    print("no command")

