# Importo la librería de bases de datos
import sqlite3

# Importo la librería de web
from flask import Flask, render_template, request

# Nombre del archivo de la base de datos
BASE_DE_DATOS = "biblioteca20261123.db"

# Creo una aplicación web
aplicacion = Flask(__name__)


def conectar():
    # Me conecto a la base de datos y pido los resultados como diccionario
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


# Escucho en la raíz /  → lista de libros
@aplicacion.route("/")
def inicio():
    conexion = conectar()
    libros = conexion.execute("SELECT * FROM libros").fetchall()
    conexion.close()
    return render_template("Libros.html", datos=libros)


# Muestro el formulario para insertar libros
@aplicacion.route("/formulario")
def formulario():
    return render_template("formulario.html")


# Recibo los datos del formulario y los guardo
@aplicacion.route("/recibedatos", methods=["POST"])
def recibedatos():
    conexion = conectar()
    conexion.execute(
        """
        INSERT INTO libros (titulo, autor, fecha_de_publicacion, sinopsis, editorial, isbn, genero, precio, disponible)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            request.form["titulo"],
            request.form["autor"],
            request.form["fecha_de_publicacion"],
            request.form["sinopsis"],
            request.form["editorial"],
            request.form["isbn"],
            request.form["genero"],
            request.form["precio"],
            request.form["disponible"],
        ),
    )
    conexion.commit()  # Sin esto el INSERT no se guarda
    conexion.close()
    return render_template("confirmacion.html", nombre=request.form["titulo"])


if __name__ == "__main__":
    aplicacion.run(debug=True)
