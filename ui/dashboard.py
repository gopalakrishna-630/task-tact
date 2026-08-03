"""
Dashboard cards.
"""

from rich.columns import Columns
from rich.panel import Panel

from core.theme import DASHBOARD_ICONS


def build_dashboard(
    total: int,
    completed: int,
    pending: int,
    overdue: int,
):
    """
    Builds dashboard cards.
    """

    cards = [
        Panel(
            f"{DASHBOARD_ICONS['Total']}\n\n{total}",
            title="Total",
            border_style="cyan",
        ),
        Panel(
            f"{DASHBOARD_ICONS['Completed']}\n\n{completed}",
            title="Completed",
            border_style="green",
        ),
        Panel(
            f"{DASHBOARD_ICONS['Pending']}\n\n{pending}",
            title="Pending",
            border_style="yellow",
        ),
        Panel(
            f"{DASHBOARD_ICONS['Overdue']}\n\n{overdue}",
            title="Overdue",
            border_style="red",
        ),
    ]

    return Columns(cards, equal=True, expand=True)