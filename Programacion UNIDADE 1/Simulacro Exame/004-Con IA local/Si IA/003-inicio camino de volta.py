from flask import Flask,render_template,request
import sqlite3

aplicacion = Flask("__name__") 

connection = sqlite3.connect('examendamceac2627.db')
cursor = connection.cursor()

cursor = connection.cursor(dictionary = True)

@aplicacion.route("/")
def inicio():
  return render_template("inicio.html")

@aplicacion.route("/insertarmedicos",methods=['POST'])
def insertarmedicos():
  print("Hola")
  cursor.execute("SELECT * FROM médicos") # Saco los médicos de la base de datos
  inicio = cursor.fetchall()		# Los meto en una variable
  print(inicio)
  return render_template("inicio.html",proyectos=inicio) # Y se los paso a la plantilla

if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()