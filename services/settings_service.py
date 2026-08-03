"""
Settings Service

Provides application settings, backup, restore, reset,
and information about the application.
"""

from pathlib import Path

from data.backup import (
    create_backup,
    restore_backup,
)

from data.storage import (
    clear_tasks,
    load_tasks,
)

from core.constants import (
    APP_NAME,
    VERSION,
    FILE_NAME,
)

from data.storage import DATA_FILE
from data.backup import BACKUP_FILE


class SettingsService:
    """
    Business logic for application settings.
    """

    @staticmethod
    def backup_data() -> bool:
        """
        Create a backup of task data.
        """
        return create_backup()

    @staticmethod
    def restore_data() -> bool:
        """
        Restore task data from backup.
        """
        return restore_backup()

    @staticmethod
    def reset_application() -> bool:
        """
        Delete all tasks.
        """
        try:
            clear_tasks()
            return True
        except Exception:
            return False

    @staticmethod
    def database_exists() -> bool:
        """
        Check whether the task database exists.
        """
        return DATA_FILE.exists()

    @staticmethod
    def total_tasks() -> int:
        """
        Return total number of tasks.
        """
        return len(load_tasks())

    @staticmethod
    def storage_size() -> float:
        """
        Return database size in KB.
        """
        path = DATA_FILE
        if not path.exists():
            return 0.0

        size = path.stat().st_size

        return round(size / 1024, 2)

    @staticmethod
    def application_info() -> dict:
        """
        Return application information.
        """
        return {
            "name": APP_NAME,
            "version": VERSION,
            "database": FILE_NAME,
            "total_tasks": SettingsService.total_tasks(),
            "database_exists": SettingsService.database_exists(),
            "database_size_kb": SettingsService.storage_size(),
        }

    @staticmethod
    def health_check() -> dict:
        """
        Return application health status.
        """
        return {
            "storage": "OK" if SettingsService.database_exists() else "Missing",
            "tasks": SettingsService.total_tasks(),
            "backup_available": BACKUP_FILE.exists(),
        }