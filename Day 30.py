    """
    Day 30 Summary: Task Management System
    Demonstrates: Classes, File I/O, Error Handling, and List Comprehension.
    """
    
    import json
    
    class TaskManager:
        def __init__(self, filename="tasks.json"):
            self.filename = filename
            self.tasks = self.load_tasks()
    
        def load_tasks(self):
            """Reads tasks from a file, handling potential errors."""
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                # Return an empty list if file doesn't exist yet
                return []
    
        def add_task(self, task_name):
            """Adds a task to the list and saves it."""
            new_task = {"name": task_name, "completed": False}
            self.tasks.append(new_task)
            self.save_tasks()
            print(f"Task '{task_name}' added successfully!")
    
        def save_tasks(self):
            """Writes the current task list to a JSON file."""
            with open(self.filename, "w") as file:
                json.dump(self.tasks, file, indent=4)
    
        def show_pending_tasks(self):
            """Uses list comprehension to filter incomplete tasks."""
            pending = [t['name'] for t in self.tasks if not t['completed']]
            
            if not pending:
                print("No pending tasks. Great job!")
            else:
                print(f"Pending Tasks: {', '.join(pending)}")
    
    def main():
        # Instantiate the class
        manager = TaskManager()
    
        print("--- Welcome to your Day 30 Python Summary ---")
        
        while True:
            print("\nOptions: 1. Add Task  2. Show Pending  3. Exit")
            choice = input("Select an option (1-3): ")
    
            if choice == '1':
                name = input("Enter task name: ").strip()
                if name:
                    manager.add_task(name)
            elif choice == '2':
                manager.show_pending_tasks()
            elif choice == '3':
                print("Congratulations on completing 30 Days of Python!")
                break
            else:
                print("Invalid choice, please try again.")
    
    if __name__ == "__main__":
        main()
