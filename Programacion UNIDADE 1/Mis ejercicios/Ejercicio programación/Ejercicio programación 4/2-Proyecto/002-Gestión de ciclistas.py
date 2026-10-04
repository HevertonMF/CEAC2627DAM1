#GESTIÓN DE CICLISTAS v0.1 By Heverton
# Importo las clases desde mi librería
import importlib
clases = importlib.import_module("001-Clases")
Persona = clases.Persona
Ciclista = clases.Ciclista

# Bienvenida, Gestión de ciclistas (CRUD)
print("Ciclistas v0.1 By Heverton")
print("Gestión de ciclistas")


# Creo una lista vacía de ciclistas
lista_de_ciclistas = []


while True:
    print()
    print("Escoge una opción:")
    print("1.- Insertar un ciclista")
    print("2.- Listar los ciclistas")
    print("3.- Actualizar un ciclista")
    print("4.- Eliminar un ciclista")
    print("5.- Salir")

    opcion = input("Indica tu opción: ")

    # CREATE
    if opcion == "1":
        print("Ahora vemos cómo insertamos un ciclista")

        # Le pido al usuario los datos del ciclista
        nombre = input("Introduce el nombre del ciclista: ")
        apellidos = input("Introduce los apellidos del ciclista: ")
        email = input("Introduce el email del ciclista: ")

        # Uso el método estático para comprobar el email
        while not Persona.validar_email(email):
            email = input("Email no válido, introdúcelo otra vez: ")

        equipo = input("Introduce el equipo del ciclista: ")
        bicicleta = input("Introduce la bicicleta del ciclista: ")

        # Creo un ciclista
        nuevo_ciclista = Ciclista(
            nombre,
            apellidos,
            email,
            equipo,
            bicicleta
        )

        # Añado el ciclista a la lista
        lista_de_ciclistas.append(nuevo_ciclista)
        print("Ciclista añadido correctamente")

    # READ
    elif opcion == "2":
        print("Ahora listamos los ciclistas")

        if len(lista_de_ciclistas) == 0:
            print("No hay ciclistas registrados")

        for indice, ciclista in enumerate(lista_de_ciclistas):
            print("-" * 30)
            print("Número:", indice)
            ciclista.mostrar()
            print("-" * 30)

    # UPDATE
    elif opcion == "3":
        print("Ahora actualizamos un ciclista")

        for indice, ciclista in enumerate(lista_de_ciclistas):
            print(indice, "-", ciclista.nombre, ciclista.apellidos)

        numero = int(input("Indica el número del ciclista a actualizar: "))

        if 0 <= numero < len(lista_de_ciclistas):
            ciclista = lista_de_ciclistas[numero]

            # Le pido los nuevos datos
            ciclista.nombre = input("Nuevo nombre: ")
            ciclista.apellidos = input("Nuevos apellidos: ")
            ciclista.set_email(input("Nuevo email: "))
            ciclista.equipo = input("Nuevo equipo: ")
            ciclista.bicicleta = input("Nueva bicicleta: ")

            print("Ciclista actualizado")
        else:
            print("Número de ciclista no válido")

    # DELETE
    elif opcion == "4":
        print("Ahora eliminamos un ciclista")

        for indice, ciclista in enumerate(lista_de_ciclistas):
            print(indice, "-", ciclista.nombre, ciclista.apellidos)

        numero = int(input("Indica el número del ciclista a eliminar: "))

        if 0 <= numero < len(lista_de_ciclistas):
            eliminado = lista_de_ciclistas.pop(numero)
            print("Ciclista", eliminado.nombre, "eliminado correctamente")
        else:
            print("Número de ciclista no válido")

    elif opcion == "5":
        print("Hasta luego")
        break

    else:
        print("Opción no reconocida")
