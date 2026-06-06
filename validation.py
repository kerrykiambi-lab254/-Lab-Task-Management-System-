from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        return False
    if len(title.strip()) == 0:
        return False
    return True
    
def validate_task_description(description):
    if not isinstance(description, str):
        return False
    if len(description.strip()) == 0:
        return False
    return True    

def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False
    value = due_date.strip()
    if len(value) == 0:
        return False
    try:
        due = datetime.strptime(value, "%Y-%m-%d").date()
        return due >= datetime.today().date()
    except ValueError:
        return False
