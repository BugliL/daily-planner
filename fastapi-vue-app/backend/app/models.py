from dataclasses import Field
import enum
import uuid
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime


class Priority(enum.Enum):
    HIGH = "HIGH"
    IMPORTANT = "IMPORTANT"
    LOW = "LOW"

    

class Task(BaseModel):
    id: Optional[str] = Field(default_factory=uuid.uuid4)
    title: Optional[str] = None
    completed: bool = False
    created_at: datetime = datetime.now()
    priority: Priority = Field(default=Priority.IMPORTANT)
    

class Note(BaseModel):
    id: Optional[str] = None
    content: str
    created_at: datetime = datetime.now()
    
class Day(BaseModel):
    day: date 
    tasks: list[Task] = Field(default_factory=list)
    note: Optional[Note] = None

