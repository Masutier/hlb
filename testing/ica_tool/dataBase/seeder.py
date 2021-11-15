import sqlite3 as sql

DB_PATH = "/home/gabriel/prog/webpages/flask/ica_tool/dataBase/tech.db"

def create_db():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Technician (
        id integer
        , idProductor integer)
        , nombreProductor text
        , nombrePredio text
        , departamentoPredio text
        , municipioPredio text
        , nombreFacilitador text
        , departamentoContratista text
    )""")
    conn.commit()
    conn.close()



