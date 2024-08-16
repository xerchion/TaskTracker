from datetime import datetime
from typing import Any

KINDS = ["", "todo", "in-progress", "done"]


class Task:

    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def get_id(self) -> Any:
        return self.id

    def get_description(self) -> str:
        return self.description

    def get_status(self) -> str:
        return self.status

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_updated_at(self) -> datetime:
        return self.updated_at

    def set_description(self, description: str) -> None:
        self.description = description

    def set_status(self, status: str) -> None:
        self.status = status

    def set_created_at(self, created_at: datetime) -> None:
        self.created_at = created_at

    def set_updated_at(self, updated_at: datetime) -> None:
        self.updated_at = updated_at

    def to_string(self) -> str:
        created_at_str = datetime.fromtimestamp(self.created_at).strftime(
            "%H:%M %d/%m/%Y"
        )
        updated_at_str = datetime.fromtimestamp(self.updated_at).strftime(
            "%H:%M %d/%m/%Y"
        )
        return (
            f"{str(self.id).ljust(5)}"
            f"{self.description.ljust(40)}"
            + str(self.status).ljust(13)
            + f"{created_at_str.ljust(20)}"
            f"{updated_at_str.ljust(20)}"
        )
