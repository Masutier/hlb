from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Technician

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def techniciansAll(incomming):
    technics = NewTechnician.query.filter_by(departamentoPredio=incomming).all()
    technicians = []

    for tech in technics:
        if tech.nombreFacilitador not in technicians:
            technicians.append(tech.nombreFacilitador)
    technicians.sort()

    return technicians
