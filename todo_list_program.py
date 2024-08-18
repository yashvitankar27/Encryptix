import os

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, (task, status) in enumerate(tasks, start=1):
            print(f"{index}. {task} - {'Done' if status else 'Not Done'}")

def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append((task, False))
    print(f"Task '{task}' added to your to-do list.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to remove: "))
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task[0]}' removed from your to-do list.")
        except (ValueError, IndexError):
            print("Invalid task number.")

def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as done: "))
            task, status = tasks[task_number - 1]
            tasks[task_number - 1] = (task, True)
            print(f"Task '{task}' marked as done.")
        except (ValueError, IndexError):
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
