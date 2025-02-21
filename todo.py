# todo.py - Simple To-Do List CLI App

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📜 No tasks found.")
    else:
        print("\n📝 To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"❌ Task removed: {removed_task}")
    else:
        print("⚠️ Invalid task number.")

def main():
    while True:
        print("\n📌 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        elif choice == "4":
            print("🚀 Exiting To-Do List. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
