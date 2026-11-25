import requests

ruta = "http://localhost:11434/api/generate" 	                # Defino la ruta 
modelo = "qwen2.5-coder:7b"									    # Elijo un modelo
pregunta = """ 
	Dame el SQL para:
  -Listar todos las películas de la tabla "películas" ordenados por título.
  -La estructura de la tabla es esta:                           
CREATE TABLE "películas" (
	"id"	INTEGER,
	"titulo"	TEXT,
	"titulo_original"	TEXT,
	"director"	TEXT,
	"genero"	TEXT,
	"sinopsis"	TEXT,
	"anio_estreno"	TEXT,
	"fecha_estreno"	TEXT,
	"duracion_minutos"	INTEGER,
	"pais"	TEXT,
	"idioma_original"	TEXT,
	"clasificacion_edades"	TEXT,
	"presupuesto"	TEXT,
	"recaudacion"	TEXT,
	"valoracion_media"	TEXT,
	"numero_valoraciones"	INTEGER,
	"numero_visualizaciones"	INTEGER,
	"disponible"	TEXT,
	"vista"	TEXT,
	"favorita"	TEXT,
	"imagen_portada"	TEXT,
	"url_trailer"	TEXT,
	"precio_alquiler"	INTEGER,
	"precio_compra"	INTEGER,
	"formato"	TEXT,
	"subtitulos_disponibles"	TEXT,
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