from datetime import datetime
import pendulum


class Task:
    total_tasks = 0
    chisinau = pendulum.timezone("Europe/Chisinau")

    def __init__(self, name):
        self.name = name
        self.is_done = False
        self.id = self.total_tasks + 1
        self.date = datetime.now(self.chisinau)
        self.update_total()

    def __str__(self):
        return f"""
            Task info:
            -----
            name: {self.name}
            id: {self.id}
            date: {self.date}
            complete: {self.is_done}
        """

    @classmethod
    def update_total(cls):
        cls.total_tasks += 1
