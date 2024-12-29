from .database import Base
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    deadline = Column(DateTime)
    completed = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    
    tasks = relationship("Tasks", back_populates="user")