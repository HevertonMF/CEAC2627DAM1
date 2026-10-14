from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template(
    	"index3.html",
      nombre = "Heverton",
      apellidos = "Marques Ferreira",
      email = "hevertonmf@gmail.com"
  )
  
if __name__ == "__main__":
  aplicacion.run()
  