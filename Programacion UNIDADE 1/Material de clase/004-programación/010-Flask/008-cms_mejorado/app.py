# Flask permite crear webs
# session guarda quién ha iniciado sesión
# redirect y url_for mandan al usuario a otra página
# flash enseña mensajes ("Artículo guardado", etc.)
from flask import Flask, render_template, request, session, redirect, url_for, flash
# Para comprobar la contraseña sin guardarla en texto plano
from werkzeug.security import check_password_hash
import mysql.connector

aplicacion = Flask(__name__)
# Clave para firmar la sesión (cámbiala por cualquier texto largo)
aplicacion.secret_key = "cambia-esto-por-un-texto-largo-y-secreto"

# Usuario y contraseña del administrador
# Genera el hash con:  python generar_clave.py
USUARIO_ADMIN = "heverton"
CLAVE_ADMIN = "scrypt:32768:8:1$2pGdAPRHBIkwMYkE$b59e82a401171b4da21a0f0f90c1ad0071aa0a88e9f14ede108f8ebbbf37d763946766ed09bed500e71b194a6cf8a0a6a38e3055309cc7a3bba06878fa5444ef"

# Abro una conexión nueva en cada petición
# (si la dejo abierta todo el rato, MySQL la cierra y la web falla)
def conectar():
  return mysql.connector.connect(
    host='localhost',
    user='blogceacdam2627',
    password='CEAC123$',
    database='blogceacdam2627'
  )

# ---------- PARTE PÚBLICA ----------

@aplicacion.route("/")
def inicio():
  conexion = conectar()
  cursor = conexion.cursor(dictionary=True)
  # Los más nuevos primero
  cursor.execute("SELECT * FROM articulos ORDER BY fecha DESC")
  articulos = cursor.fetchall()
  conexion.close()
  return render_template("frente.html", articulos=articulos)

# ---------- LOGIN ----------

@aplicacion.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    usuario = request.form['usuario']
    clave = request.form['clave']
    if usuario == USUARIO_ADMIN and check_password_hash(CLAVE_ADMIN, clave):
      session['admin'] = True
      return redirect(url_for('tabla'))
    flash("Usuario o contraseña incorrectos")
  return render_template("login.html")

@aplicacion.route("/logout")
def logout():
  session.clear()
  return redirect(url_for('inicio'))

# ---------- PANEL DE ADMINISTRACIÓN ----------
# Todas estas rutas comprueban primero si has iniciado sesión

@aplicacion.route("/tabla")
def tabla():
  if not session.get('admin'):
    return redirect(url_for('login'))
  conexion = conectar()
  cursor = conexion.cursor(dictionary=True)
  cursor.execute("SELECT * FROM articulos ORDER BY fecha DESC")
  todoslosarticulos = cursor.fetchall()
  conexion.close()
  return render_template("tabla.html", tepasolosarticulos=todoslosarticulos)

@aplicacion.route("/formulario")
def formulario():
  if not session.get('admin'):
    return redirect(url_for('login'))
  return render_template("formulario.html")

@aplicacion.route("/inserta", methods=['POST'])
def inserta():
  if not session.get('admin'):
    return redirect(url_for('login'))
  conexion = conectar()
  cursor = conexion.cursor()
  # Los %s los rellena MySQL de forma segura (evita la inyección SQL)
  cursor.execute(
    "INSERT INTO articulos (titulo, fecha, contenido) VALUES (%s, %s, %s)",
    (request.form['titulo'], request.form['fecha'], request.form['contenido'])
  )
  conexion.commit()
  conexion.close()
  flash("Artículo publicado")
  return redirect(url_for('tabla'))

@aplicacion.route("/elimina/<int:id>", methods=['POST'])
def elimina(id):
  if not session.get('admin'):
    return redirect(url_for('login'))
  conexion = conectar()
  cursor = conexion.cursor()
  cursor.execute("DELETE FROM articulos WHERE id = %s", (id,))
  conexion.commit()
  conexion.close()
  flash("Artículo eliminado")
  return redirect(url_for('tabla'))

if __name__ == "__main__":
  aplicacion.run(debug=True)
