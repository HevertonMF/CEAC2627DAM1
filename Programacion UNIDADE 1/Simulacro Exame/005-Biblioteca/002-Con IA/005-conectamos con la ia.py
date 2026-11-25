import requests

ruta = "http://localhost:11434/api/generate" 	                # Defino la ruta 
modelo = "qwen2.5-coder:7b"									    # Elijo un modelo
pregunta = """ 
	Dame el SQL para:
  -Listar todos los libros de la tabla "libros"
  -La estructura de la tabla es esta:                           
CREATE TABLE "libros" (
	"id"	INTEGER,
	"titulo"	TEXT,
	"autor"	TEXT,
	"fecha_de_publicacion"	TEXT,
	"sinopsis"	TEXT,
	"editorial"	TEXT,
	"isbn"	TEXT,
	"genero"	TEXT,
	"precio"	INTEGER,
	"disponible"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
    - Dame solo código SQL - no pongas comentarios
    - Elimina los fences markdown opentick
  
"""									                            # Establezco una pregunta
flujo = False													# Elijo stream
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																# Hago una petición
print(r.json()["response"])										# Imprime la respuesta