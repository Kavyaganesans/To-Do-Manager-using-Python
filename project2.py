# To do list 1 : complete / Incomplete
# 1. Create a new item 
# 2. Add a new item to the list
# 3.Mark an item as complete
# 4. Save items to a file

import json

file_name = "To-Do_list.json"

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": []}

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Failed to save tasks: {e}")

def view_tasks(tasks):
    """Display the current to-do list."""
    print()
    task_list = tasks["tasks"]
    if not task_list:
        print("No tasks available.")
    else:
        print("Your To-Do list:")
        for idx, task in enumerate(task_list):
            status = "[Complete]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} {status}")

def create_task(tasks):
    """Add a new task to the list."""
    description = input("Enter task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def mark_task_complete(tasks):
    """Mark a task as complete."""
    view_tasks(tasks)
    
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task complete")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
