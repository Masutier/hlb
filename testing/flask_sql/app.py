from flask import Flask
from dataBase.Models import db, Techs
from .imports.importCsv import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase/tech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def home():

    return '<h1>Hello to all</h1>'


@app.route('/techs')
def getTecnisians():
    tecnisians_all = Techs.query.all()

    return '<h1>Redy to show</h1>'
