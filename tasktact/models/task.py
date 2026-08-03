"""
Task model for TaskTact.
"""

from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Task:
    """
    Represents a single task.
    """

    id: str
    title: str
    description: str
    category: str
    priority: str
    deadline: str
    status: str = "Pending"

    created_at: str = ""
    updated_at: str = ""
    completed_at: Optional[str] = None

    tags: list[str] = field(default_factory=list)

    def mark_completed(self, completed_time: str) -> None:
        """
        Mark the task as completed.
        """
        self.status = "Completed"
        self.completed_at = completed_time
        self.updated_at = completed_time

    def update_timestamp(self, updated_time: str) -> None:
        """
        Update the last modified timestamp.
        """
        self.updated_at = updated_time

    def to_dict(self) -> dict:
        """
        Convert Task object to dictionary.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Task object from a dictionary.
        """
        return cls(**data)

    def __str__(self) -> str:
        return (
            f"{self.id} | "
            f"{self.title} | "
            f"{self.category} | "
            f"{self.priority} | "
            f"{self.status}"
        )