"""
Task table renderer.
"""

from rich.table import Table

from tasktact.core.theme import (
    PRIORITY_COLORS,
    STATUS_COLORS,
)


def build_task_table(tasks: list):
    """
    Builds the task table.
    """

    table = Table(
        title="Tasks",
        show_lines=False,
        expand=True,
    )

    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Category")
    table.add_column("Priority")
    table.add_column("Deadline")
    table.add_column("Status")

    for task in tasks:

        table.add_row(
            task.id,
            task.title,
            task.category,
            f"[{PRIORITY_COLORS.get(task.priority.capitalize(), 'white')}]{task.priority.capitalize()}[/]",
            task.deadline,
            f"[{STATUS_COLORS.get(task.status.capitalize(), 'white')}]{task.status.capitalize()}[/]",
        )

    return table