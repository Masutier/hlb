from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    dorm = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, dorm):
        self.name = name
        self.email = email
        self.dorm = dorm
