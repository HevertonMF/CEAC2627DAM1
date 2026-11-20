import sqlite3

conexion = sqlite3.connect("examendamceac2627.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()
cursor.execute("SELECT * FROM Médicos")

for fila in cursor.fetchall():
    print(dict(fila))

conexion.close()