from flask import Flask, render_template
from models import User
from db import db
from pathlib import Path
# ---------------- Authentications ----------------------------
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
# ------------------------------------------------------------
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)

app.instance_path = Path("data").resolve

# ---------------- Authentications ----------------------------
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
		min=4, max=20)], render_kw={"placeholder": "username"})
    
    password = PasswordField(validators=[InputRequired(), Length(
		min=4, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Register")
    
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
			username=username.data).first()
        if existing_user_username:
            raise ValidationError(
				"That username already exists. Please choose a different name"
			)
            
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
		min=4, max=20)], render_kw={"placeholder": "username"})
    
    password = PasswordField(validators=[InputRequired(), Length(
		min=4, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Login")
    
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
			username=username.data).first()
        if existing_user_username:
            raise ValidationError(
				"That username already exists. Please choose a different name"
			)
# ------------------------------------------------------------- 
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
