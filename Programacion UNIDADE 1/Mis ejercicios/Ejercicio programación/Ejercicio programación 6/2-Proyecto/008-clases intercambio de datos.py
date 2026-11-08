# h) Clases para tratar documentos en lenguajes de intercambio de datos
# json             -> JSON (el que usamos en el programa de ciclistas)
# csv              -> CSV (tablas separadas por comas, se abren en Excel)
# xml.etree        -> XML (etiquetas como en HTML)
import json
import csv
import xml.etree.ElementTree as ET

print("Programa Ciclistas - Clases de intercambio de datos")

ciclista = {"nombre":"Ana","apellidos":"López","email":"ana@gmail.com","Tipo de bicicleta":"Montaña"}

# JSON: json.dumps convierte el diccionario en texto JSON
print("JSON:", json.dumps(ciclista, ensure_ascii=False))

# CSV: csv.writer / csv.DictWriter escriben filas separadas por comas
print("CSV usa:", csv.DictWriter)

# XML: ET.Element crea etiquetas
nodo = ET.Element("ciclista")
nodo.set("nombre", ciclista["nombre"])
nodo.text = ciclista["Tipo de bicicleta"]
print("XML:", ET.tostring(nodo, encoding="unicode"))
