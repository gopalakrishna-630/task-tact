"""
Task Service

Contains all CRUD operations for tasks.
"""

from models.task import Task

from data.storage import (
    load_tasks,
    save_tasks,
    add_task,
)

from data.task_id import generate_task_id

from core.utils import (
    current_datetime,
    is_overdue,
)


class TaskService:
    """
    Business logic for task management.
    """

    @staticmethod
    def create_task(
        title: str,
        description: str,
        category: str,
        priority: str,
        deadline: str,
        tags: list[str] | None = None,
    ) -> Task:

        if tags is None:
            tags = []

        now = current_datetime()

        task = Task(
            id=generate_task_id(),
            title=title.strip(),
            description=description.strip(),
            category=category,
            priority=priority,
            deadline=deadline,
            status="Pending",
            created_at=now,
            updated_at=now,
            completed_at=None,
            tags=tags,
        )

        add_task(task)

        return task

    @staticmethod
    def get_all_tasks() -> list[Task]:
        return load_tasks()

    @staticmethod
    def get_task(task_id: str) -> Task | None:

        tasks = load_tasks()

        for task in tasks:
            if task.id == task_id:
                return task

        return None

    @staticmethod
    def update_task(
        task_id: str,
        **updates,
    ) -> bool:

        tasks = load_tasks()

        for task in tasks:

            if task.id == task_id:

                for key, value in updates.items():

                    if hasattr(task, key):
                        setattr(task, key, value)

                task.update_timestamp(current_datetime())

                save_tasks(tasks)

                return True

        return False

    @staticmethod
    def delete_task(task_id: str) -> bool:

        tasks = load_tasks()

        updated = [
            task
            for task in tasks
            if task.id != task_id
        ]

        if len(updated) == len(tasks):
            return False

        save_tasks(updated)

        return True

    @staticmethod
    def complete_task(task_id: str) -> bool:

        tasks = load_tasks()

        for task in tasks:

            if task.id == task_id:

                task.mark_completed(
                    current_datetime()
                )

                save_tasks(tasks)

                return True

        return False

    @staticmethod
    def update_overdue_tasks() -> None:

        tasks = load_tasks()

        changed = False

        for task in tasks:

            if (
                task.status == "Pending"
                and is_overdue(task.deadline)
            ):
                task.status = "Overdue"
                task.update_timestamp(
                    current_datetime()
                )
                changed = True

        if changed:
            save_tasks(tasks)