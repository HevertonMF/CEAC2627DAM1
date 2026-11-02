import json

nombre = input("Dime el nombre del ciclista: ")
apellidos = input("Dime sus apellidos: ")
equipo = input("Dime su equipo: ")
pais = input("Dime su país: ")
edad = int(input("Dime su edad: "))
especialidad = input("Dime su especialidad (escalador, sprinter, contrarrelojista...): ")
bicicleta = input("Dime la marca de su bicicleta: ")

diccionario = {
  "nombre": nombre,
  "apellidos": apellidos,
  "equipo": equipo,
  "pais": pais,
  "edad": edad,
  "especialidad": especialidad,
  "bicicleta": bicicleta
}

archivo = open("ciclista.json", "w", encoding="utf-8")
json.dump(diccionario, archivo, indent=4, ensure_ascii=False)
archivo.close()

print("Ciclista guardado en ciclista.json")