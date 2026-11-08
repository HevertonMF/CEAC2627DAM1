import re
import sqlite3

import requests
from flask import Flask, jsonify, render_template, request

# Variables invariables ##################################
RUTA = "http://localhost:11434/api/generate"   # Ruta de Ollama
MODELO = "qwen2.5-coder:7b"                    # Modelo
BASE_DATOS = "empresa.db"                      # Base de datos

ESQUEMA = """
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
"""

app = Flask(__name__)


def limpiar_sql(texto):
    """Quita fences markdown, la palabra 'sql' suelta y espacios sobrantes."""
    texto = texto.strip()
    bloque = re.search(r"```(?:sql)?\s*(.*?)```", texto, re.DOTALL | re.IGNORECASE)
    if bloque:
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
    return limpiar_sql(r.json()["response"])


def es_solo_lectura(sql):
    """True si la sentencia solo consulta datos (SELECT / WITH)."""
    return re.match(r"^\s*(select|with)\b", sql, re.IGNORECASE) is not None


@app.route("/")
def inicio():
    return render_template("index.html", modelo=MODELO)


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

    # 2. Proteger la base de datos si no se permiten cambios
    if not permitir_cambios and not es_solo_lectura(sql):
        return jsonify({
            "sql": sql,
            "error": "La IA ha generado una sentencia que modifica datos. "
                     "Activa «Permitir modificar datos» si quieres ejecutarla.",
        }), 400

    # 3. Ejecutar (una conexión por petición: SQLite no comparte bien entre hilos)
    conexion = sqlite3.connect(BASE_DATOS)
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
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