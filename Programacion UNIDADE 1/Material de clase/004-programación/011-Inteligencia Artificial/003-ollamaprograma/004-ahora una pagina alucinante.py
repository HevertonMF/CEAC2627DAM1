from flask import Flask	# Para la web
import requests																		# Para hacer peticiones http

aplicacion = Flask("__name__") 										# Creamos una aplicacion


@aplicacion.route("/")														# Escucho en la raiz
def inicio():
  ruta = "http://localhost:11434/api/generate"		# Llamo a ollama
  modelo = "codellama:7b"										# Elijo el modelo
  pregunta = """
- Create an HTML web page that is a copy of Facebook.
- Add CSS styling similar to Facebook's.
- Provide only the code; no comments, no code blocks, no Markdown formatting—just the HTML, CSS, and images (such as profile pictures and feed content), designed to look like the Facebook homepage.
    """ 																					# Es la pregunta que le lanzo
  flujo = False																		# No me des palabra por palabra
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })																							# Ejecutamos la petición
  mirespuesta = str(r.json()["response"])					# Obtenemos la respuesta
  return mirespuesta															# Lo que sea que venga, lo pinto en html

if __name__ == "__main__":
  aplicacion.run()