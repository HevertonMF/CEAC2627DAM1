# c) Listas para almacenar y procesar información
# [{ = Tengo una lista de diccionarios
print("Programa Ciclistas - Listas")
Ciclistas = []

# Almaceno: añado ciclistas a la lista
Ciclistas.append({"nombre":"Ana","apellidos":"López","email":"ana@gmail.com","Tipo de bicicleta":"Montaña"})
Ciclistas.append({"nombre":"Luis","apellidos":"Pérez","email":"luis@gmail.com","Tipo de bicicleta":"Carretera"})
Ciclistas.append({"nombre":"Marta","apellidos":"Ruiz","email":"marta@gmail.com","Tipo de bicicleta":"Urbana"})

# Proceso: cuántos hay
print("Total de ciclistas:", len(Ciclistas))

# Proceso: accedo por posición
print("El primero es:", Ciclistas[0]["nombre"])
print("El último es:", Ciclistas[-1]["nombre"])

# Proceso: borro el segundo de la lista
borrado = Ciclistas.pop(1)
print("He borrado a:", borrado["nombre"])

print(Ciclistas)
