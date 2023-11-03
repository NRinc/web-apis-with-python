from pydantic import BaseModel
from typing import NewType, Optional

# Declare a new type of variable ID
ID = NewType("ID", int)

class Task(BaseModel):
    """
    Definition of components of a task
    """
    summary: str
    priority: int

class TaskList(BaseModel):
    """
    Definition of the TaskList
    """
    id: ID
    task: Task
