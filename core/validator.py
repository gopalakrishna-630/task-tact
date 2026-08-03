"""
Validation utilities.
"""

from datetime import datetime

from core.constants import (
    DATE_FORMAT,
    CATEGORIES,
    PRIORITIES,
    STATUS,
    MAX_TITLE_LENGTH,
    MAX_DESCRIPTION_LENGTH,
)


def validate_title(title: str) -> bool:
    title = title.strip()
    return 0 < len(title) <= MAX_TITLE_LENGTH


def validate_description(description: str) -> bool:
    return len(description.strip()) <= MAX_DESCRIPTION_LENGTH


def validate_date(date: str) -> bool:
    try:
        datetime.strptime(date, DATE_FORMAT)
        return True
    except ValueError:
        return False


def validate_category(category: str) -> bool:
    return category in CATEGORIES


def validate_priority(priority: str) -> bool:
    return priority in PRIORITIES


def validate_status(status: str) -> bool:
    return status in STATUS


def validate_menu_choice(choice: str, valid_choices: list[str]) -> bool:
    return choice in valid_choices


def validate_yes_no(choice: str) -> bool:
    return choice.upper() in ("Y", "N")


def validate_task_id(task_id: str) -> bool:
    return task_id.startswith("TT") and task_id[2:].isdigit()