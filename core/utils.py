"""
Common utility functions.
"""

from datetime import datetime
from rich.console import Console

from core.constants import DATETIME_FORMAT

console = Console()


def clear_screen() -> None:
    console.clear()


def current_datetime() -> str:
    return datetime.now().strftime(DATETIME_FORMAT)


def pause() -> None:
    input("\nPress Enter to continue...")


def format_datetime(date_string: str) -> str:
    try:
        dt = datetime.strptime(date_string, DATETIME_FORMAT)
        return dt.strftime("%d %b %Y %I:%M %p")
    except ValueError:
        return date_string


def format_date(date_string: str) -> str:
    try:
        dt = datetime.strptime(date_string, "%Y-%m-%d")
        return dt.strftime("%d %b %Y")
    except ValueError:
        return date_string


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def is_overdue(deadline: str) -> bool:
    try:
        due = datetime.strptime(deadline, "%Y-%m-%d").date()
        return due < datetime.today().date()
    except ValueError:
        return False