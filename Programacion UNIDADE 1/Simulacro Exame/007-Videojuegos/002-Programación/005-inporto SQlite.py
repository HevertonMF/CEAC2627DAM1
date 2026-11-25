import sqlite3

conexion = sqlite3.connect("videojuegos20261125.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()
cursor.execute("SELECT * FROM videojuegos")

for fila in cursor.fetchall():
    print(dict(fila))

conexion.close()