# e) Características y ventajas de cada colección
print("Programa Ciclistas - Colecciones")

# LISTA: ordenada, se puede modificar y admite duplicados
# Ventaja: ideal para guardar todos los registros en orden
nombres = ["Ana", "Luis", "Marta", "Ana"]
nombres.append("Pedro")
print("Lista:", nombres)

# TUPLA: ordenada pero NO se puede modificar
# Ventaja: datos fijos que no deben cambiar
tipos_permitidos = ("Montaña", "Carretera", "Urbana")
print("Tupla:", tipos_permitidos)

# CONJUNTO (set): sin orden y SIN duplicados
# Ventaja: quitar repetidos y buscar muy rápido
bicicletas = {"Montaña", "Carretera", "Montaña", "Urbana"}
print("Conjunto:", bicicletas)

# DICCIONARIO: pares clave:valor
# Ventaja: acceder a un dato por su nombre, no por su posición
ciclista = {"nombre":"Ana","apellidos":"López","email":"ana@gmail.com","Tipo de bicicleta":"Montaña"}
print("Diccionario:", ciclista["nombre"], "usa", ciclista["Tipo de bicicleta"])
