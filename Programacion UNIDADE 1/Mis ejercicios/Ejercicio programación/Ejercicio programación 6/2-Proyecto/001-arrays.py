# a) Programas que utilizan matrices (arrays)
# En Python no hay arrays nativos, usamos listas de listas = matriz de 2 dimensiones
# Cada fila es un ciclista y cada columna un dato
print("Programa Ciclistas - Matrices")

ciclistas = [
  ["Ana", "López", "ana@gmail.com", "Montaña"],
  ["Luis", "Pérez", "luis@gmail.com", "Carretera"],
  ["Marta", "Ruiz", "marta@gmail.com", "Urbana"]
]

# Añado una fila nueva a la matriz
ciclistas.append(["Pedro", "Gómez", "pedro@gmail.com", "Montaña"])

# Accedo a una posición concreta [fila][columna]
print("Nombre del primer ciclista:", ciclistas[0][0])
print("Bicicleta del segundo ciclista:", ciclistas[1][3])

# Recorro la matriz fila a fila y columna a columna
for fila in range(len(ciclistas)):
  for columna in range(len(ciclistas[fila])):
    print(ciclistas[fila][columna], end=" | ")
  print()
