"""
Backup and restore task data.
"""

import shutil
from pathlib import Path

from core.constants import FILE_NAME

DATA_FILE = Path(__file__).parent / FILE_NAME
BACKUP_FILE = Path(__file__).parent / "tasks_backup.json"


def create_backup() -> bool:
    """
    Create a backup of the task database.
    """
    try:
        shutil.copy(DATA_FILE, BACKUP_FILE)
        return True
    except FileNotFoundError:
        return False


def restore_backup() -> bool:
    """
    Restore tasks from backup.
    """
    try:
        shutil.copy(BACKUP_FILE, DATA_FILE)
        return True
    except FileNotFoundError:
        return False