# Reporte de proyecto

## Información de generación

- **Fecha:** 25/11/2026, 20:20:15
- **Proyecto documentado:** `Ejercicio programación 9`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio programación 9
    ├── 1-Ejercicios
    │   ├── 001-Acceso a bases de datos. Estándares. Características
    │   │   ├── 001-Preparacion.sql
    │   │   ├── 002-trabajo pesado.sql
    │   │   ├── 003-nos aseguramos de que todo esta ok.sql
    │   │   └── 004-crear un usuario.sql
    │   ├── 002-Establecimiento de conexiones
    │   │   ├── 001-primero instalo libreria.md
    │   │   └── 002-codigo de prueba.py
    │   └── 003-Almacenamiento, recuperación, actualización y eliminación de información en bases de datos
    │       ├── 001-recordamos conectar.py
    │       └── 002-recuperamos.py
    ├── 2-Proyecto
    │   ├── 001-Preparacion.sql
    │   ├── 002-trabajo pesado.sql
    │   ├── 003-nos aseguramos de que todo esta ok.sql
    │   ├── 004-crear un usuario.sql
    │   ├── 005-codigo de prueba.py
    │   ├── 006-recordamos conectar.py
    │   ├── 007-recuperamos.py
    │   ├── 008-insertamos.py
    │   ├── 009-modificamos.py
    │   ├── 010-borramos.py
    │   └── 011-gestionamos.py
    ├── 3-Resultado de aprendizaje
    │   └── Resultado de aprendizaje.md
    └── tiendabicicletas.db [SQLite]
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

### Ejercicio programación 9/tiendabicicletas.db

```text
Ejercicio programación 9/tiendabicicletas.db
└── tabla bicicletas
    └── columnas
        ├── id INTEGER PRIMARY KEY
        ├── nombre TEXT
        ├── descripcion TEXT
        └── precio REAL
```

## Código (intercalado)

### Ejercicio programación 9/1-Ejercicios/001-Acceso a bases de datos. Estándares. Características

**001-Preparacion.sql**

```sql
sudo mysql -u root -p

CREATE DATABASE tiendacalzados;

USE tiendacalzados;

CREATE TABLE calzados(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  precio DECIMAL(4,2)
);
```

**002-trabajo pesado.sql**

```sql
INSERT INTO calzados (nombre, descripcion, precio) VALUES
('Urban Step', 'Zapatilla urbana ligera de color negro', 49.95),
('Runner Pro', 'Zapatilla deportiva para running', 69.90),
('Classic Walk', 'Zapato clásico de piel sintética', 59.95),
('Mountain Trek', 'Bota de montaña resistente al agua', 89.90),
('Summer Sand', 'Sandalia ligera para verano', 29.95),
('City Sneaker', 'Zapatilla casual para uso diario', 44.90),
('Elegant Black', 'Zapato elegante negro para vestir', 74.95),
('Sport Flex', 'Zapatilla deportiva flexible', 54.90),
('Trail Master', 'Zapatilla preparada para senderismo', 79.95),
('Beach Walk', 'Chancla cómoda para playa y piscina', 19.90),

('Retro Runner', 'Zapatilla deportiva de estilo retro', 64.95),
('Office Brown', 'Zapato marrón para oficina', 69.95),
('Winter Boot', 'Bota cálida para los meses de invierno', 84.90),
('Canvas Blue', 'Zapatilla de lona azul', 34.95),
('Street White', 'Zapatilla urbana blanca', 49.90),
('Comfort Plus', 'Zapato cómodo para largas caminatas', 59.90),
('Sport Air', 'Zapatilla deportiva con cámara de aire', 79.90),
('Hiking Pro', 'Bota técnica para senderismo', 94.95),
('Casual Grey', 'Zapatilla casual de color gris', 44.95),
('Elegant Brown', 'Zapato elegante marrón', 72.90),

('Running Light', 'Zapatilla ultraligera para correr', 74.95),
('Urban Red', 'Zapatilla urbana de color rojo', 46.90),
('Trekking Green', 'Bota de trekking verde', 86.95),
('Classic Oxford', 'Zapato clásico estilo Oxford', 78.90),
('Summer Beach', 'Sandalia abierta para verano', 27.95),
('Fitness Move', 'Zapatilla para gimnasio y fitness', 57.90),
('Daily Comfort', 'Calzado cómodo para uso diario', 52.95),
('Street High', 'Zapatilla urbana de caña alta', 61.90),
('Trail Rock', 'Calzado resistente para terrenos rocosos', 88.95),
('Soft Moccasin', 'Mocasín ligero y flexible', 64.90),

('Urban Canvas', 'Zapatilla urbana fabricada en lona', 39.95),
('Running Speed', 'Zapatilla diseñada para entrenamientos rápidos', 82.90),
('Business Black', 'Zapato negro para traje y oficina', 76.95),
('Mountain Peak', 'Bota de montaña con suela reforzada', 92.90),
('Casual Navy', 'Zapatilla casual azul marino', 47.95),
('Sport Energy', 'Zapatilla deportiva para entrenamiento', 67.90),
('Summer Comfort', 'Sandalia acolchada para verano', 32.95),
('Winter Trek', 'Bota de invierno para exteriores', 89.95),
('Street Classic', 'Zapatilla urbana de diseño clásico', 51.90),
('Running Cloud', 'Zapatilla de running con alta amortiguación', 84.95),

('Urban Night', 'Zapatilla negra de estilo moderno', 55.90),
('Hiking Adventure', 'Bota para rutas y excursiones', 91.95),
('Casual Beige', 'Zapatilla casual de color beige', 45.90),
('Sport Dynamic', 'Zapatilla deportiva dinámica y ligera', 62.95),
('Classic Derby', 'Zapato clásico estilo Derby', 73.90),
('Beach Flip', 'Chancla ligera y resistente al agua', 17.95),
('Fitness Power', 'Zapatilla para entrenamiento intensivo', 71.90),
('Urban Minimal', 'Zapatilla urbana de diseño minimalista', 53.95),
('Trail Explorer', 'Zapatilla todoterreno para rutas', 87.90),
('Premium Walk', 'Zapato cómodo con acabado premium', 81.95);
```

**003-nos aseguramos de que todo esta ok.sql**

```sql
SELECT * FROM calzados;
```

**004-crear un usuario.sql**

```sql
CREATE USER 'tiendacalzado'@'localhost' IDENTIFIED BY 'TiendaCalzado123$';

GRANT USAGE ON *.* TO 'tiendacalzado'@'localhost';

ALTER USER 'tiendacalzado'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendacalzados.* 
TO 'tiendacalzado'@'localhost';

FLUSH PRIVILEGES;
```

### Ejercicio programación 9/1-Ejercicios/002-Establecimiento de conexiones

**001-primero instalo libreria.md**

```markdown
En el caso de que la librería no esté instalada:

import mysql.connector

Si estáis en Linux:
pip3 install mysql-connector-python --break-system-packages

Si estáis en Windows
pip install mysql-connector-python

Esto debe hacerse desde fuera de MySQL
Si estáis todavía dentro de MySQL:
EXIT;
```

**002-codigo de prueba.py**

```python
# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='tiendacalzado',
  password='TiendaCalzado123$',
  database='tiendacalzados'
)
# Compruebo si la conexión es correcta
if connection.is_connected():
  print("Todo ha ido bien")
else:
  print("Ha habido un error")
  
connection.close()
```

### Ejercicio programación 9/1-Ejercicios/003-Almacenamiento, recuperación, actualización y eliminación de información en bases de datos

**001-recordamos conectar.py**

```python
# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='tiendacalzado',
  password='TiendaCalzado123$',
  database='tiendacalzados'
)
# Compruebo si la conexión es correcta
if connection.is_connected():
  print("Todo ha ido bien")
else:
  print("Ha habido un error")
  
connection.close()
```

**002-recuperamos.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendacalzado',
  password='TiendaCalzado123$',
  database='tiendacalzados'
)

# Creo un cursor
cursor = connection.cursor()

# Ejecuto una petición a la base de datos
cursor.execute("SELECT * FROM calzados")	

# Recupero el resultado de la petición
filas = cursor.fetchall()	

# Recorro el resultado y lo pinto en pantalla
for fila in filas:
  print(fila)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

## Ejercicio programación 9/2-Proyecto

**001-Preparacion.sql**

```sql
sudo mysql -u root -p

CREATE DATABASE tiendabicicletas;

USE tiendabicicletas;

CREATE TABLE bicicletas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  precio DECIMAL(7,2)
);
```

**002-trabajo pesado.sql**

```sql
--insert muchas bicicletas 

INSERT INTO bicicletas (nombre, descripcion, precio) VALUES
('Urban Ride', 'Bicicleta urbana ligera de color negro', 349.95),
('Mountain Pro', 'Bicicleta de montaña con doble suspensión', 1299.90),
('Road Speed', 'Bicicleta de carretera con cuadro de aluminio', 899.95),
('City Classic', 'Bicicleta de paseo con cesta delantera', 299.90),
('Kids Fun', 'Bicicleta infantil con ruedines', 129.95),
('E-Bike Comfort', 'Bicicleta eléctrica para ciudad', 1499.00),
('Gravel Explorer', 'Bicicleta gravel para caminos de tierra', 1099.95),
('BMX Street', 'BMX para trucos en skatepark', 279.90),
('Folding Go', 'Bicicleta plegable para llevar en el tren', 449.95),
('Trekking Tour', 'Bicicleta de trekking con portabultos', 699.90),

('Retro Vintage', 'Bicicleta de estilo retro con sillín de piel', 399.95),
('Carbon Race', 'Bicicleta de carretera con cuadro de carbono', 2499.00),
('Fat Snow', 'Bicicleta fat bike para nieve y arena', 899.90),
('Beach Cruiser', 'Bicicleta cruiser para paseos por la playa', 329.95),
('Fixie White', 'Bicicleta de piñón fijo blanca', 279.95),
('Comfort Plus', 'Bicicleta cómoda con manillar alto', 379.90),
('Enduro Max', 'Bicicleta de enduro para bajadas técnicas', 2899.95),
('Hybrid Daily', 'Bicicleta híbrida para uso diario', 499.95),
('Junior Mountain', 'Bicicleta de montaña para niños de 8 a 12 años', 249.90),
('Cargo Family', 'Bicicleta de carga para llevar niños o compras', 1899.00),

('Tandem Duo', 'Bicicleta tándem para dos personas', 799.95),
('Urban Red', 'Bicicleta urbana de color rojo', 359.90),
('Trail Green', 'Bicicleta de trail verde con frenos de disco', 1199.95),
('Classic Dutch', 'Bicicleta holandesa clásica', 549.90),
('Summer Ride', 'Bicicleta ligera para paseos de verano', 289.95),
('Fitness Bike', 'Bicicleta de fitness con manillar plano', 649.90),
('Daily Commuter', 'Bicicleta para ir al trabajo cada día', 529.95),
('Downhill Pro', 'Bicicleta de descenso con suspensión larga', 3299.90),
('Cross Country', 'Bicicleta XC rígida y ligera', 999.95),
('Electric Mountain', 'Bicicleta eléctrica de montaña', 2799.00),

('Urban Steel', 'Bicicleta urbana con cuadro de acero', 419.95),
('Aero Speed', 'Bicicleta aerodinámica para triatlón', 3499.90),
('Touring Long', 'Bicicleta para viajes largos con alforjas', 1299.95),
('Mountain Peak', 'Bicicleta de montaña con 24 velocidades', 599.90),
('Casual Navy', 'Bicicleta de paseo azul marino', 339.95),
('Sport Energy', 'Bicicleta deportiva para entrenamiento', 759.90),
('Balance Kids', 'Bicicleta sin pedales para aprender', 79.95),
('Winter Trek', 'Bicicleta con ruedas anchas para invierno', 899.95),
('Street Classic', 'Bicicleta urbana de diseño clásico', 389.90),
('E-Folding', 'Bicicleta eléctrica plegable', 1199.95),

('Urban Night', 'Bicicleta negra con luces integradas', 459.90),
('Hiking Adventure', 'Bicicleta para rutas y excursiones', 849.95),
('Casual Beige', 'Bicicleta de paseo de color beige', 349.90),
('Sport Dynamic', 'Bicicleta deportiva dinámica y ligera', 899.95),
('Track Racer', 'Bicicleta de pista para velódromo', 1599.90),
('Dirt Jump', 'Bicicleta para saltos de tierra', 699.95),
('Ladies Comfort', 'Bicicleta de cuadro bajo fácil de montar', 399.90),
('Urban Minimal', 'Bicicleta urbana de diseño minimalista', 479.95),
('Trail Explorer', 'Bicicleta todoterreno para rutas', 1099.90),
('Premium Road', 'Bicicleta de carretera de gama alta', 4999.95);

```

**003-nos aseguramos de que todo esta ok.sql**

```sql
SELECT * FROM bicicletas;
```

**004-crear un usuario.sql**

```sql
CREATE USER 'tiendabicicleta'@'localhost' IDENTIFIED BY 'TiendaBicicleta123$';

GRANT USAGE ON *.* TO 'tiendabicicleta'@'localhost';

ALTER USER 'tiendabicicleta'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendabicicletas.* 
TO 'tiendabicicleta'@'localhost';

FLUSH PRIVILEGES;
```

**005-codigo de prueba.py**

```python
# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)
# Compruebo si la conexión es correcta
if connection.is_connected():
  print("Todo ha ido bien")
else:
  print("Ha habido un error")
  
connection.close()
```

**006-recordamos conectar.py**

```python
# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)
# Compruebo si la conexión es correcta
if connection.is_connected():
  print("Todo ha ido bien")
else:
  print("Ha habido un error")
  
connection.close()
```

**007-recuperamos.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)

# Creo un cursor
cursor = connection.cursor()

# Ejecuto una petición a la base de datos
cursor.execute("SELECT * FROM bicicletas")	

# Recupero el resultado de la petición
filas = cursor.fetchall()	

# Recorro el resultado y lo pinto en pantalla
for fila in filas:
  print(fila)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

**008-insertamos.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)

# Creo un cursor
cursor = connection.cursor()

# Pido los datos al usuario
nombre = input("Nombre de la bicicleta: ")
descripcion = input("Descripción: ")
precio = input("Precio: ")

# Inserto la bicicleta (los %s se rellenan con los datos)
cursor.execute(
  "INSERT INTO bicicletas (nombre, descripcion, precio) VALUES (%s, %s, %s)",
  (nombre, descripcion, precio)
)

# Sin commit no se guarda
connection.commit()
print("Bicicleta guardada con el id", cursor.lastrowid)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

**009-modificamos.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)

# Creo un cursor
cursor = connection.cursor()

# Pido qué bicicleta quiero cambiar y el precio nuevo
id = input("Id de la bicicleta: ")
precio = input("Nuevo precio: ")

# Cambio el precio
cursor.execute("UPDATE bicicletas SET precio = %s WHERE id = %s", (precio, id))

# Sin commit no se guarda
connection.commit()
print("Filas modificadas:", cursor.rowcount)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

**010-borramos.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)

# Creo un cursor
cursor = connection.cursor()

# Pido qué bicicleta quiero borrar
id = input("Id de la bicicleta a borrar: ")

# La borro
cursor.execute("DELETE FROM bicicletas WHERE id = %s", (id,))

# Sin commit no se borra
connection.commit()
print("Filas borradas:", cursor.rowcount)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

**011-gestionamos.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendabicicleta',
  password='TiendaBicicleta123$',
  database='tiendabicicletas'
)

# Creo un cursor
cursor = connection.cursor()

# Bucle infinito con el menú
while True:
  print("")
  print("===== TIENDA DE BICICLETAS =====")
  print("1. Ver todas las bicicletas")
  print("2. Añadir una bicicleta")
  print("3. Cambiar el precio de una bicicleta")
  print("4. Borrar una bicicleta")
  print("5. Salir")
  opcion = input("Elige una opción: ")

    # 1. Leer (SELECT)
  if opcion == "1":
    cursor.execute("SELECT * FROM bicicletas")
    filas = cursor.fetchall()
    for fila in filas:
      print(fila[0], "-", fila[1], "-", fila[2], "-", fila[3], "€")
    input("Pulsa Enter para volver al menú...")   # Espera antes de volver al menú

  # 2. Guardar (INSERT)
  elif opcion == "2":
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = input("Precio: ")
    cursor.execute(
      "INSERT INTO bicicletas (nombre, descripcion, precio) VALUES (%s, %s, %s)",
      (nombre, descripcion, precio)
    )
    connection.commit()      # Sin commit no se guarda
    print("Bicicleta añadida")

  # 3. Modificar (UPDATE)
  elif opcion == "3":
    id = input("Id de la bicicleta: ")
    precio = input("Nuevo precio: ")
    cursor.execute("UPDATE bicicletas SET precio = %s WHERE id = %s", (precio, id))
    connection.commit()
    print("Filas modificadas:", cursor.rowcount)

  # 4. Borrar (DELETE)
  elif opcion == "4":
    id = input("Id de la bicicleta a borrar: ")
    cursor.execute("DELETE FROM bicicletas WHERE id = %s", (id,))
    connection.commit()
    print("Filas borradas:", cursor.rowcount)

  # 5. Salir del bucle
  elif opcion == "5":
    print("Adiós")
    break

  else:
    print("Opción no válida")

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

## Ejercicio programación 9/3-Resultado de aprendizaje

**Resultado de aprendizaje.md**

```markdown
*Resultado de aprendizaje*

**a) ¿Se han identificado las características y métodos de acceso a sistemas gestores de bases de datos?**
Sí. Creé la base de datos, la tabla y un usuario en MySQL.

**b) ¿Se han programado conexiones con bases de datos?**
Sí. Me conecto desde Python con el usuario y la contraseña.

**c) ¿Se ha escrito un código para almacenar información en bases de datos?**
Sí. Guardo bicicletas nuevas con INSERT.

**d) ¿Se han creado programas para recuperar y mostrar información almacenada en bases de datos?**
Sí. Saco las bicicletas con SELECT y las enseño en pantalla.

**e) ¿Se han efectuado borrados y modificaciones sobre la información almacenada?**
Sí. Cambio el precio con UPDATE y borro con DELETE.

**f) ¿Se han creado aplicaciones que muestren la información almacenada en bases de datos?**
Sí. El menú tiene una opción para ver todas las bicicletas.

**g) ¿Se han creado aplicaciones para gestionar la información presente en bases de datos?**
Sí. Hice un menú para ver, añadir, cambiar y borrar bicicletas.
```

