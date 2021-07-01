import task

tasks = []


def get_task(num: int) -> task.Task:
    for entry in tasks:
        if entry.id == num:
            return entry
        else:
            return None


def add_task(name: task.Task) -> None:
    tasks.append(name)


def print_task(num: int) -> None:
    task = get_task(num)
    if task:
        print(task)


def list_tasks() -> None:
    if len(tasks) == 0:
        print("No tasks to display")
    else:
        for entry in tasks:
            print(f"{entry.id} - {entry.name}")


def get_length() -> int:
    return len(tasks)


def toggle_complete(num: int):
    task = get_task(num)
    if task:
       task.is_done = not task.is_done


def remove_task(num: int):
    task = get_task(num)
    if task:
        task_index = tasks.index(task)
        tasks.pop(task_index)
