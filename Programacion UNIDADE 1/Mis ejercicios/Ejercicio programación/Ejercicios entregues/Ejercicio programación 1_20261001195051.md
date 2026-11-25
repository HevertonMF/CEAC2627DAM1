# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-01 19:50:51 +0200
- **Usuario:** Heverton Marques
- **UID:** 197609
- **Equipo:** Heverton
- **Sistema operativo:** MINGW64_NT-10.0-26300
- **Versión del kernel:** 3.6.10-3ea87a50.x86_64
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `/c/Users/samar/Documents/DAM 1/Programacion UNIDADE 1`
- **Proyecto documentado:** `/c/Users/samar/Documents/DAM 1/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 1`
- **HMAC-SHA-256 de autenticidad:** `25cce91b24835a70883235b6d2656cfb3e4523e94913308ec03c81f53e294650`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
/c/Users/samar/Documents/DAM 1/Programacion UNIDADE 1/Meus Ejercicios/Ejercicio programación 1
├── 1-Ejercicios
│   ├── 001-Estructura y bloques fundamentales
│   │   ├── 000-instruccion.md
│   │   ├── 001-comentrios.py
│   │   ├── 002-docstrings.py
│   │   ├── 003-print.py
│   │   ├── 004-input.py
│   │   └── 005-pequenoprograma.py
│   ├── 002-variables
│   │   ├── 001-mi primera variable.py
│   │   ├── 002-saco variable por pantalha.py
│   │   ├── 003-pregunta y respuesta.py
│   │   └── 004- cambiando el valor.py
│   ├── 003-tipos de variables
│   │   ├── 000-intruciones.md
│   │   ├── 001-edad entera.py
│   │   ├── 002-altura flotante.py
│   │   ├── 003-cadena.py
│   │   ├── 004-error en tipos de dados.py
│   │   ├── 005-separador.py
│   │   └── 006-conversion de tipo.py
│   ├── 004-Literales
│   │   ├── 000-introducion.md
│   │   ├── 001-ejemplos.py
│   │   └── 002-resumen.py
│   ├── 005-Constantes
│   │   ├── 000-introducion.md
│   │   └── 001- cons en python.py
│   ├── 006-Operadores y expresiones
│   │   ├── 000-introducion.md
│   │   ├── 0001-aritmeticos.py
│   │   ├── 002-comparacion.py
│   │   ├── 003-operadores booleanos.py
│   │   └── 004-aritmetico abreviado.py
│   └── 007-ejercio final de unidad
│       ├── 001-calculadora iva.py
│       ├── 002-salidas y entradas.py
│       ├── 003-cambio de tipo.py
│       ├── 004-operadores.py
│       ├── 005-A continuacion vososotros.md
│       ├── 006-modificaciones.py
│       ├── 007-modificaciones funcionales.py
│       ├── 008-ejemplo ciclismo.py
│       └── 009-mi ejercicio.py
├── 2-Proyecto
│   ├── 001-selecion.py
│   ├── 002-repeticion.py
│   ├── 003-solto.py
│   ├── 004-exepciones.py
│   ├── 005-probar.py
│   ├── 006-aserciones.py
│   ├── 007-documentar.py
│   ├── 008-Calculadora de meta.py
│   └── 009-Calculadora de meta IA.py
└── 3-Resultado de aprendizaje
    └── 000-Criterios de evaluación.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Ejercicio programación 1
## 1-Ejercicios
### 001-Estructura y bloques fundamentales
**000-instruccion.md**
```markdown
```
**001-comentrios.py**
```python
'''
	Las comillas pueden ser dobles
  O pueden ser sencillas
  Pero tiene que haber tres
'''
```
**002-docstrings.py**
```python
"""
	Esto es un docstring
  Y a la vez es un comentario de varias lineas
"""
```
**003-print.py**
```python
print("Empezamos con Python")
```
**004-input.py**
```python
input("como te llamas?")

```
**005-pequenoprograma.py**
```python
# Importamos librerias
print("Importamos librerias")
# Define condiciones iniciales
print("Definimos condiciones iniciales")
# Define funciones y clases
print("Definimos funciones y clases")
# Ejecuta el bucle principal
print("Y ahora ejecutamos el bloque principal")
```
### 002-variables
**001-mi primera variable.py**
```python
edad = 35 #solo mmeto el valor en la memoria
```
**002-saco variable por pantalha.py**
```python
edad = 35 #solo mmeto el valor en la memoria
print(edad)

```
**003-pregunta y respuesta.py**
```python
edad = input("¿Cuántos años tienes?: ")
print("Tienes",edad,"años")
```
**004- cambiando el valor.py**
```python
edad = input("¿Cuántos años tienes?: ")
print("Tienes",edad,"años")
edad = input("¿Cuántos años tienes?: ")
print("Tienes",edad,"años")
```
### 003-tipos de variables
**000-intruciones.md**
```markdown
```
**001-edad entera.py**
```python
edad = 35
print(edad)
print(type(edad))

```
**002-altura flotante.py**
```python
edad = 35
print(edad)
print(type(edad))

altura = 1.69
print(altura)
print(type(altura))
```
**003-cadena.py**
```python
edad = 35
print(edad)
print(type(edad))

altura = 1.69
print(altura)
print(type(altura))

nombre = "Heverton"
print(nombre)
print(type(nombre))
```
**004-error en tipos de dados.py**
```python
edad = 35	# Esto es un entero
print(edad * 2)
edad = "35"	# Pero esto es una cadena
print(edad * 2)
```
**005-separador.py**
```python
print("-" * 20)

```
**006-conversion de tipo.py**
```python
edad = input("Dime tu edad: ") # Input siempre es cadena
edad = int(edad)  # Convierte el dato a tipo entero
print(edad*2) 		# Multiplicación ahora es correcta

```
### 004-Literales
**000-introducion.md**
```markdown
```
**001-ejemplos.py**
```python
edad = 48 # 48 es un literal de tipo entero
altura = 1.78 # 1.78 es un literal de tipo flotante
nombre = "Jose Vicente" # Jose Vicente es un literal de tipo cadena

```
**002-resumen.py**
```python
edad = 48
print(edad)

# print es una instrucción - es lo que aporta el lenguaje
# 48 es un literal - es lo que aporta el humano

# Programar es combinar las instrucciones con los literales
```
### 005-Constantes
**000-introducion.md**
```markdown
```
**001- cons en python.py**
```python
# Pero en python no hay constantes

PI = 3.1416
print(PI)

PI = 4
print(PI)

# Convención: Constantes en mayúscula
# (variables en minúscula)

```
### 006-Operadores y expresiones
**000-introducion.md**
```markdown
```
**0001-aritmeticos.py**
```python
print(4 + 3)
print(4 - 3)
print(4 * 3)
print(4 / 3)
print(4 % 3)
```
**002-comparacion.py**
```python
print(4 < 3)
print(4 > 3)
print(4 <= 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```
**003-operadores booleanos.py**
```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 2)
print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)

```
**004-aritmetico abreviado.py**
```python
edad = 35

# Sumar 5 años
edad = edad + 5
edad += 5 # A lo que valía, le sumo 5
edad -= 5 # A lo que valía le resto 5
edad *= 5 # Lo que valía lo multiplico por 5
edad /= 5 # Lo que valía lo divido por 5
```
### 007-ejercio final de unidad
**001-calculadora iva.py**
```python
"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""
```
**002-salidas y entradas.py**
```python
"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

print("Bienvenidos al programa calculadora") 	# Salida
base = input("Introduce la base imponible: ")	# Entrada y variable
```
**003-cambio de tipo.py**
```python
"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

print("Bienvenidos al programa calculadora") 	# Salida
base = input("Introduce la base imponible: ")	# Entrada y variable

base = int(base)										# Convierto el tipo en entero


```
**004-operadores.py**
```python
"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

# OPERACIONES DE ENTRADA - METEMOS INFORMACIÓN EN EL PROGRAMA
print("Bienvenidos al programa calculadora") 	# Salida
base = input("Introduce la base imponible: ")	# Entrada y variable

# OPERACIONES DE CÁLCULO - TRABAJAMOS CON LA INFORMACIÓN
base = int(base)										# Convierto el tipo en entero
iva = base * 0.21										# Operadores = literales
total = base + iva									# Siguen siendo operadores

# OPERACIONES DE SALIDA - EL PROGRAMA NOS DA LOS RESULTADOS
print("Totales de la factura:")
print("Base imponible: ",base)
```
**005-A continuacion vososotros.md**
```markdown
Ahora cada uno de vosotros tiene que hacer operaciones de modificación:
1.-Modificaciones estéticas - personalizar la apariencia del programa
2.-Modificaciones funcionales - que haga cosas diferentes  al ejercicio de referencia
```
**006-modificaciones.py**
```python
"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

# OPERACIONES DE ENTRADA - METEMOS INFORMACIÓN EN EL PROGRAMA
print("-"*60)
print("Bienvenidos al programa calculadora") 	# Salida
print("-"*60)
base = input("Introduce la base imponible: ")	# Entrada y variable

# OPERACIONES DE CÁLCULO - TRABAJAMOS CON LA INFORMACIÓN
base = int(base)										# Convierto el tipo en entero
iva = base * 0.21										# Operadores = literales
total = base + iva									# Siguen siendo operadores

# OPERACIONES DE SALIDA - EL PROGRAMA NOS DA LOS RESULTADOS
print("-"*30)
print("Totales de la factura:")
print("Base imponible: ",base,"€")
print("IVA: ",iva,"€")
print("Total: ",total,"€")
print("-"*30)
```
**007-modificaciones funcionales.py**
```python
"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

# OPERACIONES DE ENTRADA - METEMOS INFORMACIÓN EN EL PROGRAMA
print("-"*60)
print("Bienvenidos al programa calculadora") 	# Salida
print("-"*60)
base = input("Introduce la base imponible: ")	# Entrada y variable
porcentaje = input("Introduce el porcentaje de impuesto: ")

# OPERACIONES DE CÁLCULO - TRABAJAMOS CON LA INFORMACIÓN
base = int(base)										# Convierto el tipo en entero
porcentaje = int(porcentaje)				# Convierto el tipo en entero
iva = base * (porcentaje/100)				# Operadores = literales
total = base + iva									# Siguen siendo operadores

# OPERACIONES DE SALIDA - EL PROGRAMA NOS DA LOS RESULTADOS
print("-"*30)
print("Totales de la factura:")
print("Base imponible: ",base,"€")
print("IVA: ",iva,"€")
print("Total: ",total,"€")
print("-"*30)
```
**008-ejemplo ciclismo.py**
```python
"""
	Calculadora de Pedaladas
  Versión 0.1
  por Jose Vicente Carratala
"""

# Estas son las condiciones iniciales
PEDALADA = 1.5

# Entrada del usuario	
numero_pedaladas = input("Cuantas pedaladas has dado?: ")
numero_pedaladas = int(numero_pedaladas)

# ahora hacemos cálculos
avance = numero_pedaladas*PEDALADA

# Operaciones de salida
print("Has dado",numero_pedaladas,"pedaladas")
print("Cada pedalada son ",pedalada,"metros")
print("Pues has avanzado",avance,"metros")
```
**009-mi ejercicio.py**
```python
"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

# OPERACIONES DE ENTRADA - METEMOS INFORMACIÓN EN EL PROGRAMA
print("-"*60)
print("Bienvenidos al programa calculadora") 	# Salida
print("-"*60)
base = input("Introduce la base imponible: ")	# Entrada y variable
porcentaje = input("Introduce el porcentaje de impuesto: ")

# OPERACIONES DE CÁLCULO - TRABAJAMOS CON LA INFORMACIÓN
base = int(base)										# Convierto el tipo en entero
porcentaje = int(porcentaje)				# Convierto el tipo en entero
iva = base * (porcentaje/100)				# Operadores = literales
total = base + iva									# Siguen siendo operadores

# OPERACIONES DE SALIDA - EL PROGRAMA NOS DA LOS RESULTADOS
print("-"*30)
print("Totales de la factura:")
print("Base imponible: ",base,"€")
print("IVA: ",iva,"€")
print("Total: ",total,"€")
print("-"*30)
```
## 2-Proyecto
**001-selecion.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")
print()

# Entrada del usuario
meta_km = input("¿Cuál es tu meta de kilómetros?: ")
meta_km = float(meta_km)

numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
numero_pedaladas = int(numero_pedaladas)
```
**002-repeticion.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    meta_km = input("¿Cuál es tu meta de kilómetros?: ")
    meta_km = float(meta_km)

    numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
    numero_pedaladas = int(numero_pedaladas)

    # Ahora hacemos los cálculos
```
**003-solto.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    meta_km = input("¿Cuál es tu meta de kilómetros?: ")
    meta_km = float(meta_km)

    numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
    numero_pedaladas = int(numero_pedaladas)

    # Ahora hacemos los cálculos

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # Operaciones de salida
    print()
    print("Has dado", numero_pedaladas, "pedaladas")
    print("Cada pedalada son", metros_por_pedalada, "metros")
    print("Pues has avanzado", round(avance_km, 2), "km")
    print("Tu meta es de", meta_km, "km")
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print("¡Felicidades! Has alcanzado tu meta")

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print("Incluso has hecho", round(kilometros_extra, 2), "km de más. ¡Enhorabuena!")
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print("Todavía no has alcanzado tu meta.")
        print("Te faltan", round(kilometros_restantes, 2), "km para conseguirlo. ¡Sigue así!")
```
**004-exepciones.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    try:
        meta_km = input("¿Cuál es tu meta de kilómetros?: ")
        meta_km = float(meta_km)

        numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print("Entrada inválida. Por favor, introduce solo números.")
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # Ahora hacemos los cálculos

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # Operaciones de salida
    print()
    print("Has dado", numero_pedaladas, "pedaladas")
    print("Cada pedalada son", metros_por_pedalada, "metros")
    print("Pues has avanzado", round(avance_km, 2), "km")
    print("Tu meta es de", meta_km, "km")
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print("¡Felicidades! Has alcanzado tu meta")

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print("Incluso has hecho", round(kilometros_extra, 2), "km de más. ¡Enhorabuena!")
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print("Todavía no has alcanzado tu meta.")
        print("Te faltan", round(kilometros_restantes, 2), "km para conseguirlo. ¡Sigue así!")
```
**005-probar.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    try:
        meta_km = input("¿Cuál es tu meta de kilómetros?: ")
        meta_km = float(meta_km)

        numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print("Entrada inválida. Por favor, introduce solo números.")
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # Ahora hacemos los cálculos

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # Operaciones de salida
    print()
    print("Has dado", numero_pedaladas, "pedaladas")
    print("Cada pedalada son", metros_por_pedalada, "metros")
    print("Pues has avanzado", round(avance_km, 2), "km")
    print("Tu meta es de", meta_km, "km")
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print("¡Felicidades! Has alcanzado tu meta")

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print("Incluso has hecho", round(kilometros_extra, 2), "km de más. ¡Enhorabuena!")
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print("Todavía no has alcanzado tu meta.")
        print("Te faltan", round(kilometros_restantes, 2), "km para conseguirlo. ¡Sigue así!")
```
**006-aserciones.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    try:
        meta_km = input("¿Cuál es tu meta de kilómetros?: ")
        meta_km = float(meta_km)

        numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print("Entrada inválida. Por favor, introduce solo números.")
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # Ahora hacemos los cálculos

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # Operaciones de salida
    print()
    print("Has dado", numero_pedaladas, "pedaladas")
    print("Cada pedalada son", metros_por_pedalada, "metros")
    print("Pues has avanzado", round(avance_km, 2), "km")
    print("Tu meta es de", meta_km, "km")
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print("¡Felicidades! Has alcanzado tu meta")

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print("Incluso has hecho", round(kilometros_extra, 2), "km de más. ¡Enhorabuena!")
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print("Todavía no has alcanzado tu meta.")
        print("Te faltan", round(kilometros_restantes, 2), "km para conseguirlo. ¡Sigue así!")
```
**007-documentar.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    try:
        meta_km = input("¿Cuál es tu meta de kilómetros?: ")
        meta_km = float(meta_km)

        numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print("Entrada inválida. Por favor, introduce solo números.")
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # Ahora hacemos los cálculos

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # Operaciones de salida
    print()
    print("Has dado", numero_pedaladas, "pedaladas")
    print("Cada pedalada son", metros_por_pedalada, "metros")
    print("Pues has avanzado", round(avance_km, 2), "km")
    print("Tu meta es de", meta_km, "km")
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print("¡Felicidades! Has alcanzado tu meta")

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print("Incluso has hecho", round(kilometros_extra, 2), "km de más. ¡Enhorabuena!")
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print("Todavía no has alcanzado tu meta.")
        print("Te faltan", round(kilometros_restantes, 2), "km para conseguirlo. ¡Sigue así!")

    # Preguntamos si el usuario quiere hacer otro cálculo o salir del programa
    print()
    continuar = input("¿Quieres calcular otra vez? (s/n): ")

    # Si no responde "s", rompemos el bucle y terminamos el programa
    if continuar.lower() != "s":
        print("¡Hasta luego!")
        break
```
**008-Calculadora de meta.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""

# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0

print("Calculadora de Kilómetros")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # Entrada del usuario
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    try:
        meta_km = input("¿Cuál es tu meta de kilómetros?: ")
        meta_km = float(meta_km)

        numero_pedaladas = input("¿Cuántas pedaladas has dado?: ")
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print("Entrada inválida. Por favor, introduce solo números.")
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # Ahora hacemos los cálculos

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # Operaciones de salida
    print()
    print("Has dado", numero_pedaladas, "pedaladas")
    print("Cada pedalada son", metros_por_pedalada, "metros")
    print("Pues has avanzado", round(avance_km, 2), "km")
    print("Tu meta es de", meta_km, "km")
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print("¡Felicidades! Has alcanzado tu meta")

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print("Incluso has hecho", round(kilometros_extra, 2), "km de más. ¡Enhorabuena!")
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print("Todavía no has alcanzado tu meta.")
        print("Te faltan", round(kilometros_restantes, 2), "km para conseguirlo. ¡Sigue así!")

    # Preguntamos si el usuario quiere hacer otro cálculo o salir del programa
    print()
    continuar = input("¿Quieres calcular otra vez? (s/n): ")

    # Si no responde "s", rompemos el bucle y terminamos el programa
    if continuar.lower() != "s":
        print("¡Hasta luego!")
        break
```
**009-Calculadora de meta IA.py**
```python
"""
Calculadora de Kilómetros
Versión 1.0 By Heverton
"""


# ------------------------------------------------------------------
# Códigos ANSI para dar color y estilo al texto en la terminal
# No necesitan ninguna librería externa
# ------------------------------------------------------------------
class Color:
    RESET = "\033[0m"
    NEGRITA = "\033[1m"
    CIAN = "\033[96m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    GRIS = "\033[90m"


ANCHO = 50


def linea():
    """Imprime una línea separadora para dividir visualmente las secciones"""
    print(Color.GRIS + "─" * ANCHO + Color.RESET)


def titulo(texto):
    """Imprime un título centrado, con color y rodeado de una caja simple"""
    print(Color.CIAN + "╔" + "═" * (ANCHO - 2) + "╗" + Color.RESET)
    print(Color.CIAN + "║" + Color.RESET + texto.center(ANCHO - 2) + Color.CIAN + "║" + Color.RESET)
    print(Color.CIAN + "╚" + "═" * (ANCHO - 2) + "╝" + Color.RESET)


# Estas son las condiciones iniciales
# Cuántos metros avanza el ciclista por cada pedalada
metros_por_pedalada = 2.0


titulo("🚴  CALCULADORA DE KILÓMETROS")

# Entrar en un bucle infinito, para poder calcular varias veces sin
# tener que volver a ejecutar el programa
while True:
    print()

    # ------------------------------------------------------------------
    # Entrada del usuario
    # Usamos try/except para controlar el caso de que el usuario
    # escriba una letra o algo que no sea un número válido
    # ------------------------------------------------------------------
    try:
        meta_km = input(Color.NEGRITA + "¿Cuál es tu meta de kilómetros?: " + Color.RESET)
        meta_km = float(meta_km)

        numero_pedaladas = input(Color.NEGRITA + "¿Cuántas pedaladas has dado?: " + Color.RESET)
        numero_pedaladas = int(numero_pedaladas)
    except ValueError:
        # Si float() o int() no consiguen convertir el texto a número,
        # se lanza un ValueError y entramos aquí
        print()
        print(Color.ROJO + "Entrada inválida. Por favor, introduce solo números." + Color.RESET)
        # Con "continue" saltamos el resto del bucle y volvemos a empezar,
        # sin llegar a hacer los cálculos con datos incorrectos
        continue

    # ------------------------------------------------------------------
    # Ahora hacemos los cálculos
    # ------------------------------------------------------------------

    # Avance en metros = número de pedaladas x metros que avanza cada una
    avance_metros = numero_pedaladas * metros_por_pedalada

    # Convertimos el avance de metros a kilómetros (1 km = 1000 m)
    avance_km = avance_metros / 1000

    # Calculamos cuánto falta para llegar a la meta
    # Si ya se pasó de la meta, esto puede dar un número negativo,
    # así que lo controlamos más abajo
    kilometros_restantes = meta_km - avance_km

    # ------------------------------------------------------------------
    # Operaciones de salida
    # ------------------------------------------------------------------
    print()
    linea()
    print(f"Has dado {Color.NEGRITA}{numero_pedaladas}{Color.RESET} pedaladas")
    print(f"Cada pedalada son {Color.NEGRITA}{metros_por_pedalada}{Color.RESET} metros")
    print(f"Pues has avanzado {Color.NEGRITA}{avance_km:.2f} km{Color.RESET}")
    print(f"Tu meta es de {Color.NEGRITA}{meta_km:.2f} km{Color.RESET}")
    linea()
    print()

    # Comprobamos si ya alcanzó (o superó) la meta
    if avance_km >= meta_km:
        # Si superó la meta, calculamos cuánto de extra hizo
        kilometros_extra = avance_km - meta_km

        print(Color.VERDE + Color.NEGRITA + "🎉 ¡Felicidades! Has alcanzado tu meta 🎉" + Color.RESET)

        # Si además hizo kilómetros de más, se lo hacemos saber
        if kilometros_extra > 0:
            print(Color.VERDE + f"Incluso has hecho {kilometros_extra:.2f} km de más. ¡Enhorabuena!" + Color.RESET)
    else:
        # Todavía no llegó a la meta: mostramos cuánto le falta
        print(Color.AMARILLO + f"Todavía no has alcanzado tu meta." + Color.RESET)
        print(Color.AMARILLO + f"Te faltan {kilometros_restantes:.2f} km para conseguirlo. ¡Sigue así!" + Color.RESET)

    # Preguntamos si el usuario quiere hacer otro cálculo o salir del programa
    print()
    continuar = input(Color.NEGRITA + "¿Quieres calcular otra vez? (s/n): " + Color.RESET)

    # Si no responde "s", rompemos el bucle y terminamos el programa
    if continuar.lower() != "s":
        print()
        print(Color.CIAN + "¡Hasta luego! 👋" + Color.RESET)
        break
```
## 3-Resultado de aprendizaje
**000-Criterios de evaluación.md**
```markdown
Criterios de evaluación


a) ¿Se han identificado los bloques que componen la estructura de un programa informático?
Sí, mi programa tiene partes bien separadas: primero recojo los datos del usuario, después hago los cálculos, y después muestro el resultado.

b) ¿Se han creado proyectos de desarrollo de aplicaciones?
Sí, he creado un programita completo que funciona solo, no solo un trozo de código suelto.

c) ¿Se han utilizado entornos integrados de desarrollo?
Sí, he escrito y ejecutado el programa varias veces para ver si funcionaba bien.

d) ¿Se han identificado los distintos tipos de variables y la utilidad específica de cada uno?
Sí, usé un número con decimales para guardar la meta y los km, y un número entero para guardar las pedaladas, porque una pedalada siempre es un número entero.

e) ¿Se ha modificado el código de un programa para crear y utilizar variables?
Sí, creé varias variables para guardar los valores que uso en el programa, como la meta, las pedaladas y lo que aún falta.

f) ¿Se han creado y utilizado constantes y literales?
Sí, creé una constante al principio para guardar cuánto avanza cada pedalada, ya que ese valor no cambia. Y también usé números y textos fijos directamente en el código.

g) ¿Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje?
Sí, usé el operador de multiplicar y dividir para hacer los cálculos, y el operador de comparación para ver si alcancé la meta o no.

h) ¿Se ha comprobado el funcionamiento de las conversiones de tipo explícitas e implícitas?
Sí, transformé lo que el usuario escribe (que llega como texto) en número, y probé lo que pasa cuando eso funciona bien y cuando falla.

i) ¿Se han introducido comentarios en el código?
Sí, puse comentarios explicando lo que hace cada parte del código.


```
