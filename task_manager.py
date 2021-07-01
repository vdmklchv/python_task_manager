import task

__tasks = []


def get_task(num: int) -> task.Task:
    for entry in __tasks:
        if entry.id == num:
            return entry
        else:
            continue
    return None


def add_task(name: task.Task) -> None:
    __tasks.append(name)


def print_task(num: int) -> None:
    task_to_print = get_task(num)
    if task:
        print(task_to_print)


def list_tasks() -> None:
    if len(__tasks) == 0:
        print("No tasks to display")
    else:
        for entry in __tasks:
            print(f"{entry.id} - {entry.name}")


def get_length() -> int:
    return len(__tasks)


def toggle_complete(num: int):
    task_to_complete = get_task(num)
    if task_to_complete:
        task_to_complete.is_done = not task_to_complete.is_done


def remove_task(num: int):
    task_to_remove = get_task(num)
    if task_to_remove:
        task_index = __tasks.index(task_to_remove)
        __tasks.pop(task_index)


def edit_task_name(num: int):
    task_to_edit = get_task(num)
    if task_to_edit:
        new_name = input("Input new task name: ")
        task.name = new_name
    else:
        print("No task with this id")
