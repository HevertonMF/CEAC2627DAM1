import requests

url = "https://encuentrame.pythonanywhere.com/"

contenido = requests.get(url, timeout=10)

ruta = "http://localhost:11434/api/generate"		# La ruta donde ollama escucha
modelo = "codellama:7b" 												# Elijo un modelo
pregunta = "Responde 'si' o 'no': Esta web trata sobre marketing? "+contenido.text+" - Importante, solo quiero un 'si' o un 'no'."		# Elevo un prompt
flujo = False 																	# Desactivo el flujo
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																							# Ejecuto la eticion
print(r.json()["response"])											# Devuelvo el resultado