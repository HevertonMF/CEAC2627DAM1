from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
import re

# Variables invariables ##################################
RUTA = "http://localhost:11434/api/generate"             # Ruta de Ollama
MODELO = "qwen2.5-coder:7b"                              # Modelo
BASE_DE_DATOS = "examendamceac2627.db"                   # Base de datos

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
# Funciones para la conexión a la base de datos y para generar el SQL con la IA

# UNA sola aplicación
app = Flask(__name__)


def conectar():
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
    sql = re.sub(r"^```(?:sql)?\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"\s*```$", "", sql)
    return sql.strip()          # <- ESTO faltaba


def es_solo_lectura(sql):
    """True si la sentencia solo consulta (no modifica datos)."""
    primera = sql.lstrip().split(None, 1)[0].upper() if sql.strip() else ""
    return primera in ("SELECT", "WITH", "PRAGMA")


@app.route("/")
def inicio():
    return render_template("index.html", modelo=MODELO)


@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/recibedatos", methods=["POST"])
def recibedatos():
    conexion = conectar()
    conexion.execute(
        """
        INSERT INTO médicos (nombre, apellidos, email, especialidad, numero_de_colegiado)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            request.form["nombre"],
            request.form["apellidos"],
            request.form["correo"],
            request.form["especialidad"],
            request.form["numero_de_colegiado"],
        ),
    )
    conexion.commit()
    conexion.close()
    return render_template("confirmacion.html", nombre=request.form["nombre"])


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
    app.run(debug=True, threaded=True)   # atiende varias pestañas a la vez