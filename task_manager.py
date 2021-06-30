import task

tasks = []


def add_task(name: task.Task) -> None:
    tasks.append(name)


def print_task(num: int) -> None:
    for entry in tasks:
        if entry.id == num:
            print(entry)


def list_tasks() -> None:
    for entry in tasks:
        print(f"{entry.id} - {entry.name}")


def get_length() -> int:
    return len(tasks)


def toggle_complete(num: int):
    for entry in tasks:
        if entry.id == num:
            entry.is_done = not entry.is_done


def remove_task(num: int):
    for entry in tasks:
        if entry.id == num:
            task_index = tasks.index(entry)
            tasks.pop(task_index)
