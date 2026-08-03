"""
Application banner.
"""

from rich.align import Align
from rich.panel import Panel
from rich.text import Text

from core.constants import APP_NAME, VERSION
from core.theme import PRIMARY


def build_banner() -> Panel:
    """
    Returns the application banner.
    """

    title = Text()
    title.append(f"{APP_NAME}\n", style=f"bold {PRIMARY}")
    title.append(
        "Intelligent To-Do Manager",
        style="italic white"
    )

    return Panel(
        Align.center(title),
        title=f"v{VERSION}",
        border_style=PRIMARY,
        padding=(1, 2),
    )