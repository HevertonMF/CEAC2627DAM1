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


