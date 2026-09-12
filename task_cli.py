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
        json.dump(tasks, file, indent=4)

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
            print("Missing required arguments")
    elif command == "update":
        if len(sys.argv) == 4:
            task_found = False
            try:
                task_id = int(sys.argv[2])
                new_description = sys.argv[3]
            except ValueError:
                print("Task ID must be a number")
            else:
                for task in tasks:
                    if task["id"] == task_id:
                        task["description"] = new_description
                        current_time = datetime.now().isoformat()
                        task["updatedAt"] = current_time
                        task_found = True
                        break
                if task_found:
                    save_tasks(tasks)
                    print("Task updated successfully")
                else:  
                    print("Task not found")
                
                
        else:
            print("Missing required arguments")

    
    elif command == "delete":
        if len(sys.argv) == 3:
            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Task ID must be a number")
            else:
                task_found = False

                for index, task in enumerate(tasks):
                    if task["id"] == task_id:
                        del tasks[index]
                        task_found = True
                        break

                if task_found:
                    save_tasks(tasks)
                    print("Task deleted successfully")
                else:
                    print("Task not found")

        else:
            print("Missing required arguments")
    elif command == "mark-in-progress":
        if len(sys.argv) == 3:
            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Task ID must be a number")
            else:
                task_found = False
                for task in tasks:
                    if task["id"] == task_id:
                        task["status"] = "in-progress"
                        current_time = datetime.now().isoformat()
                        task["updatedAt"] = current_time
                        task_found = True
                        break
                if task_found:
                    save_tasks(tasks)
                    print("Task marked in progress successfully")
                else:
                    print("Task not found")
                    
        else:
            print("Missing required arguments")
    elif command == "mark-done":
        if len(sys.argv) == 3:
            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Task ID must be a number")
            else:
                task_found = False
                for task in tasks:
                    if task["id"] == task_id:
                        task["status"] = "done"
                        current_time = datetime.now().isoformat()
                        task["updatedAt"] = current_time
                        task_found = True
                        break
                if task_found:
                    save_tasks(tasks)
                    print("Task marked done successfully")
                else:
                    print("Task not found")
        else:
            print("Missing required arguments")
    elif command == "list":
        if len(sys.argv) == 2:
            if not tasks:
                print("No tasks found")
            else:
                for task in tasks:
                    print(task)
        elif len(sys.argv) == 3:
            status = sys.argv[2]
            if status in valid_statuses:
                task_found = False
                for task in tasks:
                    if task["status"] == status:
                        task_found = True
                        print(task)
                if not task_found:
                    print("No tasks found")
                    
            else:
                print("Invalid status")
        else:
            print("Missing required arguments")
        
    
else:
    print("No command provided")

