import json
# [{ = Tengo una lista de diccionarios
print("Programa Ciclistas JSON v0.1")
Ciclistas = []
#while True para um bucle infinito, para que el programa no se cierre hasta que el usuario lo decida
while True:
  print("Escoge una opcion:")
  print("1.-Insertar un registro")
  print("2.-Listar registros")
  print("3.-Guardar registros en disco")
  opcion = input("Tu opción: ")
  #insertar un registro
  if opcion == "1":
    nombre = input("Introduce el nombre de la persona: ")
    apellidos = input("Introduce los apellidos de la persona: ")
    email = input("Introduce el email de la persona: ")
    tipo_de_bicicleta = input("Introduce el tipo de bicicleta: ")
    # A la lista le añadimos un diccionario
    Ciclistas.append({"nombre":nombre,"apellidos":apellidos,"email":email,"Tipo de bicicleta":tipo_de_bicicleta})
  # Listar registros
  elif opcion == "2":
    print(Ciclistas)
  # Guardar registros en disco
  elif opcion == "3":
    archivo = open("ciclistas.json",'w')
    json.dump(Ciclistas,archivo)
    archivo.close()
