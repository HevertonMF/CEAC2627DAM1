import requests																# Importamos librería de requests
from lxml import html													# Importamos librería de XML

url = "https://encuentrame.pythonanywhere.com"						# Indicamos la URL

try:
    contenido = requests.get(url, timeout=10)			# Cojo el contenido de la web en crudo
    contenido.raise_for_status()									# Compruebo si hubo un error HTTP al cargar la página

    arbol = html.fromstring(contenido.content)		# El contenido crudo lo convierto a HTML (XML con estructura)

    titulo = arbol.xpath("//title/text()")				# Busco el titulo (title)

    print(titulo[0].strip() if titulo else "Sin título")	# Lo imprimo en pantalla

except requests.exceptions.RequestException as erro:
    print(f"No fue posible acceder a la página: {erro}")