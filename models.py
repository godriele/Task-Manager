from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from db import db 

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(20), nullable=False, unique=True)
    password = mapped_column(String(80), nullable=False)
    
    # -------- Relationship ------------
    tasks = relationship("Task", back_populates="user") 

class Task(db.Model):
    __tablename__ = 'tasks'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    
    user_id = mapped_column(Integer, ForeignKey('user.id'))  
    category_id = mapped_column(Integer, ForeignKey("category.id"))  
    
    # -------- Relationship ------------
    user = relationship("User", back_populates="tasks")  
    category = relationship("Category", back_populates="tasks")

class Category(db.Model):
    __tablename__ = 'category'
    
    id = mapped_column(Integer, primary_key=True)  
    name = mapped_column(String)
    
    task = relationship("Task", back_populates="category")
