# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-01 19:57:15 +0200
- **Usuario:** Heverton Marques
- **UID:** 197609
- **Equipo:** Heverton
- **Sistema operativo:** MINGW64_NT-10.0-26300
- **Versión del kernel:** 3.6.10-3ea87a50.x86_64
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `/c/Users/samar/Documents/DAM 1/Programacion UNIDADE 1`
- **Proyecto documentado:** `/c/Users/samar/Documents/DAM 1/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 3`
- **HMAC-SHA-256 de autenticidad:** `21f4be4a8d3019fe4e6714ebec3409821f3d0cd59939eaf0c0ac78a5f1c3ebfe`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
/c/Users/samar/Documents/DAM 1/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 3
├── 1-Ejercicios
│   ├── 001-estructuras de selección
│   │   ├── 000-introducion.md
│   │   ├── 001-estructura if.py
│   │   ├── 002-else.py
│   │   ├── 003-imput.py
│   │   └── 004-elif.py
│   ├── 002-Estructuras de repetición
│   │   ├── 000-introdución.md
│   │   ├── 001-for.py
│   │   ├── 002-for dia.py
│   │   ├── 003-for anidado.py
│   │   └── 004-mas for anidado.py
│   ├── 003-estructuras de salto
│   │   ├── 000-introducion.md
│   │   ├── 001-programa.py
│   │   ├── 002-crud.py
│   │   ├── 003-introducimos codigo.py
│   │   └── 004-rellenando.py
│   ├── 004-Control de excepciones
│   │   ├── 000-introducion.md
│   │   ├── 001-prueba.py
│   │   ├── 002-prog divisor.py
│   │   └── 003-control.py
│   ├── 005-Aserciones
│   │   ├── 000-intoducion
│   │   ├── 001-asercion positiva.py
│   │   ├── 002-asercion erronea.py
│   │   └── 003-combinacion.py
│   ├── 006-Prueba, depuración y documentación de la aplicación
│   │   ├── 000-introducion.md
│   │   ├── 001-limite de las variables.py
│   │   ├── 002-lista de la compra.py
│   │   ├── 003-while.py
│   │   └── 004-lista de la compra.py
│   └── 007-Ejercicio
│       ├── 000-introducion.md
│       ├── 001-selecion.py
│       ├── 002-repeticion.py
│       ├── 003-solto.py
│       ├── 004-exepciones.py
│       ├── 005-probar.py
│       ├── 006-aserciones.py
│       ├── 007-documentar.py
│       ├── 008-ejemplo ciclismo.py
│       └── 009-preguntas y respuestas.md
├── 2-Proyecto
│   ├── 001-programa.py
│   ├── 002-primer codigo.py
│   ├── 003-crud.py
│   ├── 004-elif.py
│   ├── 005-listas.py
│   ├── 006-probar.py
│   ├── 007-ejercicio.py
│   └── 008-ejercicio mejorado con IA.py
└── 3-Resultado de aprendizaje
    └── 000-Criterios de evaluación.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Ejercicio programación 3
## 1-Ejercicios
### 001-estructuras de selección
**000-introducion.md**
```markdown
```
**001-estructura if.py**
```python
edad = 48
if edad < 10:
	print("Eres un niño")
```
**002-else.py**
```python
edad = 48
if edad < 10:
	print("Eres un niño")
else:
  print("Ya no eres un niño")
```
**003-imput.py**
```python
edad = input("Dime tu edad: ")
edad = int(edad)
if edad < 13:
	print("Eres un niño")
else:
  print("Ya no eres un niño")
```
**004-elif.py**
```python
edad = input("Dime tu edad: ")
edad = int(edad)
if edad < 10:
	print("Eres un niño")
elif edad >=10 and edad < 20:
  print("Eres un adolescente")
elif edad >=20 and edad < 30:
  print("Eres un joven")
elif edad >=30 and edad < 40:
  print("Eres un adulto")
else:
  print("Eres un viejo")
```
### 002-Estructuras de repetición
**000-introdución.md**
```markdown
```
**001-for.py**
```python
for _ in range(0,100):
  print("Hola que tal")
```
**002-for dia.py**
```python
for dia in range(1,31):
  print("Hoy es el dia",dia,"del mes")
```
**003-for anidado.py**
```python
for mes in range(1,13):
  for dia in range(1,31):
    print("Hoy es el dia",dia,"del mes",mes)
```
**004-mas for anidado.py**
```python
for anho in range(1978,2027):
  for mes in range(1,13):
    for dia in range(1,31):
      print("Hoy es el dia",dia,"del mes",mes,"del año",anho)
```
### 003-estructuras de salto
**000-introducion.md**
```markdown
```
**001-programa.py**
```python
# Primero presento el programa

# Mensaje de bienvenida

# Entrar en un bucle infinito

# Le enseño al usuario lo que puede hacer

# Le pregunto qué quiere hacer

# Anoto su decisión y tomo una acción
```
**002-crud.py**
```python
# Primero presento el programa
# CRUD = Create, Read, Update, Delete

# Mensaje de bienvenida

# Entrar en un bucle infinito

# Le enseño al usuario lo que puede hacer

# Le pregunto qué quiere hacer

# Anoto su decisión y tomo una acción - la acción puede ser

# 1.-Crear un nuevo registro

# 2.-Listar los registros existentes

# 3.-Actualizar un registro

# 4.-Eliminar un registros
```
**003-introducimos codigo.py**
```python
# Primero presento el programa
# CRUD = Create, Read, Update, Delete
"""
	Programa CRUD
  Versión 0.1
  por Jose Vicente Carratala
"""
# Mensaje de bienvenida
print("Programa CRUD v 0.1")
print("En este programa practicamos en clase")
# Entrar en un bucle infinito
while True:
  # Le enseño al usuario lo que puede hacer
	print("1.-Insertar un registro")
  print("2.-Leer los registros")
  print("3.-Actualizar un registro")
  print("4.-Eliminar un registro")
  # Le pregunto qué quiere hacer
	
  # Anoto su decisión y tomo una acción - la acción puede ser

  # 1.-Crear un nuevo registro

  # 2.-Listar los registros existentes

  # 3.-Actualizar un registro
```
**004-rellenando.py**
```python
# Primero presento el programa
# CRUD = Create, Read, Update, Delete
"""
Programa CRUD
Versión 0.1
por Jose Vicente Carratala
"""

# Mensaje de bienvenida
print("Programa CRUD v 0.1")
print("En este programa practicamos en clase")

# Entrar en un bucle infinito
while True:
    # Le enseño al usuario lo que puede hacer
    print("1.-Insertar un registro")
    print("2.-Leer los registros")
    print("3.-Actualizar un registro")
    print("4.-Eliminar un registro")

    # Le pregunto qué quiere hacer
    opcion = input("Escoge una de las opciones: ")

    # Anoto su decisión y tomo una acción - la acción puede ser
    if opcion == "1":
        # 1.-Crear un nuevo registro
        print("Voy a crear un nuevo registro")
    elif opcion == "2":
        # 2.-Listar los registros existentes
        print("Voy a listar los registros")
    elif opcion == "3":
        # 3.-Actualizar un registro
        print("Voy a actualizar un registro")
    elif opcion == "4":
        # 4.-Eliminar un registros
        print("Voy a eliminar un registro")
    else:
        print("Opción no válida")
:
```
### 004-Control de excepciones
**000-introducion.md**
```markdown
```
**001-prueba.py**
```python
print("Este es el principio del programa")
print(10/0)
print("Este es el final del programa")md
```
**002-prog divisor.py**
```python
dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

division = dividendo/divisor

print(division)	
```
**003-control.py**
```python
print("Empiezo el programa")

try:
  print(10/0)
except Exception as e:
  print(e)

print("Acabo el programa")
```
### 005-Aserciones
**001-asercion positiva.py**
```python
print("Principio del programa")
assert 4 > 3
print("Final del programa")
```
**002-asercion erronea.py**
```python
print("Principio del programa")
assert 4 < 3
print("Final del programa")
```
**003-combinacion.py**
```python
print("Principio del programa")
try:
	assert 4 < 3
except Exception as e:
  print("No puedo continuar porque:",e)
print("Final del programa")
```
### 006-Prueba, depuración y documentación de la aplicación
**000-introducion.md**
```markdown
```
**001-limite de las variables.py**
```python
agenda = "Jose Vicente"
print(agenda)

agenda = input("Introduce un elemento en la agenda: ")
print(agenda)
```
**002-lista de la compra.py**
```python
lista_de_la_compra = []

nuevo_elemento = input("Introduce un nuevo elemento: ")
lista_de_la_compra.append(nuevo_elemento)
print(lista_de_la_compra)
```
**003-while.py**
```python
lista_de_la_compra = []

while True:
  nuevo_elemento = input("Introduce un nuevo elemento: ")
  lista_de_la_compra.append(nuevo_elemento)
  print(lista_de_la_compra)
```
**004-lista de la compra.py**
```python
"""
Lista de la compra v0.1
"""

print("Programa lista de la compra")
lista_de_la_compra = []

while True:
    print("Escoge una opcion")
    print("1.- Insertar un nuevo elemento")
    print("2.- Listar elementos")

    opcion = input("Escoge una opción: ")

    if opcion == "1":
        elemento = input("Introduce un nuevo elemento: ")
        lista_de_la_compra.append(elemento)

    elif opcion == "2":
        print(lista_de_la_compra)
```
### 007-Ejercicio
**000-introducion.md**
```markdown
Resultado de aprendizaje
Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

Criterios de evaluación
a) Se ha escrito y probado código que haga uso de estructuras de selección.
Mi ejercicio cumple con este apartado porque he hecho una estrutura
if - elif para atrapar la opción del usuario en la lista de alumnos

b) Se han utilizado estructuras de repetición.
He utilizado la estructura de control While para crear una 
repetición infinita en mi programa porque quiero que el programa
pregunte por nuevos alumnos sin fin

c) Se han reconocido las posibilidades de las sentencias de salto.
d) Se ha escrito código utilizando control de excepciones.
e) Se han creado programas ejecutables utilizando diferentes estructuras de control.
f) Se han probado y depurado los programas.
g) Se ha comentado y documentado el código.
h) Se han creado excepciones.
i) Se han utilizado aserciones para la detección y corrección de errores durante la fase de desarrollo.
```
**001-selecion.py**
```python
if opcion == "1":
  print("Voy a insertar")
elif opcion == "2":
  print("Voy a listar")
```
**002-repeticion.py**
```python
while True:
	print("1.-Insertar  registro")
  print("2.-Leer registro")
	opcion = input("Introduce tu opcion: ")
  if opcion == "1":
    print("Voy a insertar")
  elif opcion == "2":
    print("Voy a listar")
```
**003-solto.py**
```python
while True:
	print("1.-Insertar  registro")
  print("2.-Leer registro")
	opcion = input("Introduce tu opcion: ")
  if opcion == "1":
    print("Voy a insertar")
  elif opcion == "2":
    print("Voy a listar")
```
**004-exepciones.py**
```python
while True:
    print("1.-Insertar registro")
    print("2.-Leer registro")

    opcion = input("Introduce tu opcion: ")

    try:
        if opcion == "1":
            print("Voy a insertar")
        elif opcion == "2":
            print("Voy a listar")
    except Exception as e:
        print("No válido")
```
**005-probar.py**
```python
alumnos = []

while True:
    print("1.-Insertar registro")
    print("2.-Leer registro")

    opcion = input("Introduce tu opcion: ")

    try:
        if opcion == "1":
            print("Voy a insertar")
            alumno = input("Introduce un alumno: ")
            alumnos.append(alumno)

        elif opcion == "2":
            print("Voy a listar")
            print(alumnos)

    except Exception as e:
        print("No válido")
```
**006-aserciones.py**
```python
alumnos = []

while True:
    print("1.-Insertar registro")
    print("2.-Leer registro")

    opcion = input("Introduce tu opcion: ")

    try:
      	
        if opcion == "1":
            print("Voy a insertar")
            alumno = input("Introduce un alumno: ")
            alumnos.append(alumno)

        elif opcion == "2":
            print("Voy a listar")
            print(alumnos)
        else:
            assert 4 < 3

    except Exception as e:
        print("No válido")
        
        
```
**007-documentar.py**
```python
"""
	Listado de alumnos v0.1 por Jose Vicente Carratala
  Este programa crea un lista de alumnos
"""
alumnos = []

while True:
    print("1.-Insertar registro")
    print("2.-Leer registro")

    opcion = input("Introduce tu opcion: ")

    try:
      	
        if opcion == "1":
            print("Voy a insertar")
            alumno = input("Introduce un alumno: ")
            alumnos.append(alumno)

        elif opcion == "2":
            print("Voy a listar")
            print(alumnos)
        else:
            assert 4 < 3			# Introduzco una asercion para forzar un error

    except Exception as e:		# Capturo el error y lo saco por pantalla
        print("No válido")
        
        
```
**008-ejemplo ciclismo.py**
```python
"""
	Calculadora de Pedaladas
  Versión 0.1
  por Jose Vicente Carratala
"""

# Estas son las condiciones iniciales
pedalada = 1.5

# Entrada del usuario	
numero_pedaladas = input("Cuantas pedaladas has dado?: ")
numero_pedaladas = int(numero_pedaladas)

# ahora hacemos cálculos
avance = numero_pedaladas*pedalada

# Operaciones de salida
print("Has dado",numero_pedaladas,"pedaladas")
print("Cada pedalada son ",pedalada,"metros")
print("Pues has avanzado",avance,"metros")
```
**009-preguntas y respuestas.md**
```markdown
Resultado de aprendizaje
Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

Criterios de evaluación
a) Se ha escrito y probado código que haga uso de estructuras de selección.
Mi ejercicio cumple con este apartado porque he hecho una estrutura
if - elif para atrapar la opción del usuario en la lista de alumnos

b) Se han utilizado estructuras de repetición.
He utilizado la estructura de control While para crear una 
repetición infinita en mi programa porque quiero que el programa
pregunte por nuevos alumnos sin fin

c) Se han reconocido las posibilidades de las sentencias de salto.
d) Se ha escrito código utilizando control de excepciones.
e) Se han creado programas ejecutables utilizando diferentes estructuras de control.
f) Se han probado y depurado los programas.
g) Se ha comentado y documentado el código.
h) Se han creado excepciones.
i) Se han utilizado aserciones para la detección y corrección de errores durante la fase de desarrollo.
```
## 2-Proyecto
**001-programa.py**
```python
# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)

# Cada ciclista es un diccionario con sus datos

# Mensaje de bienvenida

# Entrar en un bucle infinito

# Le enseño al usuario lo que puede hacer
	
# Le pregunto qué quiere hacer
  
# Anoto su decisión y tomo una acción - la acción puede ser
  
# Añadimos el nuevo ciclista a la lista

# Rompe el bucle y termina el programa

#Mensaje de Hasta luego
```
**002-primer codigo.py**
```python
"""
Registro de Ciclistas
Ciclistas Versión 1.0 By Heverton
"""

# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    print("\n--- Insertar nuevo ciclista ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    email = input("Email: ")
    telefono = input("Teléfono: ")


```
**003-crud.py**
```python
# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 1.0 By Heverton
"""

# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    print("\n--- Insertar nuevo ciclista ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    email = input("Email: ")
    telefono = input("Teléfono: ")


```
**004-elif.py**
```python
# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 1.0 By Heverton
"""

# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    print("\n--- Insertar nuevo ciclista ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    # Creamos un diccionario con los datos del nuevo ciclista
    nuevo_ciclista = {
        "id": siguiente_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "fecha_nacimiento": fecha_nacimiento,
        "email": email,
        "telefono": telefono,
    }

    # Añadimos el nuevo ciclista a la lista
    ciclistas.append(nuevo_ciclista)

    print(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1


def listar_ciclistas():
    """
    READ - Muestra todos los ciclistas registrados
    """
    print("\n--- Lista de ciclistas ---")

    # Si la lista está vacía, avisamos al usuario
    if len(ciclistas) == 0:
        print("No hay ciclistas registrados todavía.")
        return

```
**005-listas.py**
```python
# Primero presento el programa
# CRUD = Create, Read, Update, Delete
# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
"""
  Programa CRUD
  Versión 0.1
  por Heverton Marques
"""
# Mensaje de bienvenida
"""
print("Registro de Ciclistas")
print("Versión 1.0 By Heverton")
"""
# Entrar en un bucle infinito
while True:
  # Le enseño al usuario lo que puede hacer
	print("1.-Insertar un registro")
  print("2.-Leer los registros")
  print("3.-Actualizar un registro")
  print("4.-Eliminar un registro")
  # Le pregunto qué quiere hacer
	 if opcion == "1":
            insertar_ciclista()
        elif opcion == "2":
            listar_ciclistas()
        elif opcion == "3":
            actualizar_ciclista()
        elif opcion == "4":
            eliminar_ciclista()
        elif opcion == "5":
            limpiar_pantalla()
            print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
            break  # Rompe el bucle y termina el programa
        else:
            mensaje_error("Opción no válida, inténtalo de nuevo.")
            pausar()
  # Anoto su decisión y tomo una acción - la acción puede ser
def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    print("\n--- Insertar nuevo ciclista ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    # Creamos un diccionario con los datos del nuevo ciclista
    nuevo_ciclista = {
        "id": siguiente_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "fecha_nacimiento": fecha_nacimiento,
        "email": email,
        "telefono": telefono,
    }

    # Añadimos el nuevo ciclista a la lista
    ciclistas.append(nuevo_ciclista)

    print(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1


def listar_ciclistas():
    """
    READ - Muestra todos los ciclistas registrados
    """
    print("\n--- Lista de ciclistas ---")

    # Si la lista está vacía, avisamos al usuario
    if len(ciclistas) == 0:
        print("No hay ciclistas registrados todavía.")
        return

    # Recorremos la lista y mostramos los datos de cada ciclista
    for ciclista in ciclistas:
        print(f"ID: {ciclista['id']}")
        print(f"  Nombre: {ciclista['nombre']} {ciclista['apellidos']}")
        print(f"  Fecha de nacimiento: {ciclista['fecha_nacimiento']}")
        print(f"  Email: {ciclista['email']}")
        print(f"  Teléfono: {ciclista['telefono']}")
        print("-" * 30)


def buscar_ciclista_por_id(id_buscado):
    """
    Función auxiliar (no es parte del menú) que busca un ciclista por su ID
    y devuelve el diccionario correspondiente, o None si no lo encuentra
    """
    for ciclista in ciclistas:
        if ciclista["id"] == id_buscado:
            return ciclista
    return None


def actualizar_ciclista():
    """
    UPDATE - Busca un ciclista por ID y actualiza sus datos
    """
    print("\n--- Actualizar ciclista ---")

    # Primero mostramos la lista para que el usuario sepa qué ID escoger
    listar_ciclistas()

    try:
        id_buscado = int(input("Introduce el ID del ciclista a actualizar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    # Buscamos el ciclista con ese ID
    ciclista = buscar_ciclista_por_id(id_buscado)

    # Si no existe, avisamos y salimos de la función
    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    print("Deja el campo en blanco y pulsa Enter si no quieres cambiarlo.")

    # Pedimos los nuevos datos; si el usuario no escribe nada, mantenemos el valor actual
    nuevo_nombre = input(f"Nombre ({ciclista['nombre']}): ")
    nuevo_apellidos = input(f"Apellidos ({ciclista['apellidos']}): ")
    nueva_fecha = input(f"Fecha de nacimiento ({ciclista['fecha_nacimiento']}): ")
    nuevo_email = input(f"Email ({ciclista['email']}): ")
    nuevo_telefono = input(f"Teléfono ({ciclista['telefono']}): ")

    # Solo actualizamos el campo si el usuario escribió algo nuevo
    if nuevo_nombre != "":
        ciclista["nombre"] = nuevo_nombre
    if nuevo_apellidos != "":
        ciclista["apellidos"] = nuevo_apellidos
    if nueva_fecha != "":
        ciclista["fecha_nacimiento"] = nueva_fecha
    if nuevo_email != "":
        ciclista["email"] = nuevo_email
    if nuevo_telefono != "":
        ciclista["telefono"] = nuevo_telefono

    print("Ciclista actualizado con éxito.")


def eliminar_ciclista():
    """
    DELETE - Busca un ciclista por ID y lo elimina de la lista
    """
    print("\n--- Eliminar ciclista ---")

    # Mostramos la lista para que el usuario sepa qué ID eliminar
    listar_ciclistas()

    try:
        id_buscado = int(input("Introduce el ID del ciclista a eliminar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    ciclista = buscar_ciclista_por_id(id_buscado)

    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    # Pedimos confirmación antes de borrar, para evitar borrados accidentales
    confirmacion = input(
        f"¿Seguro que quieres eliminar a {ciclista['nombre']} {ciclista['apellidos']}? (s/n): "
    )

    if confirmacion.lower() == "s":
        # Quitamos el ciclista de la lista
        ciclistas.remove(ciclista)
        print("Ciclista eliminado con éxito.")
    else:
        print("Operación cancelada.")


def menu_principal():
    """
    Función principal - Muestra el menú y controla el bucle del programa
    """
    print("Registro de Ciclistas")
    print("Versión 1.0 By Heverton")



 
```
**006-probar.py**
```python
# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 1.1 By Heverton
"""

# ------------------------------------------------------------------
# Excepción personalizada
# Creamos nuestra propia clase de error para cuando el usuario
# introduce un ID que no tiene sentido (negativo o cero).
# Hereda de Exception, que es la clase base de todos los errores.
# ------------------------------------------------------------------
class IDInvalidoError(Exception):
    """Se lanza cuando el ID introducido por el usuario no es válido (<= 0)"""
    pass


# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    print("\n--- Insertar nuevo ciclista ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    # Creamos un diccionario con los datos del nuevo ciclista
    nuevo_ciclista = {
        "id": siguiente_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "fecha_nacimiento": fecha_nacimiento,
        "email": email,
        "telefono": telefono,
    }

    # Aserción: comprobamos, durante el desarrollo, que el diccionario
    # que acabamos de crear tiene realmente el ID que esperábamos.
    # Si esto fallara alguna vez, sería un error de lógica en el programa,
    # no un error del usuario.
    assert nuevo_ciclista["id"] == siguiente_id, "El ID del nuevo ciclista no coincide con el contador"

    # Añadimos el nuevo ciclista a la lista
    ciclistas.append(nuevo_ciclista)

    print(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1

    # Otra aserción: el contador siempre debe quedar en 1 o más.
    # Si esto fallara, algo estaría muy mal en la lógica del programa.
    assert siguiente_id >= 1, "El contador de IDs no puede ser menor que 1"


def listar_ciclistas():
    """
    READ - Muestra todos los ciclistas registrados
    """
    print("\n--- Lista de ciclistas ---")

    # Si la lista está vacía, avisamos al usuario
    if len(ciclistas) == 0:
        print("No hay ciclistas registrados todavía.")
        return

    # Recorremos la lista y mostramos los datos de cada ciclista
    for ciclista in ciclistas:
        print(f"ID: {ciclista['id']}")
        print(f"  Nombre: {ciclista['nombre']} {ciclista['apellidos']}")
        print(f"  Fecha de nacimiento: {ciclista['fecha_nacimiento']}")
        print(f"  Email: {ciclista['email']}")
        print(f"  Teléfono: {ciclista['telefono']}")
        print("-" * 30)


def buscar_ciclista_por_id(id_buscado):
    """
    Función auxiliar (no es parte del menú) que busca un ciclista por su ID
    y devuelve el diccionario correspondiente, o None si no lo encuentra
    """
    for ciclista in ciclistas:
        if ciclista["id"] == id_buscado:
            return ciclista
    return None


def pedir_id_valido(mensaje):
    """
    Función auxiliar que pide un ID al usuario, lo convierte a número,
    y lanza nuestra excepción personalizada si el ID no es válido
    (negativo o cero). Devuelve el ID ya validado, o None si hubo
    algún error (ya sea de conversión o de valor).
    """
    try:
        id_introducido = int(input(mensaje))

        # Si el ID no es positivo, lanzamos nuestra propia excepción
        if id_introducido <= 0:
            raise IDInvalidoError(f"El ID {id_introducido} no es válido, debe ser mayor que 0")

        return id_introducido

    except ValueError:
        # Esto ocurre si el usuario escribe una letra en vez de un número
        print("El ID debe ser un número.")
        return None

    except IDInvalidoError as error:
        # Esto ocurre si el número es válido pero no tiene sentido como ID
        print(f"Error: {error}")
        return None


def actualizar_ciclista():
    """
    UPDATE - Busca un ciclista por ID y actualiza sus datos
    """
    print("\n--- Actualizar ciclista ---")

    # Primero mostramos la lista para que el usuario sepa qué ID escoger
    listar_ciclistas()

    # Usamos la función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a actualizar: ")

    # Si hubo cualquier error (conversión o ID inválido), salimos de la función
    if id_buscado is None:
        return

    # Buscamos el ciclista con ese ID
    ciclista = buscar_ciclista_por_id(id_buscado)

    # Si no existe, avisamos y salimos de la función
    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    print("Deja el campo en blanco y pulsa Enter si no quieres cambiarlo.")

    # Pedimos los nuevos datos; si el usuario no escribe nada, mantenemos el valor actual
    nuevo_nombre = input(f"Nombre ({ciclista['nombre']}): ")
    nuevo_apellidos = input(f"Apellidos ({ciclista['apellidos']}): ")
    nueva_fecha = input(f"Fecha de nacimiento ({ciclista['fecha_nacimiento']}): ")
    nuevo_email = input(f"Email ({ciclista['email']}): ")
    nuevo_telefono = input(f"Teléfono ({ciclista['telefono']}): ")

    # Solo actualizamos el campo si el usuario escribió algo nuevo
    if nuevo_nombre != "":
        ciclista["nombre"] = nuevo_nombre
    if nuevo_apellidos != "":
        ciclista["apellidos"] = nuevo_apellidos
    if nueva_fecha != "":
        ciclista["fecha_nacimiento"] = nueva_fecha
    if nuevo_email != "":
        ciclista["email"] = nuevo_email
    if nuevo_telefono != "":
        ciclista["telefono"] = nuevo_telefono

    print("Ciclista actualizado con éxito.")


def eliminar_ciclista():
    """
    DELETE - Busca un ciclista por ID y lo elimina de la lista
    """
    print("\n--- Eliminar ciclista ---")

    # Mostramos la lista para que el usuario sepa qué ID eliminar
    listar_ciclistas()

    # Usamos la misma función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a eliminar: ")

    if id_buscado is None:
        return

    ciclista = buscar_ciclista_por_id(id_buscado)

    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    # Pedimos confirmación antes de borrar, para evitar borrados accidentales
    confirmacion = input(
        f"¿Seguro que quieres eliminar a {ciclista['nombre']} {ciclista['apellidos']}? (s/n): "
    )

    if confirmacion.lower() == "s":
        # Cuántos ciclistas había antes de borrar, para comprobarlo después
        total_antes = len(ciclistas)

        # Quitamos el ciclista de la lista
        ciclistas.remove(ciclista)

        # Aserción: comprobamos que la lista realmente se quedó con un
        # elemento menos. Si no fuera así, habría un error de lógica.
        assert len(ciclistas) == total_antes - 1, "La lista no se actualizó correctamente al eliminar"

        print("Ciclista eliminado con éxito.")
    else:
        print("Operación cancelada.")


def menu_principal():
    """
    Función principal - Muestra el menú y controla el bucle del programa
    """
    print("Registro de Ciclistas")
    print("Versión 1.1 by Heverton")

    # Bucle infinito: el programa sigue funcionando hasta que el usuario decida salir
    while True:
        print("\n=== MENÚ ===")
        print("1.- Insertar un ciclista")
        print("2.- Listar los ciclistas")
        print("3.- Actualizar un ciclista")
        print("4.- Eliminar un ciclista")
        print("5.- Salir")

        opcion = input("Escoge una opción: ")

        # Según la opción elegida, llamamos a la función correspondiente
        if opcion == "1":
            insertar_ciclista()
        elif opcion == "2":
            listar_ciclistas()
        elif opcion == "3":
            actualizar_ciclista()
        elif opcion == "4":
            eliminar_ciclista()
        elif opcion == "5":
            print("¡Hasta luego!")
            break  # Rompe el bucle y termina el programa
        else:
            print("Opción no válida, inténtalo de nuevo.")


# Este bloque solo se ejecuta si el archivo se corre directamente
# (y no si se importa desde otro programa)
if __name__ == "__main__":
    menu_principal()
```
**007-ejercicio.py**
```python
# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 1.1 By Heverton
"""

# ------------------------------------------------------------------
# Excepción personalizada
# Creamos nuestra propia clase de error para cuando el usuario
# introduce un ID que no tiene sentido (negativo o cero).
# Hereda de Exception, que es la clase base de todos los errores.
# ------------------------------------------------------------------
class IDInvalidoError(Exception):
    """Se lanza cuando el ID introducido por el usuario no es válido (<= 0)"""
    pass


# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    print("\n--- Insertar nuevo ciclista ---")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    email = input("Email: ")
    telefono = input("Teléfono: ")

    # Creamos un diccionario con los datos del nuevo ciclista
    nuevo_ciclista = {
        "id": siguiente_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "fecha_nacimiento": fecha_nacimiento,
        "email": email,
        "telefono": telefono,
    }

    # Aserción: comprobamos, durante el desarrollo, que el diccionario
    # que acabamos de crear tiene realmente el ID que esperábamos.
    # Si esto fallara alguna vez, sería un error de lógica en el programa,
    # no un error del usuario.
    assert nuevo_ciclista["id"] == siguiente_id, "El ID del nuevo ciclista no coincide con el contador"

    # Añadimos el nuevo ciclista a la lista
    ciclistas.append(nuevo_ciclista)

    print(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1

    # Otra aserción: el contador siempre debe quedar en 1 o más.
    # Si esto fallara, algo estaría muy mal en la lógica del programa.
    assert siguiente_id >= 1, "El contador de IDs no puede ser menor que 1"


def listar_ciclistas():
    """
    READ - Muestra todos los ciclistas registrados
    """
    print("\n--- Lista de ciclistas ---")

    # Si la lista está vacía, avisamos al usuario
    if len(ciclistas) == 0:
        print("No hay ciclistas registrados todavía.")
        return

    # Recorremos la lista y mostramos los datos de cada ciclista
    for ciclista in ciclistas:
        print(f"ID: {ciclista['id']}")
        print(f"  Nombre: {ciclista['nombre']} {ciclista['apellidos']}")
        print(f"  Fecha de nacimiento: {ciclista['fecha_nacimiento']}")
        print(f"  Email: {ciclista['email']}")
        print(f"  Teléfono: {ciclista['telefono']}")
        print("-" * 30)


def buscar_ciclista_por_id(id_buscado):
    """
    Función auxiliar (no es parte del menú) que busca un ciclista por su ID
    y devuelve el diccionario correspondiente, o None si no lo encuentra
    """
    for ciclista in ciclistas:
        if ciclista["id"] == id_buscado:
            return ciclista
    return None


def pedir_id_valido(mensaje):
    """
    Función auxiliar que pide un ID al usuario, lo convierte a número,
    y lanza nuestra excepción personalizada si el ID no es válido
    (negativo o cero). Devuelve el ID ya validado, o None si hubo
    algún error (ya sea de conversión o de valor).
    """
    try:
        id_introducido = int(input(mensaje))

        # Si el ID no es positivo, lanzamos nuestra propia excepción
        if id_introducido <= 0:
            raise IDInvalidoError(f"El ID {id_introducido} no es válido, debe ser mayor que 0")

        return id_introducido

    except ValueError:
        # Esto ocurre si el usuario escribe una letra en vez de un número
        print("El ID debe ser un número.")
        return None

    except IDInvalidoError as error:
        # Esto ocurre si el número es válido pero no tiene sentido como ID
        print(f"Error: {error}")
        return None


def actualizar_ciclista():
    """
    UPDATE - Busca un ciclista por ID y actualiza sus datos
    """
    print("\n--- Actualizar ciclista ---")

    # Primero mostramos la lista para que el usuario sepa qué ID escoger
    listar_ciclistas()

    # Usamos la función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a actualizar: ")

    # Si hubo cualquier error (conversión o ID inválido), salimos de la función
    if id_buscado is None:
        return

    # Buscamos el ciclista con ese ID
    ciclista = buscar_ciclista_por_id(id_buscado)

    # Si no existe, avisamos y salimos de la función
    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    print("Deja el campo en blanco y pulsa Enter si no quieres cambiarlo.")

    # Pedimos los nuevos datos; si el usuario no escribe nada, mantenemos el valor actual
    nuevo_nombre = input(f"Nombre ({ciclista['nombre']}): ")
    nuevo_apellidos = input(f"Apellidos ({ciclista['apellidos']}): ")
    nueva_fecha = input(f"Fecha de nacimiento ({ciclista['fecha_nacimiento']}): ")
    nuevo_email = input(f"Email ({ciclista['email']}): ")
    nuevo_telefono = input(f"Teléfono ({ciclista['telefono']}): ")

    # Solo actualizamos el campo si el usuario escribió algo nuevo
    if nuevo_nombre != "":
        ciclista["nombre"] = nuevo_nombre
    if nuevo_apellidos != "":
        ciclista["apellidos"] = nuevo_apellidos
    if nueva_fecha != "":
        ciclista["fecha_nacimiento"] = nueva_fecha
    if nuevo_email != "":
        ciclista["email"] = nuevo_email
    if nuevo_telefono != "":
        ciclista["telefono"] = nuevo_telefono

    print("Ciclista actualizado con éxito.")


def eliminar_ciclista():
    """
    DELETE - Busca un ciclista por ID y lo elimina de la lista
    """
    print("\n--- Eliminar ciclista ---")

    # Mostramos la lista para que el usuario sepa qué ID eliminar
    listar_ciclistas()

    # Usamos la misma función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a eliminar: ")

    if id_buscado is None:
        return

    ciclista = buscar_ciclista_por_id(id_buscado)

    if ciclista is None:
        print(f"No existe ningún ciclista con el ID {id_buscado}")
        return

    # Pedimos confirmación antes de borrar, para evitar borrados accidentales
    confirmacion = input(
        f"¿Seguro que quieres eliminar a {ciclista['nombre']} {ciclista['apellidos']}? (s/n): "
    )

    if confirmacion.lower() == "s":
        # Cuántos ciclistas había antes de borrar, para comprobarlo después
        total_antes = len(ciclistas)

        # Quitamos el ciclista de la lista
        ciclistas.remove(ciclista)

        # Aserción: comprobamos que la lista realmente se quedó con un
        # elemento menos. Si no fuera así, habría un error de lógica.
        assert len(ciclistas) == total_antes - 1, "La lista no se actualizó correctamente al eliminar"

        print("Ciclista eliminado con éxito.")
    else:
        print("Operación cancelada.")


def menu_principal():
    """
    Función principal - Muestra el menú y controla el bucle del programa
    """
    print("Registro de Ciclistas")
    print("Versión 1.1 by Heverton")

    # Bucle infinito: el programa sigue funcionando hasta que el usuario decida salir
    while True:
        print("\n=== MENÚ ===")
        print("1.- Insertar un ciclista")
        print("2.- Listar los ciclistas")
        print("3.- Actualizar un ciclista")
        print("4.- Eliminar un ciclista")
        print("5.- Salir")

        opcion = input("Escoge una opción: ")

        # Según la opción elegida, llamamos a la función correspondiente
        if opcion == "1":
            insertar_ciclista()
        elif opcion == "2":
            listar_ciclistas()
        elif opcion == "3":
            actualizar_ciclista()
        elif opcion == "4":
            eliminar_ciclista()
        elif opcion == "5":
            print("¡Hasta luego!")
            break  # Rompe el bucle y termina el programa
        else:
            print("Opción no válida, inténtalo de nuevo.")


# Este bloque solo se ejecuta si el archivo se corre directamente
# (y no si se importa desde otro programa)
if __name__ == "__main__":
    menu_principal()
```
**008-ejercicio mejorado con IA.py**
```python
#Es un programa para inscribir a nuevos ciclistas en un equipo.
# CRUD = Create, Read, Update, Delete
"""
Registro de Ciclistas
Ciclistas Versión 2.1 By Heverton
"""

import os


# ------------------------------------------------------------------
# Códigos ANSI para dar color y estilo al texto en la terminal
# No necesitan ninguna librería externa, funcionan en la mayoría
# de terminales (Windows Terminal, macOS, Linux)
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


# ------------------------------------------------------------------
# Excepción personalizada
# Creamos nuestra propia clase de error para cuando el usuario
# introduce un ID que no tiene sentido (negativo o cero).
# Hereda de Exception, que es la clase base de todos los errores.
# ------------------------------------------------------------------
class IDInvalidoError(Exception):
    """Se lanza cuando el ID introducido por el usuario no es válido (<= 0)"""
    pass


# Ancho fijo que usamos para las líneas separadoras y las tablas
ANCHO = 60


# Lista donde vamos a guardar todos los ciclistas (nuestra "base de datos" en memoria)
# Cada ciclista es un diccionario con sus datos
ciclistas = []

# Variable para ir generando un identificador único para cada ciclista
siguiente_id = 1


def limpiar_pantalla():
    """
    Limpia la terminal para que el programa se vea más ordenado
    (funciona tanto en Windows como en macOS/Linux)
    """
    os.system("cls" if os.name == "nt" else "clear")


def linea(caracter="─"):
    """
    Imprime una línea separadora del ancho definido arriba,
    para dividir visualmente las secciones del programa
    """
    print(Color.GRIS + caracter * ANCHO + Color.RESET)


def titulo(texto):
    """
    Imprime un título centrado, con color y rodeado de una caja simple
    """
    print(Color.CIAN + "╔" + "═" * (ANCHO - 2) + "╗" + Color.RESET)
    print(Color.CIAN + "║" + Color.RESET + texto.center(ANCHO - 2) + Color.CIAN +"║" + Color.RESET)
    print(Color.CIAN + "╚" + "═" * (ANCHO - 2) + "╝" + Color.RESET)


def mensaje_exito(texto):
    """Imprime un mensaje de éxito en verde, con un icono de check"""
    print(Color.VERDE + "✔ " + texto + Color.RESET)


def mensaje_error(texto):
    """Imprime un mensaje de error en rojo, con un icono de aviso"""
    print(Color.ROJO + "✘ " + texto + Color.RESET)


def mensaje_info(texto):
    """Imprime un mensaje informativo en amarillo"""
    print(Color.AMARILLO + "ℹ " + texto + Color.RESET)


def pausar():
    """Pausa el programa hasta que el usuario pulse Enter, para que pueda leer el resultado"""
    input(Color.GRIS + "\nPulsa Enter para continuar..." + Color.RESET)


def pedir_id_valido(mensaje):
    """
    Función auxiliar que pide un ID al usuario, lo convierte a número,
    y lanza nuestra excepción personalizada si el ID no es válido
    (negativo o cero). Devuelve el ID ya validado, o None si hubo
    algún error (ya sea de conversión o de valor).
    """
    try:
        id_introducido = int(input(mensaje))

        # Si el ID no es positivo, lanzamos nuestra propia excepción
        if id_introducido <= 0:
            raise IDInvalidoError(f"El ID {id_introducido} no es válido, debe ser mayor que 0")

        return id_introducido

    except ValueError:
        # Esto ocurre si el usuario escribe una letra en vez de un número
        mensaje_error("El ID debe ser un número.")
        return None

    except IDInvalidoError as error:
        # Esto ocurre si el número es válido pero no tiene sentido como ID
        mensaje_error(str(error))
        return None


def insertar_ciclista():
    """
    CREATE - Pide los datos al usuario y crea un nuevo registro de ciclista
    """
    global siguiente_id

    limpiar_pantalla()
    titulo("🚴  INSERTAR NUEVO CICLISTA")
    print()

    nombre = input(Color.NEGRITA + "Nombre: " + Color.RESET)
    apellidos = input(Color.NEGRITA + "Apellidos: " + Color.RESET)
    fecha_nacimiento = input(Color.NEGRITA + "Fecha de nacimiento (DD-MM-AAAA): " + Color.RESET)
    email = input(Color.NEGRITA + "Email: " + Color.RESET)
    telefono = input(Color.NEGRITA + "Teléfono: " + Color.RESET)

    # Creamos un diccionario con los datos del nuevo ciclista
    nuevo_ciclista = {
        "id": siguiente_id,
        "nombre": nombre,
        "apellidos": apellidos,
        "fecha_nacimiento": fecha_nacimiento,
        "email": email,
        "telefono": telefono,
    }

    # Aserción: comprobamos, durante el desarrollo, que el diccionario
    # que acabamos de crear tiene realmente el ID que esperábamos.
    # Si esto fallara alguna vez, sería un error de lógica en el programa,
    # no un error del usuario.
    assert nuevo_ciclista["id"] == siguiente_id, "El ID del nuevo ciclista no coincide con el contador"

    # Añadimos el nuevo ciclista a la lista
    ciclistas.append(nuevo_ciclista)

    print()
    mensaje_exito(f"Ciclista '{nombre} {apellidos}' insertado con éxito (ID: {siguiente_id})")

    # Aumentamos el contador para que el próximo ciclista tenga un ID distinto
    siguiente_id += 1

    # Otra aserción: el contador siempre debe quedar en 1 o más.
    # Si esto fallara, algo estaría muy mal en la lógica del programa.
    assert siguiente_id >= 1, "El contador de IDs no puede ser menor que 1"

    pausar()


def listar_ciclistas():
    """
    READ - Muestra todos los ciclistas registrados en formato de tabla
    """
    limpiar_pantalla()
    titulo("📋  LISTA DE CICLISTAS")
    print()

    # Si la lista está vacía, avisamos al usuario
    if len(ciclistas) == 0:
        mensaje_info("No hay ciclistas registrados todavía.")
        pausar()
        return

    # Cabecera de la tabla, en negrita y color
    cabecera = f"{'ID':<4}{'NOMBRE':<20}{'EMAIL':<25}{'TELÉFONO':<12}"
    print(Color.AZUL + Color.NEGRITA + cabecera + Color.RESET)
    linea()

    # Recorremos la lista y mostramos los datos de cada ciclista en una fila
    for ciclista in ciclistas:
        nombre_completo = f"{ciclista['nombre']} {ciclista['apellidos']}"
        fila = (
            f"{ciclista['id']:<4}"
            f"{nombre_completo:<20}"
            f"{ciclista['email']:<25}"
            f"{ciclista['telefono']:<12}"
        )
        print(fila)

    linea()
    print(Color.GRIS + f"Total: {len(ciclistas)} ciclista(s)" + Color.RESET)
    pausar()


def buscar_ciclista_por_id(id_buscado):
    """
    Función auxiliar (no es parte del menú) que busca un ciclista por su ID
    y devuelve el diccionario correspondiente, o None si no lo encuentra
    """
    for ciclista in ciclistas:
        if ciclista["id"] == id_buscado:
            return ciclista
    return None


def actualizar_ciclista():
    """
    UPDATE - Busca un ciclista por ID y actualiza sus datos
    """
    limpiar_pantalla()
    titulo("✏️  ACTUALIZAR CICLISTA")
    print()

    # Si no hay ciclistas, no tiene sentido continuar
    if len(ciclistas) == 0:
        mensaje_info("No hay ciclistas registrados todavía.")
        pausar()
        return

    # Mostramos una lista rápida de IDs disponibles para orientar al usuario
    for ciclista in ciclistas:
        print(Color.GRIS + f"  {ciclista['id']}. {ciclista['nombre']} {ciclista['apellidos']}" + Color.RESET)
    print()

    # Usamos la función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a actualizar: ")

    # Si hubo cualquier error (conversión o ID inválido), salimos de la función
    if id_buscado is None:
        pausar()
        return

    # Buscamos el ciclista con ese ID
    ciclista = buscar_ciclista_por_id(id_buscado)

    # Si no existe, avisamos y salimos de la función
    if ciclista is None:
        mensaje_error(f"No existe ningún ciclista con el ID {id_buscado}")
        pausar()
        return

    print()
    mensaje_info("Deja el campo en blanco y pulsa Enter si no quieres cambiarlo.")
    print()

    # Pedimos los nuevos datos; si el usuario no escribe nada, mantenemos el valor actual
    nuevo_nombre = input(f"Nombre ({ciclista['nombre']}): ")
    nuevo_apellidos = input(f"Apellidos ({ciclista['apellidos']}): ")
    nueva_fecha = input(f"Fecha de nacimiento ({ciclista['fecha_nacimiento']}): ")
    nuevo_email = input(f"Email ({ciclista['email']}): ")
    nuevo_telefono = input(f"Teléfono ({ciclista['telefono']}): ")

    # Solo actualizamos el campo si el usuario escribió algo nuevo
    if nuevo_nombre != "":
        ciclista["nombre"] = nuevo_nombre
    if nuevo_apellidos != "":
        ciclista["apellidos"] = nuevo_apellidos
    if nueva_fecha != "":
        ciclista["fecha_nacimiento"] = nueva_fecha
    if nuevo_email != "":
        ciclista["email"] = nuevo_email
    if nuevo_telefono != "":
        ciclista["telefono"] = nuevo_telefono

    print()
    mensaje_exito("Ciclista actualizado con éxito.")
    pausar()


def eliminar_ciclista():
    """
    DELETE - Busca un ciclista por ID y lo elimina de la lista
    """
    limpiar_pantalla()
    titulo("🗑️  ELIMINAR CICLISTA")
    print()

    if len(ciclistas) == 0:
        mensaje_info("No hay ciclistas registrados todavía.")
        pausar()
        return

    # Mostramos una lista rápida de IDs disponibles para orientar al usuario
    for ciclista in ciclistas:
        print(Color.GRIS + f"  {ciclista['id']}. {ciclista['nombre']} {ciclista['apellidos']}" + Color.RESET)
    print()

    # Usamos la misma función auxiliar para pedir y validar el ID
    id_buscado = pedir_id_valido("Introduce el ID del ciclista a eliminar: ")

    if id_buscado is None:
        pausar()
        return

    ciclista = buscar_ciclista_por_id(id_buscado)

    if ciclista is None:
        mensaje_error(f"No existe ningún ciclista con el ID {id_buscado}")
        pausar()
        return

    # Pedimos confirmación antes de borrar, para evitar borrados accidentales
    print()
    confirmacion = input(
        Color.AMARILLO
        + f"¿Seguro que quieres eliminar a {ciclista['nombre']} {ciclista['apellidos']}? (s/n): "
        + Color.RESET
    )

    print()
    if confirmacion.lower() == "s":
        # Cuántos ciclistas había antes de borrar, para comprobarlo después
        total_antes = len(ciclistas)

        # Quitamos el ciclista de la lista
        ciclistas.remove(ciclista)

        # Aserción: comprobamos que la lista realmente se quedó con un
        # elemento menos. Si no fuera así, habría un error de lógica.
        assert len(ciclistas) == total_antes - 1, "La lista no se actualizó correctamente al eliminar"

        mensaje_exito("Ciclista eliminado con éxito.")
    else:
        mensaje_info("Operación cancelada.")

    pausar()


def menu_principal():
    """
    Función principal - Muestra el menú y controla el bucle del programa
    """
    # Bucle infinito: el programa sigue funcionando hasta que el usuario decida salir
    while True:
        limpiar_pantalla()
        titulo("🚴  REGISTRO DE CICLISTAS  v2.1 By Heverton")
        print()
        print(Color.NEGRITA + "  1." + Color.RESET + " 🆕  Insertar un ciclista")
        print(Color.NEGRITA + "  2." + Color.RESET + " 📋  Listar los ciclistas")
        print(Color.NEGRITA + "  3." + Color.RESET + " ✏️   Actualizar un ciclista")
        print(Color.NEGRITA + "  4." + Color.RESET + " 🗑️   Eliminar un ciclista")
        print(Color.NEGRITA + "  5." + Color.RESET + " 🚪  Salir")
        print()
        linea()

        opcion = input(Color.MAGENTA + "Escoge una opción: " + Color.RESET)

        # Según la opción elegida, llamamos a la función correspondiente
        if opcion == "1":
            insertar_ciclista()
        elif opcion == "2":
            listar_ciclistas()
        elif opcion == "3":
            actualizar_ciclista()
        elif opcion == "4":
            eliminar_ciclista()
        elif opcion == "5":
            limpiar_pantalla()
            print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
            break  # Rompe el bucle y termina el programa
        else:
            mensaje_error("Opción no válida, inténtalo de nuevo.")
            pausar()


# Este bloque solo se ejecuta si el archivo se corre directamente
# (y no si se importa desde otro programa)
if __name__ == "__main__":
    menu_principal()
```
## 3-Resultado de aprendizaje
**000-Criterios de evaluación.md**
```markdown
Criterios de evaluación

a) ¿Se ha escrito y probado código que haga uso de estructuras de selección?
Sí, usé condiciones para decidir qué hacer según la opción que el usuario escoge en el menú.

b) ¿Se han utilizado estructuras de repetición?
Sí, usé un bucle para que el menú siga apareciendo hasta que el usuario quiera salir, y otro bucle para mostrar todos los ciclistas de la lista.

c) ¿Se han reconocido las posibilidades de las sentencias de salto?
Sí, usé una sentencia para salir del programa cuando el usuario elige salir, y otra para parar una función cuando algo no está bien, por ejemplo si el ID no existe.

d) ¿Se ha escrito código utilizando control de excepciones?
Sí, cuando pido un ID, controlo el error por si el usuario escribe una letra en vez de un número, así el programa no se rompe.

e) ¿Se han creado programas ejecutables utilizando diferentes estructuras de control?
Sí, mi programa usa condiciones, bucles, control de errores y sentencias de salto todo junto.

f) ¿Se han probado y depurado los programas?
Sí, probé insertar, listar, actualizar y eliminar ciclistas, y también probé poner cosas incorrectas para ver si el programa aguantaba.

g) ¿Se ha comentado y documentado el código?
Sí, dejé comentarios explicando qué hace cada parte del código.

h) ¿Se han creado excepciones?
Sí, creé una excepción mía llamada IDInvalidoError, para cuando el ID es negativo o cero.

i) ¿Se han utilizado aserciones para la detección y corrección de errores durante la fase de desarrollo?
Sí, puse aserciones pra comprobar cosas como que el ID coincide con el contador y que la lista se queda con un elemento menos al eliminar.
```
