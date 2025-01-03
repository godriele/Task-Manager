from flask import Flask, render_template, redirect, url_for
from models import User
from db import db
from pathlib import Path
# ---------------- Authentications ----------------------------
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_login import login_user, LoginManager, login_required, logout_user

# ------------------------------------------------------------
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = 'secret'

# Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirects to login page if not logged in

# This function loads the user by their ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Hashing
bcrypt = Bcrypt(app)
db.init_app(app)

app.instance_path = Path("data").resolve

# ---------------- Authentications ----------------------------
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

# ------------------------------------------------------------- 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)  
            return redirect(url_for('dashboard'))  
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required  
def dashboard():
    return render_template("dashboard.html")

@app.route('/logout')
@login_required  
def logout():
    logout_user()  
    return redirect(url_for('home'))  

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
