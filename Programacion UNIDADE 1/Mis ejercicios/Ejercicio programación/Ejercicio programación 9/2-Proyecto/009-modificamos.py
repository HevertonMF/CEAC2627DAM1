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

# Pido qué bicicleta quiero cambiar y el precio nuevo
id = input("Id de la bicicleta: ")
precio = input("Nuevo precio: ")

# Cambio el precio
cursor.execute("UPDATE bicicletas SET precio = %s WHERE id = %s", (precio, id))

# Sin commit no se guarda
connection.commit()
print("Filas modificadas:", cursor.rowcount)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
