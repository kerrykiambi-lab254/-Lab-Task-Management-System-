from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Task title must be a string.")
    if len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return True
    
def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Task description must be a string.")
    if len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")
    return True    

def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string.")
    value = due_date.strip()
    if len(value) == 0:
        raise ValueError("Due date cannot be empty.")
    try:
        datetime.strptime(value, "%Y-%m-%d").date()
        return True
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

