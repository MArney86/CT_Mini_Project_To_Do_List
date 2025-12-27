"""
To-Do List Application

A simple command-line interface (CLI) application for managing a to-do list.
Tasks are stored in a Python list as tuples containing the task name and completion status.

Main Program Flow:
1. Initialize an empty todo_list to store tasks
2. Display welcome message
3. Enter main program loop displaying menu with options:
   - Add a task
   - View tasks
   - Mark a task as complete
   - Delete a task
   - Quit the application
4. Get user's menu selection with input validation
5. Execute selected function based on user choice
6. Loop continues until user selects quit option

Task Format:
    Tasks are stored as tuples: (task_name: str, completion_status: bool)
    
Error Handling:
    All user inputs are validated using try/except/else/finally blocks
    Invalid inputs trigger appropriate error messages without crashing the program
"""

def add_task(todo_list):
    """
    Function to add a task to a todo list.
    
    Prompts the user for a task name and adds it to the list if it doesn't already exist.
    Tasks are stored as tuples with the task name and a boolean completion status (False by default).
    Checks for duplicate tasks (case-insensitive) before adding.
    
    Args:
        todo_list: List of task tuples (task_name, completion_status)
    """
    new_task = input("What is the task you'd like to add to the Todo List? ")
    exists = False
    for task in todo_list:
        if new_task.lower() == task[0].lower():
            print("That task is already in the list")
            exists = True
            break
    if not exists:
        todo_list.append((new_task, False))
        print(f"New task: '{new_task}' added to the To Do List")
        

def view_tasks(todo_list):
    """
    Function to view all the tasks in the To Do List.
    
    Displays all tasks with color-coded completion status:
    - Red text for incomplete tasks
    - Green text for complete tasks
    Each task is numbered for easy reference.
    Alerts the user if the list is empty.
    
    Args:
        todo_list: List of task tuples (task_name, completion_status)
    """
    if len(todo_list) == 0:
        print("There are no tasks in your To Do list currently.")
    else:
        print("The current tasks on your To Do List (Red is incomplete, Green is complete):")
        i = 1 
        for task, completed in todo_list:
            if completed:
                print(f"\033[32m{i}: " + task + ": complete\033[0m")
            else:
                print(f"\033[31m{i}: " + task + ": incomplete\033[0m")
            i += 1

def mark_complete(todo_list):
    """
    Function to mark a task in the To Do List complete.
    
    Displays the current task list and prompts user to select a task by number.
    Updates the selected task's completion status to True.
    Handles invalid input with appropriate error messages:
    - Non-numeric input
    - Out-of-range task numbers
    Exits early if the list is empty.
    
    Args:
        todo_list: List of task tuples (task_name, completion_status)
    """
    if len(todo_list) == 0:
        print("There are no tasks in your To Do list to mark as complete.")
        return
    
    view_tasks(todo_list)
    while True:
        try:
            task_selection = int(input("Please choose the number of the task you wish to mark as complete: "))
            if task_selection < 0 or task_selection > len(todo_list):
                raise ValueError("That selection is not in the list, please try again")
            else:
                todo_list[task_selection - 1] = (todo_list[task_selection - 1][0], True)
                print(f"Task '{todo_list[task_selection - 1][0]}' is now marked as complete")
                break
        except ValueError as ve:
            if "invalid literal" in str(ve):
                print("Please enter the number for the listed task only.")
            else:
                print(ve)
        finally:
            pass

def delete_task(todo_list):
    """
    Function to delete a task from the To Do List.
    
    Displays the current task list and prompts user to select a task by number to delete.
    Removes the selected task from the list permanently.
    Handles invalid input with appropriate error messages:
    - Non-numeric input
    - Out-of-range task numbers
    Exits early if the list is empty.
    
    Args:
        todo_list: List of task tuples (task_name, completion_status)
    """
    if len(todo_list) == 0:
        print("There are no tasks in your To Do list to delete.")
        return
    
    view_tasks(todo_list)
    while True:
        try: 
            task_selection = int(input("Please choose the number of the task you wish to delete from your To Do List: "))
            if task_selection < 0 or task_selection > len(todo_list):
                raise ValueError("That selection is not in the list, please try again")
            else:
                task_temp = todo_list[task_selection - 1][0]
                del todo_list[task_selection - 1]
                print(f"Task '{task_temp}' has been deleted from your To Do List")
                break
        except ValueError as ve:
            if "invalid literal" in str(ve):
                print("Please enter the number for the listed task only.")
            else:
                print(ve)
        finally:
            pass

todo_list = []

print("Welcome to the To-Do List App!\n\n")

while True:
    print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")
    try:
        user_selection = int(input("Please input the number for the feature you'd like to use: "))
        if user_selection < 1 or user_selection > 5:
            raise ValueError("Please choose a number from the menu list.")
    except ValueError as ve:
        if "invalid literal" in str(ve):
            print("That's not a number. Please enter a number from the menu list.")
        else:
            print(ve)
    else:
        if user_selection == 1:
            add_task(todo_list)
        elif user_selection == 2:
            view_tasks(todo_list)
        elif user_selection == 3:
            mark_complete(todo_list)
        elif user_selection == 4:
            delete_task(todo_list)
        elif user_selection == 5:
            break
    finally:
        pass