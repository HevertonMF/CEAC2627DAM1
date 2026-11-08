# j) Operaciones agregadas: filtrado, transformación, reducción y recolección
from functools import reduce

print("Programa Ciclistas - Operaciones agregadas")

Ciclistas = [
  {"nombre":"Ana","edad":25,"Tipo de bicicleta":"Montaña"},
  {"nombre":"Luis","edad":32,"Tipo de bicicleta":"Carretera"},
  {"nombre":"Marta","edad":19,"Tipo de bicicleta":"Montaña"},
  {"nombre":"Pedro","edad":41,"Tipo de bicicleta":"Urbana"}
]

# FILTRADO: solo los de montaña
montana = list(filter(lambda c: c["Tipo de bicicleta"] == "Montaña", Ciclistas))
print("De montaña:", [c["nombre"] for c in montana])

# TRANSFORMACIÓN (map): solo los nombres en mayúsculas
nombres = list(map(lambda c: c["nombre"].upper(), Ciclistas))
print("Nombres:", nombres)

# REDUCCIÓN: suma de todas las edades
suma = reduce(lambda total, c: total + c["edad"], Ciclistas, 0)
print("Suma de edades:", suma)
print("Edad media:", suma / len(Ciclistas))

# RECOLECCIÓN: agrupo los nombres por tipo de bicicleta en un diccionario
grupos = {}
for c in Ciclistas:
  grupos.setdefault(c["Tipo de bicicleta"], []).append(c["nombre"])
print("Agrupados:", grupos)

# ORDENACIÓN: de menor a mayor edad
ordenados = sorted(Ciclistas, key=lambda c: c["edad"])
print("Por edad:", [c["nombre"] for c in ordenados])
