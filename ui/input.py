"""
User input helpers.
"""

from rich.console import Console
from rich.prompt import Confirm
from rich.prompt import Prompt

console = Console()


def ask(message: str) -> str:
    """
    Ask for user input.
    """
    return Prompt.ask(message).strip()


def ask_int(message: str) -> int:
    """
    Ask for integer input.
    """

    while True:
        value = Prompt.ask(message)

        if value.isdigit():
            return int(value)

        console.print("[red]Please enter a valid number.[/red]")


def ask_yes_no(message: str) -> bool:
    """
    Ask yes/no confirmation.
    """
    return Confirm.ask(message)


def pause() -> None:
    """
    Pause execution.
    """
    input("\nPress Enter to continue...")