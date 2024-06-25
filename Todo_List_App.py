def add_task(todo_list): #function to add a task to a todo list
    new_task = input("What is the task you'd like to add to the Todo List? ") #ask user for the task
    if new_task in todo_list.items():  #test if the task is already in the list
        print("That task is already in the list") #let user know that the task is already in the list
    else:
        todo_list[new_task] = False #add the new task to the todo list with a value of false to indicate the default of being incomplete
        print(f"New task: '{new_task}' added to the To Do List") #print a message to the user that the task was added to the list

def view_tasks(todo_list): #function to view all the tasks in the To Do List
    pass

def mark_complete(todo_list): #funtion to mark a task in the To Do List complete
    pass

def delete_task(todo_list) #function to delete a task from the To Do List
    pass

todo_list = {} #initialize an empty todo list
print("Welcome to the To-Do List App!") #a welcome to the program for users

while True: #main program loop
    print("Menu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit") #print the main feature menu to the user
    try: #try/except/else block for the menu interaction
        user_selection = int(input("Please input the number for the feature you'd like to use: ")) #get the user's selection from the menu
        if user_selection < 1 or user_selection > 5: #check that the user's input is a valid entry if not errored earlier
            raise ValueError("Please choose a number from the menu list.") #raise and exception if the input is not on the list
    except ValueError as ve: #except block for when a ValueError is encountered because of the user's input
        if "invalid literal" in str(ve): #check if the user is because of improper input type from user
            print("That's not a number. Please enter a number from the menu list.") #Warn the user about the improper input
        else: #other ValueError encountered
            print(ve) #print the message from the raised error
    else: #else loop to run if no ValueError encountered
        if user_selection == 1: #user selects to add a task
            add_task(todo_list)
        elif user_selection == 2: #user selects to view tasks
            view_tasks(todo_list)
        elif user_selection == 3: #user selects to mark a task complete
            mark_complete(todo_list)
        elif user_selection == 4: #user select to delet a task
            delete_task(todo_list)
        elif user_selection = 5: #user selects to quit
            break