from ica_tool import app
from flask import render_template as render
from flask import flash, redirect, request, url_for, flash
from ica_tool.models import Technician


@app.route('/', methods=['GET', 'POST'])
def home():
    techs = Technician.query.all()
    departamentos = []

    if request.method == 'POST':
        incomming = request.form["depto"]
        techs = Technician.query.filter_by(departamentoPredio=incomming).all()
        return render('departamento.html', techs=techs)
    else:
        for tech in techs:
            if tech.departamentoPredio not in departamentos and tech.departamentoPredio and tech.departamentoPredio != "DEPARTAMENTOPREDIO":
                departamentos.append(tech.departamentoPredio)
        departamentos.sort()

        return render('index.html', departamentos=departamentos)
