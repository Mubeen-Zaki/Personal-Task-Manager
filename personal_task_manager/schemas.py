from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum
from typing import List

class Task(BaseModel):
    title: str
    description: str
    deadline: datetime
    completed: Optional[bool] = False

class User(BaseModel):
    username: str
    email: str
    password: str

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None

class Status(str, Enum):
    done = "completed"
    not_done = "not completed"

class ShowUser(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True

class ShowUserDetails(ShowUser):
    tasks: List[Task] = []

class Logger(BaseModel):
    user_id: int
    task_id: int
    title: str
    timestamp: datetime
    description: str

class ShowTask(Task):
    id: int
    user: ShowUser
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str]

class CurrentUser(User):
    id: int
    class Config:
        orm_mode = True