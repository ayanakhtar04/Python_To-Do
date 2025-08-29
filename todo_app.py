"""
A simple command-line To-Do List application in Python.
"""

# Define a constant for the filename to avoid "magic strings".
FILE_NAME = "tasks.txt"

# This list will store all the tasks. It's defined globally so all functions can access it.
tasks = []

def load_tasks():
    """
    Loads tasks from the tasks.txt file when the application starts.
    Uses a try-except block to handle the case where the file doesn't exist yet.
    """
    global tasks
    try:
        # 'with open' ensures the file is automatically closed.
        with open(FILE_NAME, 'r') as f:
            # Read all lines, and use a list comprehension to strip the newline character from each.
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # It's okay if the file doesn't exist on the first run.
        # It will be created when the user exits.
        pass # Do nothing, tasks list will remain empty.

def save_tasks():
    """Saves the current list of tasks to tasks.txt before exiting."""
    with open(FILE_NAME, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def display_menu():
    """Displays the main menu to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    """
    (Step 2)
    Prompts the user for a new task and adds it to the `tasks` list.
    """
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    """
    (Step 3)
    Displays all the tasks. If the list is empty, it prints a message.
    Otherwise, it prints each task with its corresponding number.
    """
    print("\n--- Your Tasks ---")
    # Check if the list is empty
    if not tasks:
        print("You have no tasks.")
    else:
        # Use enumerate to get both the index (starting from 1) and the task
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_task_complete():
    """
    (Step 4)
    Marks a specific task as complete by appending '[DONE]' to it.
    Includes error handling for invalid user input.
    """
    # Show tasks first so the user can choose which one to mark
    view_tasks()
    
    # Don't proceed if there are no tasks to mark
    if not tasks:
        return

    try:
        task_number_str = input("Enter the number of the task to mark as complete: ")
        task_number = int(task_number_str)

        # Convert the 1-based number to a 0-based list index
        task_index = task_number - 1

        # Check if the user-provided number is a valid index
        if 0 <= task_index < len(tasks):
            # Check if the task is not already marked as done
            if not tasks[task_index].endswith(" [DONE]"):
                tasks[task_index] += " [DONE]"
                print(f"Task {task_number} marked as complete!")
            else:
                print("That task is already marked as complete.")
        else:
            # Handle cases where the number is out of the list's range
            print("Invalid task number. Please try again.")
    except ValueError:
        # Handle cases where the input is not a number
        print("Invalid input. Please enter a number.")

def delete_task():
    """
    Deletes a specific task from the list.
    Includes error handling for invalid user input.
    """
    # Show tasks first so the user can choose which one to delete
    view_tasks()

    # Don't proceed if there are no tasks to delete
    if not tasks:
        return

    try:
        task_number_str = input("Enter the number of the task to delete: ")
        task_number = int(task_number_str)

        # Convert the 1-based number to a 0-based list index
        task_index = task_number - 1

        # Check if the user-provided number is a valid index
        if 0 <= task_index < len(tasks):
            # Use pop() to remove the task and get its value for the confirmation message
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task.split(' [DONE]')[0]}' deleted successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """
    (Step 1)
    The main function that runs the application loop.
    """
    # Load any existing tasks from the file when the program starts.
    load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            # Save tasks to the file before exiting.
            save_tasks()
            print("Exiting the To-Do List application. Goodbye!")
            break  # Exit the while loop
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# This ensures the `main` function is called only when the script is executed directly
if __name__ == "__main__":
    main()