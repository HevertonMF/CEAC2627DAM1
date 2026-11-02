# Primero importo las librerías
import mysql.connector
from flask import Flask

# Me conecto con las credenciales correctas a la base de datos
connection = mysql.connector.connect(
  host='localhost',
  user='encuentrame',
  password='Encuentrame123$',
  database='encuentrame'
)

# Creo un cursor
cursor = connection.cursor()

# Creo una nueva aplicación
aplicacion = Flask("__name__")

# METO EL CODIGO DE LA PETICION DENTRO DEL INICIO DE FLASK
@aplicacion.route("/")
def inicio():
  #################### TROZO DE ARRIBA #########################
  cadena = """
  <!doctype html>
  <html>
    <head>
      <meta charset="utf-8">
    </head>
    <body>
      <table border=1>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Teléfono</th>
            <th>Especialidades</th>
          </tr>
        </thead>
        <tbody>
  """
  # Ejecuto una petición a la base de datos
  cursor.execute("SELECT * FROM psicologos")	

  # Recupero el resultado de la petición
  filas = cursor.fetchall()	

  # Recorro el resultado y lo pinto en pantalla
  for fila in filas:
    #################### TROZO DEL MEDIO VA DENTRO DEL FOR #######################
    cadena += """
    <tr>
          <td>"""+str(fila[1])+"""</td>
          <td>"""+str(fila[2])+"""</td>
          <td>"""+str(fila[3])+"""</td>
          <td>"""+str(fila[4])+"""</td>
        </tr>
    """
  #################### TROZO DE ABAJO #####################
  cadena += """
        </tbody>
    </table>
  </body>
</html>
  """
  return cadena

if __name__ == "__main__":
  aplicacion.run(port=5001)
  
# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()