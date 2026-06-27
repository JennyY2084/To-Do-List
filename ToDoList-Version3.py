# This is Version 3

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
    user_option = easygui.choicebox("Please select an option: ", title, menu_option)
    # Call the corresponding function based on the user's choice, 
    # and pass the tasks list to the function.
    if user_option == "1. Create a new list":
        list_name = ask_list_name_to_create()
        if list_name is not None:
            create_list_file()
    elif user_option == "2. Load an existing list":
        list_name = list_option_to_load()
        if list_name is not None:
            load_list_file()
    elif user_option == "3. Delete an existing list":
        list_name = list_option_to_delete()
        if list_name is not None:
            delete_list_file()
    elif user_option == "4. Exit":
        easygui.msgbox("Exiting...")
        return "EXIT"
    # Prints out an message to tell te user that they 
    # entered an invalid option and reload the menu.
    else: # If the user closes the window or clicked cancel.
        return None


# Create an empty list to store the user's tasks.
task_list = []


# Ask the user to enter the name of the list they want to create or load, and return the name.
def ask_list_name_to_create():
    list_name_to_create = easygui.enterbox("Please enter the name of the list you want to create: ")
    if list_name_to_create is None: # If the user closes the window or clicked cancel.
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
        return None
    return list_name_to_delete


# The function to ask the user if they want to add a task to the list, 
# and call the add task function if they choose yes.
def add_task_option():
    choice = ["No", "Yes"]
    add_task_option = easygui.buttonbox("Do you want to add a task to this list?", "Add Task", choice)
    if add_task_option == "Yes":
        while True:
            if add_task(task_list) == False:
                return False
            easygui.msgbox("Finished adding tasks.")
            easygui.msgbox(f"Your current tasks: {task_list}")
            # Ask the user whether they want to save the task list after adding tasks.
            save_option = easygui.buttonbox("Do you want to save the task list?", "Save Task List", choice)
            if save_option == "Yes":
                save_to_file(task_list)
                easygui.msgbox("Task list saved.")
                return True
            elif save_option == "No":
                easygui.msgbox("Task list is not saved.")
                return True
            else: # If the user closes the window or clicked cancel.
                return False
    elif add_task_option == "No":
        easygui.msgbox("Skipping adding tasks.")
        return True
    else:
        return False
    
    
# The function to ask the user if they want to delete a task from the list,
# and call the remove task function if they choose yes.
def delete_task_option():
    choice = ["No", "Yes"]
    delete_choice = easygui.buttonbox("Do you want to delete a task from this list?", "Delete Task", choice)
    if delete_choice == "Yes":
        if remove_task(task_list) == False:
            return False
        easygui.msgbox("Finished deleting tasks.")
        easygui.msgbox(f"Your current tasks: {task_list}")
        save_option = easygui.buttonbox("Do you want to save the task list?", "Save Task List", choice)
        if save_option == "Yes":
            save_to_file(task_list)
            easygui.msgbox("Task list saved.")
            return True
        elif save_option == "No":
            easygui.msgbox("Task list is not saved.")
            return True
        else:
            return False
    elif delete_choice == "No":
        easygui.msgbox("Skipping deleting tasks.")
        return True
    else:
        return False
    
   
# The function to ask the user if they want to mark a task as completed
def mark_task_as_completed():
    choice = ["No", "Yes"]
    if not task_list:
        easygui.msgbox("Your task list is empty")
        return True
    # Ask the user if they want to mark a task as completed.
    mark_completed_option = easygui.buttonbox("Do you want to mark a task as completed?", "Mark Task as Completed", choice)
    if mark_completed_option == "Yes":
        # Present the user with a list of tasks to choose from, 
        # and allow them to select multiple tasks to mark as completed.
        completed_tasks = easygui.multchoicebox("Please tick the tasks you have completed: ", "Mark task as completed", task_list)
        if completed_tasks is None:
            return None
        for i in range(len(task_list)):
            if task_list[i] in completed_tasks:
                task_list[i] = task_list[i] + "✅"
        easygui.msgbox("Selected tasks have been marked as completed.")
        easygui.msgbox(f"Your current tasks: {task_list}")
        save_option = easygui.buttonbox("Do you want to save the task list?", "Save Task List", choice)
        if save_option == "Yes":
            save_to_file(task_list)
            easygui.msgbox("Task list saved.")
            return True
        elif save_option == "No":
            easygui.msgbox("Task list is not saved.")
            return True
        else: # If the user closes the window or clicked cancel.
            return False
    elif mark_completed_option == "No":
        easygui.msgbox("Skipping marking tasks as completed.")
        return True


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
        new_tasks = easygui.textbox(f"Current tasks: \n{task_list}\nPlease enter the tasks you want to add to this list (One task per line): ", "Add Tasks")
        if new_tasks is None: # If the user closes the window or clicked cancel, it will be seen as an empty input and return to menu.
            return None
        tasks = new_tasks.splitlines()
        added_tasks = []
        existing_tasks = []
        for task in tasks:
            task = task.strip()
            if not task:
                easygui.msgbox("Task cannot be empty, please enter a valid task:")
                continue
            elif task in task_list:
                existing_tasks.append(task)
            else:
                task_list.append(task)
                added_tasks.append(task)    
        if added_tasks:
            easygui.msgbox(f"Tasks {added_tasks} are now added to the list.")
        if existing_tasks:
            message = "These tasks are already in the list: "
            if len(existing_tasks) == 1:
                    message += existing_tasks[0]
            else:
                for i in range(len(existing_tasks)):
                    message += existing_tasks[i]
                    if i < len(existing_tasks) -1 :
                        message += ", "
            easygui.msgbox(message)
        return True
    
    
    
# The function to remove tasks from the task list.    
def remove_task(task_list):
    # Ask the user for the task they want to remove.
    if not task_list:
        easygui.msgbox("Your task list is empty.")
        return True
    task_to_remove = easygui.multchoicebox("Please tick the task you want to delete: ", "Delete Task", task_list)
    if task_to_remove is None: # If the user closes the window or clicked cancel
        return None
    # Remove the chosen tasks from the task list
    for task in task_to_remove:
        task_list.remove(task)
    easygui.msgbox(f"Task(s) '{task_to_remove}' has been removed from the list.")
    easygui.msgbox(f"Your current tasks: {task_list}")
    return True


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
            return False
    return True
    
    
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
        return True
    except FileNotFoundError:
        easygui.msgbox(f"List '{list_name}' does not exist, please enter a valid list name.")
        list_option_to_load()
    return True
   
 
# The function to delete an existing list file.
def delete_list_file():
    choice = ["No", "Yes"]
    if list_name:
        os.remove(list_name)
        easygui.msgbox(f"List '{list_name}' has been deleted.")
        delete_another = easygui.buttonbox("Do you want to delete another list?", "Delete List", choice)
        if delete_another == "Yes":
            delete_list_file()
        elif delete_another == "No":
            return True
        else: # If the user closes the window or clicked cancel
            return False
    elif list_name is None: # If the user closes the window or clicked cancel
        return None
    else:
        easygui.msgbox("No list is selected for deletion.")
        return True
    
 
# The main function to start the program from loading the menu.     
def main():
   while True:
       result = load_menu()
       if result == "EXIT":
           break


# Call the main function to start the program.
if __name__ == "__main__":
    main()
