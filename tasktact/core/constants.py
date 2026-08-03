"""
Application constants for TaskTact.
"""

APP_NAME = "TaskTact"
VERSION = "1.0.0"

FILE_NAME = "tasks.json"

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

TASK_ID_PREFIX = "TT"
TASK_ID_PADDING = 3

CATEGORIES = [
    "Study",
    "Personal",
    "Work",
    "Fitness",
    "Shopping",
    "Finance",
    "Other",
]

PRIORITIES = [
    "High",
    "Medium",
    "Low",
]

STATUS = [
    "Pending",
    "Completed",
    "Overdue",
]

MAX_TITLE_LENGTH = 100
MAX_DESCRIPTION_LENGTH = 500