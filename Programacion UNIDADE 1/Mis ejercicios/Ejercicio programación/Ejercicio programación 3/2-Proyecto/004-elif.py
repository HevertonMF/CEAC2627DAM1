# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 1.0 By Heverton
"""

# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


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

