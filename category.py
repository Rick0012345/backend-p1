from dataclasses import dataclass, field
from typing import Optional, Dict
from datetime import datetime
from events.category_events import (
    CategoryCreated,
    CategoryUpdated,
    CategoryActivated,
    CategoryDeactivated
)

@dataclass
class Category:
    name: str
    description: Optional[str] = None
    is_active: bool = True
    id: str = field(default_factory=lambda: str(hash(datetime.now())))
    events: list = field(default_factory=list)

    def __post_init__(self):
        self.validate()
        self.events.append(
            CategoryCreated(
                category_id=self.id,
                name=self.name,
                description=self.description,
                is_active=self.is_active
            )
        )

    def validate(self):
        if not self.name:
            raise ValueError("Nome é obrigatório")
        if len(self.name) > 255:
            raise ValueError("Nome não pode ter mais que 255 caracteres")
        if self.description and len(self.description) > 1000:
            raise ValueError("Descrição não pode ter mais que 1000 caracteres")

    def update(self, name: Optional[str] = None, description: Optional[str] = None):
        changes: Dict[str, any] = {}
        if name is not None and name != self.name:
            changes["name"] = {"from": self.name, "to": name}
            self.name = name
        if description is not None and description != self.description:
            changes["description"] = {"from": self.description, "to": description}
            self.description = description
        
        if changes:
            self.validate()
            self.events.append(CategoryUpdated(category_id=self.id, changes=changes))

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.events.append(CategoryActivated(category_id=self.id))

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.events.append(CategoryDeactivated(category_id=self.id))

    def to_dict(self) -> dict:
        return {
            "class_name": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Category":
        if data.get("class_name") != cls.__name__:
            raise ValueError(f"Dados não pertencem à classe {cls.__name__}")
        
        return cls(
            id=data["id"],
            name=data["name"],
            description=data.get("description"),
            is_active=data["is_active"]
        )