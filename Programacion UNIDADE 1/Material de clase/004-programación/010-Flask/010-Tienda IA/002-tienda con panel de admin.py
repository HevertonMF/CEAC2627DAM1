from flask import Flask,render_template,request	# Importo flask para crear una web
import json	# Importo json para poder enviar json
import sqlite3	# Import sqlite3 para poder conectarme a una base de datos
from datetime import datetime # Quiero usar la fecha
import os # Para comprobar si existe un archivo

aplicacion = Flask("__name__") 

# Al arrancar, si la tienda tiene pocos productos, añado los del archivo 001-mas productos.sql
def preparabasededatos():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos")
    cuantos = cursor.fetchone()[0]
    if cuantos < 50 and os.path.exists("001-mas productos.sql"):
        with open("001-mas productos.sql", encoding="utf-8") as archivo:
            cursor.executescript(archivo.read())
        conexion.commit()
        print("He añadido los productos nuevos a la base de datos")
    conexion.close()

# ruta de la tienda
@aplicacion.route("/")
def inicio():
  return render_template("tienda.html")

# ruta del panel de administración
@aplicacion.route("/admin")
def admin():
  return render_template("admin.html")

# ruta de dame los datos
@aplicacion.route("/datos")
def datos():
    conexion = sqlite3.connect("tienda.db") # Me conecto a la base de datos
    conexion.row_factory = sqlite3.Row # Lo que venga lo quiero como diccionario
    cursor = conexion.cursor() # Creo un cursor necesario
    cursor.execute("SELECT * FROM productos") # Le pido los artículos
    productos = cursor.fetchall() # Cargo los artículos en una variable
    conexion.close() # Cierro la conexión
    return json.dumps([dict(producto) for producto in productos]) # Convierte cada fila de la base de datos en un diccionario

# ruta de dame los pedidos (para el panel de administración)
@aplicacion.route("/pedidos")
def pedidos():
    conexion = sqlite3.connect("tienda.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pedidos ORDER BY id DESC") # Los más nuevos primero
    filas = cursor.fetchall()
    conexion.close()
    return json.dumps([dict(fila) for fila in filas], ensure_ascii=False)
  
# ruta de inserta pedido
@aplicacion.route("/insertapedido", methods=['POST'])
def insertapedido():
    fecha = datetime.now()
    pedido = request.get_json()
    print(pedido)

    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO pedidos VALUES(
            NULL,
            ?,
            ?,
            ?
        )
    """, (
        fecha.strftime("%Y%m%d%H%M%S"),       # Número de pedido
        fecha.strftime("%Y-%m-%d %H:%M"),     # Fecha legible
        json.dumps(pedido, ensure_ascii=False)
    ))

    conexion.commit()
    conexion.close()

    return "ok tu pedido ha sido insertado"

# ruta de borra pedido (desde el panel de administración)
@aplicacion.route("/borrapedido", methods=['POST'])
def borrapedido():
    datos = request.get_json() # Me llega {"id": 3}
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM pedidos WHERE id = ?", (datos["id"],))
    conexion.commit()
    conexion.close()
    return "ok pedido eliminado"

# ruta de actualiza pedido (desde el panel de administración)
@aplicacion.route("/actualizapedido", methods=['POST'])
def actualizapedido():
    datos = request.get_json() # Me llega {"id": 3, "carga": [{"nombre":..., "precio":...}]}
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE pedidos SET carga = ? WHERE id = ?", (
        json.dumps(datos["carga"], ensure_ascii=False),
        datos["id"]
    ))
    conexion.commit()
    conexion.close()
    return "ok pedido actualizado"

if __name__ == "__main__":
  preparabasededatos()
  aplicacion.run()
