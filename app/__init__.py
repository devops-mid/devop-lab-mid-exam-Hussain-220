from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-2022220'  # Add this for flash messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes, models