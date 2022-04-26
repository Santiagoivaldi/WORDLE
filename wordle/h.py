import sqlite3
f = open("palabras.txt", "r")
h = (f.readline())


conexion=sqlite3.connect("banana.db")
try:
    conexion.execute("""create table Palabras (
                              id integer primary key autoincrement,
                              palabra text,
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    

f = open("palabras.txt", "r")
for linea in f:
    qry = f"INSERT INTO Palabras (palabra) VALUES('{linea[:-1]}');"
    conexion.execute(qry)
    conexion.commit()

conexion.close()

