import pytest
from tasks_manager_fixtures import task_manager_two_tasks, task_manager_empty
from tasks_project.dashboard import generate_task_report

@pytest.mark.integration
def test_dashboard(task_manager_two_tasks):
    task_manager_two_tasks.complete_task("Buy groceries")
    pending, completed, top_priority = generate_task_report(task_manager_two_tasks)
    assert pending == "Pending Tasks: 1"
    assert completed ==  "Completed Tasks: 1"
    assert top_priority == "Top Priority Task: Study Python"
