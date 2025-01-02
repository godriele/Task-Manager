from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship
from db import db 

class User(db.Model):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    
    # -------- Relationship ------------
    task = relationship("Task", back_populates="users")
    
class Task(db.Model):
    __tablename__ = 'tasks'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    
    # -------- Relationship ------------
    users = relationship("User", back_populates="tasks")