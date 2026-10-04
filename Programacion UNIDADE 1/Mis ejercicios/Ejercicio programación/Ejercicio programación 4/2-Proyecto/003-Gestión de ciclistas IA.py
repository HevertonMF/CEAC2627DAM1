#GESTIÓN DE CICLISTAS v0.2 By Heverton
# Importo las clases desde mi librería
import importlib
clases = importlib.import_module("001-Clases")
Persona = clases.Persona
Ciclista = clases.Ciclista
import os

# Activo los colores en la consola de Windows
os.system("")

# Colores para la consola
AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
CIAN = "\033[96m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


# Funciones para que se vea más bonito
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def titulo(texto):
    print(AZUL + "╔" + "═" * 50 + "╗" + RESET)
    print(AZUL + "║" + RESET + NEGRITA + texto.center(50) + RESET + AZUL + "║" + RESET)
    print(AZUL + "╚" + "═" * 50 + "╝" + RESET)


def exito(texto):
    print(VERDE + "✔ " + texto + RESET)


def error(texto):
    print(ROJO + "✘ " + texto + RESET)


def pausa():
    input(AMARILLO + "\nPulsa Enter para continuar..." + RESET)


def pedir_numero(texto):
    numero = input(texto)
    while not numero.isdigit():
        error("Tienes que escribir un número")
        numero = input(texto)
    return int(numero)


def tabla_ciclistas():
    print(CIAN + f"{'Nº':<4}{'Nombre':<12}{'Apellidos':<15}{'Equipo':<12}{'Bicicleta':<12}" + RESET)
    print("─" * 55)
    for indice, ciclista in enumerate(lista_de_ciclistas):
        print(f"{indice:<4}{ciclista.nombre:<12}{ciclista.apellidos:<15}{ciclista.equipo:<12}{ciclista.bicicleta:<12}")


# Creo una lista vacía de ciclistas
lista_de_ciclistas = []


while True:
    limpiar()
    titulo("🚴 GESTIÓN DE CICLISTAS v0.2 🚴")
    print()
    print(f"  {AMARILLO}1{RESET} ➜ Insertar un ciclista")
    print(f"  {AMARILLO}2{RESET} ➜ Listar los ciclistas")
    print(f"  {AMARILLO}3{RESET} ➜ Actualizar un ciclista")
    print(f"  {AMARILLO}4{RESET} ➜ Eliminar un ciclista")
    print(f"  {AMARILLO}5{RESET} ➜ Salir")
    print()
    print(f"  Ciclistas registrados: {VERDE}{len(lista_de_ciclistas)}{RESET}")
    print()

    opcion = input(NEGRITA + "Indica tu opción: " + RESET)

    # CREATE
    if opcion == "1":
        limpiar()
        titulo("➕ NUEVO CICLISTA")

        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        email = input("Email: ")

        # Uso el método estático para comprobar el email
        while not Persona.validar_email(email):
            error("Email no válido")
            email = input("Email: ")

        equipo = input("Equipo: ")
        bicicleta = input("Bicicleta: ")

        nuevo_ciclista = Ciclista(nombre, apellidos, email, equipo, bicicleta)
        lista_de_ciclistas.append(nuevo_ciclista)

        print()
        exito("Ciclista añadido correctamente")
        pausa()

    # READ
    elif opcion == "2":
        limpiar()
        titulo("📋 LISTA DE CICLISTAS")

        if len(lista_de_ciclistas) == 0:
            error("No hay ciclistas registrados")
        else:
            for indice, ciclista in enumerate(lista_de_ciclistas):
                print(CIAN + f"┌─── Ciclista nº {indice} " + "─" * 30 + RESET)
                ciclista.mostrar()
                print(CIAN + "└" + "─" * 47 + RESET)
        pausa()

    # UPDATE
    elif opcion == "3":
        limpiar()
        titulo("✏️  ACTUALIZAR CICLISTA")

        if len(lista_de_ciclistas) == 0:
            error("No hay ciclistas para actualizar")
        else:
            tabla_ciclistas()
            print()
            numero = pedir_numero("Número del ciclista a actualizar: ")

            if numero < len(lista_de_ciclistas):
                ciclista = lista_de_ciclistas[numero]
                print(AMARILLO + "(Deja vacío para no cambiar)" + RESET)

                # Si el usuario no escribe nada, se queda el dato antiguo
                nombre = input(f"Nombre [{ciclista.nombre}]: ")
                if nombre != "":
                    ciclista.nombre = nombre

                apellidos = input(f"Apellidos [{ciclista.apellidos}]: ")
                if apellidos != "":
                    ciclista.apellidos = apellidos

                email = input(f"Email [{ciclista.get_email()}]: ")
                if email != "":
                    ciclista.set_email(email)

                equipo = input(f"Equipo [{ciclista.equipo}]: ")
                if equipo != "":
                    ciclista.equipo = equipo

                bicicleta = input(f"Bicicleta [{ciclista.bicicleta}]: ")
                if bicicleta != "":
                    ciclista.bicicleta = bicicleta

                print()
                exito("Ciclista actualizado")
            else:
                error("Número de ciclista no válido")
        pausa()

    # DELETE
    elif opcion == "4":
        limpiar()
        titulo("🗑️  ELIMINAR CICLISTA")

        if len(lista_de_ciclistas) == 0:
            error("No hay ciclistas para eliminar")
        else:
            tabla_ciclistas()
            print()
            numero = pedir_numero("Número del ciclista a eliminar: ")

            if numero < len(lista_de_ciclistas):
                ciclista = lista_de_ciclistas[numero]
                confirmar = input(ROJO + f"¿Seguro que quieres eliminar a {ciclista.nombre}? (s/n): " + RESET)

                if confirmar.lower() == "s":
                    lista_de_ciclistas.pop(numero)
                    exito("Ciclista eliminado correctamente")
                else:
                    print("Operación cancelada")
            else:
                error("Número de ciclista no válido")
        pausa()

    elif opcion == "5":
        limpiar()
        titulo("👋 ¡HASTA LUEGO!")
        break

    else:
        error("Opción no reconocida")
        pausa()
