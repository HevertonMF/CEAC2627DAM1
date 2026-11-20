# Hospital São Paulo - versión final y bonita
# Une todo lo de los pasos 001-009: listado, formulario y consultor SQL con IA local (Ollama)

import re
import sqlite3

import requests
from flask import Flask, jsonify, render_template, request

# Variables invariables ##################################
RUTA = "http://localhost:11434/api/generate"   # Ruta de Ollama
MODELO = "qwen2.5-coder:7b"                    # Modelo
BASE_DE_DATOS = "examendamceac2627.db"         # Base de datos

ESQUEMA = """
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
"""

app = Flask(__name__)


def conectar():
    # Me conecto y pido las filas como diccionario
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


def generar_sql(preguntausuario):
    """Pide a Ollama el SQL para la pregunta del usuario."""
    pregunta = f"""
    Eres un generador de SQL para SQLite.
    Dame el SQL para:
    - {preguntausuario}
    - La estructura de la tabla es esta:
    {ESQUEMA}
    - El nombre de la tabla es "médicos" (con tilde y entre comillas dobles).
    - Responde SOLO con la sentencia SQL en texto plano.
    - Sin markdown, sin ```, sin la palabra sql delante, sin comentarios ni explicaciones.
    """
    r = requests.post(RUTA, json={
        "model": MODELO,
        "prompt": pregunta,
        "stream": False,
        "options": {"temperature": 0},
    }, timeout=120)
    r.raise_for_status()

    sql = r.json()["response"].strip()
    # Por si la IA pone ```sql ... ``` igualmente
    bloque = re.search(r"```(?:sql)?\s*(.*?)```", sql, re.DOTALL | re.IGNORECASE)
    if bloque:
        sql = bloque.group(1)
    sql = sql.replace("`", "").strip()
    sql = re.sub(r"^sql\b\s*", "", sql, flags=re.IGNORECASE)
    return sql.strip()


def es_solo_lectura(sql):
    """True si la sentencia solo consulta (no modifica datos)."""
    primera = sql.lstrip().split(None, 1)[0].upper() if sql.strip() else ""
    return primera in ("SELECT", "WITH", "PRAGMA")


# Páginas ##################################################

@app.route("/")
def inicio():
    # Consultor con IA
    return render_template("index.html", modelo=MODELO, pagina="consultor")


@app.route("/medicos")
def medicos():
    # Listado de médicos con un pequeño resumen arriba
    conexion = conectar()
    datos = conexion.execute(
        'SELECT * FROM "médicos" ORDER BY apellidos, nombre'
    ).fetchall()
    especialidades = conexion.execute(
        'SELECT DISTINCT especialidad FROM "médicos" ORDER BY especialidad'
    ).fetchall()
    conexion.close()

    activos = sum(1 for m in datos if m["activo"])
    return render_template(
        "medicos.html",
        datos=datos,
        especialidades=[e["especialidad"] for e in especialidades],
        total=len(datos),
        activos=activos,
        pagina="medicos",
    )


@app.route("/formulario")
def formulario():
    return render_template("formulario.html", pagina="formulario")


@app.route("/recibedatos", methods=["POST"])
def recibedatos():
    conexion = conectar()
    conexion.execute(
        """
        INSERT INTO "médicos" (nombre, apellidos, email, especialidad, numero_de_colegiado, activo)
        VALUES (?, ?, ?, ?, ?, 1)
        """,
        (
            request.form["nombre"].strip(),
            request.form["apellidos"].strip(),
            request.form["correo"].strip().lower(),
            request.form["especialidad"].strip(),
            request.form["numero_de_colegiado"].strip(),
        ),
    )
    conexion.commit()  # Sin esto el INSERT no se guarda
    conexion.close()
    return render_template(
        "confirmacion.html",
        nombre=request.form["nombre"],
        apellidos=request.form["apellidos"],
        especialidad=request.form["especialidad"],
        pagina="formulario",
    )


# API para el consultor ####################################

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
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = [list(f) for f in cursor.fetchall()]
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


if __name__ == "__main__":
    app.run(debug=True)
