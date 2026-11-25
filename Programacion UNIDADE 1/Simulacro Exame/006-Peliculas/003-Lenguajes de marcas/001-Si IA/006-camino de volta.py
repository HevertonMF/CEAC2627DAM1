# Importo la librería de bases de datos
import sqlite3

# Importo la librería de web
from flask import Flask, render_template, request

# Nombre del archivo de la base de datos
BASE_DE_DATOS = "videoteca20261124.db"

# Creo una aplicación web
aplicacion = Flask(__name__)


def conectar():
    # Me conecto a la base de datos y pido los resultados como diccionario
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


# Escucho en la raíz /  → lista de películas
@aplicacion.route("/")
def inicio():
    conexion = conectar()
    películas = conexion.execute("SELECT * FROM películas").fetchall()
    conexion.close()
    return render_template("index.html", datos=películas)


# Muestro el formulario para insertar películas
@aplicacion.route("/formulario")
def formulario():
    return render_template("formulario.html")


# Recibo los datos del formulario y los guardo
@aplicacion.route("/recibedatos", methods=["POST"])
def recibedatos():
    conexion = conectar()
    conexion.execute(
        """
        INSERT INTO películas (titulo, titulo_original, director, genero, sinopsis, anio_estreno, fecha_estreno, duracion_minutos, pais, idioma_original, clasificacion_edades, presupuesto, recaudacion, valoracion_media, numero_valoraciones, numero_visualizaciones, disponible, vista, favorita, imagen_portada, url_trailer, precio_alquiler, precio_compra, formato, subtitulos_disponibles)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            request.form["titulo"],
            request.form["titulo_original"],
            request.form["director"],
            request.form["genero"],
            request.form["sinopsis"],
            request.form["anio_estreno"],
            request.form["fecha_estreno"],
            request.form["duracion_minutos"],
            request.form["pais"],
            request.form["idioma_original"],
            request.form["clasificacion_edades"],
            request.form["presupuesto"],
            request.form["recaudacion"],
            request.form["valoracion_media"],
            request.form["numero_valoraciones"],
            request.form["numero_visualizaciones"],
            request.form["disponible"],
            request.form["vista"],
            request.form["favorita"],
            request.form["imagen_portada"],
            request.form["url_trailer"],
            request.form["precio_alquiler"],
            request.form["precio_compra"],
            request.form["formato"],
            request.form["subtitulos_disponibles"],
        ),
    )
    conexion.commit()  # Sin esto el INSERT no se guarda
    conexion.close()
    return render_template("confirmacion.html", nombre=request.form["titulo"])


if __name__ == "__main__":
    aplicacion.run(debug=True)
