import sqlite3 as sql

DB_PATH = "/home/gabriel/prog/webpages/flask/flask_sql/dataBase/tech.db"

def create_db():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE techs (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        , idProductor integer
        , nombreProductor TEXT
        , nombrePredio TEXT
        , departamentoPredio TEXT
        , municipioPredio TEXT
        , nombreFacilitador TEXT
        , date_created TIMESTAMP
    )""")
    conn.commit()
    conn.close()

