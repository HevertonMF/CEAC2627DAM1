import requests

ruta = "http://localhost:11434/api/generate" 	                # Defino la ruta 
modelo = "qwen2.5-coder:7b"									    # Elijo un modelo
pregunta = """ 
	Dame el SQL para:
  -Listar todos los médicos de España
  -La estructura de la tabla es esta:                           
      CREATE TABLE "médicos" (                                  
	"id"	INTEGER,
	"nombre"	TEXT,                                   
	"apellidos"	TEXT,
	"email"	TEXT,
	"especialidad"	TEXT,
	"numero_de_colegiado"	INTEGER,
	"activo"	INTEGER,
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