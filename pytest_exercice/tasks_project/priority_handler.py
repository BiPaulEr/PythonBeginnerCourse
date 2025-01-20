def sort_tasks_by_priority(tasks):
    return sorted(tasks, key=lambda task: task["priority"])