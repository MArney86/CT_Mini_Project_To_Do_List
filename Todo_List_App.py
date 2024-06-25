def add_task(todo_list):
    pass

def view_tasks(todo_list):
    pass

def mark_complete(todo_list):
    pass

def delete_task(todo_list)
    pass

todo_list = []
print("Welcome to the To-Do List App!")

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
        elif user_selection = 5:
            break
        