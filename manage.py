from models import User
from app import app
from db import db

#Drop all tables from the database
def drop_all():
    with app.app_context():
        # Will drop all tables
        db.drop_all()
    print("Dropped Table")

# aWDw
#Create all tables in the database
def create_all():
    with app.app_context(): 
        # Will create all tables (and the sqllite database if it doesnt exist)
        db.create_all()
    print("Created Table")

if __name__ == "__main__": 
    drop_all()
    create_all()