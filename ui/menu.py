"""
Generic menu renderer.
"""

from rich.table import Table
from rich.panel import Panel

from core.theme import PRIMARY


def build_menu(title: str, menu_items: list[dict]) -> Panel:
    """
    Builds any menu using menu definitions.
    """

    table = Table.grid(expand=True)

    table.add_column(justify="center", style="cyan", width=8)
    table.add_column(style="white")

    for item in menu_items:
        table.add_row(
            item["key"],
            item["label"]
        )

    return Panel(
        table,
        title=title,
        border_style=PRIMARY,
        padding=(1, 2),
    )