print("Programa registro de ciclistas v0.2")
print("por Heverton Marques")

while True:
    print("Escoge una opcion")
    print("1.-Insertar un registro")
    print("2.-Listado de registros")

    opcion = input("Indica tu opción: ")

    if opcion == "1":
        nombre = input("Introduce un nombre: ")
        apellidos = input("Introduce unos apellidos: ")
        telefono = input("Introduce un teléfono: ")

        categoria_bicicleta = input("Introduce una categoría de bicicleta: ")

        archivo = open("agenda.csv", "a")
        archivo.write(nombre + "," + apellidos + "," + telefono + "," + categoria_bicicleta + "\n")
        archivo.close()

    elif opcion == "2":
        archivo = open("agenda.csv", "r")
        lineas = archivo.readlines()

        for linea in lineas:
            print(linea, end="")

        archivo.close()

    else:
        print("Opción no válida")
