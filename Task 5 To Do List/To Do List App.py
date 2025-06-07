class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")
        print()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            try:
                num = int(input("Enter task number to complete: ")) - 1
                todo.complete_task(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()