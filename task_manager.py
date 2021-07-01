import task

__tasks = []


def get_task(num: int) -> task.Task:
    for entry in __tasks:
        if entry.id == num:
            return entry
        else:
            return None


def add_task(name: task.Task) -> None:
    __tasks.append(name)


def print_task(num: int) -> None:
    task = get_task(num)
    if task:
        print(task)


def list_tasks() -> None:
    if len(__tasks) == 0:
        print("No tasks to display")
    else:
        for entry in __tasks:
            print(f"{entry.id} - {entry.name}")


def get_length() -> int:
    return len(__tasks)


def toggle_complete(num: int):
    task = get_task(num)
    if task:
        task.is_done = not task.is_done


def remove_task(num: int):
    task = get_task(num)
    if task:
        task_index = __tasks.index(task)
        __tasks.pop(task_index)


def edit_task_name(num: int):
    task = get_task(num)
    if task:
        new_name = input("Input new task name: ")
        task.name = new_name
    else:
        print("No task with this id")
