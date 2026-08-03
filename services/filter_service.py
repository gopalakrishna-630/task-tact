"""
Filter Service

Provides different ways to filter tasks.
"""

from datetime import datetime, timedelta

from data.storage import load_tasks
from models.task import Task


class FilterService:
    """
    Business logic for filtering tasks.
    """

    @staticmethod
    def by_category(category: str) -> list[Task]:
        """Filter tasks by category."""
        return [
            task
            for task in load_tasks()
            if task.category.lower() == category.lower()
        ]

    @staticmethod
    def by_priority(priority: str) -> list[Task]:
        """Filter tasks by priority."""
        return [
            task
            for task in load_tasks()
            if task.priority.lower() == priority.lower()
        ]

    @staticmethod
    def by_status(status: str) -> list[Task]:
        """Filter tasks by status."""
        return [
            task
            for task in load_tasks()
            if task.status.lower() == status.lower()
        ]

    @staticmethod
    def completed() -> list[Task]:
        """Return all completed tasks."""
        return [
            task
            for task in load_tasks()
            if task.status == "Completed"
        ]

    @staticmethod
    def pending() -> list[Task]:
        """Return all pending tasks."""
        return [
            task
            for task in load_tasks()
            if task.status == "Pending"
        ]

    @staticmethod
    def overdue() -> list[Task]:
        """Return overdue tasks."""
        today = datetime.today().date()

        return [
            task
            for task in load_tasks()
            if task.status != "Completed"
            and datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date() < today
        ]

    @staticmethod
    def due_today() -> list[Task]:
        """Return tasks due today."""
        today = datetime.today().strftime("%Y-%m-%d")

        return [
            task
            for task in load_tasks()
            if task.deadline == today
        ]

    @staticmethod
    def due_this_week() -> list[Task]:
        """Return tasks due within the next 7 days."""
        today = datetime.today().date()
        week = today + timedelta(days=7)

        tasks = []

        for task in load_tasks():

            due = datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date()

            if today <= due <= week:
                tasks.append(task)

        return tasks

    @staticmethod
    def by_tags(tag: str) -> list[Task]:
        """Filter tasks by tag."""
        keyword = tag.lower()

        return [
            task
            for task in load_tasks()
            if any(keyword == t.lower() for t in task.tags)
        ]

    @staticmethod
    def high_priority_pending() -> list[Task]:
        """Return all pending high-priority tasks."""
        return [
            task
            for task in load_tasks()
            if task.priority == "High"
            and task.status == "Pending"
        ]

    @staticmethod
    def sort_by_deadline(reverse: bool = False) -> list[Task]:
        """Sort tasks by deadline."""

        tasks = load_tasks()

        return sorted(
            tasks,
            key=lambda task: datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ),
            reverse=reverse,
        )

    @staticmethod
    def sort_by_priority() -> list[Task]:
        """Sort tasks by priority."""

        order = {
            "High": 1,
            "Medium": 2,
            "Low": 3,
        }

        tasks = load_tasks()

        return sorted(
            tasks,
            key=lambda task: order.get(task.priority, 99),
        )

    @staticmethod
    def sort_by_title() -> list[Task]:
        """Sort tasks alphabetically."""

        tasks = load_tasks()

        return sorted(
            tasks,
            key=lambda task: task.title.lower(),
        )

    @staticmethod
    def sort_by_created() -> list[Task]:
        """Sort tasks by creation time."""

        tasks = load_tasks()

        return sorted(
            tasks,
            key=lambda task: task.created_at,
        )