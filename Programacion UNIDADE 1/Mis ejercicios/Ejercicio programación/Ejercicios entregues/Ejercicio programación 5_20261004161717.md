# Reporte de proyecto

## Información de generación

- **Fecha:** 4/10/2026, 18:17:01
- **Proyecto documentado:** `Ejercicio programación 5`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio programación 5
    ├── 1-Ejercicios
    │   ├── 001-flujos. tipos de bytes y caracteres
    │   │   ├── 000-introducion.md
    │   │   ├── 001-escribir.py
    │   │   ├── 002-leer.py
    │   │   └── agenda.txt
    │   ├── 002-Ficheros de datos. Registros
    │   │   ├── 000-introducion.md
    │   │   ├── 001-miniagenda.py
    │   │   ├── agenda.csv
    │   │   └── pastas
    │   ├── 003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros
    │   │   ├── 000-introducion.md
    │   │   ├── 001-programa agenda.py
    │   │   ├── 002-agora com IA.py
    │   │   └── agenda.csv
    │   ├── 004-Utilización de los sistemas de ficheros
    │   │   ├── 001-crear carpeta.py
    │   │   ├── 002-eliminar carpeta.py
    │   │   ├── 003-crear archivo.py
    │   │   ├── 004-eliminar archivo.py
    │   │   ├── 005-caminar.py
    │   │   ├── 006-caminar por partes.py
    │   │   └── 007-arbol.py
    │   ├── 006-Entrada desde teclado. Salida a pantalla. Formatos de visualización
    │   │   ├── 001-miniagenda.py
    │   │   ├── 002-bucle infinito.py
    │   │   ├── 003-ahora quiero leer y escribir.py
    │   │   ├── 004-opcion salir.py
    │   │   ├── 005-guardar agenda en carpeta.py
    │   │   ├── 006-try except.py
    │   │   ├── agenda.csv
    │   │   └── mibasededatos
    │   │       └── agenda.csv
    │   ├── 007-Interfaces gráficas
    │   │   ├── 001-ventana.py
    │   │   ├── 002-geometria.py
    │   │   ├── 003-label.py
    │   │   ├── 004-boton.py
    │   │   ├── 005-entrada.py
    │   │   ├── 006-separaciones.py
    │   │   └── para instalar
    │   ├── 008-Concepto de evento
    │   │   ├── 000-introdución.md
    │   │   ├── 001-continuamos ejercicio anterior.py
    │   │   ├── 002-comando en el boton.py
    │   │   ├── 003-solucionamos el error.py
    │   │   ├── 004-calculos.py
    │   │   ├── 005-conversion de tipo.py
    │   │   ├── 006-la calculadora de iva.py
    │   │   └── 007-mi calculadora de meta de kilometros.py
    │   └── 009-Criação de controladores de eventos
    │       ├── 001-frame.py
    │       ├── 002-mostrar y ocultar.py
    │       ├── 003-funcion de los botones.py
    │       ├── 004-completando las funciones.py
    │       ├── 005-grid.py
    │       ├── 006-grid ahora si.py
    │       ├── 007-esquema tabla.md
    │       ├── 008-escribir archivo.py
    │       ├── 009-ahora guardo en archivo.py
    │       ├── 010-campo de texto.py
    │       ├── 011-leer.py
    │       ├── 012-grid y marco.py
    │       ├── 013-ia.py
    │       └── 014-pip instal.md
    ├── 2-Proyecto
    │   ├── 001-Gestión de ciclistas.py
    │   ├── 002-Gestión de ciclistas IA.py
    │   └── ciclistas.csv
    └── 3-Resultado de aprendizaje
        └── Resultado de aprendizaje.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite.

## Código (intercalado)

### Ejercicio programación 5/1-Ejercicios/001-flujos. tipos de bytes y caracteres

**000-introducion.md**

```markdown
```

**001-escribir.py**

```python
archivo = open("agenda.txt",'w')
archivo.write("Esto es una prueba")
archivo.close()

```

**002-leer.py**

```python
archivo = open("agenda.txt",'r')
lineas = archivo.readlines()
print(lineas)
archivo.close()

```

**agenda.txt**

```text
Esto es una prueba
```

### Ejercicio programación 5/1-Ejercicios/002-Ficheros de datos. Registros

**000-introducion.md**

```markdown
```

**001-miniagenda.py**

```python
while True:
  nombre = input("Dime un nombre: ")
  apellidos = input("Dime unos apellidos: ")
  email = input("Dime un email: ")
  archivo = open("agenda.csv",'a')
  archivo.write(nombre+","+apellidos+","+email+"\n")
  archivo.close()
```

### Ejercicio programación 5/1-Ejercicios/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros

**000-introducion.md**

```markdown
```

**001-programa agenda.py**

```python
print("Programa registro de ciclistas v0.2")
print("por Heverton Marques")

while True:
    print("Escoge una opcion")
    print("1.-Insertar un registro")
    print("2.-Listado de registros")

    opcion = input("Indica tu opción: ")

    if opcion == "1":
        nombre = input("Introduce un nombre: ")
        apellidos = input("Introduce unos apellidos: ")
        telefono = input("Introduce un teléfono: ")

        categoria_bicicleta = input("Introduce una categoría de bicicleta: ")

        archivo = open("agenda.csv", "a")
        archivo.write(nombre + "," + apellidos + "," + telefono + "," + categoria_bicicleta + "\n")
        archivo.close()

    elif opcion == "2":
        archivo = open("agenda.csv", "r")
        lineas = archivo.readlines()

        for linea in lineas:
            print(linea, end="")

        archivo.close()

    else:
        print("Opción no válida")
```

**002-agora com IA.py**

```python
"""
Programa registro de ciclistas
Versión 0.3 
por Heverton Marques
"""

import os


# ------------------------------------------------------------------
# Códigos ANSI para dar color y estilo al texto en la terminal
# ------------------------------------------------------------------
class Color:
    RESET = "\033[0m"
    NEGRITA = "\033[1m"
    CIAN = "\033[96m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    GRIS = "\033[90m"


# Nombre del archivo donde se guardan los ciclistas
ARCHIVO = "agenda.csv"

# Ancho fijo para las cajas y las líneas
ANCHO = 64


def limpiar_pantalla():
    """Limpia la terminal (funciona en Windows, macOS y Linux)"""
    os.system("cls" if os.name == "nt" else "clear")


def linea():
    """Imprime una línea separadora"""
    print(Color.GRIS + "─" * ANCHO + Color.RESET)


def titulo(texto):
    """Imprime un título centrado dentro de una caja de color"""
    print(Color.CIAN + "╔" + "═" * (ANCHO - 2) + "╗" + Color.RESET)
    print(Color.CIAN + "║" + Color.RESET + texto.center(ANCHO - 2) + Color.CIAN + "║" + Color.RESET)
    print(Color.CIAN + "╚" + "═" * (ANCHO - 2) + "╝" + Color.RESET)


def mensaje_exito(texto):
    print(Color.VERDE + "✔ " + texto + Color.RESET)


def mensaje_error(texto):
    print(Color.ROJO + "✘ " + texto + Color.RESET)


def mensaje_info(texto):
    print(Color.AMARILLO + "ℹ " + texto + Color.RESET)


def pausar():
    """Espera a que el usuario pulse Enter para poder leer el resultado"""
    input(Color.GRIS + "\nPulsa Enter para continuar..." + Color.RESET)


def limpiar_campo(texto):
    """
    Quita las comas del texto escrito por el usuario.
    Así no se rompe el formato del CSV (que separa los campos con comas).
    """
    return texto.replace(",", " ").strip()


def insertar_registro():
    """Pide los datos de un ciclista y los guarda al final del archivo"""
    limpiar_pantalla()
    titulo("🚴  INSERTAR NUEVO CICLISTA")
    print()

    nombre = limpiar_campo(input(Color.NEGRITA + "Nombre: " + Color.RESET))
    apellidos = limpiar_campo(input(Color.NEGRITA + "Apellidos: " + Color.RESET))
    telefono = limpiar_campo(input(Color.NEGRITA + "Teléfono: " + Color.RESET))
    categoria_bicicleta = limpiar_campo(
        input(Color.NEGRITA + "Categoría de bicicleta (montaña, carretera...): " + Color.RESET)
    )

    # No guardamos registros sin nombre
    if nombre == "":
        print()
        mensaje_error("El nombre es obligatorio. No se guardó nada.")
        pausar()
        return

    # Modo "a" = append: añade al final sin borrar lo que ya había
    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.write(nombre + "," + apellidos + "," + telefono + "," + categoria_bicicleta + "\n")
    archivo.close()

    print()
    mensaje_exito(f"Ciclista '{nombre} {apellidos}' guardado con éxito.")
    pausar()


def listar_registros():
    """Muestra todos los ciclistas guardados en formato de tabla"""
    limpiar_pantalla()
    titulo("📋  LISTADO DE CICLISTAS")
    print()

    # Si el archivo todavía no existe, avisamos en vez de dar error
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
    except FileNotFoundError:
        mensaje_info("Todavía no hay registros. Inserta el primero desde el menú.")
        pausar()
        return

    lineas = archivo.readlines()
    archivo.close()

    if len(lineas) == 0:
        mensaje_info("El archivo está vacío.")
        pausar()
        return

    # Cabecera de la tabla
    cabecera = f"{'Nº':<4}{'NOMBRE':<30}{'TELÉFONO':<14}{'CATEGORÍA':<16}"
    print(Color.AZUL + Color.NEGRITA + cabecera + Color.RESET)
    linea()

    numero = 1
    for registro in lineas:
        # Separamos los campos por coma y rellenamos si falta alguno
        campos = registro.strip().split(",")
        while len(campos) < 4:
            campos.append("")

        nombre_completo = f"{campos[0]} {campos[1]}"

        # Si el nombre es demasiado largo, lo cortamos para no romper la tabla
        if len(nombre_completo) > 28:
            nombre_completo = nombre_completo[:27] + "…"

        print(f"{numero:<4}{nombre_completo:<30}{campos[2]:<14}{campos[3]:<16}")
        numero += 1

    linea()
    print(Color.GRIS + f"Total: {len(lineas)} ciclista(s)" + Color.RESET)
    pausar()


def menu():
    """Muestra el menú principal y repite hasta que el usuario decida salir"""
    while True:
        limpiar_pantalla()
        titulo("🚴  REGISTRO DE CICLISTAS  v0.3")
        print(Color.GRIS + "por Heverton Marques".center(ANCHO) + Color.RESET)
        print()
        print(Color.NEGRITA + "  1." + Color.RESET + " 🆕  Insertar un registro")
        print(Color.NEGRITA + "  2." + Color.RESET + " 📋  Listado de registros")
        print(Color.NEGRITA + "  3." + Color.RESET + " 🚪  Salir")
        print()
        linea()

        opcion = input(Color.MAGENTA + "Indica tu opción: " + Color.RESET)

        if opcion == "1":
            insertar_registro()
        elif opcion == "2":
            listar_registros()
        elif opcion == "3":
            limpiar_pantalla()
            print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
            break
        else:
            mensaje_error("Opción no válida, inténtalo de nuevo.")
            pausar()


# Solo se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    menu()
```

### Ejercicio programación 5/1-Ejercicios/004-Utilización de los sistemas de ficheros

**001-crear carpeta.py**

```python
import os

os.mkdir("micarpeta")
```

**002-eliminar carpeta.py**

```python
import os

os.rmdir("micarpeta")
```

**003-crear archivo.py**

```python
archivo = open("miarchivo.txt",'w')
archivo.close()
```

**004-eliminar archivo.py**

```python
import os

os.remove("miarchivo.txt")
```

**005-caminar.py**

```python
import os

directorio = "/home/hevertonmf/Escritorio/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 3"

for x,y,z in os.walk(directorio):
  print(x)
  print(y)
  print(z)
```

**006-caminar por partes.py**

```python
import os

directorio = "/home/hevertonmf/Escritorio/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 3"

for x,y,z in os.walk(directorio):
  print(x)

for x,y,z in os.walk(directorio):
  print(y)
  
for x,y,z in os.walk(directorio):
  print(z)

```

**007-arbol.py**

```python
import os

directorio = "/home/hevertonmf/Escritorio/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 3"


def arbol(ruta, prefijo=""):

    elementos = sorted(os.listdir(ruta))

    for i, elemento in enumerate(elementos):

        ruta_completa = os.path.join(ruta, elemento)

        ultimo = i == len(elementos) - 1

        if ultimo:
            conector = "└── "
        else:
            conector = "├── "

        print(prefijo + conector + elemento)

        if os.path.isdir(ruta_completa):

            if ultimo:
                nuevo_prefijo = prefijo + "    "
            else:
                nuevo_prefijo = prefijo + "│   "

            arbol(ruta_completa, nuevo_prefijo)


print(os.path.basename(directorio) + "/")
arbol(directorio)
```

### Ejercicio programación 5/1-Ejercicios/006-Entrada desde teclado. Salida a pantalla. Formatos de visualización

**001-miniagenda.py**

```python
# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Heverton Marques")

# introducir datos
nombre = input("Dime un nombre: ")
apellidos = input("Dime unos apellidos: ")
email = input("Dime un email: ")

# guardar los datos a un archivo
archivo = open("agenda.csv",'a')
archivo.write(nombre+","+apellidos+","+email+"\n")
archivo.close()


```

**002-bucle infinito.py**

```python
# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Heverton Marques")

#Entro en un bucle infinito
while True:
  
  # introducir datos
  nombre = input("Dime un nombre: ")
  apellidos = input("Dime unos apellidos: ")
  email = input("Dime un email: ")

  # guardar los datos a un archivo
  archivo = open("agenda.csv",'a')
  archivo.write(nombre+","+apellidos+","+email+"\n")
  archivo.close()

```

**003-ahora quiero leer y escribir.py**

```python
# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Heverton Marques")

#Entro en un bucle infinito
while True:
  print("Escoge una opcion:")
  print("1.-insertar datos")
  print("2.-leer datos")
  opcion = input("Escoge una opción: ")
  if opcion == "1":
    # introducir datos
    nombre = input("Dime un nombre: ")
    apellidos = input("Dime unos apellidos: ")
    email = input("Dime un email: ")

    # guardar los datos a un archivo
    archivo = open("agenda.csv",'a')
    archivo.write(nombre+","+apellidos+","+email+"\n")
    archivo.close()
  elif opcion == "2":
    archivo = open("agenda.csv",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()
```

**004-opcion salir.py**

```python
# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Heverton Marques")

#Entro en un bucle infinito
while True:
  print("Escoge una opcion:")
  print("1.-insertar datos")
  print("2.-leer datos")
  print("3.-salir del programa")
  opcion = input("Escoge una opción: ")
  if opcion == "1":
    # introducir datos
    nombre = input("Dime un nombre: ")
    apellidos = input("Dime unos apellidos: ")
    email = input("Dime un email: ")

    # guardar los datos a un archivo
    archivo = open("agenda.csv",'a')
    archivo.write(nombre+","+apellidos+","+email+"\n")
    archivo.close()
  elif opcion == "2":
    archivo = open("agenda.csv",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()
  elif opcion == "3":
    exit()
```

**005-guardar agenda en carpeta.py**

```python
import os

# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Heverton Marques")

os.mkdir("mibasededatos")

#Entro en un bucle infinito
while True:
  print("Escoge una opcion:")
  print("1.-insertar datos")
  print("2.-leer datos")
  print("3.-salir del programa")
  opcion = input("Escoge una opción: ")
  if opcion == "1":
    # introducir datos
    nombre = input("Dime un nombre: ")
    apellidos = input("Dime unos apellidos: ")
    email = input("Dime un email: ")

    # guardar los datos a un archivo
    archivo = open("mibasededatos/agenda.csv",'a')
    archivo.write(nombre+","+apellidos+","+email+"\n")
    archivo.close()
  elif opcion == "2":
    archivo = open("mibasededatos/agenda.csv",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()
  elif opcion == "3":
    exit()

```

**006-try except.py**

```python
import os

# imprimir un mensaje de bienvenida
print("agenda v0.1")
print("por Heverton Marques")
try:
  os.mkdir("mibasededatos")
except Exception:
  print("La carpeta ya existe")

#Entro en un bucle infinito
while True:
  print("Escoge una opcion:")
  print("1.-insertar datos")
  print("2.-leer datos")
  print("3.-salir del programa")
  opcion = input("Escoge una opción: ")
  if opcion == "1":
    # introducir datos
    nombre = input("Dime un nombre: ")
    apellidos = input("Dime unos apellidos: ")
    email = input("Dime un email: ")

    # guardar los datos a un archivo
    archivo = open("mibasededatos/agenda.csv",'a')
    archivo.write(nombre+","+apellidos+","+email+"\n")
    archivo.close()
  elif opcion == "2":
    archivo = open("mibasededatos/agenda.csv",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()
  elif opcion == "3":
    exit()

```

### Ejercicio programación 5/1-Ejercicios/007-Interfaces gráficas

**001-ventana.py**

```python
import tkinter as tk

ventana = tk.Tk()

ventana.mainloop() # no te salgas, bucle infinito
```

**002-geometria.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

ventana.mainloop() # no te salgas, bucle infinito
```

**003-label.py**

```python
```

**004-boton.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Hola mundo en Tkinter")
etiqueta.pack()

boton = tk.Button(text="Pulsame si te atreves")
boton.pack()
 
ventana.mainloop() # no te salgas, bucle infinito
```

**005-entrada.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Hola mundo en Tkinter")
etiqueta.pack()

boton = tk.Button(text="Pulsame si te atreves")
boton.pack()

entrada = tk.Entry()
entrada.pack()
 
ventana.mainloop() # no te salgas, bucle infinito
```

**006-separaciones.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Hola mundo en Tkinter")
etiqueta.pack(padx=20,pady=20)

boton = tk.Button(text="Pulsame si te atreves")
boton.pack(padx=20,pady=20)

entrada = tk.Entry()
entrada.pack(padx=20,pady=20)
 
ventana.mainloop() # no te salgas, bucle infinito

```

### Ejercicio programación 5/1-Ejercicios/008-Concepto de evento

**000-introdución.md**

```markdown
```

**001-continuamos ejercicio anterior.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack(padx=20,pady=20)

operando1 = tk.Entry()
operando1.pack(padx=20,pady=20)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack(padx=20,pady=20)

operando2 = tk.Entry()
operando2.pack(padx=20,pady=20)

boton = tk.Button(text="Vamos a calcular")
boton.pack(padx=20,pady=20)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=20,pady=20)
 
ventana.mainloop() # no te salgas, bucle infinito
```

**002-comando en el boton.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack(padx=10,pady=10)

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Vamos a calcular",command=calcula)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
 
ventana.mainloop() # no te salgas, bucle infinito
```

**003-solucionamos el error.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack(padx=10,pady=10)

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Vamos a calcular",command=calcula)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
 
ventana.mainloop() # no te salgas, bucle infinito
```

**004-calculos.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")
  op1 = operando1.get()				# Dame  el contenido del entry 1
  op2 = operando2.get()				# Dame el contenido del entry 2
  suma = op1 + op2						# Realiza una suma aritmética
  resultado.config(text=suma)	# Pon el resultado en el label ultimo

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack(padx=10,pady=10)

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Vamos a calcular",command=calcula)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
 
ventana.mainloop() # no te salgas, bucle infinito
```

**005-conversion de tipo.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")
  op1 = operando1.get()				# Dame  el contenido del entry 1
  op2 = operando2.get()				# Dame el contenido del entry 2
  suma = int(op1) + int(op2)						# Realiza una suma aritmética
  resultado.config(text=suma)	# Pon el resultado en el label ultimo

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack(padx=10,pady=10)

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Vamos a calcular",command=calcula)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
 
ventana.mainloop() # no te salgas, bucle infinito
```

**006-la calculadora de iva.py**

```python
# sudo apt update && sudo apt install python3-tk -y
# sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")
  base_imp = base.get()
  base_imp = float(base_imp) 
  iva = base_imp*0.21
  resultado.config(text=iva)

ventana = tk.Tk()
ventana.geometry("400x300")

# entradas de datos
etiqueta = tk.Label(text="Dime la base imponible")
etiqueta.pack(padx=10,pady=10)

base = tk.Entry()
base.pack(padx=10,pady=10)

# Dispara la acción
boton = tk.Button(text="Vamos a calcular el IVA",command=calcula)
boton.pack(padx=10,pady=10)

# Solemos usar label para sacar el resultado
resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)
 
ventana.mainloop() # no te salgas, bucle infinito
```

**007-mi calculadora de meta de kilometros.py**

```python
# sudo apt update && sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")
  km = float(distancia.get().replace(",", "."))
  minutos = float(tiempo.get().replace(",", "."))
  horas = minutos / 60
  velocidad = km / horas
  resultado.config(text=f"Velocidad media: {velocidad:.2f} km/h")

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Velocidad media")

# entrada de los kilómetros
etiqueta_km = tk.Label(text="¿Cuántos km has pedaleado?")
etiqueta_km.pack(padx=10, pady=5)

distancia = tk.Entry()
distancia.pack(padx=10, pady=5)

# entrada del tiempo
etiqueta_tiempo = tk.Label(text="¿Cuánto tiempo has tardado? (en minutos)")
etiqueta_tiempo.pack(padx=10, pady=5)

tiempo = tk.Entry()
tiempo.pack(padx=10, pady=5)

# dispara la acción
boton = tk.Button(text="Calcular velocidad media", command=calcula)
boton.pack(padx=10, pady=10)

# label para sacar el resultado
resultado = tk.Label(text="Resultado")
resultado.pack(padx=10, pady=10)

ventana.mainloop() # no te salgas, bucle infinito
```

### Ejercicio programación 5/1-Ejercicios/009-Criação de controladores de eventos

**001-frame.py**

```python
import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

etiqueta = tk.Label(marco,text="Hola mundo")
etiqueta.pack(padx=10,pady=10)

boton = tk.Button(marco,text="Pulsame")
boton.pack(padx=10,pady=10)

marco.pack()

ventana.mainloop()
```

**002-mostrar y ocultar.py**

```python
import tkinter as tk

ventana = tk.Tk()
# Contenido del marco
marco = tk.Frame(ventana)
etiqueta = tk.Label(marco,text="Hola mundo")
etiqueta.pack(padx=10,pady=10)
boton = tk.Button(marco,text="Pulsame")
boton.pack(padx=10,pady=10)

# Botones de control
mostrar = tk.Button(ventana,text="Mostrar")
mostrar.pack(padx=10,pady=10)

ocultar = tk.Button(ventana,text="Ocultar")
ocultar.pack(padx=10,pady=10)

ventana.mainloop()
```

**003-funcion de los botones.py**

```python
import tkinter as tk

def muestraContenido():
  print("Te voy a mostrar el marco")

def ocultaContenido():
  print("Te voy a ocultar el marco")

ventana = tk.Tk()
# Contenido del marco
marco = tk.Frame(ventana)
etiqueta = tk.Label(marco,text="Hola mundo")
etiqueta.pack(padx=10,pady=10)
boton = tk.Button(marco,text="Pulsame")
boton.pack(padx=10,pady=10)

# Botones de control
mostrar = tk.Button(ventana,text="Mostrar",command=muestraContenido)
mostrar.pack(padx=10,pady=10)

ocultar = tk.Button(ventana,text="Ocultar",command=ocultaContenido)
ocultar.pack(padx=10,pady=10)

ventana.mainloop()
```

**004-completando las funciones.py**

```python
import tkinter as tk

def muestraContenido():
  print("Te voy a mostrar el marco")
  marco.pack(padx=10,pady=10)

def ocultaContenido():
  print("Te voy a ocultar el marco")
  marco.pack_forget()

ventana = tk.Tk()
# Contenido del marco
marco = tk.Frame(ventana)
etiqueta = tk.Label(marco,text="Hola mundo")
etiqueta.pack(padx=10,pady=10)
boton = tk.Button(marco,text="Pulsame")
boton.pack(padx=10,pady=10)

# Botones de control
mostrar = tk.Button(ventana,text="Mostrar",command=muestraContenido)
mostrar.pack(padx=10,pady=10)

ocultar = tk.Button(ventana,text="Ocultar",command=ocultaContenido)
ocultar.pack(padx=10,pady=10)

ventana.mainloop()
```

**005-grid.py**

```python
import tkinter as tk

ventana = tk.Tk()

texto1 = tk.Label(text="Soy el texto 1")
texto1.pack(padx=10,pady=10)

texto2 = tk.Label(text="Soy el texto 2")
texto2.pack(padx=10,pady=10)

texto3 = tk.Label(text="Soy el texto 3")
texto3.pack(padx=10,pady=10)

texto4 = tk.Label(text="Soy el texto 4")
texto4.pack(padx=10,pady=10)

ventana.mainloop()
```

**006-grid ahora si.py**

```python
import tkinter as tk

ventana = tk.Tk()

texto1 = tk.Label(text="Soy el texto 1")
texto1.grid(row=0,column=0,padx=10,pady=10)

texto2 = tk.Label(text="Soy el texto 2")
texto2.grid(row=0,column=1,padx=10,pady=10)

texto3 = tk.Label(text="Soy el texto 3")
texto3.grid(row=1,column=0,padx=10,pady=10)

texto4 = tk.Label(text="Soy el texto 4")
texto4.grid(row=1,column=1,padx=10,pady=10)

ventana.mainloop()
```

**007-esquema tabla.md**

```markdown
|---|---|---|---|
|0,0|0,1|0,2|0,3|
|---|---|---|---|
|1,0|1,1|1,2|1,3|
|---|---|---|---|
|2,0|2,1|2,2|2,3|
|---|---|---|---|
|3,0|3,1|3,2|3,3|
|---|---|---|---|
```

**008-escribir archivo.py**

```python
import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un cliente")
  

titulo = tk.Label(ventana,text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(ventana,text="Introduce el nombre del cliente")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(ventana)
inputnombre.pack(padx=20,pady=20)

apellidos = tk.Label(ventana,text="Introduce los apellidos del cliente")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(ventana)
inputapellidos.pack(padx=20,pady=20)

email = tk.Label(ventana,text="Introduce el email del cliente")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(ventana)
inputemail.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx=20,pady=20)

ventana.mainloop()
```

**009-ahora guardo en archivo.py**

```python
import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un cliente")
  stringnombre = inputnombre.get()
  stringapellidos = inputapellidos.get()
  stringemail = inputemail.get()
  archivo = open("agenda.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+"\n")
  archivo.close()

titulo = tk.Label(ventana,text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(ventana,text="Introduce el nombre del cliente")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(ventana)
inputnombre.pack(padx=20,pady=20)

apellidos = tk.Label(ventana,text="Introduce los apellidos del cliente")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(ventana)
inputapellidos.pack(padx=20,pady=20)

email = tk.Label(ventana,text="Introduce el email del cliente")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(ventana)
inputemail.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx=20,pady=20)

ventana.mainloop()
```

**010-campo de texto.py**

```python
import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un cliente")
  stringnombre = inputnombre.get()
  stringapellidos = inputapellidos.get()
  stringemail = inputemail.get()
  archivo = open("agenda.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+"\n")
  archivo.close()

titulo = tk.Label(ventana,text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(ventana,text="Introduce el nombre del cliente")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(ventana)
inputnombre.pack(padx=20,pady=20)

apellidos = tk.Label(ventana,text="Introduce los apellidos del cliente")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(ventana)
inputapellidos.pack(padx=20,pady=20)

email = tk.Label(ventana,text="Introduce el email del cliente")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(ventana)
inputemail.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx=20,pady=20)

campodetexto = tk.Text(ventana)
campodetexto.pack(padx=20,pady=20)

ventana.mainloop()
```

**011-leer.py**

```python
import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un cliente")
  stringnombre = inputnombre.get()
  stringapellidos = inputapellidos.get()
  stringemail = inputemail.get()
  archivo = open("agenda.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+"\n")
  archivo.close()
  #campodetexto.delete("1.0", tk.END)	# Primero borra todo lo que haya
  archivo = open("agenda.csv",'r')
  lineas = archivo.readlines()
  for linea in lineas:
    campodetexto.insert(tk.END, linea)	# Insertame una linea
  archivo.close()

titulo = tk.Label(ventana,text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(ventana,text="Introduce el nombre del cliente")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(ventana)
inputnombre.pack(padx=20,pady=20)

apellidos = tk.Label(ventana,text="Introduce los apellidos del cliente")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(ventana)
inputapellidos.pack(padx=20,pady=20)

email = tk.Label(ventana,text="Introduce el email del cliente")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(ventana)
inputemail.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Insertar cliente",command=insertaCliente)
boton.pack(padx=20,pady=20)

campodetexto = tk.Text(ventana)
campodetexto.pack(padx=20,pady=20)

ventana.mainloop()
```

**012-grid y marco.py**

```python
import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un cliente")
  stringnombre = inputnombre.get()
  stringapellidos = inputapellidos.get()
  stringemail = inputemail.get()
  archivo = open("agenda.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+"\n")
  archivo.close()
  campodetexto.delete("1.0", tk.END)	# Primero borra todo lo que haya
  archivo = open("agenda.csv",'r')
  lineas = archivo.readlines()
  for linea in lineas:
    campodetexto.insert(tk.END, linea)	# Insertame una linea
  archivo.close()

marco = tk.Frame(ventana)

titulo = tk.Label(marco,text="Programa agenda v0.1")
titulo.pack(padx=20,pady=20)

nombre = tk.Label(marco,text="Introduce el nombre del cliente")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(marco)
inputnombre.pack(padx=20,pady=20)

apellidos = tk.Label(marco,text="Introduce los apellidos del cliente")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(marco)
inputapellidos.pack(padx=20,pady=20)

email = tk.Label(marco,text="Introduce el email del cliente")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(marco)
inputemail.pack(padx=20,pady=20)

boton = tk.Button(marco,text="Insertar cliente",command=insertaCliente)
boton.pack(padx=20,pady=20)

marco.grid(row=0,column=0)

campodetexto = tk.Text(ventana)
campodetexto.grid(row=0,column=1,padx=20,pady=20)

ventana.mainloop()
```

**013-ia.py**

```python
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# ============================================
# VENTANA
# ============================================

ventana = ttk.Window(
    title="Agenda de clientes",
    themename="flatly",
    size=(950, 580),
    resizable=(True, True)
)

ventana.place_window_center()


# ============================================
# FUNCIONES
# ============================================

def insertaCliente():
    stringnombre = inputnombre.get()
    stringapellidos = inputapellidos.get()
    stringemail = inputemail.get()

    # Evitar insertar registros completamente vacíos
    if stringnombre == "" and stringapellidos == "" and stringemail == "":
        estado.config(
            text="Introduce algún dato antes de guardar",
            bootstyle="danger"
        )
        return

    archivo = open("agenda.csv", "a")
    archivo.write(
        stringnombre + "," +
        stringapellidos + "," +
        stringemail + "\n"
    )
    archivo.close()

    # Limpiar formulario
    inputnombre.delete(0, tk.END)
    inputapellidos.delete(0, tk.END)
    inputemail.delete(0, tk.END)

    # Actualizar listado
    cargarClientes()

    estado.config(
        text="✓ Cliente guardado correctamente",
        bootstyle="success"
    )

    inputnombre.focus()


def cargarClientes():

    campodetexto.delete("1.0", tk.END)

    try:
        archivo = open("agenda.csv", "r")
        lineas = archivo.readlines()

        for linea in lineas:
            campodetexto.insert(tk.END, linea)

        archivo.close()

        contador.config(
            text=str(len(lineas)) + " clientes registrados"
        )

    except FileNotFoundError:
        contador.config(text="0 clientes registrados")


# ============================================
# CONTENEDOR PRINCIPAL
# ============================================

principal = ttk.Frame(
    ventana,
    padding=30
)

principal.pack(
    fill=BOTH,
    expand=True
)

principal.columnconfigure(0, weight=1)
principal.columnconfigure(1, weight=2)
principal.rowconfigure(1, weight=1)


# ============================================
# CABECERA
# ============================================

cabecera = ttk.Frame(principal)

cabecera.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky=EW,
    pady=(0, 25)
)

titulo = ttk.Label(
    cabecera,
    text="Agenda",
    font=("Arial", 26, "bold"),
    bootstyle="primary"
)

titulo.pack(anchor=W)

subtitulo = ttk.Label(
    cabecera,
    text="Gestión sencilla de clientes",
    font=("Arial", 11),
    bootstyle="secondary"
)

subtitulo.pack(anchor=W, pady=(3, 0))


# ============================================
# FORMULARIO IZQUIERDO
# ============================================

marco = ttk.Labelframe(
    principal,
    text=" Nuevo cliente ",
    padding=25,
    bootstyle="primary"
)

marco.grid(
    row=1,
    column=0,
    sticky=NSEW,
    padx=(0, 15)
)


# NOMBRE

nombre = ttk.Label(
    marco,
    text="Nombre",
    font=("Arial", 10, "bold")
)

nombre.pack(
    anchor=W,
    pady=(0, 5)
)

inputnombre = ttk.Entry(
    marco,
    font=("Arial", 11)
)

inputnombre.pack(
    fill=X,
    ipady=6,
    pady=(0, 20)
)


# APELLIDOS

apellidos = ttk.Label(
    marco,
    text="Apellidos",
    font=("Arial", 10, "bold")
)

apellidos.pack(
    anchor=W,
    pady=(0, 5)
)

inputapellidos = ttk.Entry(
    marco,
    font=("Arial", 11)
)

inputapellidos.pack(
    fill=X,
    ipady=6,
    pady=(0, 20)
)


# EMAIL

email = ttk.Label(
    marco,
    text="Correo electrónico",
    font=("Arial", 10, "bold")
)

email.pack(
    anchor=W,
    pady=(0, 5)
)

inputemail = ttk.Entry(
    marco,
    font=("Arial", 11)
)

inputemail.pack(
    fill=X,
    ipady=6,
    pady=(0, 25)
)


# BOTÓN

boton = ttk.Button(
    marco,
    text="＋  Insertar cliente",
    command=insertaCliente,
    bootstyle="primary"
)

boton.pack(
    fill=X,
    ipady=7
)


# MENSAJE DE ESTADO

estado = ttk.Label(
    marco,
    text="",
    font=("Arial", 9)
)

estado.pack(
    anchor=W,
    pady=(15, 0)
)


# ============================================
# PANEL DERECHO
# ============================================

derecha = ttk.Labelframe(
    principal,
    text=" Clientes ",
    padding=20,
    bootstyle="secondary"
)

derecha.grid(
    row=1,
    column=1,
    sticky=NSEW,
    padx=(15, 0)
)

derecha.columnconfigure(0, weight=1)
derecha.rowconfigure(1, weight=1)


# CONTADOR

contador = ttk.Label(
    derecha,
    text="0 clientes registrados",
    font=("Arial", 10),
    bootstyle="secondary"
)

contador.grid(
    row=0,
    column=0,
    sticky=W,
    pady=(0, 10)
)


# ============================================
# ÁREA DE TEXTO
# ============================================

marcotexto = ttk.Frame(derecha)

marcotexto.grid(
    row=1,
    column=0,
    sticky=NSEW
)

marcotexto.columnconfigure(0, weight=1)
marcotexto.rowconfigure(0, weight=1)


campodetexto = tk.Text(
    marcotexto,
    font=("Ubuntu Mono", 11),
    relief="flat",
    padx=15,
    pady=15,
    wrap="none"
)

campodetexto.grid(
    row=0,
    column=0,
    sticky=NSEW
)


# SCROLL

scroll = ttk.Scrollbar(
    marcotexto,
    orient=VERTICAL,
    command=campodetexto.yview
)

scroll.grid(
    row=0,
    column=1,
    sticky=NS
)

campodetexto.config(
    yscrollcommand=scroll.set
)


# ============================================
# PIE
# ============================================

pie = ttk.Label(
    principal,
    text="Agenda v0.2 · Python + Tkinter + ttkbootstrap",
    font=("Arial", 9),
    bootstyle="secondary"
)

pie.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky=W,
    pady=(20, 0)
)


# ============================================
# INICIO
# ============================================

cargarClientes()

inputnombre.focus()

ventana.mainloop()
```

**014-pip instal.md**

```markdown
# pip install ttkbootstrap
# pip3 install ttkbootstrap --break-system-packages
```

## Ejercicio programación 5/2-Proyecto

**001-Gestión de ciclistas.py**

```python
import tkinter as tk

ventana = tk.Tk()

def insertaCliente():
  print("Voy a insertar un ciclista")
  stringnombre = inputnombre.get() #datos que se han introducido en el campo de texto
  stringapellidos = inputapellidos.get() 
  stringemail = inputemail.get()
  stringequipo = inputequipo.get()
  stringtipobicicleta = inputtipobicicleta.get()
  archivo = open("ciclistas.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+","+stringequipo+","+stringtipobicicleta+"\n")
  archivo.close()
  campodetexto.delete("1.0", tk.END)	# Primero borra todo lo que haya
  archivo = open("ciclistas.csv",'r')
  lineas = archivo.readlines()
  for linea in lineas:
    campodetexto.insert(tk.END, linea)	# Insertame una linea
  archivo.close()

marco = tk.Frame(ventana)

titulo = tk.Label(marco,text="Gestión de ciclistas v0.1")
titulo.pack(padx=20,pady=20)

#insertar un ciclista
nombre = tk.Label(marco,text="Introduce el nombre del ciclista")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(marco)
inputnombre.pack(padx=20,pady=20)

#insertar apellidos
apellidos = tk.Label(marco,text="Introduce los apellidos del ciclista")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(marco)
inputapellidos.pack(padx=20,pady=20)

#insertar email
email = tk.Label(marco,text="Introduce el email del ciclista")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(marco)
inputemail.pack(padx=20,pady=20)

#insertar equipo
equipo = tk.Label(marco,text="Introduce el equipo del ciclista")
equipo.pack(padx=2,pady=2)
inputequipo = tk.Entry(marco)
inputequipo.pack(padx=20,pady=20)

#insertar tipo de bicicleta
tipobicicleta = tk.Label(marco,text="Introduce el tipo de bicicleta")
tipobicicleta.pack(padx=2,pady=2)
inputtipobicicleta = tk.Entry(marco)
inputtipobicicleta.pack(padx=20,pady=20)

boton = tk.Button(marco,text="Insertar ciclista",command=insertaCliente)
boton.pack(padx=20,pady=20)

marco.grid(row=0,column=0)

campodetexto = tk.Text(ventana)
campodetexto.grid(row=0,column=1,padx=20,pady=20)

ventana.mainloop()
```

**002-Gestión de ciclistas IA.py**

```python
import tkinter as tk

# ---------- Colores y fuentes ----------
FONDO = "#1e1e2e"
TARJETA = "#2a2a3d"
TEXTO = "#e4e4ef"
SECUNDARIO = "#a0a0b8"
ACENTO = "#f5a623"
ACENTO_HOVER = "#ffb84d"
CAMPO = "#38384f"

FUENTE_TITULO = ("Segoe UI", 18, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 10)
FUENTE_LABEL = ("Segoe UI", 10, "bold")
FUENTE_INPUT = ("Segoe UI", 11)
FUENTE_TEXTO = ("Consolas", 10)

ventana = tk.Tk()
ventana.title("Gestión de ciclistas")
ventana.configure(bg=FONDO)
ventana.resizable(False, False)

def insertaCliente():
  print("Voy a insertar un ciclista")
  stringnombre = inputnombre.get() #datos que se han introducido en el campo de texto
  stringapellidos = inputapellidos.get()
  stringemail = inputemail.get()
  stringequipo = inputequipo.get()
  stringtipobicicleta = inputtipobicicleta.get()
  archivo = open("ciclistas.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+","+stringequipo+","+stringtipobicicleta+"\n")
  archivo.close()
  campodetexto.delete("1.0", tk.END)	# Primero borra todo lo que haya
  archivo = open("ciclistas.csv",'r')
  lineas = archivo.readlines()
  for linea in lineas:
    campodetexto.insert(tk.END, linea)	# Insertame una linea
  archivo.close()

# Crea una etiqueta + campo de texto con el mismo estilo
def crearCampo(texto):
  etiqueta = tk.Label(marco, text=texto, font=FUENTE_LABEL, bg=TARJETA, fg=SECUNDARIO, anchor="w")
  etiqueta.pack(fill="x", padx=25, pady=(10, 3))
  campo = tk.Entry(marco, font=FUENTE_INPUT, bg=CAMPO, fg=TEXTO, insertbackground=TEXTO,
                   relief="flat", width=30, highlightthickness=1,
                   highlightbackground=CAMPO, highlightcolor=ACENTO)
  campo.pack(fill="x", padx=25, ipady=6)
  return campo

# ---------- Formulario (izquierda) ----------
marco = tk.Frame(ventana, bg=TARJETA)

titulo = tk.Label(marco, text="🚴 Gestión de ciclistas", font=FUENTE_TITULO, bg=TARJETA, fg=TEXTO)
titulo.pack(padx=25, pady=(25, 0), anchor="w")
subtitulo = tk.Label(marco, text="v0.1 · Registro de participantes", font=FUENTE_SUBTITULO, bg=TARJETA, fg=SECUNDARIO)
subtitulo.pack(padx=25, pady=(0, 10), anchor="w")

inputnombre = crearCampo("Nombre")
inputapellidos = crearCampo("Apellidos")
inputemail = crearCampo("Email")
inputequipo = crearCampo("Equipo")
inputtipobicicleta = crearCampo("Tipo de bicicleta")

boton = tk.Button(marco, text="Insertar ciclista", command=insertaCliente,
                  font=FUENTE_LABEL, bg=ACENTO, fg="#1e1e2e",
                  activebackground=ACENTO_HOVER, activeforeground="#1e1e2e",
                  relief="flat", cursor="hand2", pady=8)
boton.pack(fill="x", padx=25, pady=25)

# Efecto hover del botón
boton.bind("<Enter>", lambda e: boton.config(bg=ACENTO_HOVER))
boton.bind("<Leave>", lambda e: boton.config(bg=ACENTO))

marco.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="n")

# ---------- Listado (derecha) ----------
marcolista = tk.Frame(ventana, bg=TARJETA)
marcolista.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="ns")

tk.Label(marcolista, text="Ciclistas registrados", font=FUENTE_LABEL,
         bg=TARJETA, fg=SECUNDARIO, anchor="w").pack(fill="x", padx=15, pady=(15, 5))

campodetexto = tk.Text(marcolista, font=FUENTE_TEXTO, bg=CAMPO, fg=TEXTO,
                       insertbackground=TEXTO, relief="flat", width=60, height=24,
                       padx=10, pady=10)
campodetexto.pack(padx=15, pady=(0, 15))

ventana.mainloop()
```

## Ejercicio programación 5/3-Resultado de aprendizaje

**Resultado de aprendizaje.md**

```markdown
# Gestión de ciclistas – Respuestas

**a) Se ha utilizado la consola para realizar operaciones de entrada y salida de información.**

Sí, con `print()` muestro un mensaje al insertar un ciclista.

**b) Se han aplicado formatos en la visualización de la información.**

Sí, con colores, fuentes y márgenes (`bg`, `fg`, `font`, `padx`).

**c) Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas.**

Sí, uso `print()`, `open()` y la librería `tkinter`.

**d) Se han utilizado ficheros para almacenar y recuperar información.**

Sí, guardo y leo los datos en `ciclistas.csv`.

**e) Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros.**

Sí, abro el fichero en modo `'a'` (añadir) y `'r'` (leer).

**f) Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficos de usuario simples.**

Sí, creo la ventana con `Label`, `Entry`, `Button` y `Text`.

**g) Se han programado controladores de eventos.**

Sí, el botón usa `command=insertaCliente` y `bind()` para el efecto hover.

**h) Se han escrito programas que utilicen interfaces gráficos para la entrada y salida de información.**

Sí, escribo datos en los `Entry` y se muestran en el `Text`.
```

