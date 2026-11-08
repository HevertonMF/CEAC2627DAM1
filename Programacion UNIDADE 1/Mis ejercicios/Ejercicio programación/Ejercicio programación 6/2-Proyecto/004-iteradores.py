# d) Iteradores para recorrer los elementos de las listas
print("Programa Ciclistas - Iteradores")

Ciclistas = [
  {"nombre":"Ana","apellidos":"López","email":"ana@gmail.com","Tipo de bicicleta":"Montaña"},
  {"nombre":"Luis","apellidos":"Pérez","email":"luis@gmail.com","Tipo de bicicleta":"Carretera"},
  {"nombre":"Marta","apellidos":"Ruiz","email":"marta@gmail.com","Tipo de bicicleta":"Urbana"}
]

# 1. Recorro con for (el for usa un iterador por dentro)
for c in Ciclistas:
  print(c["nombre"], c["apellidos"])

# 2. Recorro con enumerate para tener también la posición
for i, c in enumerate(Ciclistas, 1):
  print(i, "-", c["nombre"])

# 3. Uso el iterador a mano con iter() y next()
iterador = iter(Ciclistas)
print("Primero:", next(iterador)["nombre"])
print("Segundo:", next(iterador)["nombre"])
print("Tercero:", next(iterador)["nombre"])
