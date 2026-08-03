"""
Search Service

Provides different ways to search tasks.
"""

from models.task import Task
from data.storage import load_tasks


class SearchService:
    """
    Business logic for searching tasks.
    """

    @staticmethod
    def by_id(task_id: str) -> Task | None:
        """
        Search task by ID.
        """
        tasks = load_tasks()

        for task in tasks:
            if task.id.lower() == task_id.lower():
                return task

        return None

    @staticmethod
    def by_title(title: str) -> list[Task]:
        """
        Search tasks by title.
        """
        keyword = title.strip().lower()

        return [
            task
            for task in load_tasks()
            if keyword in task.title.lower()
        ]

    @staticmethod
    def by_description(description: str) -> list[Task]:
        """
        Search tasks by description.
        """
        keyword = description.strip().lower()

        return [
            task
            for task in load_tasks()
            if keyword in task.description.lower()
        ]

    @staticmethod
    def by_category(category: str) -> list[Task]:
        """
        Search tasks by category.
        """
        keyword = category.strip().lower()
        return [
            task
            for task in load_tasks()
            if keyword in task.category.lower()
        ]

    @staticmethod
    def by_priority(priority: str) -> list[Task]:
        """
        Search tasks by priority.
        """
        keyword = priority.strip().lower()
        return [
            task
            for task in load_tasks()
            if keyword in task.priority.lower()
        ]

    @staticmethod
    def by_status(status: str) -> list[Task]:
        """
        Search tasks by status.
        """
        keyword = status.strip().lower()
        return [
            task
            for task in load_tasks()
            if keyword in task.status.lower()
        ]

    @staticmethod
    def by_tag(tag: str) -> list[Task]:
        """
        Search tasks by tag.
        """
        keyword = tag.strip().lower()

        return [
            task
            for task in load_tasks()
            if any(keyword in t.lower() for t in task.tags)
        ]

    @staticmethod
    def by_deadline(deadline: str) -> list[Task]:
        """
        Search tasks by deadline.
        """
        keyword = deadline.strip().lower()
        return [
            task
            for task in load_tasks()
            if keyword in task.deadline.lower()
        ]

    @staticmethod
    def search_all(keyword: str) -> list[Task]:
        """
        Global search across multiple fields.
        """
        keyword = keyword.strip().lower()

        results = []

        for task in load_tasks():

            if (
                keyword in task.id.lower()
                or keyword in task.title.lower()
                or keyword in task.description.lower()
                or keyword in task.category.lower()
                or keyword in task.priority.lower()
                or keyword in task.status.lower()
                or keyword in task.deadline.lower()
                or any(keyword in tag.lower() for tag in task.tags)
            ):
                results.append(task)

        return results

    @staticmethod
    def task_exists(task_id: str) -> bool:
        """
        Check whether a task exists.
        """
        return SearchService.by_id(task_id) is not None