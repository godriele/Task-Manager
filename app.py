from flask import Flask, render_template
from models import User
from db import db
from pathlib import Path

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)

app.instance_path = Path("data").resolve

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
	app.run(debug=True, port=3000)
