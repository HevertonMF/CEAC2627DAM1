# Primero importo Flask y la librería de conexión
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Función para quedarme solo con el año de una fecha "dd/mm/aaaa"
def anio(fecha):
  if fecha is None:
    return None
  if fecha == "Actual":
    return "la actualidad"
  return fecha[-4:]

@app.route("/")
def inicio():
  # Me conecto a la base de datos con el usuario que hemos creado
  connection = mysql.connector.connect(
    host='localhost',
    user='curriculum',
    password='CEAC123$',
    database='curriculum'
  )

  # Creo un cursor que me devuelve cada fila como diccionario
  cursor = connection.cursor(dictionary=True)

  # Datos personales (solo hay una fila)
  cursor.execute("SELECT * FROM datos_personales WHERE id = 1")
  persona = cursor.fetchone()

  # Datos de contacto
  cursor.execute("SELECT * FROM datos_contacto WHERE id_usuario = 1")
  contacto = cursor.fetchall()

  # Redes sociales
  cursor.execute("SELECT * FROM redes_sociales WHERE id_usuario = 1")
  redes = cursor.fetchall()

  # Idiomas
  cursor.execute("SELECT * FROM idiomas WHERE id_usuario = 1")
  idiomas = cursor.fetchall()

  # Habilidades
  cursor.execute("SELECT * FROM habilidades WHERE id_usuario = 1")
  habilidades = cursor.fetchall()

  # Experiencias laborales
  cursor.execute("SELECT * FROM experiencias_laborales WHERE id_usuario = 1 ORDER BY id")
  experiencias = cursor.fetchall()

  # Formación
  cursor.execute("SELECT * FROM formacion WHERE id_usuario = 1 ORDER BY id")
  formacion = cursor.fetchall()

  connection.close()

  # Le paso todos los datos a la plantilla
  return render_template(
    "curriculum.html",
    persona=persona,
    contacto=contacto,
    redes=redes,
    idiomas=idiomas,
    habilidades=habilidades,
    experiencias=experiencias,
    formacion=formacion,
    anio=anio
  )

if __name__ == "__main__":
  app.run(debug=True)
