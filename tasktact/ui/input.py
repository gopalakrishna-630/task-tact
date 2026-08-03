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


def ask_choice(name: str, options: list[str]) -> str:
    """
    Ask user to select an option by number from a list.
    """
    if name.endswith("y"):
        plural = name[:-1] + "ies"
    elif name.endswith("s"):
        plural = name + "es"
    else:
        plural = name + "s"
        
    console.print(f"\n[cyan]Available {plural}:[/cyan]")
    for i, opt in enumerate(options, 1):
        console.print(f"  [white]{i}. {opt}[/white]")
        
    while True:
        value = Prompt.ask(f"Enter {name} number").strip()
        if value.isdigit():
            idx = int(value) - 1
            if 0 <= idx < len(options):
                return options[idx]
        console.print("[red]Invalid choice. Please enter a valid number from the list.[/red]")


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