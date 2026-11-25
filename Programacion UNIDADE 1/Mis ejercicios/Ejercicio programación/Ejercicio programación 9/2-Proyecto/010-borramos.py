# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)

# Creo un cursor
cursor = connection.cursor()

# Pido qué bicicleta quiero borrar
id = input("Id de la bicicleta a borrar: ")

# La borro
cursor.execute("DELETE FROM bicicletas WHERE id = %s", (id,))

# Sin commit no se borra
connection.commit()
print("Filas borradas:", cursor.rowcount)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
