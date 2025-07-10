from behave import given, when, then
from todo_list import TodoList
import traceback

# === Setup y estado inicial ===

@given('the to-do list is empty')
def step_given_list_empty(context):
    context.todo = TodoList()

@given('the to-do list contains tasks')
def step_given_list_has_tasks(context):
    context.todo = TodoList()
    for row in context.table:
        context.todo.add_task(row['Task'])

@given('the to-do list contains a task "{task}" with status "{status}"')
def step_given_task_with_status(context, task, status):
    context.todo = TodoList()
    context.todo.add_task(task)
    if status.lower() == "completed":
        context.todo.mark_completed(task)

# === Acciones del usuario ===

@when('the user adds a task "{task}"')
def step_when_add_task(context, task):
    context.todo.add_task(task)

@when('the user lists all tasks')
def step_when_list_tasks(context):
    context.result = context.todo.list_tasks()

@when('the user marks task "{task}" as completed')
def step_when_mark_task_completed(context, task):
    try:
        context.todo.mark_completed(task)
        context.error = None
    except Exception as e:
        context.error = str(e)

@when('the user clears the to-do list')
def step_when_clear_list(context):
    context.todo.clear_tasks()

@when('the user removes task "{task}"')
def step_when_remove_task(context, task):
    try:
        context.todo.remove_task(task)
        context.error = None
    except Exception as e:
        context.error = str(e)

# === Resultados esperados ===

@then('the to-do list should contain "{task}"')
def step_then_list_should_contain(context, task):
    assert task in context.todo.list_tasks(), f"Expected task '{task}' in list {context.todo.list_tasks()}"

@then('the output should include')
def step_output_should_include(context):
    actual_tasks = context.result
    expected_tasks = [row['Task'] for row in context.table]
    for task in expected_tasks:
        assert task in actual_tasks, f"Expected '{task}' in {actual_tasks}"

@then('the to-do list should be empty')
def step_then_list_empty(context):
    assert context.todo.count_tasks() == 0, f"Expected empty list, found {context.todo.count_tasks()} tasks"

@then('the task "{task}" should be marked as completed')
def step_then_task_completed(context, task):
    for t in context.todo.list_all():
        if t.description == task:
            assert t.completed is True, f"Task '{task}' is not marked as completed"
            return
    assert False, f"Task '{task}' not found in list"

@then('the to-do list should contain only')
def step_then_should_contain_only(context):
    expected = [row['Task'] for row in context.table]
    actual = context.todo.list_tasks()
    assert actual == expected, f"Expected tasks {expected}, but got {actual}"

@then('an error should be shown')
def step_then_error_shown(context):
    assert context.error is not None, "Expected an error but none was raised"
    assert "not found" in context.error.lower(), f"Unexpected error message: {context.error}"
 