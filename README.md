# Simple Command-Line To-Do List in Python

This project is a simple, yet functional, command-line To-Do list application written in Python. It's designed for beginners to understand fundamental programming concepts through a practical example.

The application allows a user to:
- Add new tasks.
- View all current tasks.
- Mark a task as complete.
- Exit the application.

## How to Run

To run the application, open your terminal or command prompt, navigate to the directory containing the file, and run:

```bash
python todo_app.py
```

## Learning Python from this Code

This code demonstrates several core concepts of the Python language. Let's break them down.

### 1. Functions (`def`)

Functions are reusable blocks of code that perform a specific action. They help organize code and make it more readable. We define a function using the `def` keyword.

**Syntax:**
```python
def function_name():
    # code to be executed
```

**Example from the code (`todo_app.py`):**
```python
def display_menu():
    """Displays the main menu to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    # ... and so on
```
Here, `display_menu` is a function that, when called, prints the menu options to the console.

### 2. The Main Loop (`while`)

A `while` loop repeatedly executes a block of code as long as a certain condition is `True`. In our app, we use `while True:` to create an infinite loop that keeps the program running until the user explicitly chooses to exit.

**Syntax:**
```python
while condition:
    # code to repeat
```

**Example from the code (`todo_app.py`):**
```python
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        # ... logic to handle choice ...
        if choice == '4':
            break # This keyword exits the loop
```

### 3. User Input (`input()`) and Variables

To make the program interactive, we need to get input from the user. The `input()` function pauses the program, displays a message (a "prompt"), and waits for the user to type something and press Enter. The typed text is then stored in a variable.

**Example from the code (`todo_app.py`):**
```python
task = input("Enter the new task: ")
```
This line shows the message "Enter the new task: " and stores whatever the user types into the `task` variable.

### 4. Lists

A list is a data structure in Python that can hold an ordered collection of items. We use a list to store our tasks.

**Syntax:**
`my_list = []` (creates an empty list)

**Example from the code (`todo_app.py`):**
```python
# This list will store all the tasks.
tasks = []

# To add an item, we use the .append() method
tasks.append(task)
```

### 5. Conditional Logic (`if/elif/else`)

Conditional statements allow the program to make decisions and execute different code blocks based on whether a condition is true or false.

**Example from the code (`todo_app.py`):**
```python
if choice == '1':
    add_task()
elif choice == '2':
    view_tasks()
elif choice == '4':
    break
else:
    print("Invalid choice.")
```
This block checks the value of the `choice` variable and calls the appropriate function or prints an error message.

### 6. Looping Through a List (`for` and `enumerate`)

To display all the tasks, we need to go through our `tasks` list one item at a time. A `for` loop is perfect for this. We use the `enumerate()` function to get both the position (index) and the value of each item, which is useful for creating a numbered list.

**Example from the code (`todo_app.py`):**
```python
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
```
`start=1` tells `enumerate` to start counting from 1 instead of the default 0. The `f"{index}. {task}"` is an **f-string**, a modern and clean way to embed variables directly inside a string.

### 7. Error Handling (`try/except`)

Sometimes, user input can cause errors. For example, if we ask for a number but the user types text, the `int()` conversion will fail and crash the program. The `try...except` block lets us "try" a piece of code that might fail and "catch" the error if it does, allowing the program to continue running gracefully.

**Example from the code (`todo_app.py`):**
```python
try:
    task_number = int(task_number_str)
    # ... more code that depends on task_number ...
except ValueError:
    # This block runs ONLY if the int() conversion fails
    print("Invalid input. Please enter a number.")
```
