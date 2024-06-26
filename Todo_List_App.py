#current task list format is a dictionary with the task as the label and the value is a bool representing the completion status

def add_task(todo_list): #function to add a task to a todo list
    new_task = input("What is the task you'd like to add to the Todo List? ") #ask user for the task
    exists = False
    for task in todo_list.keys(): #iterate through the tasks
        if new_task.lower() == task.lower():  #test if the task is already in the list
            print("That task is already in the list") #let user know that the task is already in the list
            exists = True
            break
    if not exists:
        todo_list[new_task] = False #add the new task to the todo list with a value of false to indicate the default of being incomplete
        print(f"New task: '{new_task}' added to the To Do List") #print a message to the user that the task was added to the list
        

def view_tasks(todo_list): #function to view all the tasks in the To Do List
    if not todo_list: #ensure that the To Do list is not empty
        print("There are no tasks in your To Do list currently.") #inform the user that the task list is empty
    else: #there is something in the task list
        Print("The current tasks on your To Do List (Red is incomplete, Green is complete):") #print header to the user explaining the colors of the text
        i = 1 #counter for printing out the list of tasks
        for task in todo_list.keys(): #iterate through the tasks
            if todo_list[task] == True: #check if the flag for completion is true
                print(f"\033[32m{i}: " + task + ": complete\033[0m") #print the task as completed and in greeen then returns the console color to default
            else: #completion flag not set
                print(f"\033[31m{i}: " + task + ": incomplete\033[0m") #print the task as incomplete and in red then returns the console color to default
            i += 1

def mark_complete(todo_list): #funtion to mark a task in the To Do List complete
    view_tasks(todo_list)
    while True:
        try:
            task_selection = int(input("Please choose the number of the task you wish to mark as complete: "))
            if task_selection < 0 or task_selection > len(todo_list):
                raise ValueError("That selection is not in the list, please try again")
            else:
                todo_values = list(todo_list.keys())
                todo_list[todo_values[task_selection - 1]] = True
                print(f"Task '{todo_values[task_selection - 1]}' is now marked as complete") #notify the user of the task being marked complete
                break #end the loop
        except ValueError as ve: #except block for ValueErrors from user input
            if "invalid literal" in str(ve): #check that it's a ValueError from improper input type 
                print("Please enter the number for the listed task only.") #inform the user of the error
            else: #other value errors
                print(ve) #print message passed by the raise call

def delete_task(todo_list): #function to delete a task from the To Do List
    view_tasks(todo_list) #print the task list for the user to choose from
    while True: #loop in case of error inputs
        try: #try block for user input
            task_selection = int(input("Please choose the number of the task you wish to delete from your To Do List: ")) #get user's selection and convert to int
            if task_selection < 0 or task_selection > len(todo_list): #check that user selection is actually on the list
                raise ValueError("That selection is not in the list, please try again") #raise exception if the user selection is not within the bounds of the list
            else: #user selection does not raise errors
                todo_values = list(todo_list.keys()) #get a list of the keys in the list
                del todo_list[todo_values[task_selection - 1]] #delete the selected task from the list
                print(f"Task '{todo_values[task_selection - 1]}' has been deleted from your To Do List") #notify the user of the deletion
                break #end the loop
        except ValueError as ve: #except block for ValueErrors from user input
            if "invalid literal" in str(ve): #check that it's a ValueError from improper input type
                print("Please enter the number for the listed task only.") #inform the user of the error
            else: #other value errors
                print(ve) #print message passed by the raise call

todo_list = {} #initialize an empty todo list
print("Welcome to the To-Do List App!\n\n") #a welcome to the program for users

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
        elif user_selection == 5: #user selects to quit
            break