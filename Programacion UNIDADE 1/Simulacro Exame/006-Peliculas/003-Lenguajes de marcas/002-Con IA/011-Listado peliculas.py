# Videoteca Heverton - versión final y bonita
# Une todo lo de los pasos 003-011: catálogo, ficha, formulario y consultor SQL con IA local (Ollama)

import os
import re
import sqlite3

import requests
from flask import Flask, abort, jsonify, render_template, request

# Variables invariables ##################################
RUTA = "http://localhost:11434/api/generate"   # Ruta de Ollama
MODELO = "qwen2.5-coder:7b"                    # Modelo
BASE_DE_DATOS = "videoteca20261124.db"         # Base de datos
CARPETA = os.path.dirname(os.path.abspath(__file__))

ESQUEMA = """
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
"""

# Columnas que se rellenan desde el formulario (todas menos id)
COLUMNAS = [
    "titulo", "titulo_original", "director", "genero", "sinopsis", "anio_estreno",
    "fecha_estreno", "duracion_minutos", "pais", "idioma_original", "clasificacion_edades",
    "presupuesto", "recaudacion", "valoracion_media", "numero_valoraciones",
    "numero_visualizaciones", "disponible", "vista", "favorita", "imagen_portada",
    "url_trailer", "precio_alquiler", "precio_compra", "formato", "subtitulos_disponibles",
]

# Cada género tiene su color para el póster
COLORES = {
    "Acción": "#e4572e", "Animación": "#f3a712", "Aventura": "#4caf50",
    "Ciencia ficción": "#2ec4b6", "Comedia": "#ffbf46", "Crimen": "#9b2226",
    "Drama": "#7b6cf6", "Fantasía": "#c77dff", "Infantil": "#ff8fab",
    "Musical": "#ff5d8f", "Romance": "#ef476f", "Terror": "#5c677d",
    "Thriller": "#3a86ff",
}

app = Flask(__name__)


def conectar():
    # Me conecto y pido las filas como diccionario
    conexion = sqlite3.connect(os.path.join(CARPETA, BASE_DE_DATOS))
    conexion.row_factory = sqlite3.Row
    return conexion


# Pequeñas ayudas para pintar los datos ####################

def a_numero(valor):
    """Convierte '8.7', '165000000'... a número. Si no se puede, None."""
    try:
        return float(str(valor).replace(",", "."))
    except (TypeError, ValueError):
        return None


def es_si(valor):
    """'Verdadero', 'Sí', '1', 'true' -> True."""
    return str(valor or "").strip().lower() in ("verdadero", "si", "sí", "1", "true", "yes")


@app.template_filter("millones")
def millones(valor):
    n = a_numero(valor)
    if n is None:
        return "—"
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f} mil M $".replace(".", ",")
    if n >= 1_000_000:
        return f"{n / 1_000_000:.0f} M $"
    return f"{n:,.0f} $".replace(",", ".")


@app.template_filter("miles")
def miles(valor):
    n = a_numero(valor)
    return "—" if n is None else f"{n:,.0f}".replace(",", ".")


@app.template_filter("euros")
def euros(valor):
    n = a_numero(valor)
    return "—" if n is None else f"{n:.2f} €".replace(".", ",")


@app.template_filter("duracion")
def duracion(minutos):
    n = a_numero(minutos)
    if not n:
        return "—"
    h, m = divmod(int(n), 60)
    return f"{h} h {m:02d} min" if h else f"{m} min"


@app.template_filter("fecha")
def fecha(valor):
    meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
    trozos = str(valor or "").split("-")
    if len(trozos) == 3 and trozos[1].isdigit() and 1 <= int(trozos[1]) <= 12:
        return f"{int(trozos[2])} {meses[int(trozos[1]) - 1]} {trozos[0]}"
    return valor or "—"


@app.context_processor
def utilidades():
    def portada(p):
        # Si existe static/portadas/<imagen>, se usa; si no, se pinta un póster con CSS
        nombre = (p["imagen_portada"] or "").strip()
        if nombre and os.path.exists(os.path.join(CARPETA, "static", "portadas", nombre)):
            return nombre
        return None

    def color(genero):
        return COLORES.get(genero, "#8d99ae")

    return {"portada": portada, "color": color, "es_si": es_si, "a_numero": a_numero}


# IA ########################################################

def generar_sql(preguntausuario):
    """Pide a Ollama el SQL para la pregunta del usuario."""
    pregunta = f"""
    Eres un generador de SQL para SQLite.
    Dame el SQL para:
    - {preguntausuario}
    - La estructura de la tabla es esta:
    {ESQUEMA}
    - El nombre de la tabla es "películas" (con tilde y entre comillas dobles).
    - Los campos de sí/no guardan el texto 'Verdadero' o 'Falso'.
    - valoracion_media, presupuesto y recaudacion son TEXT: usa CAST(... AS REAL) para ordenar o comparar.
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
    # Catálogo con todas las películas
    conexion = conectar()
    peliculas = conexion.execute('SELECT * FROM "películas" ORDER BY titulo').fetchall()
    conexion.close()

    notas = [a_numero(p["valoracion_media"]) for p in peliculas]
    notas = [n for n in notas if n is not None]
    minutos = sum(a_numero(p["duracion_minutos"]) or 0 for p in peliculas)

    resumen = {
        "total": len(peliculas),
        "horas": int(minutos // 60),
        "nota": f"{sum(notas) / len(notas):.1f}".replace(".", ",") if notas else "—",
        "disponibles": sum(1 for p in peliculas if es_si(p["disponible"])),
    }
    generos = sorted({p["genero"] for p in peliculas if p["genero"]})
    formatos = sorted({p["formato"] for p in peliculas if p["formato"]})

    # La más valorada sale destacada arriba
    destacada = max(peliculas, key=lambda p: a_numero(p["valoracion_media"]) or 0, default=None)

    return render_template(
        "index.html", datos=peliculas, resumen=resumen, generos=generos,
        formatos=formatos, destacada=destacada, pagina="catalogo",
    )


@app.route("/pelicula/<int:id>")
def pelicula(id):
    conexion = conectar()
    p = conexion.execute('SELECT * FROM "películas" WHERE id = ?', (id,)).fetchone()
    parecidas = []
    if p:
        parecidas = conexion.execute(
            'SELECT * FROM "películas" WHERE genero = ? AND id <> ? ORDER BY RANDOM() LIMIT 4',
            (p["genero"], id),
        ).fetchall()
    conexion.close()
    if p is None:
        abort(404)
    return render_template("pelicula.html", p=p, parecidas=parecidas, pagina="catalogo")


@app.route("/formulario")
def formulario():
    return render_template("formulario.html", pagina="formulario")


@app.route("/recibedatos", methods=["POST"])
def recibedatos():
    valores = [request.form.get(c, "").strip() for c in COLUMNAS]
    conexion = conectar()
    cursor = conexion.execute(
        f'INSERT INTO "películas" ({", ".join(COLUMNAS)}) VALUES ({", ".join("?" * len(COLUMNAS))})',
        valores,
    )
    conexion.commit()  # Sin esto el INSERT no se guarda
    nuevo_id = cursor.lastrowid
    conexion.close()
    return render_template(
        "confirmacion.html", titulo=request.form.get("titulo", ""),
        nuevo_id=nuevo_id, pagina="formulario",
    )


@app.route("/consultor")
def consultor():
    return render_template("consultor.html", modelo=MODELO, pagina="consultor")


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
    conexion = sqlite3.connect(os.path.join(CARPETA, BASE_DE_DATOS))
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


@app.errorhandler(404)
def no_encontrada(e):
    return render_template("404.html", pagina=""), 404


if __name__ == "__main__":
    app.run(debug=True, threaded=True)   # atiende varias pestañas a la vez
