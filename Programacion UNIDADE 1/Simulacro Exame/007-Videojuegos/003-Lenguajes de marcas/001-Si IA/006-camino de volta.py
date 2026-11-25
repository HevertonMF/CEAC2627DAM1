# Importo la librería de bases de datos
import sqlite3

# Importo la librería de web
from flask import Flask, render_template, request

# Nombre del archivo de la base de datos
BASE_DE_DATOS = "videojuegos20261125.db"

# Creo una aplicación web
aplicacion = Flask(__name__)


def conectar():
    # Me conecto a la base de datos y pido los resultados como diccionario
    conexion = sqlite3.connect(BASE_DE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


# Escucho en la raíz /  → lista de videojuegos
@aplicacion.route("/")
def inicio():
    conexion = conectar()
    videojuegos = conexion.execute("SELECT * FROM videojuegos").fetchall()
    conexion.close()
    return render_template("index.html", datos=videojuegos)


# Muestro el formulario para insertar videojuegos
@aplicacion.route("/formulario")
def formulario():
    return render_template("formulario.html")


# Recibo los datos del formulario y los guardo
@aplicacion.route("/recibedatos", methods=["POST"])
def recibedatos():
    conexion = conectar()
    conexion.execute(
        """
        INSERT INTO videojuegos (titulo, desarrollador, distribuidor, genero, descripcion, anio_lanzamiento, fecha_lanzamiento, plataforma, pais, idioma, clasificacion_edades, presupuesto, ingresos, valoracion_media, numero_valoraciones, unidades_vendidas, disponible, multijugador, favorito, imagen_portada, url_trailer, precio_original, precio_rebajado, espacio_requerido, compras_integradas)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            request.form["titulo"],
                            request.form["desarrollador"],
                            request.form["distribuidor"],
                            request.form["genero"],
                            request.form["descripcion"],
                            request.form["anio_lanzamiento"],
                            request.form["fecha_lanzamiento"],
                            request.form["plataforma"],
                            request.form["pais"],
                            request.form["idioma"],
                            request.form["clasificacion_edades"],
                            request.form["presupuesto"],
                            request.form["ingresos"],
                            request.form["valoracion_media"],
                            request.form["numero_valoraciones"],
                            request.form["unidades_vendidas"],
                            request.form["disponible"],
                            request.form["multijugador"],
                            request.form["favorito"],
                            request.form["imagen_portada"],
                            request.form["url_trailer"],
                            request.form["precio_original"],
                            request.form["precio_rebajado"],
                            request.form["espacio_requerido"],
                            request.form["compras_integradas"],
        ),
    )
    conexion.commit()  # Sin esto el INSERT no se guarda
    conexion.close()
    return render_template("confirmacion.html", nombre=request.form["titulo"])


if __name__ == "__main__":
    aplicacion.run(debug=True)
