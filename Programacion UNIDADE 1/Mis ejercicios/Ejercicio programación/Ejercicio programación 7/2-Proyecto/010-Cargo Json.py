import json                            #cargo json

archivo = open("mipedido.json",'r')    #abro el archivo en modo lectura
datos = json.load(archivo)
archivo.close()
#print datos cliente
print("Fecha:", datos["fecha"])
print("Cliente:", datos["cliente"]["nombre"], datos["cliente"]["apellidos"])
#print Productos 
for producto in datos["productos"]:
  print(producto["nombre"], "-", producto["precio"], "€")