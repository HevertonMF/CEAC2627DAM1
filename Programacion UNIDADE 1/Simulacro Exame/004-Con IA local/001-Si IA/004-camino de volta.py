# Importo la librería de bases de datos
import sqlite3

# Importo la librería de web
from flask import Flask, render_template, request

# Nombre del archivo de la base de datos
BASE_DE_DATOS = "examendamceac2627.db"

# Creo una aplicación web
aplicacion = Flask(__name__)


def conectar():
    # Me conecto a la base de datos y pido los resultados como diccionario
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


# Escucho en la raíz /  → lista de médicos
@aplicacion.route("/")
def inicio():
    conexion = conectar()
    medicos = conexion.execute("SELECT * FROM médicos").fetchall()
    conexion.close()
    return render_template("Médicos.html", datos=medicos)


# Muestro el formulario para insertar médicos
@aplicacion.route("/formulario")
def formulario():
    return render_template("formulario.html")


# Recibo los datos del formulario y los guardo
@aplicacion.route("/recibedatos", methods=["POST"])
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
    conexion.commit()  # Sin esto el INSERT no se guarda
    conexion.close()
    return render_template("confirmacion.html", nombre=request.form["nombre"])


if __name__ == "__main__":
    aplicacion.run(debug=True)
