# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 1.1 By Heverton
"""

# ------------------------------------------------------------------
# Excepción personalizada
# Creamos nuestra propia clase de error para cuando el usuario
# introduce un ID que no tiene sentido (negativo o cero).
# Hereda de Exception, que es la clase base de todos los errores.
# ------------------------------------------------------------------
class IDInvalidoError(Exception):
    """Se lanza cuando el ID introducido por el usuario no es válido (<= 0)"""
    pass


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

    # Aserción: comprobamos, durante el desarrollo, que el diccionario
    # que acabamos de crear tiene realmente el ID que esperábamos.
    # Si esto fallara alguna vez, sería un error de lógica en el programa,
    # no un error del usuario.
    assert nuevo_ciclista["id"] == siguiente_id, "El ID del nuevo ciclista no coincide con el contador"

    # Añadimos el nuevo ciclista a la lista
    ciclistas.append(nuevo_ciclista)

    print(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1

    # Otra aserción: el contador siempre debe quedar en 1 o más.
    # Si esto fallara, algo estaría muy mal en la lógica del programa.
    assert siguiente_id >= 1, "El contador de IDs no puede ser menor que 1"


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


def pedir_id_valido(mensaje):
    """
    Función auxiliar que pide un ID al usuario, lo convierte a número,
    y lanza nuestra excepción personalizada si el ID no es válido
    (negativo o cero). Devuelve el ID ya validado, o None si hubo
    algún error (ya sea de conversión o de valor).
    """
    try:
        id_introducido = int(input(mensaje))

        # Si el ID no es positivo, lanzamos nuestra propia excepción
        if id_introducido <= 0:
            raise IDInvalidoError(f"El ID {id_introducido} no es válido, debe ser mayor que 0")

        return id_introducido

    except ValueError:
        # Esto ocurre si el usuario escribe una letra en vez de un número
        print("El ID debe ser un número.")
        return None

    except IDInvalidoError as error:
        # Esto ocurre si el número es válido pero no tiene sentido como ID
        print(f"Error: {error}")
        return None


def actualizar_ciclista():
    """
    UPDATE - Busca un ciclista por ID y actualiza sus datos
    """
    print("\n--- Actualizar ciclista ---")

    # Primero mostramos la lista para que el usuario sepa qué ID escoger
    listar_ciclistas()

    # Usamos la función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a actualizar: ")

    # Si hubo cualquier error (conversión o ID inválido), salimos de la función
    if id_buscado is None:
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

    # Usamos la misma función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a eliminar: ")

    if id_buscado is None:
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
        # Cuántos ciclistas había antes de borrar, para comprobarlo después
        total_antes = len(ciclistas)

        # Quitamos el ciclista de la lista
        ciclistas.remove(ciclista)

        # Aserción: comprobamos que la lista realmente se quedó con un
        # elemento menos. Si no fuera así, habría un error de lógica.
        assert len(ciclistas) == total_antes - 1, "La lista no se actualizó correctamente al eliminar"

        print("Ciclista eliminado con éxito.")
    else:
        print("Operación cancelada.")


def menu_principal():
    """
    Función principal - Muestra el menú y controla el bucle del programa
    """
    print("Registro de Ciclistas")
    print("Versión 1.1 by Heverton")

    # Bucle infinito: el programa sigue funcionando hasta que el usuario decida salir
    while True:
        print("\n=== MENÚ ===")
        print("1.- Insertar un ciclista")
        print("2.- Listar los ciclistas")
        print("3.- Actualizar un ciclista")
        print("4.- Eliminar un ciclista")
        print("5.- Salir")

        opcion = input("Escoge una opción: ")

        # Según la opción elegida, llamamos a la función correspondiente
        if opcion == "1":
            insertar_ciclista()
        elif opcion == "2":
            listar_ciclistas()
        elif opcion == "3":
            actualizar_ciclista()
        elif opcion == "4":
            eliminar_ciclista()
        elif opcion == "5":
            print("¡Hasta luego!")
            break  # Rompe el bucle y termina el programa
        else:
            print("Opción no válida, inténtalo de nuevo.")


# Este bloque solo se ejecuta si el archivo se corre directamente
# (y no si se importa desde otro programa)
if __name__ == "__main__":
    menu_principal()
