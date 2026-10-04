import os

directorio = "/home/hevertonmf/Escritorio/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 3"

for x,y,z in os.walk(directorio):
  print(x)

for x,y,z in os.walk(directorio):
  print(y)
  
for x,y,z in os.walk(directorio):
  print(z)

