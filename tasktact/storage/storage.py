"""
Handles reading and writing tasks to JSON storage.
"""

import json
from pathlib import Path

from tasktact.core.constants import FILE_NAME
from tasktact.models.task import Task

DATA_FILE = Path(__file__).parent.parent.parent / 'data' / FILE_NAME


def initialize_storage() -> None:
    """
    Create the JSON file if it doesn't exist.
    """
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_tasks() -> list[Task]:
    """
    Load all tasks from storage.
    """
    initialize_storage()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Task.from_dict(task) for task in data]

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks: list[Task]) -> None:
    """
    Save all tasks to storage.
    """
    initialize_storage()

    data = [task.to_dict() for task in tasks]

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def add_task(task: Task) -> None:
    """
    Add a new task.
    """
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)


def update_tasks(tasks: list[Task]) -> None:
    """
    Replace all tasks.
    """
    save_tasks(tasks)


def clear_tasks() -> None:
    """
    Remove all tasks.
    """
    save_tasks([])