import sqlite3

conexion = sqlite3.connect("biblioteca20261123.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()
cursor.execute("SELECT * FROM libros")

for fila in cursor.fetchall():
    print(dict(fila))

conexion.close()