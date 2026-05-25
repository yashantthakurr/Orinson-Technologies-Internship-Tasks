
from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    description: str | None = None
    status: str = "pending"

class TaskResponse(TaskCreate):
    id: int
    class Config:
        from_attributes = True
