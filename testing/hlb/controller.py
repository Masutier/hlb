import csv
import os
import operator
from datetime import datetime
from flask import render_template as render
from flask import Flask, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProductor = db.Column(db.Integer)
    nombreProductor = db.Column(db.String(100))
    nombrePredio = db.Column(db.String(100))
    departamentoPredio = db.Column(db.String(50))
    municipioPredio = db.Column(db.String(50))
    nombreFacilitador = db.Column(db.String(100))
    departamentoContratista = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, idProductor, nombreProductor, nombrePredio, departamentoPredio
                    ,municipioPredio, nombreFacilitador, departamentoContratista):
        self.idProductor = idProductor
        self.nombreProductor = nombreProductor
        self.nombrePredio = nombrePredio
        self.departamentoPredio = departamentoPredio
        self.municipioPredio = municipioPredio
        self.nombreFacilitador = nombreFacilitador
        self.departamentoContratista = departamentoContratista
        

@app.route('/', methods=['GET', 'POST'])
def home():
    techs = Technician.query.all()
    departamentos = []

    if request.method == 'POST':
        incomming = request.form["depto"]
        print(incomming)
        techs = Technician.query.filter_by(departamentoPredio=incomming).all()
        return render('departamento.html', techs=techs, incomming=incomming)
    else:
        for tech in techs:
            if tech.departamentoPredio not in departamentos and tech.departamentoPredio and tech.departamentoPredio != "DEPARTAMENTOPREDIO":
                departamentos.append(tech.departamentoPredio)
        departamentos.sort()

        return render('index.html', departamentos=departamentos)


@app.route('/upCsvFile', methods=['POST'])
def upCsvFile():
    openFile = request.files['inputFile']
    technicianFile = []

    if request.files['inputFile'].filename == '':
        flash('No File or wrong extenssion ".csv"')
        return redirect(url_for("/"))
    else:

        with open(openFile.filename, "r") as techList:
            techRead = csv.reader(techList)

            for tech in techRead:
                technicianFile.append(tech)

        techList.close()

    for item in technicianFile:
        technician = Technician(idProductor=item[0], nombreProductor=item[3]
        , nombrePredio=item[25], departamentoPredio=item[36]
        , municipioPredio=item[37], nombreFacilitador=item[40]
        , departamentoContratista=item[41])
        # db.session.add(technician)
        # db.session.commit()

    flash('File was successfully loaded')

    return render('index.html')


if __name__ == '__main__':
    app.run(debug=True)
