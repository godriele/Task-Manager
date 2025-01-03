from sqlalchemy import Integer, String, ForeignKey, Text
from sqlalchemy.orm import mapped_column, relationship
from flask_login import UserMixin
from db import db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(20), nullable=False, unique=True)
    password = mapped_column(String(80), nullable=False)
    
    # -------- Relationship ------------
    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan") 


class Task(db.Model):
    __tablename__ = 'tasks'
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(100), nullable=False)  
    description = mapped_column(Text, nullable=False)
    
    user_id = mapped_column(Integer, ForeignKey('user.id'), nullable=False)  
    category_id = mapped_column(Integer, ForeignKey("category.id"), nullable=True)  
    
    # -------- Relationship ------------
    user = relationship("User", back_populates="tasks")  
    category = relationship("Category", back_populates="tasks", lazy="joined")


class Category(db.Model):
    __tablename__ = 'category'
    
    id = mapped_column(Integer, primary_key=True)  
    name = mapped_column(String(50), nullable=False, unique=True)
    
    # -------- Relationship ------------
    tasks = relationship("Task", back_populates="category")
