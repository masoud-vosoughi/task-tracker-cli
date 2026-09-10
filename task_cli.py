import sys
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

tasks = load_tasks()
print(tasks)

valid_commands = ["add", "update", "delete" ,"mark-in-progress", "mark-done", "list"]
valid_statuses = ["todo", "in-progress", "done"]

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command not in valid_commands:
        print("Invalid command")
    elif command == "add":
        if len(sys.argv) == 3:
            pass
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
            print("not enough inputی")
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

