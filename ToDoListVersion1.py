# The function toload the menu and ask the user to input an option.
def load_menu():
    print("To Do List Menu")
    option_1 = "1. Create a new list"
    option_2 = "2. Load an existing list"
    option_3 = "3. Add a task"
    option_4 = "4. View tasks"
    option_5 = "5. Remove a task"
    option_6 = "6. Exit"
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)
    print(option_6)
    # Ask the user to select an option.
    user_option = input("Please select an option: ")
    # Create an empty list to store the user's tasks.
    tasks_list = []
    # Call the corresponding function based on the user's choice, 
    # and pass the tasks list to the function.
    if user_option == "1":
        ask_list_name()
        create_list_file()
    elif user_option == "2":
        ask_list_name()
        load_list_file()
    elif user_option == "3":
        add_task(tasks_list)
    elif user_option == "4":
        view_task(tasks_list)
    elif user_option == "5":
       remove_task(tasks_list)
    elif user_option == "6":
        print("Exiting...")
    # Prints out an message to tell te user that they 
    # entered an invalid option and reload the menu.
    else:
        print("Invalid option, please try again.")
        load_menu()
        
def ask_list_name():
    list_name = input("Please enter the name of the list you want to create: ")
    return list_name

LIST_NAME = ask_list_name

def create_list_file():
    open(LIST_NAME, "w").close()
    print(f"List '{LIST_NAME}' has been created.")
    return_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if return_to_menu.lower() == "yes":
        load_menu()
    elif return_to_menu.lower() == "no":
        print("Exiting...")
    else:
        print("Invalid option, exiting...")
    
def load_list_file():
    with open(LIST_NAME, "r") as file:
        tasks = file.read()
        print(f"Your current tasks: {tasks}")
    add_task_option = input(f"Do you want to add a task to the list {LIST_NAME}? (yes/no): ")
    if add_task_option.lower() == "yes":
        add_task(tasks)
    elif add_task_option.lower() == "no":
        print("Returning to menu...")
    else:
        print("Invalid option, returning to menu...")
    
# The function to add tasks to the tasks list.
def add_task(task_list):
    # Ask the user to to enter a task.
    new_task = input("Please enter a task: ")
    # Add the new task to the task list.
    task_list.append(new_task)
    # Print out a message to tell the user that the task is successfully added.
    print(f"Task '{new_task}' is now added to the list.")
    # Print out the current task list.
    print(f"Your current tasks: {task_list}")
    # Ask the user if they want to save the task list to a file.
    save_option = input("Do you want to save the task list? (yes/no): ")
    # If the user choose to save, call the function to append the task list to the file, 
    # otherwise tell the user the task is not saved.
    if save_option.lower() == "yes":
        print("Task list saved.")
        append_to_file(task_list)
    elif save_option.lower() == "no":
        print("Task list is not saved.")
    else:
        print("You have entered an invalid option, task list is not saved.")
    # Ask the user to choose if they want to return to the menu or exit the program.
    back_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if back_to_menu.lower() == "yes":
        load_menu()
    elif back_to_menu.lower() == "no":
        print("Exiting...")
    else:
        print("This option is invalid, exiting...")
    
# The function to view the current tasks in the tasks list.
def view_task(task_list):
    print(f"Your current tasks: {read_from_file()}")
    # Ask the user to choose if they want to return to the menu or exit the program.
    back_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if back_to_menu == "yes":
        load_menu()
    else:
        print("Exiting...")
    
# The function to remove tasks from the task list.    
def remove_task(task_list):
    # Ask the user for the task they want to remove.
    task_to_remove = input("Please enter the task you want to remove: ")
    # Check if the task is in the task list and remove it if it is,
    # otherwise print out a message to tell the user the task is not found.
    if task_to_remove in task_list:
        task_list.remove(task_to_remove)
        print(f"Task '{task_to_remove}' has been removed.")
    else:
        print(f"Task '{task_to_remove}' not found in the list.")
    print(f"Your current tasks: {task_list}")
    # Ask the user to choose if they want to return to the menu or exit the program.
    back_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if back_to_menu == "yes":
        load_menu()
    else:
        print("Exiting...") 

# The function to append tasks to the file.
def append_to_file(task_list):
    with open(LIST_NAME, "a") as file:
        for task in task_list:
            # Append tasks in the task list to the file and add a new line after each task.
            file.write(task + "\n")

# The function to read existing tasks from the file and return them as a string, 
# to be displayed whent the user choose to view tasks.
def read_from_file():
    with open(LIST_NAME, "r") as file:
        tasks = file.read()
        return tasks
            
# The main function to start the program from loading the menu.     
def main():
   load_menu()

main()
