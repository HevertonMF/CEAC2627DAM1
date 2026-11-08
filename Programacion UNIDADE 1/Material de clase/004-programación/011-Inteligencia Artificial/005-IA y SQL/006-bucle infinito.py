import requests
import sqlite3
import re

# Variables invariables ##################################
ruta = "http://localhost:11434/api/generate"   # Defino la ruta
modelo = "qwen2.5-coder:7b"                    # Elijo un modelo
conexion = sqlite3.connect("empresa.db")       # Abro la base de datos
cursor = conexion.cursor()                     # Creo un cursor


def limpiar_sql(texto):
    """Quita fences markdown, la palabra 'sql' suelta y espacios sobrantes."""
    texto = texto.strip()
    # Si viene dentro de ```sql ... ```, me quedo solo con lo de dentro
    bloque = re.search(r"```(?:sql)?\s*(.*?)```", texto, re.DOTALL | re.IGNORECASE)
    if bloque:
        texto = bloque.group(1)
    texto = texto.replace("`", "").strip()
    # Si aún empieza por "sql", lo elimino
    texto = re.sub(r"^sql\b\s*", "", texto, flags=re.IGNORECASE)
    return texto.strip()


while True:                                    # Entro en un bucle infinito
    preguntausuario = input("Dime qué es lo que quieres (o 'salir'): ")
    if preguntausuario.lower() == "salir":
        break

    pregunta = """
    Eres un generador de SQL para SQLite.
    Dame el SQL para:
    - """ + preguntausuario + """
    - La estructura de la tabla es esta:
        CREATE TABLE "clientes" (
        "id"	INTEGER,
        "nombre"	TEXT,
        "apellidos"	TEXT,
        "email"	TEXT,
        "telefono"	TEXT,
        "ciudad"	TEXT,
        "provincia"	TEXT,
        "direccionpostal"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
        );
    - Responde SOLO con la sentencia SQL en texto plano.
    - Sin markdown, sin ```, sin la palabra sql delante, sin comentarios ni explicaciones.
    """                                         # Establezco una pregunta

    r = requests.post(ruta, json={
        "model": modelo,
        "prompt": pregunta,
        "stream": False,
        "options": {"temperature": 0}           # Respuestas más estables
    })                                          # Hago una petición

    sql = limpiar_sql(r.json()["response"])     # Limpio la respuesta
    print(sql)                                  # Imprime el SQL limpio

    try:
        cursor.execute(sql)                     # Ejecuto la petición
        filas = cursor.fetchall()               # Recupero el resultado
        conexion.commit()                       # Guarda si es INSERT/UPDATE/DELETE
        for fila in filas:                      # Para cada fila
            print(fila)                         # Imprime la fila
    except sqlite3.Error as e:
        print("Error en el SQL:", e)            # No rompe el bucle

conexion.close()