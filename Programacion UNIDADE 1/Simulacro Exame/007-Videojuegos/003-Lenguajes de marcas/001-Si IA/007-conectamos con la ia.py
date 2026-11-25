import requests

ruta = "http://localhost:11434/api/generate" 	                # Defino la ruta 
modelo = "qwen2.5-coder:7b"									    # Elijo un modelo
pregunta = """ 
	Dame el SQL para:
  -Listar todos las películas de la tabla "películas" ordenados por título.
  -La estructura de la tabla es esta:                           
  CREATE TABLE "videojuegos" (
	"id"	INTEGER,
	"titulo"	TEXT,
	"desarrollador"	TEXT,
	"distribuidor"	TEXT,
	"genero"	TEXT,
	"descripcion"	TEXT,
	"anio_lanzamiento"	INTEGER,
	"fecha_lanzamiento"	TEXT,
	"plataforma"	TEXT,
	"pais"	TEXT,
	"idioma"	TEXT,
	"clasificacion_edades"	TEXT,
	"presupuesto"	TEXT,
	"ingresos"	TEXT,
	"valoracion_media"	TEXT,
	"numero_valoraciones"	INTEGER,
	"unidades_vendidas"	INTEGER,
	"disponible"	TEXT,
	"multijugador"	TEXT,
	"favorito"	TEXT,
	"imagen_portada"	TEXT,
	"url_trailer"	TEXT,
	"precio_original"	INTEGER,
	"precio_rebajado"	INTEGER,
	"espacio_requerido"	INTEGER,
	"compras_integradas"	TEXT,
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