class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority=3):
        if not title:
            raise ValueError("Task title cannot be empty.")
        self.tasks.append({"title": title, "priority": priority, "completed": False})

    def complete_task(self, title):
        for task in self.tasks:
            if task["title"] == title:
                task["completed"] = True
                return f"Task '{title}' marked as completed."
        return f"Task '{title}' not found."