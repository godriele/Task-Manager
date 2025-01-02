from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship
from flask_login import UserMixin
from db import db 

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(20), nullable=False, unique=True)
    password = mapped_column(String(80), nullable=False)
    
    # -------- Relationship ------------
    task = relationship("Task", back_populates="users")
    
class Task(db.Model):
    __tablename__ = 'tasks'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    
    # -------- Relationship ------------
    users = relationship("User", back_populates="tasks")