# Reporte de proyecto

## Información de generación

- **Fecha:** 24/11/2026, 22:45:34
- **Proyecto documentado:** `Ejercicio programación 7`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio programación 7
    ├── 1-Ejercicios
    │   ├── 001-Composición de clases
    │   │   ├── 001-repaso de clases.py
    │   │   ├── 002-clase rueda.py
    │   │   ├── 003-compongo.py
    │   │   └── 004-composicion multiple.py
    │   ├── 002-Herencia y polimorfismo
    │   │   ├── 001-nuestros amigos los gatos.py
    │   │   ├── 002-ahora los perros.py
    │   │   ├── 003-mismos metodos.py
    │   │   ├── 004-metodos diferentes.py
    │   │   └── 005-herencia.py
    │   ├── 003-Jerarquía de clases Superclases y subclases
    │   │   ├── 001-repasamos perros y gatos.py
    │   │   └── 002-supersuperclase.py
    │   ├── 004-Clases y métodos abstractos y finales
    │   │   └── 001-repasamos.py
    │   ├── 005-Interfaces
    │   │   ├── 001-clase pedido.py
    │   │   ├── 002-ahora le pongo cliente.py
    │   │   ├── 003-convierto al cliente en una clase.py
    │   │   ├── 004-uso la subclase.py
    │   │   ├── 005-clase con lista.py
    │   │   └── 006-subclase producto.py
    │   ├── 006-Sobreescritura de métodos
    │   │   ├── 001-lo lanzo como json.py
    │   │   └── 002-convierto a json.py
    │   └── 007-Constructores y herencia
    │       ├── 001-me guardo el json.py
    │       └── mipedido.json
    ├── 2-Proyecto
    │   ├── 001-clase pedido.py
    │   ├── 002-ahora le pongo cliente.py
    │   ├── 003-convierto al cliente en una clase.py
    │   ├── 004-uso la subclase.py
    │   ├── 005-clase con lista.py
    │   ├── 006-subclase producto.py
    │   ├── 007-Convierto a json.py
    │   ├── 008-lo lanzo como json.py
    │   ├── 009-me guardo el json.py
    │   ├── 010-Cargo Json.py
    │   ├── 011-herencia con json.py
    │   └── pedidos.json
    └── 3-Resultado de aprendizaje
        └── Resultado de aprendizaje.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite.

## Código (intercalado)

### Ejercicio programación 7/1-Ejercicios/001-Composición de clases

**001-repaso de clases.py**

```python
class Coche:
  def __init__(self,combustible,ada,cv,micolor):
    tipocombustible = combustible
    sistema_ada = ada
    potencia = cv
    color = micolor
  def arrancar(self):
    return "El coche ha arrancado"
  def acelerar(self):
    return "El coche ha acelerado"
```

**002-clase rueda.py**

```python
class Rueda():
  def __init__(self,mi_radio):
    radio = mi_radio
    
class Motor():
  def __init__(self,micilindrada,caballos):
    cilindrada = micilindrada
    potencia = caballos

class Coche():
  def __init__(self,combustible,ada,cv,micolor):
    tipocombustible = combustible
    sistema_ada = ada
    potencia = cv
    color = micolor
  def arrancar(self):
    return "El coche ha arrancado"
  def acelerar(self):
    return "El coche ha acelerado"
```

**003-compongo.py**

```python
class Rueda():
  def __init__(self,mi_radio):
    radio = mi_radio
    
class Motor():
  def __init__(self,micilindrada,caballos):
    cilindrada = micilindrada
    potencia = caballos

class Coche():
  def __init__(self,combustible,ada,micolor):
    tipocombustible = combustible
    sistema_ada = ada
    motor = Motor(45,100)
    rueda1 = Rueda(21)
    color = micolor
  def arrancar(self):
    return "El coche ha arrancado"
  def acelerar(self):
    return "El coche ha acelerado"
  
micoche = Coche("gasolina",True,"rojo")

```

**004-composicion multiple.py**

```python
class Tornillo():
  def __init__(self,mi_radio):
    radio = mi_radio

class Rueda():
  def __init__(self,mi_radio):
    radio = mi_radio
    tornillo1 = Tornillo(5)
    
class Motor():
  def __init__(self,micilindrada,caballos):
    cilindrada = micilindrada
    potencia = caballos

class Coche():
  def __init__(self,combustible,ada,micolor):
    tipocombustible = combustible
    sistema_ada = ada
    motor = Motor(45,100)
    rueda1 = Rueda(21)
    color = micolor
  def arrancar(self):
    return "El coche ha arrancado"
  def acelerar(self):
    return "El coche ha acelerado"
  
micoche = Coche("gasolina",True,"rojo")

```

### Ejercicio programación 7/1-Ejercicios/002-Herencia y polimorfismo

**001-nuestros amigos los gatos.py**

```python
class Gato():
  def __init__(self,micolor):
    color = micolor
    
```

**002-ahora los perros.py**

```python
class Gato():
  def __init__(self,micolor,miedad):
    color = micolor
    edad = miedad
    
class Perro():
  def __init__(self,micolor,miedad):
    color = micolor
    edad = miedad
```

**003-mismos metodos.py**

```python
class Gato():
  def __init__(self,micolor,miedad):
    color = micolor
    edad = miedad
  def mama()
  	return "Este animal mama cuando es pequeño"
    
class Perro():
  def __init__(self,micolor,miedad):
    color = micolor
    edad = miedad
  def mama()
  	return "Este animal mama cuando es pequeño"
```

**004-metodos diferentes.py**

```python
class Gato():
  def __init__(self,micolor,miedad):
    color = micolor
    edad = miedad
  def mama(self):
  	return "Este animal mama cuando es pequeño"
 	def maulla(self):
    return "miau"
    
class Perro():
  def __init__(self,micolor,miedad):
    color = micolor
    edad = miedad
  def mama(self):
  	return "Este animal mama cuando es pequeño"
 	def ladra(self):
    return "guau"
    
```

**005-herencia.py**

```python

class Mamifero:
    def __init__(self, micolor, miedad):
        self.color = micolor
        self.edad = miedad

    def mama(self):
        return "Estoy mamando"


class Gato(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def maulla(self):
        return "miau"


class Perro(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def ladra(self):
        return "guau"


micifu = Gato("naranja", 0)
firulais = Perro("marrón", 3)

print(micifu.color)
print(micifu.edad)
print(micifu.maulla())
print(micifu.mama())

print(firulais.color)
print(firulais.edad)
print(firulais.ladra())
print(firulais.mama())
```

### Ejercicio programación 7/1-Ejercicios/003-Jerarquía de clases Superclases y subclases

**001-repasamos perros y gatos.py**

```python

class Mamifero:
    def __init__(self, micolor, miedad):
        self.color = micolor
        self.edad = miedad

    def mama(self):
        return "Estoy mamando"


class Gato(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def maulla(self):
        return "miau"


class Perro(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def ladra(self):
        return "guau"


```

**002-supersuperclase.py**

```python
class Animal:
    def __init__(self, micolor, miedad):
        self.color = micolor
        self.edad = miedad


class Mamifero(Animal):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def mama(self):
        return "Estoy mamando"


class Oviparo(Animal):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def mama(self):
        return "Estoy mamando"


class Gato(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def maulla(self):
        return "miau"


class Perro(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def ladra(self):
        return "guau"
```

### Ejercicio programación 7/1-Ejercicios/004-Clases y métodos abstractos y finales

**001-repasamos.py**

```python
class Animal:
    def __init__(self, micolor, miedad):
        self.color = micolor
        self.edad = miedad


class Mamifero(Animal):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def mama(self):
        return "Estoy mamando"


class Oviparo(Animal):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def saleHuevo(self):
        return "Estoy saliendo del huevo"


class Gato(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def maulla(self):
        return "miau"


class Perro(Mamifero):
    def __init__(self, micolor, miedad):
        super().__init__(micolor, miedad)

    def ladra(self):
        return "guau"
```

### Ejercicio programación 7/1-Ejercicios/005-Interfaces

**001-clase pedido.py**

```python
class Pedido():
  def __init__(self,mifecha):
    fecha = mifecha
    
pedido1 = Pedido("2026-11-02")
print(pedido1)
```

**002-ahora le pongo cliente.py**

```python
class Pedido():
  def __init__(self,mifecha,micliente):
    fecha = mifecha
    cliente = micliente
    
pedido1 = Pedido("2026-11-02","Heverton")
print(pedido1)
pedido2 = Pedido("2026-11-03","Juan")
print(pedido2)
```

**003-convierto al cliente en una clase.py**

```python
class Cliente():
  def __init__(self,minombre,misapellidos,miemail,mitelefono):
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():
  def __init__(self,mifecha,micliente):
    self.fecha = mifecha
    self.cliente = Cliente()
    
```

**004-uso la subclase.py**

```python
class Cliente():
  def __init__(self,minombre,misapellidos,miemail,mitelefono):
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():
  def __init__(self,mifecha,minombre,misapellidos,miemail,mitelefono):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos,miemail,mitelefono)
    

pedido1 = Pedido("2026-11-02","Heverton","Marques","hevertonmf@gmail.com","662353018")

print(pedido1)
```

**005-clase con lista.py**

```python
class Persona():
  def __init__(self,minombre):
    self.nombre = minombre
    self.emails = []
    
persona1 = Persona("Heverton")
persona1.emails.append("hevertonmf@gmail.com")
persona1.emails.append("info@heverton.com")

print(persona1)
```

**006-subclase producto.py**

```python
class Cliente():
  def __init__(self,minombre,misapellidos):
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():
  def __init__(self,minombre,miprecio):
    self.nombre = minombre
    self.precio = miprecio
    
class Pedido():
  def __init__(self,mifecha,minombre,misapellidos):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []
    

pedido1 = Pedido("2026-11-02","Heverton","Marques")
pedido1.productos.append(Producto("Producto1",34))
pedido1.productos.append(Producto("Producto2",45))

print(pedido1)
```

### Ejercicio programación 7/1-Ejercicios/006-Sobreescritura de métodos

**001-lo lanzo como json.py**

```python
class Cliente():
  def __init__(self,minombre,misapellidos):
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():
  def __init__(self,minombre,miprecio):
    self.nombre = minombre
    self.precio = miprecio
    
class Pedido():
  def __init__(self,mifecha,minombre,misapellidos):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []
    

pedido1 = Pedido("2026-11-02","Jose Vicente","Carratala")
pedido1.productos.append(Producto("Producto1",34))
pedido1.productos.append(Producto("Producto2",45))

print(pedido1)
```

**002-convierto a json.py**

```python
import json

class Cliente():
  def __init__(self,minombre,misapellidos):
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():
  def __init__(self,minombre,miprecio):
    self.nombre = minombre
    self.precio = miprecio

class Pedido():
  def __init__(self,mifecha,minombre,misapellidos):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []

pedido1 = Pedido("2026-11-02","Heverton","Marques")
pedido1.productos.append(Producto("Producto1",34))
pedido1.productos.append(Producto("Producto2",45))

mijson = json.dumps(pedido1, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)

print(mijson)
```

### Ejercicio programación 7/1-Ejercicios/007-Constructores y herencia

**001-me guardo el json.py**

```python
import json

class Cliente():
  def __init__(self,minombre,misapellidos):
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():
  def __init__(self,minombre,miprecio):
    self.nombre = minombre
    self.precio = miprecio

class Pedido():
  def __init__(self,mifecha,minombre,misapellidos):
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []

pedido1 = Pedido("2026-11-02","Heverton","Marques")
pedido1.productos.append(Producto("Producto1",34))
pedido1.productos.append(Producto("Producto2",45))

mijson = json.dumps(pedido1, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)

print(mijson)
archivo = open("mipedido.json",'w')
archivo.write(mijson)
archivo.close()
```

**mipedido.json**

```json
{
  "fecha": "2026-11-02",
  "cliente": {
    "nombre": "Heverton",
    "apellidos": "Marques"
  },
  "productos": [
    {
      "nombre": "Producto1",
      "precio": 34
    },
    {
      "nombre": "Producto2",
      "precio": 45
    }
  ]
}
```

## Ejercicio programación 7/2-Proyecto

**001-clase pedido.py**

```python
class Pedido():                  # Clase para representar a un pedido

  def __init__(self,mifecha):             # Constructor de la clase Pedido
    fecha = mifecha
    
pedido1 = Pedido("2026-11-02")    # Creación de un objeto de la clase Pedido
#print pedido                 
print(pedido1)
```

**002-ahora le pongo cliente.py**

```python
class Pedido():                                # Clase para representar a un pedido

  def __init__(self,mifecha,micliente):          # Constructor de la clase Pedido
    fecha = mifecha
    cliente = micliente
    
pedido1 = Pedido("2026-11-02","Heverton")   # Creación de un objeto de la clase Pedido
print(pedido1)
pedido2 = Pedido("2026-11-03","Juan")        # Creación de un objeto de la clase Pedido
#print pedido2
print(pedido2)
```

**003-convierto al cliente en una clase.py**

```python
class Cliente():                                               # Clase para representar a un cliente

  def __init__(self,minombre,misapellidos,miemail,mitelefono):         # Constructor de la clase Cliente
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():                                               # Clase para representar a un pedido

  def __init__(self,mifecha,micliente):                       # Constructor de la clase Pedido

    self.fecha = mifecha
    self.cliente = Cliente()
    
```

**004-uso la subclase.py**

```python
class Cliente():                                               # Clase para representar a un cliente

  def __init__(self,minombre,misapellidos,miemail,mitelefono):  # Constructor de la clase Cliente
    self.nombre = minombre
    self.apellidos = misapellidos
    self.email = miemail
    self.telefono = mitelefono

class Pedido():                                                   # Clase para representar a un pedido

  def __init__(self,mifecha,minombre,misapellidos,miemail,mitelefono): #constructor de la clase Pedido
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos,miemail,mitelefono)
    
# Creación de un objeto de la clase Cliente

pedido1 = Pedido("2026-11-02","Heverton","Marques","hevertonmf@gmail.com","662353018")
#print pedido                 

print(pedido1)
```

**005-clase con lista.py**

```python
class Persona():                     # Clase para representar a una persona

  def __init__(self,minombre):                # Constructor de la clase Persona
    self.nombre = minombre
    self.emails = []
    # Agregar un email a la lista de emails de la persona

persona1 = Persona("Heverton")
persona1.emails.append("hevertonmf@gmail.com")
persona1.emails.append("info@heverton.com")
# Convertir el objeto a JSON y mostrarlo en
print(persona1)
```

**006-subclase producto.py**

```python
class Cliente():                             # Clase para representar a un cliente

  def __init__(self,minombre,misapellidos):  # Constructor de la clase Cliente
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():                             #clase para representar a un producto

  def __init__(self,minombre,miprecio):      # Constructor de la clase Producto
    self.nombre = minombre
    self.precio = miprecio
    
class Pedido():                                 # Clase para representar a un pedido

  def __init__(self,mifecha,minombre,misapellidos): # Constructor de la clase Pedido

    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []
    
# Agregar un producto al pedido

pedido1 = Pedido("2026-11-02","Heverton","Marques")
pedido1.productos.append(Producto("Ordenador",34))
pedido1.productos.append(Producto("Teléfono",45))
# Convertir el objeto a JSON y mostrarlo en
print(pedido1)
```

**007-Convierto a json.py**

```python
import json                     # Para trabajar con JSON


class Cliente():                 # Clase para representar a un cliente

  def __init__(self,minombre,misapellidos):  # Constructor de la clase Cliente

    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():                       #clase para representar a un producto

  def __init__(self,minombre,miprecio): # Constructor de la clase Producto
    self.nombre = minombre
    self.precio = miprecio

class Pedido():                         # Clase para representar a un pedido

  def __init__(self,mifecha,minombre,misapellidos): # Constructor de la clase Pedido
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []
## Agregar un producto al pedido

pedido1 = Pedido("2026-11-02","Heverton","Marques")
pedido1.productos.append(Producto("Ordenador",34))
pedido1.productos.append(Producto("Teléfono",45))

mijson = json.dumps(pedido1, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)
# Convertir el objeto a JSON y mostrarlo en
print(mijson)
```

**008-lo lanzo como json.py**

```python
class Cliente():                             #creo una clase cliente

  def __init__(self,minombre,misapellidos):   #creo un constructor 
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():                           #creo una clase producto        

  def __init__(self,minombre,miprecio):     #creo un constructor 
    self.nombre = minombre
    self.precio = miprecio
    
class Pedido():                             #creo una clase pedido 

  def __init__(self,mifecha,minombre,misapellidos): #creo un constructor 
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []
    

pedido1 = Pedido("2026-11-02","Heverton","Marques") #creo un objeto de tipo pedido 

pedido1.productos.append(Producto("Ordenador",34))
pedido1.productos.append(Producto("Teléfono",45))

print(pedido1)    #print pedido1

```

**009-me guardo el json.py**

```python
import json                                  #importo json

class Cliente():                            #creo una clase cliente

  def __init__(self,minombre,misapellidos):  #creo un constructor 
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():                            #creo una clase producto        

  def __init__(self,minombre,miprecio):      #creo un constructor 
    self.nombre = min
    self.nombre = minombre
    self.precio = miprecio

class Pedido():                              #creo una clase pedido        

  def __init__(self,mifecha,minombre,misapellidos): #creo un constructor 
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []


pedido1 = Pedido("2026-11-02","Heverton","Marques")
pedido1.productos.append(Producto("Ordenador",34))
pedido1.productos.append(Producto("Teléfono",45))
print(pedido1)                                     #print pedido1


#archivo = open("mipedido.json",'r')

mijson = json.dumps(pedido1, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)

print(mijson)                                      #print mijson

archivo = open("mipedido.json",'w')
archivo.write(mijson)
archivo.close()
```

**010-Cargo Json.py**

```python
import json                            #cargo json

archivo = open("mipedido.json",'r')    #abro el archivo en modo lectura
datos = json.load(archivo)
archivo.close()
#print datos cliente
print("Fecha:", datos["fecha"])
print("Cliente:", datos["cliente"]["nombre"], datos["cliente"]["apellidos"])
#print Productos 
for producto in datos["productos"]:
  print(producto["nombre"], "-", producto["precio"], "€")
```

**011-herencia con json.py**

```python
import json
from abc import ABC, abstractmethod
from typing import final

# Clase abstracta: no se puede crear, solo heredar de ella
class Documento(ABC):
  @abstractmethod
  def mostrar(self):          # las hijas están obligadas a tener este método
    pass

# Superclase (clase padre)
class Pedido(Documento):
  def __init__(self,mifecha,micliente):
    self.fecha = mifecha
    self.cliente = micliente

  def mostrar(self):
    print("Pedido:", self.fecha, self.cliente)

# Subclase (clase hija) que hereda de Pedido
@final                        # nadie debería heredar de esta clase
class PedidoUrgente(Pedido):
  def __init__(self,mifecha,micliente,mienvio):
    super().__init__(mifecha,micliente)   # uso el constructor del padre
    self.envio = mienvio                  # y añado un dato nuevo

  def mostrar(self):          # sobrescribo el método del padre
    print("Pedido urgente:", self.fecha, self.cliente, self.envio)

# CREATE: creo los pedidos
pedido1 = Pedido("2026-11-02","Heverton")
pedido2 = PedidoUrgente("2026-11-03","Juan","24 horas")

# Los meto en una lista
pedidos = [pedido1, pedido2]

# Convierto la lista a JSON
mijson = json.dumps(pedidos, default=lambda obj: obj.__dict__, indent=2, ensure_ascii=False)

# Guardo el JSON en un archivo
archivo = open("pedidos.json",'w')
archivo.write(mijson)
archivo.close()

# READ: leo el archivo JSON
archivo = open("pedidos.json",'r')
datos = json.load(archivo)
archivo.close()

# Muestro los pedidos leídos
for pedido in datos:
  print(pedido)
```

**pedidos.json**

```json
[
  {
    "fecha": "2026-11-02",
    "cliente": "Heverton"
  },
  {
    "fecha": "2026-11-03",
    "cliente": "Juan",
    "envio": "24 horas"
  }
]
```

## Ejercicio programación 7/3-Resultado de aprendizaje

**Resultado de aprendizaje.md**

```markdown
*Resultado de aprendizaje*

**a) ¿Se han identificado los conceptos de herencia, superclase y subclase?**
Sí. En `011-herencia.py`, `Pedido` es la superclase y `PedidoUrgente` es la subclase que hereda de ella.

**b) ¿Se han utilizado modificadores para bloquear y forzar la herencia de clases y métodos?**
Sí. Con `ABC` y `@abstractmethod` obligo a heredar de `Documento`, y con `@final` bloqueo la clase `PedidoUrgente`.

**c) ¿Se ha reconocido la incidencia de los constructores en la herencia?**
Sí. El constructor es `__init__`. En `PedidoUrgente` uso `super().__init__()` para usar el constructor del padre y luego añado el envío.

**d) ¿Se han creado clases heredadas que sobrescriben la implementación de métodos de la superclase?**
Sí. `PedidoUrgente` cambia el método `mostrar()` de `Pedido`.

**e) ¿Se han diseñado y aplicado jerarquías de clases?**
Sí. Con herencia: `Documento` → `Pedido` → `PedidoUrgente`. Y con composición: un `Pedido` tiene un `Cliente` y varios `Producto`.

**f) ¿Se han probado y depurado las jerarquías de clases?**
Sí. Lo hice paso a paso y fui corrigiendo errores, como cuando me faltaba `self.`.

**g) ¿Se han realizado programas que implementen y utilicen jerarquías de clases?**
Sí. Creo un pedido y lo guardo en JSON (Create), y luego lo leo (Read). También creo pedidos normales y urgentes.

**h) ¿Se ha comentado y documentado el código?**
Sí. Todos los archivos tienen comentarios y nombres claros por pasos.

**i) ¿Se han identificado y evaluado los escenarios de uso de interfaces?**
Sí. `Documento` funciona como una interfaz: obliga a las clases hijas a tener el método `mostrar()`.

**j) ¿Se han identificado y evaluado los escenarios de utilización de la herencia y la composición?**
Sí. Uso herencia cuando algo "es un" tipo de otra cosa (un pedido urgente es un pedido) y composición cuando algo "tiene" otra cosa (un pedido tiene un cliente).
```

