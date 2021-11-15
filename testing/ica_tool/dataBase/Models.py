from ica_tool import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tech.db'
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

