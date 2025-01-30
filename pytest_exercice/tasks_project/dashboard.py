from task_manager import TaskManager
from priority_handler import sort_tasks_by_priority

def generate_task_report(task_manager):
    pending_tasks = [task for task in task_manager.tasks if not task["completed"]]
    completed_tasks = [task for task in task_manager.tasks if task["completed"]]

    pending_summary = f"Pending Tasks: {len(pending_tasks)}"
    completed_summary = f"Completed Tasks: {len(completed_tasks)}"
    
    sorted_pending = sort_tasks_by_priority(pending_tasks)

    top_priority_task = sorted_pending[0]['title'] if sorted_pending else 'None'
    return pending_summary, completed_summary, f"Top Priority Task: {top_priority_task}"

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.add_task("Study Python", priority=2)
    task_manager.add_task("Buy groceries", priority=1)
    task_manager.add_task("Write blog post", priority=3)
    task_manager.complete_task("Buy groceries")
    report = generate_task_report(task_manager)
    print(report)
