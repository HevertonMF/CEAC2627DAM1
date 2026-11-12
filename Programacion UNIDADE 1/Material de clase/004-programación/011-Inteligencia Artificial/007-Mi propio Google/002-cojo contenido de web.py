import requests

url = "https://encuentrame.pythonanywhere.com/"

contenido = requests.get(url, timeout=10)

print(contenido.text)

