"""
AMABLE - mini Lovable con Flask + Ollama + SQLite
---------------------------------------------------
Novedades respecto a 005:
  - Historial: se listan todos los proyectos guardados y se pueden volver a abrir
  - Edición: pedir cambios a la IA sobre un proyecto existente o editar el código a mano
  - Versiones: cada cambio guarda una versión y se puede restaurar cualquiera
  - Más rápido: streaming (stream=True), modelo precargado y mantenido en memoria (keep_alive)
  - Progreso: el servidor envía el porcentaje de avance mientras la IA genera
"""
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import requests
import sqlite3
import json
import re
import os
import threading
from datetime import datetime

aplicacion = Flask(__name__)

# ---------------- CONFIGURACIÓN ----------------
OLLAMA = "http://localhost:11434/api/generate"
MODELO = "qwen2.5-coder:7b"
USUARIO = "HMF"
BASE_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "amable.db")
MANTENER_MODELO = "30m"            # Ollama mantiene el modelo cargado 30 min (evita recargarlo en cada petición)
CARACTERES_POR_TOKEN = 3.5         # Aproximación para estimar el progreso

sesion = requests.Session()         # Reutiliza la conexión con Ollama (más rápido)

SISTEMA_CREAR = """Eres un generador de páginas web.
- Devuelve SOLO un documento HTML completo (<!DOCTYPE html> ... </html>)
- CSS dentro de <style> y JavaScript dentro de <script>, todo en un único archivo
- No uses markdown, no uses ```, no des explicaciones
- Diseño moderno, limpio y responsive
- Solo se pueden pedir páginas web; si piden otra cosa, devuelve una página que diga que solo creas webs"""

SISTEMA_EDITAR = """Eres un editor de páginas web.
Recibes el código HTML actual de una página y un cambio que quiere el usuario.
- Aplica el cambio y devuelve el documento HTML COMPLETO ya modificado
- Mantén todo lo demás igual
- No uses markdown, no uses ```, no des explicaciones"""


# ---------------- BASE DE DATOS ----------------
def conectar():
  conexion = sqlite3.connect(BASE_DATOS)
  conexion.row_factory = sqlite3.Row             # Para acceder a las columnas por nombre
  return conexion

def preparar_base_datos():
  """Crea las tablas si no existen y añade las columnas nuevas a la tabla antigua"""
  conexion = conectar()
  cursor = conexion.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS webs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      usuario TEXT, fecha TEXT, pregunta TEXT, respuesta TEXT
    )""")
  columnas = [c["name"] for c in cursor.execute("PRAGMA table_info(webs)")]
  if "titulo" not in columnas:
    cursor.execute("ALTER TABLE webs ADD COLUMN titulo TEXT")
    cursor.execute("UPDATE webs SET titulo = substr(pregunta, 1, 50)")
  if "actualizado" not in columnas:
    cursor.execute("ALTER TABLE webs ADD COLUMN actualizado TEXT")
    cursor.execute("UPDATE webs SET actualizado = fecha")
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS versiones (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      web_id INTEGER, fecha TEXT, peticion TEXT, codigo TEXT, tipo TEXT
    )""")
  # Limpio los ```html que quedaron guardados en proyectos antiguos
  for fila in cursor.execute("SELECT id, respuesta FROM webs WHERE respuesta LIKE '%```%'").fetchall():
    cursor.execute("UPDATE webs SET respuesta = ? WHERE id = ?", (limpiar_codigo(fila["respuesta"]), fila["id"]))
  # Los proyectos antiguos (sin versiones) reciben su versión inicial
  cursor.execute("""
    INSERT INTO versiones (web_id, fecha, peticion, codigo, tipo)
    SELECT id, fecha, pregunta, respuesta, 'ia' FROM webs
    WHERE id NOT IN (SELECT DISTINCT web_id FROM versiones)""")
  conexion.commit()
  conexion.close()

def ahora():
  return datetime.now().strftime("%Y-%m-%d %H:%M")

def guardar_version(cursor, web_id, peticion, codigo, tipo):
  cursor.execute("INSERT INTO versiones (web_id, fecha, peticion, codigo, tipo) VALUES (?,?,?,?,?)",
                 (web_id, ahora(), peticion, codigo, tipo))


# ---------------- UTILIDADES ----------------
def limpiar_codigo(texto):
  """Quita ```html ... ``` y cualquier texto fuera del documento HTML"""
  bloque = re.search(r"```(?:html)?\s*(.*?)```", texto, re.S | re.I)
  if bloque:
    texto = bloque.group(1)
  texto = re.sub(r"^```(?:html)?", "", texto.strip(), flags=re.I).strip()
  inicio = re.search(r"<!doctype html|<html", texto, re.I)
  if inicio:
    texto = texto[inicio.start():]
  fin = texto.lower().rfind("</html>")
  if fin != -1:
    texto = texto[:fin + 7]
  return texto.strip()

def tokens_esperados(codigo_actual=None):
  """Estima cuántos tokens va a generar la IA para poder calcular el porcentaje"""
  if codigo_actual:                                   # Al editar, la respuesta mide más o menos lo mismo que el código actual
    return max(300, int(len(codigo_actual) / CARACTERES_POR_TOKEN * 1.05))
  conexion = conectar()                               # Al crear, uso la media de las webs anteriores
  media = conexion.execute("SELECT AVG(LENGTH(respuesta)) FROM webs").fetchone()[0]
  conexion.close()
  return int(media / CARACTERES_POR_TOKEN) if media else 1200

def linea(datos):
  return json.dumps(datos, ensure_ascii=False) + "\n"

def precargar_modelo():
  """Carga el modelo en memoria al arrancar para que la primera petición sea rápida"""
  try:
    sesion.post(OLLAMA, json={"model": MODELO, "keep_alive": MANTENER_MODELO}, timeout=120)
    print("Modelo", MODELO, "cargado en memoria")
  except Exception as error:
    print("No se pudo precargar el modelo (¿está Ollama encendido?):", error)


# ---------------- RUTAS ----------------
@aplicacion.route("/")
def inicio():
  return render_template("principal.html")

@aplicacion.route("/api/proyectos")
def listar_proyectos():
  conexion = conectar()
  filas = conexion.execute("""
    SELECT w.id, w.titulo, w.fecha, w.actualizado,
           (SELECT COUNT(*) FROM versiones v WHERE v.web_id = w.id) AS num_versiones
    FROM webs w ORDER BY w.actualizado DESC, w.id DESC""").fetchall()
  conexion.close()
  return jsonify([dict(f) for f in filas])

@aplicacion.route("/api/proyectos/<int:web_id>")
def ver_proyecto(web_id):
  conexion = conectar()
  web = conexion.execute("SELECT * FROM webs WHERE id = ?", (web_id,)).fetchone()
  if not web:
    conexion.close()
    return jsonify({"error": "No existe"}), 404
  versiones = conexion.execute(
    "SELECT id, fecha, peticion, tipo FROM versiones WHERE web_id = ? ORDER BY id DESC", (web_id,)).fetchall()
  conexion.close()
  datos = dict(web)
  datos["versiones"] = [dict(v) for v in versiones]
  return jsonify(datos)

@aplicacion.route("/api/proyectos/<int:web_id>", methods=["PUT"])
def guardar_manual(web_id):
  """Guarda los cambios hechos a mano en el editor de código (o un cambio de título)"""
  datos = request.get_json()
  conexion = conectar()
  cursor = conexion.cursor()
  if "titulo" in datos:
    cursor.execute("UPDATE webs SET titulo = ? WHERE id = ?", (datos["titulo"].strip()[:80], web_id))
  if "codigo" in datos:
    cursor.execute("UPDATE webs SET respuesta = ?, actualizado = ? WHERE id = ?", (datos["codigo"], ahora(), web_id))
    guardar_version(cursor, web_id, "Edición manual", datos["codigo"], "manual")
  conexion.commit()
  conexion.close()
  return jsonify({"ok": True})

@aplicacion.route("/api/proyectos/<int:web_id>", methods=["DELETE"])
def borrar_proyecto(web_id):
  conexion = conectar()
  conexion.execute("DELETE FROM versiones WHERE web_id = ?", (web_id,))
  conexion.execute("DELETE FROM webs WHERE id = ?", (web_id,))
  conexion.commit()
  conexion.close()
  return jsonify({"ok": True})

@aplicacion.route("/api/proyectos/<int:web_id>/restaurar/<int:version_id>", methods=["POST"])
def restaurar_version(web_id, version_id):
  conexion = conectar()
  cursor = conexion.cursor()
  version = cursor.execute("SELECT * FROM versiones WHERE id = ? AND web_id = ?", (version_id, web_id)).fetchone()
  if not version:
    conexion.close()
    return jsonify({"error": "No existe"}), 404
  cursor.execute("UPDATE webs SET respuesta = ?, actualizado = ? WHERE id = ?", (version["codigo"], ahora(), web_id))
  guardar_version(cursor, web_id, "Restaurada versión del " + version["fecha"], version["codigo"], "restaurar")
  conexion.commit()
  conexion.close()
  return jsonify({"ok": True})

@aplicacion.route("/ver/<int:web_id>")
def ver_web(web_id):
  """Abre la web generada sola, en una pestaña nueva"""
  conexion = conectar()
  web = conexion.execute("SELECT respuesta FROM webs WHERE id = ?", (web_id,)).fetchone()
  conexion.close()
  return web["respuesta"] if web else ("No existe", 404)

@aplicacion.route("/api/generar", methods=["POST"])
def generar():
  """
  Crea una web nueva o edita una existente (si llega un id).
  La respuesta es un flujo de líneas JSON:
    {"tipo":"progreso","porcentaje":..,"fase":".."}
    {"tipo":"token","texto":".."}
    {"tipo":"fin","id":..,"codigo":".."}
    {"tipo":"error","mensaje":".."}
  """
  datos = request.get_json()
  peticion = (datos.get("peticion") or "").strip()
  web_id = datos.get("id")
  if not peticion:
    return jsonify({"error": "Escribe una petición"}), 400

  codigo_actual = None
  if web_id:
    conexion = conectar()
    fila = conexion.execute("SELECT respuesta FROM webs WHERE id = ?", (web_id,)).fetchone()
    conexion.close()
    codigo_actual = fila["respuesta"] if fila else None

  if codigo_actual:
    sistema = SISTEMA_EDITAR
    prompt = "CÓDIGO ACTUAL:\n" + codigo_actual + "\n\nCAMBIO QUE QUIERE EL USUARIO:\n" + peticion
  else:
    sistema = SISTEMA_CREAR
    prompt = "Petición del usuario: " + peticion
  esperados = tokens_esperados(codigo_actual)

  def flujo():
    yield linea({"tipo": "progreso", "porcentaje": 2, "fase": "Enviando petición a la IA..."})
    texto = ""
    generados = 0
    try:
      r = sesion.post(OLLAMA, stream=True, timeout=600, json={
        "model": MODELO,
        "system": sistema,
        "prompt": prompt,
        "stream": True,                              # Ahora SÍ palabra por palabra: se ve el avance
        "keep_alive": MANTENER_MODELO,
        "options": {
          "temperature": 0.3,
          "num_ctx": 8192 if codigo_actual else 4096,  # Contexto justo: menos memoria = más rápido
          "num_predict": 6000,
        },
      })
      r.raise_for_status()
      yield linea({"tipo": "progreso", "porcentaje": 5, "fase": "La IA está pensando..."})
      for fragmento in r.iter_lines():
        if not fragmento:
          continue
        parte = json.loads(fragmento)
        if parte.get("error"):
          raise Exception(parte["error"])
        trozo = parte.get("response", "")
        if trozo:
          texto += trozo
          generados += 1
          yield linea({"tipo": "token", "texto": trozo})
          if generados % 5 == 0:                     # Cada 5 tokens actualizo el porcentaje (5% → 95%)
            porcentaje = min(95, 5 + int(90 * generados / esperados))
            yield linea({"tipo": "progreso", "porcentaje": porcentaje,
                         "fase": "Generando código... (" + str(generados) + " tokens)"})
        if parte.get("done"):
          break
    except Exception as error:
      yield linea({"tipo": "error", "mensaje": "Error con Ollama: " + str(error)})
      return

    yield linea({"tipo": "progreso", "porcentaje": 97, "fase": "Guardando en la base de datos..."})
    codigo = limpiar_codigo(texto)
    try:
      conexion = conectar()
      cursor = conexion.cursor()
      if codigo_actual:
        cursor.execute("UPDATE webs SET respuesta = ?, actualizado = ? WHERE id = ?", (codigo, ahora(), web_id))
        nuevo_id = web_id
      else:
        cursor.execute("""INSERT INTO webs (usuario, fecha, pregunta, respuesta, titulo, actualizado)
                          VALUES (?,?,?,?,?,?)""",
                       (USUARIO, ahora(), peticion, codigo, peticion[:50], ahora()))
        nuevo_id = cursor.lastrowid
      guardar_version(cursor, nuevo_id, peticion, codigo, "ia")
      conexion.commit()
      conexion.close()
    except Exception as error:
      yield linea({"tipo": "error", "mensaje": "Error al guardar en la base de datos: " + str(error)})
      return
    yield linea({"tipo": "progreso", "porcentaje": 100, "fase": "¡Listo!"})
    yield linea({"tipo": "fin", "id": nuevo_id, "codigo": codigo})

  return Response(stream_with_context(flujo()), mimetype="application/x-ndjson",
                  headers={"X-Accel-Buffering": "no", "Cache-Control": "no-cache"})


if __name__ == "__main__":
  preparar_base_datos()
  threading.Thread(target=precargar_modelo, daemon=True).start()   # Carga el modelo sin bloquear el arranque
  aplicacion.run(debug=True, threaded=True)
