# This is Version 2

import easygui
import os

# The function to load the menu and ask the user to input an option.
def load_menu():
    global list_name
    menu_option = ["1. Create a new list", 
                   "2. Load an existing list", 
                   "3. Delete an existing list", 
                   "4. Exit"]
    title = "To Do List Menu"
    user_option = easygui.choicebox(title, "Please select an option: ", menu_option)
    # Call the corresponding function based on the user's choice, 
    # and pass the tasks list to the function.
    if user_option == "1. Create a new list":
        list_name = ask_list_name_to_create()
        create_list_file()
    elif user_option == "2. Load an existing list":
        list_name = list_option_to_load()
        load_list_file()
    elif user_option == "3. Delete an existing list":
        list_name = list_option_to_delete()
        delete_list_file()
    elif user_option == "4. Exit":
        easygui.msgbox("Exiting...")
        return None
    # Prints out an message to tell te user that they 
    # entered an invalid option and reload the menu.
    else: # If the user closes the window or clicked cancel.
        easygui.msgbox("Exiting...")
        return None


# Create an empty list to store the user's tasks.
task_list = []


# Ask the user to enter the name of the list they want to create or load, and return the name.
def ask_list_name_to_create():
    list_name_to_create = easygui.enterbox("Please enter the name of the list you want to create: ")
    if list_name_to_create is None: # If the user closes the window or clicked cancel.
        easygui.msgbox("Exiting...")
        return None
    elif not list_name_to_create: # If the user enters nothing and clicked ok,
        # it will be seen as an empty input and ask the user again for the list name.
        easygui.msgbox("List name cannot be empty, please enter a valid name.")
        return ask_list_name_to_create()
    return list_name_to_create + ".txt"

def list_option_to_load():
    existing_lists = [file for file in os.listdir() if file.endswith(".txt")]
    if len(existing_lists) == 0:
        easygui.msgbox("Currently there are no existing lists, please create a new list first.")
        create_list_file()
        return None
    elif len(existing_lists) == 1:
        easygui.msgbox(f"Only one list found: {existing_lists[0]}")
        return existing_lists[0]
    list_name_to_load = easygui.choicebox("Please choose the list you want to view", "Load List", existing_lists)
    if list_name_to_load is None: # If the user closes the window or clicked cancel.
        easygui.msgbox("Exiting...")
        return None
    return list_name_to_load

def list_option_to_delete():
    existing_lists = [file for file in os.listdir() if file.endswith(".txt")]
    if len(existing_lists) == 0:
        easygui.msgbox("Currently there are no existing lists, please create a new list first.")
        create_list_file()
        return None
    elif len(existing_lists) == 1:
        easygui.msgbox(f"Only one list found: {existing_lists[0]}")
        return existing_lists[0]
    list_name_to_delete = easygui.choicebox("Please choose the list you want to delete", "Delete List", existing_lists)
    if list_name_to_delete is None: # If the user closes the window or clicked cancel.
        easygui.msgbox("Exiting...")
        return None
    return list_name_to_delete


# The function to ask the user if they want to add a task to the list, 
# and call the add task function if they choose yes.
def add_task_option():
    choice = ["Yes", "No"]
    add_task_option = easygui.choicebox("Do you want to add a task to this list?", "Add Task", choice)
    if add_task_option == "Yes":
        while True:
            if add_task(task_list) == False:
                easygui.msgbox("Exiting...")
                return False
            another_task = easygui.choicebox("Do you want to add another task to this list?", "Add Task", choice)
            if another_task == "No":
                break
            elif another_task is None: # If the user closes the window or clicked cancel.
                easygui.msgbox("Exiting...")
                return False
        easygui.msgbox("Finished adding tasks.")
        easygui.msgbox(f"Your current tasks: {task_list}")
        # Ask the user whether they want to save the task list after adding tasks.
        save_option = easygui.choicebox("Do you want to save the task list?", "Save Task List", choice)
        if save_option == "Yes":
            save_to_file(task_list)
            easygui.msgbox("Task list saved.")
            return True
        elif save_option == "No":
            easygui.msgbox("Task list is not saved.")
            return_to_menu_option()
        else: # If the user closes the window or clicked cancel.
            easygui.msgbox("Exiting...")
            return False
    elif add_task_option == "No":
        easygui.msgbox("Skipping adding tasks.")
        return True
    else:
        easygui.msgbox("Exiting...")
        return False
    
    
# The function to ask the user if they want to delete a task from the list,
# and call the remove task function if they choose yes.
def delete_task_option():
    choice = ["Yes", "No"]
    delete_task_option = easygui.choicebox("Do you want to delete a task from this list?", "Delete Task", choice)
    if delete_task_option == "Yes":
        while True:
            if remove_task(task_list) == False:
                easygui.msgbox("Exiting...")
                return False
            remove_another_task = easygui.choicebox("Do you want to delete another task from this list?", "Delete Task", choice)
            if remove_another_task == "No":
                break
            else: # If the user closes the window or clicked cancel.
                return False
        easygui.msgbox("Finished deleting tasks.")
        easygui.msgbox(f"Your current tasks: {task_list}")
        save_option = easygui.choicebox("Do you want to save the task list?", "Save Task List", choice)
        if save_option == "Yes":
            save_to_file(task_list)
            easygui.msgbox("Task list saved.")
            return_to_menu_option()
            return True
        elif save_option == "No":
            easygui.msgbox("Task list is not saved.")
            return_to_menu_option()
            return True
        else: # If the user closes the window or clicked cancel.
            easygui.msgbox("Task list is not saved. \nExiting...")
            return False
    elif delete_task_option == "No":
        easygui.msgbox("Skipping deleting tasks.")
        return True
    else:
        easygui.msgbox("Exiting...")
        return False
    
   
# The function to ask the user if they want to mark a task as completed
def mark_task_as_completed():
    choice = ["Yes", "No"]
    mark_completed_option = easygui.choicebox("Do you want to mark a task as completed?", "Mark Task as Completed", choice)
    while True:
        if mark_completed_option == "Yes":
            task_to_mark = easygui.enterbox(f"Your current tasks are: {task_list}\nPlease enter the task you want to mark as completed: ")
            if task_to_mark is None: # If the user closes the window or clicked cancel.
                return False
            elif not task_to_mark: # If the user enters nothing and clicked ok,
                easygui.msgbox("Task cannot be empty, please enter a valid task.")
                continue
            if task_to_mark in task_list:
                task_list.remove(task_to_mark)
                easygui.msgbox(f"Task '{task_to_mark}' has been marked as completed and removed from the list.")
            else:
                easygui.msgbox(f"Task '{task_to_mark}' is not found in the list, please enter a valid task.")
                continue
        elif mark_completed_option == "No":
            easygui.msgbox("Skipping marking tasks as completed.")
            return True
        else: # If the user closes the window or clicked cancel.
            easygui.msgbox("Exiting...")
            return False
        mark_another_task = easygui.choicebox("Do you want to mark another task as completed?", "Mark Task as Completed", choice)
        if mark_another_task == "Yes":
            continue
        elif mark_another_task == "No":
            easygui.msgbox("Finished marking tasks as completed.")
            return True
        else: # If the user closes the window or clicked cancel.
            easygui.msgbox("Exiting...")
            return False
    
        
    
# Ask the user to choose if they want to return to the menu or exit the program.
def return_to_menu_option():
    choice = ["Yes", "No"]
    return_to_menu = easygui.choicebox("Do you want to return to the menu?", "Return to Menu", choice)
    if return_to_menu == "Yes":
        return True
    elif return_to_menu == "No":
        easygui.msgbox("Exiting...")
        return False
    else: # If the user closes the window or clicked cancel
        easygui.msgbox("Exiting...")
        return False


# The function to append tasks to the file.
def save_to_file(task_list):
    with open(list_name, "w") as file:
        for tasks in task_list:
            # Append tasks in the task list to the file and add a new line after each task.
            file.write(tasks + "\n")
            
# The function to read existing tasks from the file and return them as a string, 
# to be displayed whent the user choose to view tasks.
def read_from_file():
    with open(list_name, "r") as file:
        tasks = file.read().capitalize()
        return tasks


# The function to add tasks to the tasks list.
def add_task(task_list):
    # Ask the user to to enter a task.
    while True:
        new_task = easygui.enterbox("Please enter a task: ")
        if new_task is None: # If the user closes the window or clicked cancel, it will be seen as an empty input and return to menu.
            return False
        elif not new_task:
                easygui.msgbox("Task cannot be empty, please enter a valid task.")
                continue
        new_task = new_task
        if new_task in task_list:
            easygui.msgbox(f"Task '{new_task}' already exists in the list, please enter a different task.")
            continue
        else:
            break
    # Add the new task to the task list.
    task_list.append(new_task)
    # Print out a message to tell the user that the task is successfully added.
    easygui.msgbox(f"Task '{new_task}' is now added to the list.")
    # Print out the current task list.
    easygui.msgbox(f"Your current tasks: {task_list}")
    
    
    
# The function to remove tasks from the task list.    
def remove_task(task_list):
    # Ask the user for the task they want to remove.
    while True: 
        task_to_remove = easygui.enterbox(f"Your current tasks are: {task_list}\n Please enter the task you want to remove: ")
        # Check if the task is in the task list and remove it if it is,
        # otherwise print out a message to tell the user the task is not found.
        if task_to_remove is None: # If the user closes the window or clicked cancel
            easygui.msgbox("Exiting...")
            return False
        if not task_to_remove:
            easygui.msgbox("Task cannot be empty, please enter a valid task.")
            continue
        if task_to_remove in task_list:
            task_list.remove(task_to_remove)
            easygui.msgbox(f"Task '{task_to_remove}' has been removed.")
        else:
            easygui.msgbox(f"Task '{task_to_remove}' not found in the list, please enter a valid task.")
            remove_task(task_list)
        # Print out the current task list after removing the task.
        easygui.msgbox(f"Your current tasks: {task_list}")


# The function to create a new list file.
def create_list_file():
    global list_name
    global task_list
    task_list = []
    while True:
        try:
            with open(list_name, "r"):
                new_name = easygui.enterbox(
                    f"List '{list_name}' already exists.\nPlease enter a different name:")
            if new_name is None:
                easygui.msgbox("Exiting...")
                return None
            elif not new_name:
                easygui.msgbox("List name cannot be empty, please enter a valid name.")
                continue
            list_name = new_name + ".txt"
        except FileNotFoundError:
            break
    with open(list_name, "w"):
        pass
    easygui.msgbox(f"List '{list_name}' has been created.")
    add_task_option()
    if len(task_list) > 0:
        if mark_task_as_completed() == False:
            easygui.msgbox("Exiting...")
            return None
    return_to_menu_option()
    
    
# The function to load an existing list file and display the current tasks,
# and ask the user whether they want to add or delete tasks.
def load_list_file():
    global task_list
    try:
        with open(list_name, "r") as file:
            task_list = file.read().splitlines()
            if task_list:
                easygui.msgbox(f"Your current tasks are: {task_list}")
            else:
                easygui.msgbox("Your task list is empty.")
        if mark_task_as_completed() == False:
            return False
        if add_task_option() == False:
            return False
        if delete_task_option() == False:
            return False
    except FileNotFoundError:
        easygui.msgbox(f"List '{list_name}' does not exist, please enter a valid list name.")
        list_option_to_load()
   
 
# The function to delete an existing list file.
def delete_list_file():
    choice = ["Yes", "No"]
    if list_name:
        os.remove(list_name)
        easygui.msgbox(f"List '{list_name}' has been deleted.")
        delete_another = easygui.choicebox("Do you want to delete another list?", "Delete List", choice)
        if delete_another == "Yes":
            delete_list_file()
        elif delete_another == "No":
            return_to_menu_option()
        else: # If the user closes the window or clicked cancel
            easygui.msgbox("Exiting...")
            return None
    elif list_name is None: # If the user closes the window or clicked cancel
        easygui.msgbox("Exiting...")
        return None
    else:
        easygui.msgbox("No list is selected for deletion.")
        return_to_menu_option()
    
 
# The main function to start the program from loading the menu.     
def main():
   load_menu()


# Call the main function to start the program.
if __name__ == "__main__":
    main()
