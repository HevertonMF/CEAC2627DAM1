# Primero presento el programa
# CRUD = Create, Read, Update, Delete
# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
"""
  Programa CRUD
  Versión 0.1
  por Heverton Marques
"""
# Mensaje de bienvenida
"""
print("Registro de Ciclistas")
print("Versión 1.0 By Heverton")
"""
# Entrar en un bucle infinito
while True:
  # Le enseño al usuario lo que puede hacer
	print("1.-Insertar un registro")
  print("2.-Leer los registros")
  print("3.-Actualizar un registro")
  print("4.-Eliminar un registro")
  # Le pregunto qué quiere hacer
	 if opcion == "1":
            insertar_ciclista()
        elif opcion == "2":
            listar_ciclistas()
        elif opcion == "3":
            actualizar_ciclista()
        elif opcion == "4":
            eliminar_ciclista()
        elif opcion == "5":
            limpiar_pantalla()
            print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
            break  # Rompe el bucle y termina el programa
        else:
            mensaje_error("Opción no válida, inténtalo de nuevo.")
            pausar()
  # Anoto su decisión y tomo una acción - la acción puede ser
def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    print("\n--- Insertar nuevo ciclista ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    # Creamos un diccionario con los datos del nuevo ciclista
    nuevo_ciclista = {
        "id": siguiente_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "fecha_nacimiento": fecha_nacimiento,
        "email": email,
        "telefono": telefono,
    }

    # Añadimos el nuevo ciclista a la lista
    ciclistas.append(nuevo_ciclista)

    print(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1


def listar_ciclistas():
    """
    READ - Muestra todos los ciclistas registrados
    """
    print("\n--- Lista de ciclistas ---")

    # Si la lista está vacía, avisamos al usuario
    if len(ciclistas) == 0:
        print("No hay ciclistas registrados todavía.")
        return

    # Recorremos la lista y mostramos los datos de cada ciclista
    for ciclista in ciclistas:
        print(f"ID: {ciclista['id']}")
        print(f"  Nombre: {ciclista['nombre']} {ciclista['apellidos']}")
        print(f"  Fecha de nacimiento: {ciclista['fecha_nacimiento']}")
        print(f"  Email: {ciclista['email']}")
        print(f"  Teléfono: {ciclista['telefono']}")
        print("-" * 30)


def buscar_ciclista_por_id(id_buscado):
    """
    Función auxiliar (no es parte del menú) que busca un ciclista por su ID
    y devuelve el diccionario correspondiente, o None si no lo encuentra
    """
    for ciclista in ciclistas:
        if ciclista["id"] == id_buscado:
            return ciclista
    return None


def actualizar_ciclista():
    """
    UPDATE - Busca un ciclista por ID y actualiza sus datos
    """
    print("\n--- Actualizar ciclista ---")

    # Primero mostramos la lista para que el usuario sepa qué ID escoger
    listar_ciclistas()

    try:
        id_buscado = int(input("Introduce el ID del ciclista a actualizar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    # Buscamos el ciclista con ese ID
    ciclista = buscar_ciclista_por_id(id_buscado)

    # Si no existe, avisamos y salimos de la función
    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    print("Deja el campo en blanco y pulsa Enter si no quieres cambiarlo.")

    # Pedimos los nuevos datos; si el usuario no escribe nada, mantenemos el valor actual
    nuevo_nombre = input(f"Nombre ({ciclista['nombre']}): ")
    nuevo_apellidos = input(f"Apellidos ({ciclista['apellidos']}): ")
    nueva_fecha = input(f"Fecha de nacimiento ({ciclista['fecha_nacimiento']}): ")
    nuevo_email = input(f"Email ({ciclista['email']}): ")
    nuevo_telefono = input(f"Teléfono ({ciclista['telefono']}): ")

    # Solo actualizamos el campo si el usuario escribió algo nuevo
    if nuevo_nombre != "":
        ciclista["nombre"] = nuevo_nombre
    if nuevo_apellidos != "":
        ciclista["apellidos"] = nuevo_apellidos
    if nueva_fecha != "":
        ciclista["fecha_nacimiento"] = nueva_fecha
    if nuevo_email != "":
        ciclista["email"] = nuevo_email
    if nuevo_telefono != "":
        ciclista["telefono"] = nuevo_telefono

    print("Ciclista actualizado con éxito.")


def eliminar_ciclista():
    """
    DELETE - Busca un ciclista por ID y lo elimina de la lista
    """
    print("\n--- Eliminar ciclista ---")

    # Mostramos la lista para que el usuario sepa qué ID eliminar
    listar_ciclistas()

    try:
        id_buscado = int(input("Introduce el ID del ciclista a eliminar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    ciclista = buscar_ciclista_por_id(id_buscado)

    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    # Pedimos confirmación antes de borrar, para evitar borrados accidentales
    confirmacion = input(
        f"¿Seguro que quieres eliminar a {ciclista['nombre']} {ciclista['apellidos']}? (s/n): "
    )

    if confirmacion.lower() == "s":
        # Quitamos el ciclista de la lista
        ciclistas.remove(ciclista)
        print("Ciclista eliminado con éxito.")
    else:
        print("Operación cancelada.")


def menu_principal():
    """
    Función principal - Muestra el menú y controla el bucle del programa
    """
    print("Registro de Ciclistas")
    print("Versión 1.0 By Heverton")



 
