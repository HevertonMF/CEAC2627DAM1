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

# Bucle infinito con el menú
while True:
  print("")
  print("===== TIENDA DE BICICLETAS =====")
  print("1. Ver todas las bicicletas")
  print("2. Añadir una bicicleta")
  print("3. Cambiar el precio de una bicicleta")
  print("4. Borrar una bicicleta")
  print("5. Salir")
  opcion = input("Elige una opción: ")

    # 1. Leer (SELECT)
  if opcion == "1":
    cursor.execute("SELECT * FROM bicicletas")
    filas = cursor.fetchall()
    for fila in filas:
      print(fila[0], "-", fila[1], "-", fila[2], "-", fila[3], "€")
    input("Pulsa Enter para volver al menú...")   # Espera antes de volver al menú

  # 2. Guardar (INSERT)
  elif opcion == "2":
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = input("Precio: ")
    cursor.execute(
      "INSERT INTO bicicletas (nombre, descripcion, precio) VALUES (%s, %s, %s)",
      (nombre, descripcion, precio)
    )
    connection.commit()      # Sin commit no se guarda
    print("Bicicleta añadida")

  # 3. Modificar (UPDATE)
  elif opcion == "3":
    id = input("Id de la bicicleta: ")
    precio = input("Nuevo precio: ")
    cursor.execute("UPDATE bicicletas SET precio = %s WHERE id = %s", (precio, id))
    connection.commit()
    print("Filas modificadas:", cursor.rowcount)

  # 4. Borrar (DELETE)
  elif opcion == "4":
    id = input("Id de la bicicleta a borrar: ")
    cursor.execute("DELETE FROM bicicletas WHERE id = %s", (id,))
    connection.commit()
    print("Filas borradas:", cursor.rowcount)

  # 5. Salir del bucle
  elif opcion == "5":
    print("Adiós")
    break

  else:
    print("Opción no válida")

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
