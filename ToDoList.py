import easygui
import os

# The function to load the menu and ask the user to input an option.
def load_menu():
    global list_name
    menu_option = ["1. Create a new list", 
                   "2. Load an existing list", 
                   "3. Delete an existing list", "4. Exit"]
    title = "To Do List Menu"
    user_option = easygui.choicebox(title, "Please select an option: ", menu_option)
    # Call the corresponding function based on the user's choice, 
    # and pass the tasks list to the function.
    if user_option == "1. Create a new list":
        list_name = ask_list_name_to_create()
        create_list_file()
    elif user_option == "2. Load an existing list":
        list_name = ask_list_name_to_load()
        load_list_file()
    elif user_option == "3. Delete an existing list":
        delete_list_file()
    elif user_option == "4. Exit":
        easygui.msgbox("Exiting...")
    # Prints out an message to tell te user that they 
    # entered an invalid option and reload the menu.
    else:
        easygui.msgbox("Invalid option, please select either 1, 2, or3.")
        load_menu()


# Create an empty list to store the user's tasks.
task_list = []


# Ask the user to enter the name of the list they want to create or load, and return the name.
def ask_list_name_to_create():
    list_name_to_create = easygui.enterbox("Please enter the name of the list you want to create: ")
    return list_name_to_create + ".txt"
def ask_list_name_to_load():
    existing_lists = [file for file in os.listdir() if file.endswith(".txt")]
    if len(existing_lists) == 0:
        easygui.msgbox("Currently there are no existing lists, please create a new list first.")
        create_list_file()
        return None
    elif len(existing_lists) == 1:
        easygui.msgbox(f"Only one list found: {existing_lists[0]}")
        return existing_lists[0]
    list_name_to_load = easygui.choicebox("Please choose the list you want to view", "Load List", existing_lists)
    return list_name_to_load


# The function to ask the user if they want to add a task to the list, 
# and call the add task function if they choose yes.
def add_task_option():
    choice = ["Yes", "No"]
    add_task_option = easygui.choicebox("Do you want to add a task to this list?", "Add Task", choice)
    if add_task_option == "Yes":
        choice = ["Yes", "No"]
        add_task(task_list)
        second_task_option = easygui.choicebox("Do you want to add another task to this list?", "Add Task", choice)
        if second_task_option == "Yes":
            add_task(task_list)
        elif second_task_option == "No":
            easygui.msgbox("Finished adding tasks.")
            easygui.msgbox(f"Your current tasks: {task_list}")
            return_to_menu_option()
        else:
            easygui.msgbox("Invalid option, returning to menu...")
            load_menu()
        save_option = easygui.choicebox("Do you want to save the task list?", choice)
        if save_option == "Yes":
            easygui.msgbox("Task list saved.")
            append_to_file(task_list)
        elif save_option == "No":
            easygui.msgbox("Task list is not saved.")
        else:
            easygui.msgbox("You have entered an invalid option, task list is not saved.")
            return_to_menu_option()
    elif add_task_option == "No":
        easygui.msgbox("Skipping add task...")
    else:
        easygui.msgbox("Invalid option, returning to menu...")
        load_menu()
    
    
# The function to ask the user if they want to delete a task from the list,
# and call the remove task function if they choose yes.
def delete_task_option():
    choice = ["Yes", "No"]
    delete_task_option = easygui.choicebox("Do you want to delete a task from this list?", choice)
    if delete_task_option == "Yes":
        remove_task(task_list)
    elif delete_task_option == "No":
        easygui.msgbox("Returning to menu...")
        load_menu()
    else:
        easygui.msgbox("Invalid option, returning to menu...")
        load_menu()
   
    
# Ask the user to choose if they want to return to the menu or exit the program.
def return_to_menu_option():
    choice = ["Yes", "No"]
    return_to_menu = easygui.choicebox("Do you want to return to the menu?", "Return to Menu", choice)
    if return_to_menu == "Yes":
        load_menu()
    elif return_to_menu == "No":
        easygui.msgbox("Exiting...")
    else:
        easygui.msgbox("Invalid option, exiting...")


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


# The function to create a new list file.
def create_list_file():
    global list_name
    try:
        with open(list_name, "r"):
            easygui.enterbox(f"List '{list_name}' already exists, please enter a different name: ")
            list_name = ask_list_name_to_create()
            create_list_file()
            return
    # If the file does not exist, create a new file with the given name.
    except FileNotFoundError:
        with open(list_name, "w"):
            pass
        easygui.msgbox(f"List '{list_name}' has been created.")
    add_task_option()
    return_to_menu_option()
    
    
# The function to load an existing list file and display the current tasks,
# and ask the user whether they want to add or delete tasks.
def load_list_file():
    try:
        with open(list_name, "r") as file:
            task_list = file.read().splitlines()
            if task_list:
                easygui.msgbox(f"Your current tasks are: {task_list}")
            else:
                easygui.msgbox("Your task list is empty.")
            add_task_option()
            delete_task_option()
    except FileNotFoundError:
        easygui.msgbox(f"List '{list_name}' does not exist, please enter a valid list name.")
        ask_list_name_to_load()
   
 
# The function to delete an existing list file.
def delete_list_file():
    global list_name
    task_to_delete = easygui.enterbox("Please enter the name of the list you want to delete: ")
    if task_to_delete == list_name:
        try:
            os.remove(list_name)
            easygui.msgbox(f"List '{list_name}' has been deleted.")
        except FileNotFoundError:
            easygui.msgbox(f"List '{list_name}' does not exist, please enter a valid list name.")
            delete_list_file()

 
# The function to add tasks to the tasks list.
def add_task(task_list):
    # Ask the user to to enter a task.
    new_task = easygui.enterbox("Please enter a task: ")
    # Add the new task to the task list.
    task_list.append(new_task)
    # Print out a message to tell the user that the task is successfully added.
    easygui.msgbox(f"Task '{new_task}' is now added to the list.")
    # Print out the current task list.
    easygui.msgbox(f"Your current tasks: {task_list}")
    # Ask the user if they want to save the task list to a file.
    choice = ["Yes", "No"]

    
    
# The function to remove tasks from the task list.    
def remove_task(task_list):
    # Ask the user for the task they want to remove.
    task_to_remove = easygui.enterbox("Please enter the task you want to remove: ")
    # Check if the task is in the task list and remove it if it is,
    # otherwise print out a message to tell the user the task is not found.
    if task_to_remove in task_list:
        task_list.remove(task_to_remove)
        easygui.msgbox(f"Task '{task_to_remove}' has been removed.")
    else:
        easygui.msgbox(f"Task '{task_to_remove}' not found in the list.")
    easygui.msgbox(f"Your current tasks: {task_list}")
    # Ask the user to choose if they want to return to the menu or exit the program.
    choice = ["Yes", "No"]
    back_to_menu = easygui.choicebox("Do you want to return to the menu?", choice)
    if back_to_menu == "Yes":
        load_menu()
    else:
        easygui.msgbox("Exiting...") 
            
            
# The main function to start the program from loading the menu.     
def main():
   load_menu()


# Call the main function to start the program.
if __name__ == "__main__":
    main()
