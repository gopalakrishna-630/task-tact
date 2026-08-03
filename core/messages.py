"""
Application messages.
"""

SUCCESS = {
    "TASK_ADDED": "Task added successfully.",
    "TASK_UPDATED": "Task updated successfully.",
    "TASK_DELETED": "Task deleted successfully.",
    "TASK_COMPLETED": "Task marked as completed.",
    "BACKUP_CREATED": "Backup created successfully.",
    "BACKUP_RESTORED": "Backup restored successfully.",
}

ERROR = {
    "INVALID_MENU": "Invalid menu option.",
    "INVALID_DATE": "Invalid date format. Use YYYY-MM-DD.",
    "INVALID_INPUT": "Invalid input.",
    "TASK_NOT_FOUND": "Task not found.",
    "NO_TASKS": "No tasks available.",
    "FILE_ERROR": "Unable to access data file.",
}

INFO = {
    "WELCOME": "Welcome to TaskTact.",
    "GOODBYE": "Thank you for using TaskTact.",
    "LOADING": "Loading...",
}

WARNING = {
    "RESET_CONFIRM": "This will delete all tasks.",
    "DELETE_CONFIRM": "Are you sure you want to delete this task?",
}