from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
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
    
