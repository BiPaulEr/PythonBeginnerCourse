import pytest
from tasks_manager_fixtures import task_manager_two_tasks, task_manager_empty

@pytest.mark.unit
def test_complete_task(task_manager_two_tasks):
    result = task_manager_two_tasks.complete_task("Study Python")
    assert result == "Task 'Study Python' marked as completed."
    assert task_manager_two_tasks.tasks[0]["completed"] is True

    result = task_manager_two_tasks.complete_task("Buy groceries")
    assert result == "Task 'Buy groceries' marked as completed."
    assert task_manager_two_tasks.tasks[1]["completed"] is True

@pytest.mark.unit
def test_comple_task_no_present(task_manager_two_tasks):
    result = task_manager_two_tasks.complete_task("Task not in TaskManager")
    assert result == "Task 'Task not in TaskManager' not found."

@pytest.mark.unit
def test_add_task(task_manager_two_tasks):
    assert len(task_manager_two_tasks.tasks) == 2
    task_manager_two_tasks.add_task("New Task", 4)
    assert len(task_manager_two_tasks.tasks) == 3
    
@pytest.mark.unit
@pytest.mark.parametrize("title, priority", [(None, 1), (None, 2)] )
def test_add_task_title_null(task_manager_empty, title, priority):
    with pytest.raises(ValueError):
        task_manager_empty.add_task(title, priority)
