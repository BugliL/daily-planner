from dataclasses import Field
import enum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Priority(enum.Enum):
    HIGH = "HIGH"
    IMPORTANT = "IMPORTANT"
    LOW = "LOW"
    

class Task(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    completed: bool = False
    created_at: datetime = datetime.now()
    priority: Priority = Field(default=Priority.IMPORTANT)
