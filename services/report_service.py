"""
Report Service

Provides dashboard statistics and reports for TaskTact.
"""

from datetime import datetime, timedelta

from data.storage import load_tasks
from models.task import Task


class ReportService:
    """
    Business logic for reports and statistics.
    """

    @staticmethod
    def total_tasks() -> int:
        """Return total number of tasks."""
        return len(load_tasks())

    @staticmethod
    def completed_tasks() -> int:
        """Return number of completed tasks."""
        return sum(
            1
            for task in load_tasks()
            if task.status == "Completed"
        )

    @staticmethod
    def pending_tasks() -> int:
        """Return number of pending tasks."""
        return sum(
            1
            for task in load_tasks()
            if task.status == "Pending"
        )

    @staticmethod
    def overdue_tasks() -> int:
        """Return number of overdue tasks."""

        today = datetime.today().date()

        return sum(
            1
            for task in load_tasks()
            if task.status != "Completed"
            and datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date() < today
        )

    @staticmethod
    def completion_rate() -> float:
        """
        Return completion percentage.
        """

        total = ReportService.total_tasks()

        if total == 0:
            return 0.0

        completed = ReportService.completed_tasks()

        return round((completed / total) * 100, 2)

    @staticmethod
    def category_report() -> dict[str, int]:
        """
        Returns number of tasks in each category.
        """

        report = {}

        for task in load_tasks():
            report[task.category] = (
                report.get(task.category, 0) + 1
            )

        return dict(sorted(report.items()))

    @staticmethod
    def priority_report() -> dict[str, int]:
        """
        Returns task count by priority.
        """

        report = {
            "High": 0,
            "Medium": 0,
            "Low": 0,
        }

        for task in load_tasks():
            report[task.priority] += 1

        return report

    @staticmethod
    def status_report() -> dict[str, int]:
        """
        Returns task count by status.
        """

        report = {
            "Pending": 0,
            "Completed": 0,
            "Overdue": 0,
        }

        today = datetime.today().date()

        for task in load_tasks():

            if (
                task.status != "Completed"
                and datetime.strptime(
                    task.deadline,
                    "%Y-%m-%d"
                ).date() < today
            ):
                report["Overdue"] += 1

            else:
                report[task.status] += 1

        return report

    @staticmethod
    def tasks_due_today() -> list[Task]:
        """
        Return tasks due today.
        """

        today = datetime.today().strftime("%Y-%m-%d")

        return [
            task
            for task in load_tasks()
            if task.deadline == today
        ]

    @staticmethod
    def tasks_due_this_week() -> list[Task]:
        """
        Return tasks due within the next 7 days.
        """

        today = datetime.today().date()
        end = today + timedelta(days=7)

        tasks = []

        for task in load_tasks():

            due = datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date()

            if today <= due <= end:
                tasks.append(task)

        return tasks

    @staticmethod
    def recent_tasks(limit: int = 5) -> list[Task]:
        """
        Return recently created tasks.
        """

        tasks = sorted(
            load_tasks(),
            key=lambda task: task.created_at,
            reverse=True,
        )

        return tasks[:limit]

    @staticmethod
    def dashboard() -> dict:
        """
        Returns dashboard statistics.
        """

        return {
            "total": ReportService.total_tasks(),
            "completed": ReportService.completed_tasks(),
            "pending": ReportService.pending_tasks(),
            "overdue": ReportService.overdue_tasks(),
            "completion_rate": ReportService.completion_rate(),
        }

    @staticmethod
    def full_report() -> dict:
        """
        Returns complete application report.
        """

        return {
            "dashboard": ReportService.dashboard(),
            "category": ReportService.category_report(),
            "priority": ReportService.priority_report(),
            "status": ReportService.status_report(),
            "today": ReportService.tasks_due_today(),
            "week": ReportService.tasks_due_this_week(),
            "recent": ReportService.recent_tasks(),
        }