from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str]

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

class TodoResponse(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
