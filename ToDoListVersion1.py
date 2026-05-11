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
    user_option = int(input("Please select an option: "))
    tasks_list = []
    if user_option == 1:
        add_task(tasks_list)
    elif user_option == 2:
        view_task(tasks_list)
    elif user_option == 3:
       remove_task(tasks_list)
    else:
        print("Exiting...")
    

def add_task(task_list):
    new_task = input("Please enter a task: ")
    task_list.append(new_task)
    print(f"Task '{new_task}' is now added to the list.")
    print(f"Your current tasks: {task_list}")
    save_option = input("Do you want to save the task list? (yes/no): ")
    if save_option.lower() == "yes":
        print("Task list saved.")
    else:
        print("Task list is not saved.")
    back_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if back_to_menu == "yes":
        load_menu()
    else:
        print("Exiting...")
   
    
    

def view_task(task_list):
    print(f"Your tasks: {task_list}")
    back_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if back_to_menu == "yes":
        load_menu()
    else:
        print("Exiting...")
    
    
def remove_task(task_list):
    task_to_remove = input("Please enter the task you want to remove: ")
    if task_to_remove in task_list:
        task_list.remove(task_to_remove)
        print(f"Task '{task_to_remove}' has been removed.")
    else:
        print(f"Task '{task_to_remove}' not found in the list.")
    print(f"Your current tasks: {task_list}")
    back_to_menu = input("Do you want to return to the menu? (yes/no): ")
    if back_to_menu == "yes":
        load_menu()
    else:
        print("Exiting...") 
    
        
def main():
   load_menu()

main()
