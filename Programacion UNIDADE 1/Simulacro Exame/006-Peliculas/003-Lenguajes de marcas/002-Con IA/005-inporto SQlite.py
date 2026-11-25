import sqlite3

conexion = sqlite3.connect("videoteca20261124.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()
cursor.execute("SELECT * FROM películas")

for fila in cursor.fetchall():
    print(dict(fila))

conexion.close()