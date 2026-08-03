"""
Message dialogs.
"""

from rich.panel import Panel
from rich.text import Text

from tasktact.core.theme import (
    SUCCESS,
    ERROR,
    WARNING,
    INFO,
)


def success(message: str) -> Panel:
    return Panel(
        Text(message, style=SUCCESS),
        title="SUCCESS",
        border_style=SUCCESS,
    )


def error(message: str) -> Panel:
    return Panel(
        Text(message, style=ERROR),
        title="ERROR",
        border_style=ERROR,
    )


def warning(message: str) -> Panel:
    return Panel(
        Text(message, style=WARNING),
        title="WARNING",
        border_style=WARNING,
    )


def info(message: str) -> Panel:
    return Panel(
        Text(message, style=INFO),
        title="INFO",
        border_style=INFO,
    )