from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase/tech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def main():

    return '<h1>Hello to all</h1>'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
