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

# Pido los datos al usuario
nombre = input("Nombre de la bicicleta: ")
descripcion = input("Descripción: ")
precio = input("Precio: ")

# Inserto la bicicleta (los %s se rellenan con los datos)
cursor.execute(
  "INSERT INTO bicicletas (nombre, descripcion, precio) VALUES (%s, %s, %s)",
  (nombre, descripcion, precio)
)

# Sin commit no se guarda
connection.commit()
print("Bicicleta guardada con el id", cursor.lastrowid)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
