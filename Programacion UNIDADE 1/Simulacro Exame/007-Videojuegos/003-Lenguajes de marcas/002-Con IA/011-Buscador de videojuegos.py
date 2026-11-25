# Importo las librerías que necesito
import re
import sqlite3

import requests
from flask import Flask, render_template, request, jsonify, abort

# Variables que no cambian ##################################
BASE_DE_DATOS = "videojuegos20261125.db"                  # Archivo de la base de datos
RUTA_IA = "http://localhost:11434/api/generate"           # Ruta de Ollama
MODELO = "qwen2.5-coder:7b"                               # Modelo de IA

# Estructura de la tabla, se la paso a la IA para que sepa qué columnas hay
ESQUEMA = """
CREATE TABLE "videojuegos" (
    "id" INTEGER, "titulo" TEXT, "desarrollador" TEXT, "distribuidor" TEXT,
    "genero" TEXT, "descripcion" TEXT, "anio_lanzamiento" INTEGER,
    "fecha_lanzamiento" TEXT, "plataforma" TEXT, "pais" TEXT, "idioma" TEXT,
    "clasificacion_edades" TEXT, "presupuesto" TEXT, "ingresos" TEXT,
    "valoracion_media" TEXT, "numero_valoraciones" INTEGER,
    "unidades_vendidas" INTEGER, "disponible" TEXT, "multijugador" TEXT,
    "favorito" TEXT, "imagen_portada" TEXT, "url_trailer" TEXT,
    "precio_original" INTEGER, "precio_rebajado" INTEGER,
    "espacio_requerido" INTEGER, "compras_integradas" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);
"""

# Las columnas del formulario (todas menos el id)
COLUMNAS = [
    "titulo", "desarrollador", "distribuidor", "genero", "descripcion",
    "anio_lanzamiento", "fecha_lanzamiento", "plataforma", "pais", "idioma",
    "clasificacion_edades", "presupuesto", "ingresos", "valoracion_media",
    "numero_valoraciones", "unidades_vendidas", "disponible", "multijugador",
    "favorito", "imagen_portada", "url_trailer", "precio_original",
    "precio_rebajado", "espacio_requerido", "compras_integradas",
]

# Un color para cada género (para las portadas)
COLORES = {
    "Acción": "#ef4444", "Aventura": "#22c55e", "Rol": "#a855f7",
    "Plataformas": "#f59e0b", "Carreras": "#06b6d4", "Simulación": "#84cc16",
    "Shooter": "#f97316", "Party": "#ec4899", "Metroidvania": "#6366f1",
    "Roguelike": "#e11d48", "Deportes": "#10b981", "MOBA": "#3b82f6",
    "Puzle": "#eab308", "Arcade": "#f43f5e", "Terror": "#64748b",
    "Sigilo": "#0ea5e9",
}

# Creo la aplicación web
app = Flask(__name__)


def conectar():
    # Me conecto a la base de datos y pido las filas como diccionario
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


# Funciones que uso dentro de las plantillas ##################
@app.context_processor
def funciones_plantilla():

    def color(genero):
        # Si el género no está en la lista uso un gris
        return COLORES.get(genero, "#475569")

    def iniciales(titulo):
        # "Grand Theft Auto V" -> "GT"
        palabras = (titulo or "?").split()
        return "".join(p[0] for p in palabras[:2]).upper()

    def numero(valor):
        # 300000000 -> "300.000.000"
        try:
            return f"{int(float(valor)):,}".replace(",", ".")
        except (TypeError, ValueError):
            return valor or "-"

    def dinero(valor):
        # 29.99 -> "29,99 €"   y 0 -> "Gratis"
        try:
            valor = float(valor)
        except (TypeError, ValueError):
            return "-"
        if valor == 0:
            return "Gratis"
        return f"{valor:.2f} €".replace(".", ",")

    return dict(color=color, iniciales=iniciales, numero=numero, dinero=dinero)


# Páginas ######################################################

# Catálogo con buscador y filtro por género
@app.route("/")
def inicio():
    texto = request.args.get("q", "").strip()
    genero = request.args.get("genero", "")

    conexion = conectar()
    sql = "SELECT * FROM videojuegos WHERE titulo <> ''"
    parametros = []
    if texto:
        sql += " AND (titulo LIKE ? OR desarrollador LIKE ?)"
        parametros += ["%" + texto + "%", "%" + texto + "%"]
    if genero:
        sql += " AND genero = ?"
        parametros.append(genero)
    sql += " ORDER BY titulo"

    juegos = conexion.execute(sql, parametros).fetchall()
    generos = conexion.execute(
        "SELECT DISTINCT genero FROM videojuegos WHERE genero <> '' ORDER BY genero"
    ).fetchall()
    conexion.close()

    return render_template("catalogo.html", juegos=juegos, generos=generos,
                           texto=texto, genero=genero)


# Ficha de un videojuego
@app.route("/juego/<int:id>")
def juego(id):
    conexion = conectar()
    fila = conexion.execute("SELECT * FROM videojuegos WHERE id = ?", (id,)).fetchone()
    conexion.close()
    if fila is None:
        abort(404)                      # Si no existe, página de error
    return render_template("juego.html", j=fila)


# Formulario para añadir un videojuego
@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


# Recibo el formulario y lo guardo
@app.route("/recibedatos", methods=["POST"])
def recibedatos():
    valores = [request.form.get(c, "") for c in COLUMNAS]
    huecos = ", ".join(["?"] * len(COLUMNAS))

    conexion = conectar()
    conexion.execute(
        "INSERT INTO videojuegos (" + ", ".join(COLUMNAS) + ") VALUES (" + huecos + ")",
        valores,
    )
    conexion.commit()                   # Sin esto no se guarda
    conexion.close()
    return render_template("confirmacion.html", nombre=request.form["titulo"])


# Página del consultor con IA
@app.route("/consultor")
def consultor():
    return render_template("consultor.html", modelo=MODELO)


# La IA ########################################################

def generar_sql(preguntausuario):
    # Le pido a Ollama el SQL para la pregunta del usuario
    pregunta = f"""
    Eres un generador de SQL para SQLite.
    Dame el SQL para:
    - {preguntausuario}
    - La estructura de la tabla es esta:
    {ESQUEMA}
    - Responde SOLO con la sentencia SQL en texto plano.
    - Sin markdown, sin ```, sin la palabra sql delante, sin comentarios ni explicaciones.
    """
    r = requests.post(RUTA_IA, json={
        "model": MODELO,
        "prompt": pregunta,
        "stream": False,
        "options": {"temperature": 0},
    }, timeout=120)
    r.raise_for_status()

    # Limpio la respuesta por si la IA pone ```sql ... ```
    sql = r.json()["response"].strip()
    sql = re.sub(r"^```(?:sql)?\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"\s*```$", "", sql)
    return sql.strip()


def es_solo_lectura(sql):
    # True si la sentencia solo consulta (no cambia datos)
    palabras = sql.split()
    if not palabras:
        return False
    return palabras[0].upper() in ("SELECT", "WITH", "PRAGMA")


@app.route("/consultar", methods=["POST"])
def consultar():
    datos = request.get_json(silent=True) or {}
    preguntausuario = (datos.get("pregunta") or "").strip()
    permitir_cambios = bool(datos.get("permitir_cambios"))

    if not preguntausuario:
        return jsonify({"error": "Escribe una pregunta."}), 400

    # 1. Pido el SQL a la IA
    try:
        sql = generar_sql(preguntausuario)
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "No se puede conectar con Ollama. ¿Está arrancado (ollama serve)?"}), 502
    except Exception as e:
        return jsonify({"error": f"Error al consultar la IA: {e}"}), 502

    if not sql:
        return jsonify({"error": "La IA no ha devuelto ningún SQL."}), 502

    # 2. Protejo la base de datos
    if not permitir_cambios and not es_solo_lectura(sql):
        return jsonify({
            "sql": sql,
            "error": "La IA ha generado una sentencia que modifica datos. "
                     "Activa «Permitir modificar datos» si quieres ejecutarla.",
        }), 400

    # 3. Ejecuto el SQL
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


# Página de error 404
@app.errorhandler(404)
def no_encontrado(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
