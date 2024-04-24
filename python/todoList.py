# todoList.py for Codesoft Intership

# List to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' deleted.")
    else:
        print("Task not found.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task = input("Enter task to delete: ")
            delete_task(task)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
