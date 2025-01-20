import pytest
from tasks_manager_fixtures import task_manager_two_tasks, task_manager_empty
from tasks_project.priority_handler import sort_tasks_by_priority

@pytest.mark.unit
def test_sort_tasks_by_priority(task_manager_two_tasks):
    sorted_tasks = sort_tasks_by_priority(task_manager_two_tasks.tasks)
    assert sorted_tasks[0]["title"] == "Buy groceries"
    assert sorted_tasks[1]["title"] == "Study Python"
    
@pytest.mark.unit
def test_sort_empty_task_list(task_manager_empty):
    sorted_tasks = sort_tasks_by_priority(task_manager_empty.tasks)
    assert sorted_tasks == []