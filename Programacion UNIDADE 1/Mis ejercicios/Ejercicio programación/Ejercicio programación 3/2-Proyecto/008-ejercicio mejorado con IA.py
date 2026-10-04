#Es un programa para inscribir a nuevos ciclistas en un equipo.
# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 2.1 By Heverton
"""

import os


# ------------------------------------------------------------------
# Códigos ANSI para dar color y estilo al texto en la terminal
# No necesitan ninguna librería externa, funcionan en la mayoría
# de terminales (Windows Terminal, macOS, Linux)
# ------------------------------------------------------------------
class Color:
    RESET = "\033[0m"
    NEGRITA = "\033[1m"
    CIAN = "\033[96m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    GRIS = "\033[90m"


# ------------------------------------------------------------------
# Excepción personalizada
# Creamos nuestra propia clase de error para cuando el usuario
# introduce un ID que no tiene sentido (negativo o cero).
# Hereda de Exception, que es la clase base de todos los errores.
# ------------------------------------------------------------------
class IDInvalidoError(Exception):
    """Se lanza cuando el ID introducido por el usuario no es válido (<= 0)"""
    pass


# Ancho fijo que usamos para las líneas separadoras y las tablas
ANCHO = 60


# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


def limpiar_pantalla():
    """
    Limpia la terminal para que el programa se vea más ordenado
    (funciona tanto en Windows como en macOS/Linux)
    """
    os.system("cls" if os.name == "nt" else "clear")


def linea(caracter="─"):
    """
    Imprime una línea separadora del ancho definido arriba,
    para dividir visualmente las secciones del programa
    """
    print(Color.GRIS + caracter * ANCHO + Color.RESET)


def titulo(texto):
    """
    Imprime un título centrado, con color y rodeado de una caja simple
    """
    print(Color.CIAN + "╔" + "═" * (ANCHO - 2) + "╗" + Color.RESET)
    print(Color.CIAN + "║" + Color.RESET + texto.center(ANCHO - 2) + Color.CIAN +"║" + Color.RESET)
    print(Color.CIAN + "╚" + "═" * (ANCHO - 2) + "╝" + Color.RESET)


def mensaje_exito(texto):
    """Imprime un mensaje de éxito en verde, con un icono de check"""
    print(Color.VERDE + "✔ " + texto + Color.RESET)


def mensaje_error(texto):
    """Imprime un mensaje de error en rojo, con un icono de aviso"""
    print(Color.ROJO + "✘ " + texto + Color.RESET)


def mensaje_info(texto):
    """Imprime un mensaje informativo en amarillo"""
    print(Color.AMARILLO + "ℹ " + texto + Color.RESET)


def pausar():
    """Pausa el programa hasta que el usuario pulse Enter, para que pueda leer el resultado"""
    input(Color.GRIS + "\nPulsa Enter para continuar..." + Color.RESET)


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
        mensaje_error("El ID debe ser un número.")
        return None

    except IDInvalidoError as error:
        # Esto ocurre si el número es válido pero no tiene sentido como ID
        mensaje_error(str(error))
        return None


def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    limpiar_pantalla()
    titulo("🚴  INSERTAR NUEVO CICLISTA")
    print()

    nombre = input(Color.NEGRITA + "Nombre: " + Color.RESET)
    apellidos = input(Color.NEGRITA + "Apellidos: " + Color.RESET)
    fecha_nacimiento = input(Color.NEGRITA + "Fecha de nacimiento (DD-MM-AAAA): " + Color.RESET)
    email = input(Color.NEGRITA + "Email: " + Color.RESET)
    telefono = input(Color.NEGRITA + "Teléfono: " + Color.RESET)

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

    print()
    mensaje_exito(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1

    # Otra aserción: el contador siempre debe quedar en 1 o más.
    # Si esto fallara, algo estaría muy mal en la lógica del programa.
    assert siguiente_id >= 1, "El contador de IDs no puede ser menor que 1"

    pausar()


def listar_ciclistas():
    """
    READ - Muestra todos los ciclistas registrados en formato de tabla
    """
    limpiar_pantalla()
    titulo("📋  LISTA DE CICLISTAS")
    print()

    # Si la lista está vacía, avisamos al usuario
    if len(ciclistas) == 0:
        mensaje_info("No hay ciclistas registrados todavía.")
        pausar()
        return

    # Cabecera de la tabla, en negrita y color
    cabecera = f"{'ID':<4}{'NOMBRE':<20}{'EMAIL':<25}{'TELÉFONO':<12}"
    print(Color.AZUL + Color.NEGRITA + cabecera + Color.RESET)
    linea()

    # Recorremos la lista y mostramos los datos de cada ciclista en una fila
    for ciclista in ciclistas:
        nombre_completo = f"{ciclista['nombre']} {ciclista['apellidos']}"
        fila = (
            f"{ciclista['id']:<4}"
            f"{nombre_completo:<20}"
            f"{ciclista['email']:<25}"
            f"{ciclista['telefono']:<12}"
        )
        print(fila)

    linea()
    print(Color.GRIS + f"Total: {len(ciclistas)} ciclista(s)" + Color.RESET)
    pausar()


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
    limpiar_pantalla()
    titulo("✏️  ACTUALIZAR CICLISTA")
    print()

    # Si no hay ciclistas, no tiene sentido continuar
    if len(ciclistas) == 0:
        mensaje_info("No hay ciclistas registrados todavía.")
        pausar()
        return

    # Mostramos una lista rápida de IDs disponibles para orientar al usuario
    for ciclista in ciclistas:
        print(Color.GRIS + f"  {ciclista['id']}. {ciclista['nombre']} {ciclista['apellidos']}" + Color.RESET)
    print()

    # Usamos la función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a actualizar: ")

    # Si hubo cualquier error (conversión o ID inválido), salimos de la función
    if id_buscado is None:
        pausar()
        return

    # Buscamos el ciclista con ese ID
    ciclista = buscar_ciclista_por_id(id_buscado)

    # Si no existe, avisamos y salimos de la función
    if ciclista is None:
        mensaje_error(f"No existe ningún ciclista con el ID {id_buscado}")
        pausar()
        return

    print()
    mensaje_info("Deja el campo en blanco y pulsa Enter si no quieres cambiarlo.")
    print()

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

    print()
    mensaje_exito("Ciclista actualizado con éxito.")
    pausar()


def eliminar_ciclista():
    """
    DELETE - Busca un ciclista por ID y lo elimina de la lista
    """
    limpiar_pantalla()
    titulo("🗑️  ELIMINAR CICLISTA")
    print()

    if len(ciclistas) == 0:
        mensaje_info("No hay ciclistas registrados todavía.")
        pausar()
        return

    # Mostramos una lista rápida de IDs disponibles para orientar al usuario
    for ciclista in ciclistas:
        print(Color.GRIS + f"  {ciclista['id']}. {ciclista['nombre']} {ciclista['apellidos']}" + Color.RESET)
    print()

    # Usamos la misma función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a eliminar: ")

    if id_buscado is None:
        pausar()
        return

    ciclista = buscar_ciclista_por_id(id_buscado)

    if ciclista is None:
        mensaje_error(f"No existe ningún ciclista con el ID {id_buscado}")
        pausar()
        return

    # Pedimos confirmación antes de borrar, para evitar borrados accidentales
    print()
    confirmacion = input(
        Color.AMARILLO
        + f"¿Seguro que quieres eliminar a {ciclista['nombre']} {ciclista['apellidos']}? (s/n): "
        + Color.RESET
    )

    print()
    if confirmacion.lower() == "s":
        # Cuántos ciclistas había antes de borrar, para comprobarlo después
        total_antes = len(ciclistas)

        # Quitamos el ciclista de la lista
        ciclistas.remove(ciclista)

        # Aserción: comprobamos que la lista realmente se quedó con un
        # elemento menos. Si no fuera así, habría un error de lógica.
        assert len(ciclistas) == total_antes - 1, "La lista no se actualizó correctamente al eliminar"

        mensaje_exito("Ciclista eliminado con éxito.")
    else:
        mensaje_info("Operación cancelada.")

    pausar()


def menu_principal():
    """
    Función principal - Muestra el menú y controla el bucle del programa
    """
    # Bucle infinito: el programa sigue funcionando hasta que el usuario decida salir
    while True:
        limpiar_pantalla()
        titulo("🚴  REGISTRO DE CICLISTAS  v2.1 By Heverton")
        print()
        print(Color.NEGRITA + "  1." + Color.RESET + " 🆕  Insertar un ciclista")
        print(Color.NEGRITA + "  2." + Color.RESET + " 📋  Listar los ciclistas")
        print(Color.NEGRITA + "  3." + Color.RESET + " ✏️   Actualizar un ciclista")
        print(Color.NEGRITA + "  4." + Color.RESET + " 🗑️   Eliminar un ciclista")
        print(Color.NEGRITA + "  5." + Color.RESET + " 🚪  Salir")
        print()
        linea()

        opcion = input(Color.MAGENTA + "Escoge una opción: " + Color.RESET)

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
            limpiar_pantalla()
            print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
            break  # Rompe el bucle y termina el programa
        else:
            mensaje_error("Opción no válida, inténtalo de nuevo.")
            pausar()


# Este bloque solo se ejecuta si el archivo se corre directamente
# (y no si se importa desde otro programa)
if __name__ == "__main__":
    menu_principal()
