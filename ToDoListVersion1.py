# The file name to store the tasks in the to do list.
FILE_NAME = "ToDoListVersion1.txt"

# The function toload the menu and ask the user to input an option.
def load_menu():
    print("To Do List Menu")
    option_1 = "1. Add a task"
    option_2 = "2. View tasks"
    option_3 = "3. Remove a task"
    option_4 = "4. Exit"
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    # Ask the user to select an option.
    user_option = input("Please select an option: ")
    # Create an empty list to store the user's tasks.
    tasks_list = []
    # Call the corresponding function based on the user's choice, 
    # and pass the tasks list to the function.
    if user_option == 1:
        add_task(tasks_list)
    elif user_option == 2:
        view_task(tasks_list)
    elif user_option == 3:
       remove_task(tasks_list)
    elif user_option == 4:
        print("Exiting...")
    # Prints out an message to tell te user that they 
    # entered an invalid option and reload the menu.
    else:
        print("Invalid option, please try again.")
        load_menu()
    
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
    else:
        print("Task list is not saved.")
    # Ask the user to choose if they want to return to the menu or exit the program.
    back_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if back_to_menu == "yes":
        load_menu()
    else:
        print("Exiting...")
    
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
    with open(FILE_NAME, "a") as file:
        for task in task_list:
            # Append tasks in the task list to the file and add a new line after each task.
            file.write(task + "\n")

# The function to read existing tasks from the file and return them as a string, 
# to be displayed whent the user choose to view tasks.
def read_from_file():
    with open(FILE_NAME, "r") as file:
        tasks = file.read()
        return tasks
            
# The main function to start the program from loading the menu.     
def main():
   load_menu()

main()
