import csv


@app.route('/upCsvFile', methods=['POST'])
def upCsvFile():
    openFile = request.files['inputFile']
    technicianFile = []

    if request.files['inputFile'].filename == '' or request.files['inputFile'].filename != '':
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
        db.session.add(technician)
        db.session.commit()

    flash('File was successfully loaded')

    return render('index.html')
    