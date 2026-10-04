# Reporte de proyecto

## Información de generación

- **Fecha:** 4/10/2026, 14:22:48
- **Proyecto documentado:** `Ejercicio programación 4`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio programación 4
    ├── 1-Ejercicios
    │   ├── 001-concepto de classe
    │   │   ├── 000-intoducion.md
    │   │   ├── 001-varias variables.py
    │   │   ├── 002-peor.py
    │   │   ├── 003-listas.py
    │   │   ├── 004- nueva clase.py
    │   │   └── EJERCICIO 22 sep
    │   ├── 002-estructura y mienbros de una clase variabilidade
    │   │   ├── 000-itroducion.md
    │   │   ├── 001-creo dos alumnos.py
    │   │   ├── 002-propiedades.py
    │   │   └── 003-recupero propiedades.py
    │   ├── 003-creacion de propriedades
    │   │   ├── 000-introducion.md
    │   │   └── 001-Alumno completo.py
    │   ├── 004-creacion de metodos
    │   │   ├── 000-introducion.md
    │   │   ├── 001-clase base.py
    │   │   ├── 002-dime tu nombre.py
    │   │   ├── 003-ahora con perros.py
    │   │   ├── 004-propiedades surrealistas.py
    │   │   └── 005-ejemplo coche.py
    │   ├── 005-Creación de constructores
    │   │   ├── 000-introducion.md
    │   │   ├── 001-clase alumno.py
    │   │   └── 002-Persona.py
    │   ├── 006-utitizacion de clases y objetos
    │   │   ├── 000-introducion.md
    │   │   ├── 001-Clase paciente.py
    │   │   ├── 002-lista de pacientes.py
    │   │   ├── 003-un buen constructor.py
    │   │   ├── 004-añadimos un paciente.py
    │   │   ├── 005-mantener pacientes.py
    │   │   ├── 006-while true.py
    │   │   ├── 007-estructura de seleccion.py
    │   │   ├── 008-datos del paciente.py
    │   │   ├── 009-listado de pacientes.py
    │   │   ├── 010-herencia.py
    │   │   └── criterios
    │   └── 007-utilizacion de classes heredadas
    │       ├── 000-uintoducion.md
    │       ├── 001-perro.py
    │       ├── 002-ahora un gato.py
    │       ├── 003-clase madre.py
    │       ├── 004-mamiferos.py
    │       ├── 005-lagarto.py
    │       └── 006-clase abuela.py
    ├── 2-Proyecto
    │   ├── 001-Clases.py
    │   ├── 002-Gestión de ciclistas.py
    │   └── 003-Gestión de ciclistas IA.py
    └── 3-Resultado de aprendizaje
        └── Resultado de aprendizaje.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite.

## Código (intercalado)

### Ejercicio programación 4/1-Ejercicios/001-concepto de classe

**000-intoducion.md**

```markdown
```

**001-varias variables.py**

```python
nombre = "Jose Vicente"
edad = 48
apellidos = "Carratala Sanchis"
altura = 1.78
...

nombre = "Juan"
apellidos = "Garcia Martinez"
edad = 49
altura = 1.80
...
```

**002-peor.py**

```python
nombre = "Jose Vicente"
edad = 48
apellidos = "Carratala Sanchis"
altura = 1.78
...

nombre2 = "Juan"
apellidos2 = "Garcia Martinez"
edad2 = 49
altura2 = 1.80
...
```

**003-listas.py**

```python
nombre = []
apellidos = []
edad = []
altura = []

nombre.append("Jose Vicente")
edad.append(48)
apellidos.append("Carratala Sanchis")
altura.append(1.78)
...

nombre.append("Juan")
apellidos.append("Garcia Martinez")
edad.append(49)
altura.append(1.80)
...
```

**004- nueva clase.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
```

### Ejercicio programación 4/1-Ejercicios/002-estructura y mienbros de una clase variabilidade

**000-itroducion.md**

```markdown
```

**001-creo dos alumnos.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    
alumno1 = Alumno()
alumno2 = Alumno()

print(alumno1)
print(alumno2)
```

**002-propiedades.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    
alumno1 = Alumno()
alumno2 = Alumno()

alumno1.nombre = "Heverton"
alumno2.nombre = "Lucas"

alumno1.ruedas = 4
```

**003-recupero propiedades.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    
alumno1 = Alumno()
alumno2 = Alumno()

alumno1.nombre = "Heverton"
alumno2.nombre = "Lucas"

print(alumno1.nombre)
print(alumno2.nombre)
```

### Ejercicio programación 4/1-Ejercicios/003-creacion de propriedades

**000-introducion.md**

```markdown
```

**001-Alumno completo.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
    self.aula_asignada = ""
    self.ordenador_asignado = ""
    
class Aula(): 
	def __init__(self):
    self.piso = ""
    self.numero = ""
    
class Ordenador():
	def __init__(self):
    self.codigo = ""
```

### Ejercicio programación 4/1-Ejercicios/004-creacion de metodos

**000-introducion.md**

```markdown
```

**001-clase base.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
  
```

**002-dime tu nombre.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
  def dimeNombre(self):
    print(self.nombre + " "+self.apellidos)
  def ponNombre(self,nuevonombre,nuevosapellidos):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos

# Esto es un paquete de datos
alumno1 = Alumno()
alumno1.nombre = "Heverton"
alumno1.apellidos = "Ferreira Maciel"
alumno1.dimeNombre()

# Y esto es otro paquete de datos
alumno2 = Alumno()
alumno2.nombre = "Adam"
alumno2.apellidos = "Founounou"
alumno2.dimeNombre()
```

**003-ahora con perros.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
  def dimeNombre(self):
    print(self.nombre + " "+self.apellidos)
  def ponNombre(self,nuevonombre,nuevosapellidos):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    
class Perro():
  def __init__(self):
    self.nombre = ""
  def dimeNombre(self):
    print(self.nombre)

# Esto es un paquete de datos
alumno1 = Alumno()
alumno1.nombre = "Heverton"
alumno1.apellidos = "Ferreira Maciel"
alumno1.dimeNombre()

# Y esto es otro paquete de datos
alumno2 = Alumno()
alumno2.nombre = "Adam"
alumno2.apellidos = "Founounou"
alumno2.dimeNombre()
print("El alumno 2 es de tipo:")
print(alumno2)

# Y ahora creo un perro
perro1 = Perro()
perro1.nombre = "Toby"
perro1.dimeNombre()
print("Toby es un:")
print(perro1)





```

**004-propiedades surrealistas.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
    self.ruedas = 0
  def dimeNombre(self):
    print(self.nombre + " "+self.apellidos)
  def ponNombre(self,nuevonombre,nuevosapellidos):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos
    
class Perro():
  def __init__(self):
    self.nombre = ""
  def dimeNombre(self):
    print(self.nombre)

# Esto es un paquete de datos
alumno1 = Alumno()
alumno1.nombre = "Heverton"
alumno1.apellidos = "Ferreira Maciel"
alumno1.dimeNombre()

# Y esto es otro paquete de datos
alumno2 = Alumno()
alumno2.nombre = "Adam"
alumno2.apellidos = "Founounou"
alumno2.dimeNombre()
print("El alumno 2 es de tipo:")
print(alumno2)

# Y ahora creo un perro
perro1 = Perro()
perro1.nombre = "Toby"
perro1.dimeNombre()
print("Toby es un:")
print(perro1)


```

**005-ejemplo coche.py**

```python
class Coche():
  def __init__(self):
    self.color = ""
    self.caballos = ""
    self.puertas = ""
  def arrancar(self):
    print("estoy arrancando")
  def frenar(self):
    print("estoy frenando")
```

### Ejercicio programación 4/1-Ejercicios/005-Creación de constructores

**000-introducion.md**

```markdown
```

**001-clase alumno.py**

```python
class Alumno():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.fecha_de_nacimiento = ""
    self.correo = ""
    self.telefono = ""
  def dimeNombre(self):
    print(self.nombre + " "+self.apellidos)
  def ponNombre(self,nuevonombre,nuevosapellidos):
    self.nombre = nuevonombre
    self.apellidos = nuevosapellidos

# Esto es un paquete de datos
alumno1 = Alumno()
alumno1.nombre = "Heverton"
alumno1.apellidos = "Ferreira Maciel"
alumno1.dimeNombre()
```

**002-Persona.py**

```python
class Persona():
  def __init__(self,nombre,apellidos):
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = 0
    
persona1 = Persona("Heverton","Ferreira Maciel")
```

### Ejercicio programación 4/1-Ejercicios/006-utitizacion de clases y objetos

**000-introducion.md**

```markdown
```

**001-Clase paciente.py**

```python
class Paciente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""
    

```

**002-lista de pacientes.py**

```python
class Paciente():
  def __init__(self):
    self.nombre = ""
    self.apellidos = ""
    self.email = ""

lista_de_clientes = []

```

**003-un buen constructor.py**

```python
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

lista_de_clientes = []

```

**004-añadimos un paciente.py**

```python
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

lista_de_pacientes = []
lista_de_pacientes.append(Paciente("maria","jose","mairia@jose.com"))
lista_de_pacientes.append(Paciente("marta","lima","marta@lima.com"))
```

**005-mantener pacientes.py**

```python
# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")

# Defino lo que es un paciente
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
# Creo una lista vacía de pacientes
lista_de_pacientes = []


```

**006-while true.py**

```python
# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")

# Defino lo que es un paciente
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
# Creo una lista vacía de pacientes
lista_de_pacientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un paciente")
  print("2.-Listar los pacientes")
  opcion = input("Indica tu opción: ")
  
```

**007-estructura de seleccion.py**

```python
# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")

# Defino lo que es un paciente
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
# Creo una lista vacía de pacientes
lista_de_pacientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un paciente")
  print("2.-Listar los pacientes")
  opcion = input("Indica tu opción: ")
  if opcion == "1":
    print("Ahora vemos como insertamos un paciente")
  elif opcion == "2":
    print("Ahora listamos los pacientes")
    
    
    
```

**008-datos del paciente.py**

```python
# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")

# Defino lo que es un paciente
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
# Creo una lista vacía de pacientes
lista_de_pacientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un paciente")
  print("2.-Listar los pacientes")
  opcion = input("Indica tu opción: ")
  if opcion == "1":
    print("Ahora vemos como insertamos un paciente")
    # Le pido al usuario los datos del paciente
    nombre = input("Introduce el nombre del paciente: ")
    apellidos = input("Introduce los apellidos del paciente: ")
    email = input("Introduce el email del paciente: ")
    # Añado el paciente a la lista
    lista_de_pacientes.append(Paciente(nombre,apellidos,email))
  elif opcion == "2":
    print("Ahora listamos los pacientes")
  else:
    print("opción no reconocida")
    
    
    
```

**009-listado de pacientes.py**

```python
# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")

# Defino lo que es un paciente
class Paciente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    
# Creo una lista vacía de pacientes
lista_de_pacientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un paciente")
  print("2.-Listar los pacientes")
  opcion = input("Indica tu opción: ")
  if opcion == "1":
    print("Ahora vemos como insertamos un paciente")
    # Le pido al usuario los datos del paciente
    nombre = input("Introduce el nombre del paciente: ")
    apellidos = input("Introduce los apellidos del paciente: ")
    email = input("Introduce el email del paciente: ")
    # Añado el paciente a la lista
    lista_de_pacientes.append(Paciente(nombre,apellidos,email))
  elif opcion == "2":
    print("Ahora listamos los pacientes")
    for paciente in lista_de_pacientes:
      print("-"*30)
      print(paciente.nombre)
      print(paciente.apellidos)
      print(paciente.email)
      print("-"*30)
  else:
    print("opción no reconocida")
    
    
    
```

**010-herencia.py**

```python
# Bienvenida
print("Aplicación Hospital v0.1")
print("por Jose Vicente Carratala")


# Defino lo que es una persona
class Persona():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email


# Defino lo que es un paciente
class Paciente(Persona):
    def __init__(self, nombre, apellidos, email):
        super().__init__(nombre, apellidos, email)


# Creo una lista vacía de pacientes
lista_de_pacientes = []


while True:
    print("Escoge una opción:")
    print("1.- Insertar un paciente")
    print("2.- Listar los pacientes")

    opcion = input("Indica tu opción: ")

    if opcion == "1":
        print("Ahora vemos cómo insertamos un paciente")

        # Le pido al usuario los datos del paciente
        nombre = input("Introduce el nombre del paciente: ")
        apellidos = input("Introduce los apellidos del paciente: ")
        email = input("Introduce el email del paciente: ")

        # Creo un paciente
        nuevo_paciente = Paciente(
            nombre,
            apellidos,
            email
        )

        # Añado el paciente a la lista
        lista_de_pacientes.append(nuevo_paciente)

    elif opcion == "2":
        print("Ahora listamos los pacientes")

        for paciente in lista_de_pacientes:
            print("-" * 30)
            print(paciente.nombre)
            print(paciente.apellidos)
            print(paciente.email)
            print("-" * 30)

    else:
        print("Opción no reconocida")
```

### Ejercicio programación 4/1-Ejercicios/007-utilizacion de classes heredadas

**000-uintoducion.md**

```markdown
```

**001-perro.py**

```python
class Perro():
  def __init__(self):
    self.edad = 0
    self.color = ""
    self.nombre = ""
```

**002-ahora un gato.py**

```python
class Perro():
  def __init__(self):
    self.edad = 0
    self.color = ""
    self.nombre = ""
    
class Gato():
  def __init__(self):
    self.edad = 0
    self.color = ""
    self.nombre = ""
    
    class Perro():
  def __init__(self):
    self.edad = 0
    self.color = ""
    self.nombre = ""
  def ladra():
    return "guau"
    
class Gato():
  def __init__(self):
    self.edad = 0
    self.color = ""
    self.nombre = ""
  def maulla():
    return "miau"
```

**003-clase madre.py**

```python
class Animal:
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.nombre = ""


class Perro(Animal):
    def __init__(self):
        super().__init__()

    def ladra(self):
        return "guau"


class Gato(Animal):
    def __init__(self):
        super().__init__()

    def maulla(self):
        return "miau"
```

**004-mamiferos.py**

```python
class Animal:
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.nombre = ""
    def mamar(self):
      return "El animal está mamando"


class Perro(Animal):
    def __init__(self):
        super().__init__()

    def ladra(self):
        return "guau"


class Gato(Animal):
    def __init__(self):
        super().__init__()

    def maulla(self):
        return "miau"
      
micifu = Gato()
print(micifu.mamar())
```

**005-lagarto.py**

```python
class Animal:
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.nombre = ""

    def mamar(self):
        return "El animal está mamando"


class Perro(Animal):
    def __init__(self):
        super().__init__()

    def ladra(self):
        return "guau"


class Gato(Animal):
    def __init__(self):
        super().__init__()

    def maulla(self):
        return "miau"


class Lagarto(Animal):
    def __init__(self):
        super().__init__()


mike = Lagarto()
print(mike.mamar())
```

**006-clase abuela.py**

```python
class Animal:
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.nombre = ""


class Viviparo(Animal):
    def __init__(self):
        super().__init__()

    def mamar(self):
        return "El animal está mamando"


class Oviparo(Animal):
    def __init__(self):
        super().__init__()

    def reptar(self):
        return "Estoy reptando"


class Perro(Viviparo):
    def __init__(self):
        super().__init__()

    def ladra(self):
        return "guau"


class Gato(Viviparo):
    def __init__(self):
        super().__init__()

    def maulla(self):
        return "miau"


class Lagarto(Oviparo):
    def __init__(self):
        super().__init__()


mike = Lagarto()

print(mike.reptar())
```

## Ejercicio programación 4/2-Proyecto

**001-Clases.py**

```python
# Librería de clases de la aplicación de ciclistas


# Defino lo que es una persona
class Persona():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__email = email  # privado: solo se toca con get/set

    # Métodos para leer y cambiar el email privado
    def get_email(self):
        return self.__email

    def set_email(self, email):
        if Persona.validar_email(email):
            self.__email = email
        else:
            print("Email no válido, no se ha cambiado")

    # Método estático: no necesita ningún objeto para funcionar
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Email:", self.__email)


# Defino lo que es un ciclista (hereda de Persona)
class Ciclista(Persona):
    def __init__(self, nombre, apellidos, email, equipo, bicicleta):
        super().__init__(nombre, apellidos, email)
        self.equipo = equipo
        self.bicicleta = bicicleta

    def mostrar(self):
        super().mostrar()
        print("Equipo:", self.equipo)
        print("Bicicleta:", self.bicicleta)
```

**002-Gestión de ciclistas.py**

```python
#GESTIÓN DE CICLISTAS v0.1 By Heverton
# Importo las clases desde mi librería
import importlib
clases = importlib.import_module("001-Clases")
Persona = clases.Persona
Ciclista = clases.Ciclista

# Bienvenida, Gestión de ciclistas (CRUD)
print("Ciclistas v0.1 By Heverton")
print("Gestión de ciclistas")


# Creo una lista vacía de ciclistas
lista_de_ciclistas = []


while True:
    print()
    print("Escoge una opción:")
    print("1.- Insertar un ciclista")
    print("2.- Listar los ciclistas")
    print("3.- Actualizar un ciclista")
    print("4.- Eliminar un ciclista")
    print("5.- Salir")

    opcion = input("Indica tu opción: ")

    # CREATE
    if opcion == "1":
        print("Ahora vemos cómo insertamos un ciclista")

        # Le pido al usuario los datos del ciclista
        nombre = input("Introduce el nombre del ciclista: ")
        apellidos = input("Introduce los apellidos del ciclista: ")
        email = input("Introduce el email del ciclista: ")

        # Uso el método estático para comprobar el email
        while not Persona.validar_email(email):
            email = input("Email no válido, introdúcelo otra vez: ")

        equipo = input("Introduce el equipo del ciclista: ")
        bicicleta = input("Introduce la bicicleta del ciclista: ")

        # Creo un ciclista
        nuevo_ciclista = Ciclista(
            nombre,
            apellidos,
            email,
            equipo,
            bicicleta
        )

        # Añado el ciclista a la lista
        lista_de_ciclistas.append(nuevo_ciclista)
        print("Ciclista añadido correctamente")

    # READ
    elif opcion == "2":
        print("Ahora listamos los ciclistas")

        if len(lista_de_ciclistas) == 0:
            print("No hay ciclistas registrados")

        for indice, ciclista in enumerate(lista_de_ciclistas):
            print("-" * 30)
            print("Número:", indice)
            ciclista.mostrar()
            print("-" * 30)

    # UPDATE
    elif opcion == "3":
        print("Ahora actualizamos un ciclista")

        for indice, ciclista in enumerate(lista_de_ciclistas):
            print(indice, "-", ciclista.nombre, ciclista.apellidos)

        numero = int(input("Indica el número del ciclista a actualizar: "))

        if 0 <= numero < len(lista_de_ciclistas):
            ciclista = lista_de_ciclistas[numero]

            # Le pido los nuevos datos
            ciclista.nombre = input("Nuevo nombre: ")
            ciclista.apellidos = input("Nuevos apellidos: ")
            ciclista.set_email(input("Nuevo email: "))
            ciclista.equipo = input("Nuevo equipo: ")
            ciclista.bicicleta = input("Nueva bicicleta: ")

            print("Ciclista actualizado")
        else:
            print("Número de ciclista no válido")

    # DELETE
    elif opcion == "4":
        print("Ahora eliminamos un ciclista")

        for indice, ciclista in enumerate(lista_de_ciclistas):
            print(indice, "-", ciclista.nombre, ciclista.apellidos)

        numero = int(input("Indica el número del ciclista a eliminar: "))

        if 0 <= numero < len(lista_de_ciclistas):
            eliminado = lista_de_ciclistas.pop(numero)
            print("Ciclista", eliminado.nombre, "eliminado correctamente")
        else:
            print("Número de ciclista no válido")

    elif opcion == "5":
        print("Hasta luego")
        break

    else:
        print("Opción no reconocida")
```

**003-Gestión de ciclistas IA.py**

```python
#GESTIÓN DE CICLISTAS v0.2 By Heverton
# Importo las clases desde mi librería
import importlib
clases = importlib.import_module("001-Clases")
Persona = clases.Persona
Ciclista = clases.Ciclista
import os

# Activo los colores en la consola de Windows
os.system("")

# Colores para la consola
AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
CIAN = "\033[96m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


# Funciones para que se vea más bonito
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def titulo(texto):
    print(AZUL + "╔" + "═" * 50 + "╗" + RESET)
    print(AZUL + "║" + RESET + NEGRITA + texto.center(50) + RESET + AZUL + "║" + RESET)
    print(AZUL + "╚" + "═" * 50 + "╝" + RESET)


def exito(texto):
    print(VERDE + "✔ " + texto + RESET)


def error(texto):
    print(ROJO + "✘ " + texto + RESET)


def pausa():
    input(AMARILLO + "\nPulsa Enter para continuar..." + RESET)


def pedir_numero(texto):
    numero = input(texto)
    while not numero.isdigit():
        error("Tienes que escribir un número")
        numero = input(texto)
    return int(numero)


def tabla_ciclistas():
    print(CIAN + f"{'Nº':<4}{'Nombre':<12}{'Apellidos':<15}{'Equipo':<12}{'Bicicleta':<12}" + RESET)
    print("─" * 55)
    for indice, ciclista in enumerate(lista_de_ciclistas):
        print(f"{indice:<4}{ciclista.nombre:<12}{ciclista.apellidos:<15}{ciclista.equipo:<12}{ciclista.bicicleta:<12}")


# Creo una lista vacía de ciclistas
lista_de_ciclistas = []


while True:
    limpiar()
    titulo("🚴 GESTIÓN DE CICLISTAS v0.2 🚴")
    print()
    print(f"  {AMARILLO}1{RESET} ➜ Insertar un ciclista")
    print(f"  {AMARILLO}2{RESET} ➜ Listar los ciclistas")
    print(f"  {AMARILLO}3{RESET} ➜ Actualizar un ciclista")
    print(f"  {AMARILLO}4{RESET} ➜ Eliminar un ciclista")
    print(f"  {AMARILLO}5{RESET} ➜ Salir")
    print()
    print(f"  Ciclistas registrados: {VERDE}{len(lista_de_ciclistas)}{RESET}")
    print()

    opcion = input(NEGRITA + "Indica tu opción: " + RESET)

    # CREATE
    if opcion == "1":
        limpiar()
        titulo("➕ NUEVO CICLISTA")

        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        email = input("Email: ")

        # Uso el método estático para comprobar el email
        while not Persona.validar_email(email):
            error("Email no válido")
            email = input("Email: ")

        equipo = input("Equipo: ")
        bicicleta = input("Bicicleta: ")

        nuevo_ciclista = Ciclista(nombre, apellidos, email, equipo, bicicleta)
        lista_de_ciclistas.append(nuevo_ciclista)

        print()
        exito("Ciclista añadido correctamente")
        pausa()

    # READ
    elif opcion == "2":
        limpiar()
        titulo("📋 LISTA DE CICLISTAS")

        if len(lista_de_ciclistas) == 0:
            error("No hay ciclistas registrados")
        else:
            for indice, ciclista in enumerate(lista_de_ciclistas):
                print(CIAN + f"┌─── Ciclista nº {indice} " + "─" * 30 + RESET)
                ciclista.mostrar()
                print(CIAN + "└" + "─" * 47 + RESET)
        pausa()

    # UPDATE
    elif opcion == "3":
        limpiar()
        titulo("✏️  ACTUALIZAR CICLISTA")

        if len(lista_de_ciclistas) == 0:
            error("No hay ciclistas para actualizar")
        else:
            tabla_ciclistas()
            print()
            numero = pedir_numero("Número del ciclista a actualizar: ")

            if numero < len(lista_de_ciclistas):
                ciclista = lista_de_ciclistas[numero]
                print(AMARILLO + "(Deja vacío para no cambiar)" + RESET)

                # Si el usuario no escribe nada, se queda el dato antiguo
                nombre = input(f"Nombre [{ciclista.nombre}]: ")
                if nombre != "":
                    ciclista.nombre = nombre

                apellidos = input(f"Apellidos [{ciclista.apellidos}]: ")
                if apellidos != "":
                    ciclista.apellidos = apellidos

                email = input(f"Email [{ciclista.get_email()}]: ")
                if email != "":
                    ciclista.set_email(email)

                equipo = input(f"Equipo [{ciclista.equipo}]: ")
                if equipo != "":
                    ciclista.equipo = equipo

                bicicleta = input(f"Bicicleta [{ciclista.bicicleta}]: ")
                if bicicleta != "":
                    ciclista.bicicleta = bicicleta

                print()
                exito("Ciclista actualizado")
            else:
                error("Número de ciclista no válido")
        pausa()

    # DELETE
    elif opcion == "4":
        limpiar()
        titulo("🗑️  ELIMINAR CICLISTA")

        if len(lista_de_ciclistas) == 0:
            error("No hay ciclistas para eliminar")
        else:
            tabla_ciclistas()
            print()
            numero = pedir_numero("Número del ciclista a eliminar: ")

            if numero < len(lista_de_ciclistas):
                ciclista = lista_de_ciclistas[numero]
                confirmar = input(ROJO + f"¿Seguro que quieres eliminar a {ciclista.nombre}? (s/n): " + RESET)

                if confirmar.lower() == "s":
                    lista_de_ciclistas.pop(numero)
                    exito("Ciclista eliminado correctamente")
                else:
                    print("Operación cancelada")
            else:
                error("Número de ciclista no válido")
        pausa()

    elif opcion == "5":
        limpiar()
        titulo("👋 ¡HASTA LUEGO!")
        break

    else:
        error("Opción no reconocida")
        pausa()
```

## Ejercicio programación 4/3-Resultado de aprendizaje

**Resultado de aprendizaje.md**

```markdown
# Preguntas sobre la aplicación de ciclistas

**a) Se ha reconocido la sintaxis, estructura y componentes típicos de una clase.**

Sí. Una clase es como un molde. Se escribe con `class`, y dentro tiene un `__init__` donde se guardan los datos y otras funciones que hacen cosas.

**b) Se han definido clases.**

Sí. He hecho dos: `Persona` y `Ciclista`.

**c) Se han definido propiedades y métodos.**

Sí. Las propiedades son los datos del ciclista: nombre, apellidos, email, equipo y bicicleta. Los métodos son las cosas que sabe hacer, como `mostrar()`, que enseña sus datos por pantalla.

**d) Se han creado constructores.**

Sí. El constructor es el `__init__`, que se ejecuta al crear un ciclista y guarda sus datos.

**e) Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente.**

Sí. Cuando el usuario mete los datos, creo un ciclista nuevo y lo guardo en una lista. Después lo puedo ver, cambiar o borrar.

**f) Se han utilizado mecanismos para controlar la visibilidad de las clases y de sus miembros.**

Sí. El email es privado (`__email`), así que no se puede tocar directamente desde fuera. Para verlo uso `get_email()` y para cambiarlo uso `set_email()`, que antes comprueba que el email esté bien.

**g) Se han definido y utilizado clases heredadas.**

Sí. `Ciclista` hereda de `Persona`, así que coge el nombre, los apellidos y el email sin tener que escribirlos otra vez. Además le añado el equipo y la bicicleta.

**h) Se han creado y utilizado métodos estáticos.**

Sí. `validar_email()` es estático, o sea, se puede usar sin tener un ciclista creado. Lo uso para comprobar que el email tenga `@` y `.`.

**i) Se han creado y utilizado conjuntos y librerías de clases.**

Sí. He puesto las clases en un archivo aparte, `001-Clases.py`, que funciona como mi librería, y en el programa principal la cargo con `importlib.import_module("001-Clases")`. Además guardo todos los ciclistas juntos en una lista.
```

