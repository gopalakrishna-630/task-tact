"""
Generates sequential Task IDs.
"""

from tasktact.core.constants import TASK_ID_PADDING, TASK_ID_PREFIX
from tasktact.storage.storage import load_tasks


def generate_task_id() -> str:
    """
    Generate the next Task ID.

    Example:
    TT001
    TT002
    TT003
    """

    tasks = load_tasks()

    if not tasks:
        return f"{TASK_ID_PREFIX}{1:0{TASK_ID_PADDING}d}"

    numbers = [
        int(task.id.replace(TASK_ID_PREFIX, ""))
        for task in tasks
        if task.id.startswith(TASK_ID_PREFIX)
    ]

    next_number = max(numbers) + 1

    return f"{TASK_ID_PREFIX}{next_number:0{TASK_ID_PADDING}d}"