# Primero importo las librerías
import mysql.connector
from flask import Flask

# Creo una nueva aplicación
aplicacion = Flask(__name__)

# METO EL CODIGO DE LA PETICION DENTRO DEL INICIO DE FLASK
@aplicacion.route("/")
def inicio():

  # Me conecto con las credenciales correctas a la base de datos
  connection = mysql.connector.connect(
    host='localhost',
    user='encuentrame',
    password='Encuentrame123$',
    database='encuentrame'
  )

  # Creo un cursor
  cursor = connection.cursor()

  # Ejecuto una petición a la base de datos
  cursor.execute("SELECT nombre, email, telefono, especialidades FROM psicologos")

  # Recupero el resultado de la petición
  filas = cursor.fetchall()

  # Empiezo el documento HTML
  cadena = '''
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
  '''

  # Recorro el resultado y lo pinto en la tabla
  for fila in filas:
    cadena += '''
          <tr>
            <td>'''+str(fila[0])+'''</td>
            <td>'''+str(fila[1])+'''</td>
            <td>'''+str(fila[2])+'''</td>
            <td>'''+str(fila[3]).replace(",", ", ")+'''</td>
          </tr>
    '''

  # Termino el documento HTML
  cadena += '''
        </tbody>
      </table>
    </body>
  </html>
  '''

  # Todo lo que se abre se debe cerrar
  cursor.close()
  connection.close()

  # Devuelvo el HTML al navegador
  return cadena

# Ejecuto la aplicación
if __name__ == "__main__":
  aplicacion.run(debug=True, port=5001)