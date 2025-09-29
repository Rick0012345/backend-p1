from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict

@dataclass
class CategoryCreated:
    category_id: str
    name: str
    description: Optional[str] = None
    is_active: bool = True
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class CategoryUpdated:
    category_id: str
    changes: Dict[str, any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class CategoryActivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class CategoryDeactivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.now)