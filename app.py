from flask import Flask
from db import db
from pathlib import Path

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sample.db"
db.init_app(app)

app.instance_path = Path("data").resolve

if __name__ == "__main__":
	app.run(debug=True, port=3000)
