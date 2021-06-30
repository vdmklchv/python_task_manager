import task
import task_manager


def create_task(name: str) -> task.Task:
    user_task = task.Task(name)
    return user_task


while True:
    menu_choice = input("What would you like to do (input number) 1 - Add 2 - List all "
                        "3 - Edit 4 - Remove 5 - Print task  Exit to exit: ")
    choices = ["1", "2", "3", "4", "5", 'exit']

    if menu_choice.lower() not in choices:
        print("Incorrect input")
    elif menu_choice.lower() == '1':
        task_name = input("Input task name: ")
        new_task = create_task(task_name)
        task_manager.add_task(new_task)
    elif menu_choice.lower() == '2':
        task_manager.list_tasks()
    elif menu_choice.lower() == '4':
        task_num = int(input("Number of task to remove: "))
        task_manager.remove_task(task_num)
    elif menu_choice.lower() == '5':
        task_num = int(input("Input task number: "))
        if (int(task_num) >= 0) and (task_num <= task_manager.get_length()):
            task_manager.print_task(task_num)
        else:
            print("No task with such id")
    continue
