import requests
import sqlite3

ruta = "http://localhost:11434/api/generate"                        	# Defino la ruta 
modelo = "qwen2.5-coder:7b"												# Elijo un modelo
preguntausuario = input("Dime qué es lo que quieres: ")
pregunta = """ 
	Dame el SQL para:
  -"""+preguntausuario+"""
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
    - no me des otra cosa que no sea código SQL - no me comentes el resultado - Importante!!!!!
    - Elimina los fences markdown opentick
  
"""									                                      # Establezco una pregunta
flujo = False														      # Elijo stream
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																		  # Hago una petición
print(r.json()["response"])										          # Imprime la respuesta
conexion = sqlite3.connect("videoteca20261124.db")
cursor = conexion.cursor()
cursor.execute(r.json()["response"].replace("`", ""))
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.commit()
conexion.close()