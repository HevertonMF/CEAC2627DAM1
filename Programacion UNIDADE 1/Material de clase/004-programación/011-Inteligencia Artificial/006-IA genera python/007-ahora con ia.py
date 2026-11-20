import os
import re
import sys
import time
import threading
import subprocess

import requests

# ─────────────────────────── Configuración ───────────────────────────
RUTA = "http://localhost:11434/api/generate"
MODELO = "qwen2.5-coder:7b"
ARCHIVO = "miprogramaconIA.py"
INTENTOS = 3

# ─────────────────────────── Colores de la consola ───────────────────
os.system("")  # activa los colores en la consola de Windows
sys.stdout.reconfigure(encoding="utf-8")  # para que se vean los ✔ y los marcos
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
CIAN = "\033[96m"
GRIS = "\033[90m"
NEGRITA = "\033[1m"
FIN = "\033[0m"

# ─────────────────────────── El encargo ──────────────────────────────
TAREA = """
Crea una calculadora de IVA mediante Flask.

REQUISITOS:
- Interfaz web moderna y visualmente atractiva con colores ricos.
- Formulario para introducir una cantidad.
- Selector de IVA: 4%, 10% y 21%.
- Calcular base imponible, IVA y total.
- Mostrar los resultados en la misma página.
- Validar las entradas del usuario.
- Diseño responsive.
"""

REGLAS = """
Eres un generador automático de código Python.
Tu respuesta se guardará DIRECTAMENTE en un archivo .py y se ejecutará con Python.

REGLAS OBLIGATORIAS:
1. Genera UN ÚNICO ARCHIVO Python con toda la aplicación.
2. Usa Flask para el servidor web.
3. NO crees carpetas templates ni static. NO uses render_template.
4. El HTML va en una cadena multilínea y se pinta con render_template_string.
5. El CSS va en una etiqueta <style> y el JavaScript en <script>, dentro del HTML.
6. Incluye todos los imports necesarios.
7. Arranca con:
   if __name__ == "__main__":
       app.run(debug=True)
8. Sin comentarios, sin explicaciones, sin Markdown, sin ```.
9. La primera línea debe ser código Python válido.

DEVUELVE ÚNICAMENTE CÓDIGO PYTHON EJECUTABLE.
"""


def titulo():
    print(f"""
{CIAN}{NEGRITA}╔══════════════════════════════════════════╗
║       Generador de apps con Ollama       ║
╚══════════════════════════════════════════╝{FIN}
{GRIS}  Modelo : {MODELO}
  Destino: {ARCHIVO}{FIN}
""")


def esperar_con_ruedita(funcion):
    """Ejecuta la función y mientras tanto enseña una ruedita con los segundos."""
    resultado = {}

    def trabajo():
        try:
            resultado["valor"] = funcion()
        except Exception as error:
            resultado["error"] = error

    hilo = threading.Thread(target=trabajo)
    hilo.start()

    ruedita = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    inicio = time.time()
    i = 0
    while hilo.is_alive():
        segundos = time.time() - inicio
        print(f"\r  {CIAN}{ruedita[i % len(ruedita)]}{FIN} La IA está escribiendo... {GRIS}{segundos:.0f}s{FIN}", end="", flush=True)
        i += 1
        time.sleep(0.1)
    print("\r" + " " * 50 + "\r", end="")

    if "error" in resultado:
        raise resultado["error"]
    return resultado["valor"], time.time() - inicio


def preguntar_a_la_ia(prompt):
    respuesta = requests.post(
        RUTA,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 4096},
        },
        timeout=600,
    )
    respuesta.raise_for_status()
    return respuesta.json()["response"]


def limpiar(codigo):
    """Quita los ```python ... ``` por si la IA los pone igualmente."""
    codigo = codigo.strip()
    codigo = re.sub(r"^\s*```(?:python|py)?\s*\n", "", codigo, flags=re.IGNORECASE)
    codigo = re.sub(r"\n?\s*```\s*$", "", codigo)
    return codigo.strip()


def revisar(codigo):
    """Devuelve None si el código está bien, o el texto del problema."""
    try:
        compile(codigo, ARCHIVO, "exec")
    except SyntaxError as error:
        return f"Error de sintaxis en la línea {error.lineno}: {error.msg}"
    if "Flask" not in codigo:
        return "El código no usa Flask"
    if "app.run" not in codigo:
        return "Falta el app.run para arrancar el servidor"
    return None


def generar():
    prompt = REGLAS + "\nTAREA:\n" + TAREA

    for intento in range(1, INTENTOS + 1):
        print(f"{NEGRITA}Intento {intento} de {INTENTOS}{FIN}")
        texto, segundos = esperar_con_ruedita(lambda: preguntar_a_la_ia(prompt))
        codigo = limpiar(texto)
        problema = revisar(codigo)

        if problema is None:
            print(f"  {VERDE}✔ Código válido{FIN} {GRIS}({segundos:.0f}s){FIN}")
            return codigo

        print(f"  {AMARILLO}✘ {problema}{FIN} {GRIS}({segundos:.0f}s){FIN}")
        # Le paso el fallo a la IA para que lo corrija en el siguiente intento
        prompt = (REGLAS + "\nTAREA:\n" + TAREA +
                  f"\nTu intento anterior falló: {problema}. Corrígelo.\n")

    return None


def main():
    titulo()

    try:
        codigo = generar()
    except requests.exceptions.ConnectionError:
        print(f"{ROJO}✘ No puedo conectar con Ollama.{FIN} ¿Está encendido? Prueba con: {NEGRITA}ollama serve{FIN}")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print(f"{ROJO}✘ La IA ha tardado demasiado (más de 10 minutos).{FIN}")
        sys.exit(1)
    except requests.exceptions.HTTPError as error:
        print(f"{ROJO}✘ Ollama ha devuelto un error:{FIN} {error}")
        print(f"  ¿Tienes el modelo? Prueba con: {NEGRITA}ollama pull {MODELO}{FIN}")
        sys.exit(1)

    if codigo is None:
        print(f"\n{ROJO}✘ La IA no ha conseguido un código válido en {INTENTOS} intentos.{FIN}")
        sys.exit(1)

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        archivo.write(codigo + "\n")

    lineas = codigo.count("\n") + 1
    print(f"\n{VERDE}{NEGRITA}✔ {ARCHIVO} generado correctamente{FIN} {GRIS}({lineas} líneas){FIN}\n")

    if input(f"¿Lo arranco ahora? {GRIS}(s/n){FIN} ").strip().lower() == "s":
        print(f"{CIAN}Abre http://127.0.0.1:5000 en el navegador. Para pararlo: Ctrl+C{FIN}\n")
        try:
            subprocess.run([sys.executable, ARCHIVO])
        except KeyboardInterrupt:
            print(f"\n{GRIS}Servidor parado.{FIN}")


if __name__ == "__main__":
    main()