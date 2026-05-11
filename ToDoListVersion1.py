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
    
