# =========================================================
#  Biblioteca Heverton
#  Flask + SQLite + IA local (Ollama) que genera SQL
# =========================================================
import os
import re
import sqlite3

import requests
from flask import Flask, jsonify, redirect, render_template, request, url_for

# Variables invariables ##################################
CARPETA = os.path.dirname(os.path.abspath(__file__))               # Carpeta de este archivo
RUTA = "http://localhost:11434/api/generate"                        # Ruta de Ollama
MODELO = "qwen2.5-coder:7b"                                         # Modelo
BASE_DE_DATOS = os.path.join(CARPETA, "biblioteca20261123.db")      # Base de datos (funciona desde cualquier carpeta)

ESQUEMA = """
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
"""

# Campos del formulario (en el mismo orden que el INSERT)
CAMPOS = ["titulo", "autor", "fecha_de_publicacion", "sinopsis", "editorial",
          "isbn", "genero", "precio", "disponible"]
OBLIGATORIOS = ["titulo", "autor"]

# UNA sola aplicación
app = Flask(__name__)


# Funciones de ayuda #####################################
def conectar():
    """Abre la base de datos y devuelve las filas como diccionario."""
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


def limpiar_sql(texto):
    """Quita fences markdown, la palabra 'sql' suelta y espacios sobrantes."""
    texto = (texto or "").strip()
    bloque = re.search(r"```(?:sql)?\s*(.*?)```", texto, re.DOTALL | re.IGNORECASE)
    if bloque:                                   # Si viene dentro de ```sql ... ```
        texto = bloque.group(1)
    texto = texto.replace("`", "").strip()
    texto = re.sub(r"^sql\b\s*", "", texto, flags=re.IGNORECASE)
    return texto.strip()


def generar_sql(preguntausuario):
    """Pide a Ollama el SQL para la pregunta del usuario."""
    pregunta = f"""
    Eres un generador de SQL para SQLite.
    Dame el SQL para:
    - {preguntausuario}
    - La estructura de la tabla es esta:
    {ESQUEMA}
    - Devuelve UNA sola sentencia SQL.
    - Para buscar texto usa LIKE con % (por ejemplo autor LIKE '%Cervantes%').
    - Responde SOLO con la sentencia SQL en texto plano.
    - Sin markdown, sin ```, sin la palabra sql delante, sin comentarios ni explicaciones.
    """
    r = requests.post(RUTA, json={
        "model": MODELO,
        "prompt": pregunta,
        "stream": False,
        "options": {"temperature": 0},           # Respuestas más estables
    }, timeout=120)
    r.raise_for_status()
    return limpiar_sql(r.json()["response"])


def es_solo_lectura(sql):
    """True si la sentencia solo consulta (no modifica datos)."""
    primera = sql.lstrip().split(None, 1)[0].upper() if sql.strip() else ""
    return primera in ("SELECT", "WITH", "PRAGMA")


def estadisticas(conexion):
    """Números para la cabecera de la página principal."""
    fila = conexion.execute("""
        SELECT COUNT(*)                                   AS total,
               SUM(CASE WHEN disponible = 'Sí' THEN 1 ELSE 0 END) AS disponibles,
               COUNT(DISTINCT genero)                     AS generos,
               ROUND(AVG(precio), 2)                      AS precio_medio
        FROM libros
    """).fetchone()
    return dict(fila)


def lista_generos(conexion):
    filas = conexion.execute(
        "SELECT DISTINCT genero FROM libros WHERE genero <> '' ORDER BY genero"
    ).fetchall()
    return [f["genero"] for f in filas]


# Rutas ##################################################
@app.route("/")
def inicio():
    conexion = conectar()
    libros = conexion.execute("SELECT * FROM libros ORDER BY titulo").fetchall()
    stats = estadisticas(conexion)
    generos = lista_generos(conexion)
    conexion.close()
    return render_template("index.html", datos=libros, stats=stats,
                           generos=generos, modelo=MODELO)


@app.route("/formulario")
def formulario():
    conexion = conectar()
    generos = lista_generos(conexion)
    conexion.close()
    return render_template("formulario.html", generos=generos, valores={}, errores=[])


@app.route("/recibedatos", methods=["POST"])
def recibedatos():
    valores = {campo: request.form.get(campo, "").strip() for campo in CAMPOS}

    # Validación sencilla en el servidor
    errores = [f"El campo «{c.replace('_', ' ')}» es obligatorio." for c in OBLIGATORIOS if not valores[c]]
    try:
        valores["precio"] = round(float(valores["precio"].replace(",", ".")), 2) if valores["precio"] else 0
        if valores["precio"] < 0:
            errores.append("El precio no puede ser negativo.")
    except ValueError:
        errores.append("El precio tiene que ser un número.")
    if valores["disponible"] not in ("Sí", "No"):
        valores["disponible"] = "Sí"

    if errores:                                  # Vuelvo al formulario con lo que había escrito
        conexion = conectar()
        generos = lista_generos(conexion)
        conexion.close()
        return render_template("formulario.html", generos=generos,
                               valores=valores, errores=errores), 400

    conexion = conectar()
    cursor = conexion.execute(
        f"INSERT INTO libros ({', '.join(CAMPOS)}) VALUES ({', '.join('?' * len(CAMPOS))})",
        [valores[c] for c in CAMPOS],
    )
    conexion.commit()                            # Sin esto el INSERT no se guarda
    nuevo_id = cursor.lastrowid
    conexion.close()
    return render_template("confirmacion.html", libro=valores, id=nuevo_id)


@app.route("/consultar", methods=["POST"])
def consultar():
    datos = request.get_json(silent=True) or {}
    preguntausuario = (datos.get("pregunta") or "").strip()
    permitir_cambios = bool(datos.get("permitir_cambios"))

    if not preguntausuario:
        return jsonify({"error": "Escribe una pregunta."}), 400

    # 1. Generar el SQL con la IA
    try:
        sql = generar_sql(preguntausuario)
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "No se puede conectar con Ollama. ¿Está arrancado (ollama serve)?"}), 502
    except requests.exceptions.Timeout:
        return jsonify({"error": "La IA ha tardado demasiado en responder. Inténtalo otra vez."}), 504
    except Exception as e:
        return jsonify({"error": f"Error al consultar la IA: {e}"}), 502

    if not sql:
        return jsonify({"error": "La IA no ha devuelto ningún SQL."}), 502

    # 2. Proteger la base de datos si no se permiten cambios
    if not permitir_cambios and not es_solo_lectura(sql):
        return jsonify({
            "sql": sql,
            "error": "La IA ha generado una sentencia que modifica datos. "
                     "Activa «Permitir modificar datos» si quieres ejecutarla.",
        }), 400

    # 3. Ejecutar
    conexion = sqlite3.connect(BASE_DE_DATOS)
    try:
        if not permitir_cambios:
            conexion.execute("PRAGMA query_only = ON")   # Doble seguridad: SQLite rechaza cualquier escritura
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = [list(f) for f in cursor.fetchmany(500)]  # Límite para no colgar el navegador
        columnas = [c[0] for c in cursor.description] if cursor.description else []
        conexion.commit()
        return jsonify({
            "sql": sql,
            "columnas": columnas,
            "filas": filas,
            "afectadas": cursor.rowcount if not columnas else None,
        })
    except sqlite3.Error as e:
        return jsonify({"sql": sql, "error": f"Error en el SQL: {e}"}), 400
    finally:
        conexion.close()


@app.errorhandler(404)
def no_encontrado(_):
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True, threaded=True)   # atiende varias pestañas a la vez
