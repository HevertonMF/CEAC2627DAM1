# i) Programas que manipulan documentos JSON, CSV y XML
import json
import csv
import os
import xml.etree.ElementTree as ET

# Los archivos se guardan en la misma carpeta que este .py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("Programa Ciclistas - Manipular documentos")

Ciclistas = [
  {"nombre":"Ana","apellidos":"López","email":"ana@gmail.com","Tipo de bicicleta":"Montaña"},
  {"nombre":"Luis","apellidos":"Pérez","email":"luis@gmail.com","Tipo de bicicleta":"Carretera"}
]

# ---------- JSON ----------
# Guardo
archivo = open("ciclistas.json", 'w', encoding='utf-8')
json.dump(Ciclistas, archivo, ensure_ascii=False, indent=2)
archivo.close()
# Leo
archivo = open("ciclistas.json", 'r', encoding='utf-8')
print("JSON leído:", json.load(archivo))
archivo.close()

# ---------- CSV ----------
# Guardo
archivo = open("ciclistas.csv", 'w', encoding='utf-8', newline='')
escritor = csv.DictWriter(archivo, fieldnames=["nombre","apellidos","email","Tipo de bicicleta"])
escritor.writeheader()
escritor.writerows(Ciclistas)
archivo.close()
# Leo
archivo = open("ciclistas.csv", 'r', encoding='utf-8')
for fila in csv.DictReader(archivo):
  print("CSV leído:", fila["nombre"], fila["Tipo de bicicleta"])
archivo.close()

# ---------- XML ----------
# Guardo
raiz = ET.Element("ciclistas")
for c in Ciclistas:
  nodo = ET.SubElement(raiz, "ciclista")
  ET.SubElement(nodo, "nombre").text = c["nombre"]
  ET.SubElement(nodo, "bicicleta").text = c["Tipo de bicicleta"]
ET.ElementTree(raiz).write("ciclistas.xml", encoding="utf-8")
# Leo
arbol = ET.parse("ciclistas.xml")
for nodo in arbol.getroot():
  print("XML leído:", nodo.find("nombre").text, nodo.find("bicicleta").text)
