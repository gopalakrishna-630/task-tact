"""
UI theme configuration for TaskTact.
"""

# ==========================
# Colors
# ==========================

PRIMARY = "cyan"
SECONDARY = "bright_blue"

SUCCESS = "green"
ERROR = "red"
WARNING = "yellow"
INFO = "bright_cyan"

TEXT = "white"
BORDER = "cyan"

# ==========================
# Status Colors
# ==========================

STATUS_COLORS = {
    "Pending": "yellow",
    "Completed": "green",
    "Overdue": "red",
}

# ==========================
# Priority Colors
# ==========================

PRIORITY_COLORS = {
    "High": "red",
    "Medium": "yellow",
    "Low": "green",
}

# ==========================
# Category Icons
# ==========================

CATEGORY_ICONS = {
    "Study": "🎓",
    "Personal": "🏠",
    "Work": "💼",
    "Fitness": "💪",
    "Shopping": "🛒",
    "Finance": "💰",
    "Other": "📌",
}

# ==========================
# Dashboard Icons
# ==========================

DASHBOARD_ICONS = {
    "Total": "📋",
    "Completed": "✅",
    "Pending": "⌛",
    "Overdue": "⚠️",
}

# ==========================
# Layout
# ==========================

HEADER_SIZE = 8
DASHBOARD_SIZE = 8
FOOTER_SIZE = 3

LEFT_RATIO = 2
RIGHT_RATIO = 3