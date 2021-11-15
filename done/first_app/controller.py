import csv
import os
from datetime import datetime
from flask import render_template as render
from flask import Flask, redirect, request
from flask_sqlalchemy import SQLAlchemy
from models import Student
from send_mail import sendMail

app=Flask(__name__)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


# CSV FILE
if not os.path.exists("students.csv"):
    fieldnames = ["name", "email", "dorm"]
    file = open("students.csv", "a")
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    file.close()


@app.route('/')
def home():
    return render('index.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    dorm = request.form.get("dorm")
    if not name or not email or not dorm:
        return render("partials/failure.html")

    students = Student.query.order_by(Student.date_created).all()
    for student in students:
        if email == student.email:
            return render("partials/email_exist.html")
    
    # SEND MAIL
    SUBJECT = "From my first App"
    TEXT = "You are registered!"
    #sendMail(SUBJECT, email, TEXT)

    # RECORD ON FILE IN HARD DRIVE
    file = open("students.csv", "a")
    writer = csv.writer(file)
    writer.writerow((name, email, dorm))
    file.close()

    # RECORD INFO IN db USING sqlite3
    db.session.add(Student(request.form['name'], request.form['email'], request.form['dorm']))
    db.session.commit()
    return redirect("/studentList")


@app.route('/studentList')
def studentList():
    students = Student.query.order_by(Student.date_created).all()

    return render('studentList.html', students=students)


@app.route('/studentsCsv')
def studentsCsv():
    students = []
    with open("students.csv", "r") as studentsList:
        print(studentsList)
        studentsRead = csv.reader(studentsList)

        next(studentsRead)

        for student in studentsRead:
            students.append(student)

    return render('studentsCsv.html', students=students)


@app.route('/update/<int:id>', methods=['get', 'POST'])
def update(id):
    to_update = Student.query.filter_by(id=id).first_or_404(id)
    if request.method == 'POST':
        to_update.name = request.form.get("name")
        to_update.email = request.form.get("email")
        to_update.dorm = request.form.get("dorm")
    
        db.session.update(Student(request.form['name'], request.form['email'], request.form['dorm']))
        db.session.commit()
        return redirect('/studentList')
    else:
        return render('update.html', to_update=to_update)


@app.route('/delete/<id>')
def delete(id):
    print(id)
    to_delete = Student.query.filter_by(id=int(id)).delete()

    db.session.commit()
    return redirect('/studentList')


if __name__ == '__main__':
    db.create_all()
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True, host="0.0.0.0")
