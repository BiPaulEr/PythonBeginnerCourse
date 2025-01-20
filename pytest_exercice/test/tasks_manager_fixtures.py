import pytest
from tasks_project.task_manager import TaskManager

@pytest.fixture
def task_manager_two_tasks():
    tm = TaskManager()
    tm.add_task("Study Python", priority=3)
    tm.add_task("Buy groceries", priority=1)
    return tm

@pytest.fixture
def task_manager_empty():
    tm = TaskManager()
    return tm