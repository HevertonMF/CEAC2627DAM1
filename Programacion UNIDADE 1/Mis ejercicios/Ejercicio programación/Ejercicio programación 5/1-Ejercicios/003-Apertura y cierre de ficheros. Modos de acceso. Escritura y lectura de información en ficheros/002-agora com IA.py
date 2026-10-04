"""
Programa registro de ciclistas
Versión 0.3 
por Heverton Marques
"""

import os


# ------------------------------------------------------------------
# Códigos ANSI para dar color y estilo al texto en la terminal
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


# Nombre del archivo donde se guardan los ciclistas
ARCHIVO = "agenda.csv"

# Ancho fijo para las cajas y las líneas
ANCHO = 64


def limpiar_pantalla():
    """Limpia la terminal (funciona en Windows, macOS y Linux)"""
    os.system("cls" if os.name == "nt" else "clear")


def linea():
    """Imprime una línea separadora"""
    print(Color.GRIS + "─" * ANCHO + Color.RESET)


def titulo(texto):
    """Imprime un título centrado dentro de una caja de color"""
    print(Color.CIAN + "╔" + "═" * (ANCHO - 2) + "╗" + Color.RESET)
    print(Color.CIAN + "║" + Color.RESET + texto.center(ANCHO - 2) + Color.CIAN + "║" + Color.RESET)
    print(Color.CIAN + "╚" + "═" * (ANCHO - 2) + "╝" + Color.RESET)


def mensaje_exito(texto):
    print(Color.VERDE + "✔ " + texto + Color.RESET)


def mensaje_error(texto):
    print(Color.ROJO + "✘ " + texto + Color.RESET)


def mensaje_info(texto):
    print(Color.AMARILLO + "ℹ " + texto + Color.RESET)


def pausar():
    """Espera a que el usuario pulse Enter para poder leer el resultado"""
    input(Color.GRIS + "\nPulsa Enter para continuar..." + Color.RESET)


def limpiar_campo(texto):
    """
    Quita las comas del texto escrito por el usuario.
    Así no se rompe el formato del CSV (que separa los campos con comas).
    """
    return texto.replace(",", " ").strip()


def insertar_registro():
    """Pide los datos de un ciclista y los guarda al final del archivo"""
    limpiar_pantalla()
    titulo("🚴  INSERTAR NUEVO CICLISTA")
    print()

    nombre = limpiar_campo(input(Color.NEGRITA + "Nombre: " + Color.RESET))
    apellidos = limpiar_campo(input(Color.NEGRITA + "Apellidos: " + Color.RESET))
    telefono = limpiar_campo(input(Color.NEGRITA + "Teléfono: " + Color.RESET))
    categoria_bicicleta = limpiar_campo(
        input(Color.NEGRITA + "Categoría de bicicleta (montaña, carretera...): " + Color.RESET)
    )

    # No guardamos registros sin nombre
    if nombre == "":
        print()
        mensaje_error("El nombre es obligatorio. No se guardó nada.")
        pausar()
        return

    # Modo "a" = append: añade al final sin borrar lo que ya había
    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.write(nombre + "," + apellidos + "," + telefono + "," + categoria_bicicleta + "\n")
    archivo.close()

    print()
    mensaje_exito(f"Ciclista '{nombre} {apellidos}' guardado con éxito.")
    pausar()


def listar_registros():
    """Muestra todos los ciclistas guardados en formato de tabla"""
    limpiar_pantalla()
    titulo("📋  LISTADO DE CICLISTAS")
    print()

    # Si el archivo todavía no existe, avisamos en vez de dar error
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
    except FileNotFoundError:
        mensaje_info("Todavía no hay registros. Inserta el primero desde el menú.")
        pausar()
        return

    lineas = archivo.readlines()
    archivo.close()

    if len(lineas) == 0:
        mensaje_info("El archivo está vacío.")
        pausar()
        return

    # Cabecera de la tabla
    cabecera = f"{'Nº':<4}{'NOMBRE':<30}{'TELÉFONO':<14}{'CATEGORÍA':<16}"
    print(Color.AZUL + Color.NEGRITA + cabecera + Color.RESET)
    linea()

    numero = 1
    for registro in lineas:
        # Separamos los campos por coma y rellenamos si falta alguno
        campos = registro.strip().split(",")
        while len(campos) < 4:
            campos.append("")

        nombre_completo = f"{campos[0]} {campos[1]}"

        # Si el nombre es demasiado largo, lo cortamos para no romper la tabla
        if len(nombre_completo) > 28:
            nombre_completo = nombre_completo[:27] + "…"

        print(f"{numero:<4}{nombre_completo:<30}{campos[2]:<14}{campos[3]:<16}")
        numero += 1

    linea()
    print(Color.GRIS + f"Total: {len(lineas)} ciclista(s)" + Color.RESET)
    pausar()


def menu():
    """Muestra el menú principal y repite hasta que el usuario decida salir"""
    while True:
        limpiar_pantalla()
        titulo("🚴  REGISTRO DE CICLISTAS  v0.3")
        print(Color.GRIS + "por Heverton Marques".center(ANCHO) + Color.RESET)
        print()
        print(Color.NEGRITA + "  1." + Color.RESET + " 🆕  Insertar un registro")
        print(Color.NEGRITA + "  2." + Color.RESET + " 📋  Listado de registros")
        print(Color.NEGRITA + "  3." + Color.RESET + " 🚪  Salir")
        print()
        linea()

        opcion = input(Color.MAGENTA + "Indica tu opción: " + Color.RESET)

        if opcion == "1":
            insertar_registro()
        elif opcion == "2":
            listar_registros()
        elif opcion == "3":
            limpiar_pantalla()
            print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
            break
        else:
            mensaje_error("Opción no válida, inténtalo de nuevo.")
            pausar()


# Solo se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    menu()
