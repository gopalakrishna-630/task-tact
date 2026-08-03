"""
Main application layout.
"""

from rich.layout import Layout
from rich.panel import Panel

from ui.banner import build_banner
from ui.dashboard import build_dashboard
from ui.menu import build_menu

from core.theme import (
    HEADER_SIZE,
    DASHBOARD_SIZE,
    FOOTER_SIZE,
    LEFT_RATIO,
    RIGHT_RATIO,
)


def create_layout(
    menu_title: str,
    menu_items: list[dict],
    dashboard_data: dict,
) -> Layout:
    """
    Creates the complete application layout.
    """

    layout = Layout()

    layout.split_column(
        Layout(name="header", size=HEADER_SIZE),
        Layout(name="dashboard", size=DASHBOARD_SIZE),
        Layout(name="body"),
        Layout(name="footer", size=FOOTER_SIZE),
    )

    layout["body"].split_row(
        Layout(name="menu", ratio=LEFT_RATIO),
        Layout(name="content", ratio=RIGHT_RATIO),
    )

    layout["header"].update(
        build_banner()
    )

    layout["dashboard"].update(
        build_dashboard(
            dashboard_data["total"],
            dashboard_data["completed"],
            dashboard_data["pending"],
            dashboard_data["overdue"],
        )
    )

    layout["menu"].update(
        build_menu(
            menu_title,
            menu_items,
        )
    )

    layout["content"].update(
        Panel(
            "Welcome to TaskTact\n\nSelect an option from the menu.",
            title="Information",
            border_style="cyan",
        )
    )

    layout["footer"].update(
        Panel(
            "Status : Ready",
            border_style="green",
        )
    )

    return layout