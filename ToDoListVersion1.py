# The function to load the menu and ask the user to input an option.
def load_menu():
    global list_name
    print("To Do List Menu")
    option_1 = "1. Create a new list"
    option_2 = "2. Load an existing list"
    option_3 = "3. Exit"
    print(option_1)
    print(option_2)
    print(option_3)
    # Ask the user to select an option.
    user_option = input("Please select an option: ")
    # Call the corresponding function based on the user's choice, 
    # and pass the tasks list to the function.
    if user_option == "1":
        list_name = ask_list_name_to_create()
        create_list_file()
    elif user_option == "2":
        list_name = ask_list_name_to_load()
        load_list_file()
    elif user_option == "3":
        print("Exiting...")
    # Prints out an message to tell te user that they 
    # entered an invalid option and reload the menu.
    else:
        print("Invalid option, please select either 1, 2, or3.")
        load_menu()

# Create an empty list to store the user's tasks.
task_list = []

def ask_list_name_to_create():
    list_name_to_create = input("Please enter the name of the list you want to create: ")
    return list_name_to_create

def ask_list_name_to_load():
    list_name_to_load = input("Please enter the name of the list you want to view: ")
    return list_name_to_load

def add_task_option():
    add_task_option = input("Do you want to add a task to this list? (yes/no): ")
    if add_task_option.lower() == "yes":
        add_task(task_list)
    elif add_task_option.lower() == "no":
        print("Skipping add task...")
    else:
        print("Invalid option, returning to menu...")
        load_menu()
    
def delete_task_option():
    delete_task_option = input("Do you want to delete a task from this list? (yes/no): ")
    if delete_task_option.lower() == "yes":
        remove_task(task_list)
    elif delete_task_option.lower() == "no":
        print("Returning to menu...")
        load_menu()
    else:
        print("Invalid option, returning to menu...")
        load_menu()
    
# Ask the user to choose if they want to return to the menu or exit the program.
def return_to_menu_option():
    return_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if return_to_menu.lower() == "yes":
        load_menu()
    elif return_to_menu.lower() == "no":
        print("Exiting...")
    else:
        print("Invalid option, exiting...")

# The function to append tasks to the file.
def append_to_file(task_list):
    with open(list_name, "a") as file:
        for tasks in task_list:
            # Append tasks in the task list to the file and add a new line after each task.
            file.write(tasks + "\n")
            
# The function to read existing tasks from the file and return them as a string, 
# to be displayed whent the user choose to view tasks.
def read_from_file():
    with open(list_name, "r") as file:
        tasks = file.read().capitalize()
        return tasks

def create_list_file():
    global list_name
    try:
        with open(list_name, "r"):
            print(f"List '{list_name}' already exists, please enter a different name: ")
            list_name = ask_list_name_to_create()
            create_list_file()
            return
    except FileNotFoundError:
        with open(list_name, "w"):
            pass
        print(f"List '{list_name}' has been created.")
    add_task_option()
    return_to_menu_option()
    
def load_list_file():
    global task_list
    try:
        with open(list_name, "r") as file:
            task_list = file.read().splitlines()
            if task_list:
                print(f"Your current tasks: {task_list}")
            else:
                print("Your task list is empty.")
            add_task_option()
            delete_task_option()
    except FileNotFoundError:
        print(f"List '{list_name}' does not exist, please enter a valid list name.")
        ask_list_name_to_load()
 
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
    return_to_menu_option()
    
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
            
# The main function to start the program from loading the menu.     
def main():
   load_menu()

main()
