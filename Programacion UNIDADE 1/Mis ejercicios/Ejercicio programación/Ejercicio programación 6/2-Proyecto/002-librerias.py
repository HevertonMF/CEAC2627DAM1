# b) Librerías relacionadas con tipos de datos avanzados
# json        -> guardar y leer datos en formato JSON
# os          -> comprobar si existen archivos
# re          -> expresiones regulares
# collections -> colecciones avanzadas como Counter
import json
import os
import re
from collections import Counter

print("Programa Ciclistas - Librerías")

ciclistas = [
  {"nombre":"Ana","apellidos":"López","email":"ana@gmail.com","Tipo de bicicleta":"Montaña"},
  {"nombre":"Luis","apellidos":"Pérez","email":"luis@gmail.com","Tipo de bicicleta":"Carretera"},
  {"nombre":"Marta","apellidos":"Ruiz","email":"marta@gmail.com","Tipo de bicicleta":"Montaña"}
]

# json: convierto la lista en texto JSON
print(json.dumps(ciclistas))

# os: compruebo si existe el archivo
print("¿Existe ciclistas.json?", os.path.exists("ciclistas.json"))

# re: compruebo si un email tiene @
print("¿Email válido?", re.search("@", "ana@gmail.com") != None)

# Counter: cuento cuántos ciclistas hay de cada tipo de bicicleta
tipos = Counter()
for c in ciclistas:
  tipos[c["Tipo de bicicleta"]] += 1
print(tipos)
