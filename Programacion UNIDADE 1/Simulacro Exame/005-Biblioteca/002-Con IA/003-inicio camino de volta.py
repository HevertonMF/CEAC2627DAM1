from flask import Flask,render_template,request
import sqlite3

aplicacion = Flask("__name__") 

connection = sqlite3.connect('biblioteca20261123.db')
cursor = connection.cursor()

cursor = connection.cursor(dictionary = True)

@aplicacion.route("/")
def inicio():
  return render_template("index.html")

@aplicacion.route("/insertarlibros",methods=['POST'])
def insertarmedicos():
  print("Hola")
  cursor.execute("SELECT * FROM libros") # Saco los médicos de la base de datos
  inicio = cursor.fetchall()		# Los meto en una variable
  print(inicio)
  return render_template("index.html", datos=inicio) # Y se los paso a la plantilla

if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()