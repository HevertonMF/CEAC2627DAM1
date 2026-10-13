# Reporte de proyecto

## Información de generación

- **Fecha:** 11/10/2026, 18:07:07
- **Proyecto documentado:** `Ejercicio base da dados 4`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio base da dados 4
    ├── 1-Ejercicios
    │   ├── 001-Inserción, borrado y modificación de registros
    │   │   ├── 001-resumen y perspectiva.md
    │   │   ├── 002-nos conectamos a la base de datos.sql
    │   │   ├── 003-insercion buena buena.sql
    │   │   ├── 004-abreviando nombres de columnas.sql
    │   │   ├── 005-cambiar orden de columnas.sql
    │   │   ├── 006-inserto solo unos campos.sql
    │   │   ├── 007-si no le dices la columna da error.sql
    │   │   ├── 008-no puedes meter menos columnas.sql
    │   │   ├── 009-no puedo meter mas columnas.sql
    │   │   ├── 010-aunque las nombres.sql
    │   │   ├── 011-diferecia.sql
    │   │   ├── 012-peligro no ejecuteis.sql
    │   │   ├── 013-delete con condiciones.sql
    │   │   ├── 014-where con booleano.sql
    │   │   ├── 015-truncar te vacia la tabla.sql
    │   │   ├── 016-mucho cuidado con esto.sql
    │   │   ├── 017-Actualizar esto no.sql
    │   │   ├── 018-actualizar solo lo que quieras.sql
    │   │   ├── 019-Mi tabla.sql
    │   │   ├── 020-insert ciudades.sql
    │   │   ├── 021-insert muchas ciudades.sql
    │   │   └── 022-delete una ciudad.sql
    │   ├── 002-Integridad referencial
    │   │   ├── 001-pensar una base de datos.md
    │   │   └── 002- entrar em mysql.md
    │   ├── 003-Subconsultas y composiciones en órdenes de edición
    │   │   ├── 001-subconsultas.sql
    │   │   ├── 002-relleno con datos de muestra.py
    │   │   ├── 003-primero join para ilustrar.sql
    │   │   ├── 004-ampliar dato decimal.sql
    │   │   ├── 004b-hacemos un usuario.sql
    │   │   ├── 005-consulta desde python.py
    │   │   └── 006-nueva consulta.py
    │   └── 004-Transacciones
    │       └── 001-Ejercicio para poner todo en practica.md
    ├── 2-Proyecto
    │   ├── 001-Inserción, borrado y modificación de registros
    │   │   ├── 001-crear base de datos.sql
    │   │   ├── 002-insertar una ciudad.sql
    │   │   ├── 003-insertar muchas ciudades.sql
    │   │   ├── 004-insertar solo unos campos.sql
    │   │   ├── 005-actualizar.sql
    │   │   └── 006-borrar.sql
    │   ├── 002-Integridad referencial
    │   │   └── 001-pensar la base de datos.md
    │   ├── 003-Subconsultas y composiciones en órdenes de edición
    │   │   ├── 001-crear tabla paises.sql
    │   │   ├── 002-relleno con datos.sql
    │   │   ├── 003-primero join.sql
    │   │   ├── 004-subconsulta.sql
    │   │   ├── 005-update con subconsulta.sql
    │   │   ├── 006-delete con subconsulta.sql
    │   │   ├── 007-guardar resultado de consulta en tabla.sql
    │   │   ├── 008-hacemos un usuario.sql
    │   │   └── 009-consulta desde python.py
    │   └── ciudades backup.sql
    ├── 3-Resultado de aprendizaje
    │   └── 001-criterios de evaluacion.md
    └── ciudades.db [SQLite]
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

### Ejercicio base da dados 4/ciudades.db

```text
Ejercicio base da dados 4/ciudades.db
├── tabla ciudades
│   ├── columnas
│   │   ├── id INTEGER PRIMARY KEY
│   │   ├── ciudades TEXT
│   │   ├── país TEXT
│   │   ├── continente TEXT
│   │   └── pais_id INTEGER
│   └── claves foráneas
│       └── pais_id → paises.id (ON UPDATE NO ACTION, ON DELETE CASCADE)
├── tabla ciudades_brasil
│   └── columnas
│       ├── id INTEGER PRIMARY KEY
│       └── ciudades TEXT
└── tabla paises
    └── columnas
        ├── id INTEGER PRIMARY KEY
        └── nombre TEXT
```

## Código (intercalado)

### Ejercicio base da dados 4/1-Ejercicios/001-Inserción, borrado y modificación de registros

**001-resumen y perspectiva.md**

```markdown
La gran mayoría de operaciones con bases de datos son CRUD

CRUD =
Create
Read
Update
Delete

en SQL el CRUD se traduce en:

CRUD =
Create = INSERT
Read = SELECT
Update = UPDATE
Delete = DELETE

En la unidad didáctica 3 hemos hecho SELECT
En la unidad didáctica 4 trabajamos con INSERT, UPDATE, DELETE
```

**002-nos conectamos a la base de datos.sql**

```sql
sudo mysql -u root -p

CREATE DATABASE tratamiento;

USE tratamiento;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);

DESCRIBE clientes;

SELECT * FROM clientes;
```

**003-insercion buena buena.sql**

```sql
INSERT INTO clientes 
(id,nombre,apellidos,email)
VALUES
(NULL,"Heverton Marques","Ferreira Maciel","hevertonmf@gmail.com");
```

**004-abreviando nombres de columnas.sql**

```sql
INSERT INTO clientes 
VALUES
(NULL,"Maria José","Silva Moreira","maria125@gmail.com");

SELECT * FROM clientes;

```

**005-cambiar orden de columnas.sql**

```sql
INSERT INTO clientes 
(email,id,apellidos,nombre)
VALUES
("jorge@lopez.com",NULL,"Lopez","Jorge");

SELECT * FROM clientes;
```

**006-inserto solo unos campos.sql**

```sql
INSERT INTO clientes 
(nombre)
VALUES
("Juan");

SELECT * FROM clientes;
```

**007-si no le dices la columna da error.sql**

```sql
INSERT INTO clientes 
VALUES
("Juan");

SELECT * FROM clientes;
```

**008-no puedes meter menos columnas.sql**

```sql
INSERT INTO clientes 
VALUES
("Juan","Lopez","juan@lopez.com");

SELECT * FROM clientes;
```

**009-no puedo meter mas columnas.sql**

```sql
INSERT INTO clientes 
VALUES
(NULL,"Juan","Lopez","juan@lopez.com","56353");
```

**010-aunque las nombres.sql**

```sql
INSERT INTO clientes 
(id,nombre,apellidos,email,telefono)
VALUES
(NULL,"Juan","Lopez","juan@lopez.com","56353");
```

**011-diferecia.sql**

```sql
INSERT INTO clientes 
(nombre,apellidos)
VALUES
(NULL,"Juan","Lopez","juan@lopez.com"); 

```

**012-peligro no ejecuteis.sql**

```sql
DELETE FROM clientes;

```

**013-delete con condiciones.sql**

```sql
SELECT * FROM clientes;

DELETE FROM clientes
WHERE id = 4;
```

**014-where con booleano.sql**

```sql
SELECT * FROM clientes;

DELETE FROM clientes
WHERE 
apellidos = 'Lopez'
AND
email = 'jorge@lopez.com';

SELECT * FROM clientes;

```

**015-truncar te vacia la tabla.sql**

```sql
TRUNCATE clientes;

-- cuidado porque vacía la tabla
```

**016-mucho cuidado con esto.sql**

```sql
DROP TABLE clientes;
```

**017-Actualizar esto no.sql**

```sql
UPDATE
clientes
SET apellidos = "Garcia";

#No executar, usar o proximo comando 018
```

**018-actualizar solo lo que quieras.sql**

```sql
UPDATE
clientes
SET apellidos = "Garcia"
WHERE id = 2;

SELECT * FROM clientes;
```

**019-Mi tabla.sql**

```sql
CREATE DATABASE ciudades;

USE ciudades;

CREATE TABLE ciudades(
	id INT PRIMARY KEY AUTO_INCREMENT,
	ciudades VARCHAR(100),
  país VARCHAR(100),
  continente VARCHAR(100)
);

DESCRIBE ciudades;

SELECT * FROM ciudades;
```

**020-insert ciudades.sql**

```sql
INSERT INTO ciudades 
(id,nombre,país,continente)
VALUES
(NULL,"Sete lagoas","Brazil","america del sur");
```

**021-insert muchas ciudades.sql**

```sql
INSERT INTO ciudades
(id,ciudades,país,continente)
VALUES
(NULL,"Sete Lagoas","Brasil","América del Sur"),
(NULL,"São Paulo","Brasil","América del Sur"),
(NULL,"Río de Janeiro","Brasil","América del Sur"),
(NULL,"Belo Horizonte","Brasil","América del Sur"),
(NULL,"Buenos Aires","Argentina","América del Sur"),
(NULL,"Córdoba","Argentina","América del Sur"),
(NULL,"Santiago","Chile","América del Sur"),
(NULL,"Lima","Perú","América del Sur"),
(NULL,"Bogotá","Colombia","América del Sur"),
(NULL,"Medellín","Colombia","América del Sur"),
(NULL,"Montevideo","Uruguay","América del Sur"),
(NULL,"Quito","Ecuador","América del Sur"),
(NULL,"Caracas","Venezuela","América del Sur"),
(NULL,"Ciudad de México","México","América del Norte"),
(NULL,"Guadalajara","México","América del Norte"),
(NULL,"Nueva York","Estados Unidos","América del Norte"),
(NULL,"Los Ángeles","Estados Unidos","América del Norte"),
(NULL,"Chicago","Estados Unidos","América del Norte"),
(NULL,"Toronto","Canadá","América del Norte"),
(NULL,"Montreal","Canadá","América del Norte"),
(NULL,"La Habana","Cuba","América Central"),
(NULL,"San José","Costa Rica","América Central"),
(NULL,"Ciudad de Panamá","Panamá","América Central"),
(NULL,"Madrid","España","Europa"),
(NULL,"Barcelona","España","Europa"),
(NULL,"Valencia","España","Europa"),
(NULL,"Sevilla","España","Europa"),
(NULL,"Lisboa","Portugal","Europa"),
(NULL,"Oporto","Portugal","Europa"),
(NULL,"París","Francia","Europa"),
(NULL,"Roma","Italia","Europa"),
(NULL,"Milán","Italia","Europa"),
(NULL,"Berlín","Alemania","Europa"),
(NULL,"Londres","Reino Unido","Europa"),
(NULL,"Ámsterdam","Países Bajos","Europa"),
(NULL,"Atenas","Grecia","Europa"),
(NULL,"Tokio","Japón","Asia"),
(NULL,"Pekín","China","Asia"),
(NULL,"Shanghái","China","Asia"),
(NULL,"Seúl","Corea del Sur","Asia"),
(NULL,"Bombay","India","Asia"),
(NULL,"Bangkok","Tailandia","Asia"),
(NULL,"Estambul","Turquía","Asia"),
(NULL,"El Cairo","Egipto","África"),
(NULL,"Lagos","Nigeria","África"),
(NULL,"Nairobi","Kenia","África"),
(NULL,"Ciudad del Cabo","Sudáfrica","África"),
(NULL,"Casablanca","Marruecos","África"),
(NULL,"Sídney","Australia","Oceanía"),
(NULL,"Auckland","Nueva Zelanda","Oceanía");
```

**022-delete una ciudad.sql**

```sql
SELECT * FROM ciudades;

DELETE FROM ciudades
WHERE id = 1;
```

### Ejercicio base da dados 4/1-Ejercicios/002-Integridad referencial

**001-pensar una base de datos.md**

```markdown
Mediante los productos van pasando los dias y va bajando el precio
por la caducidad de producto. Es una aplicación donde habrá
clientes que comprarán esos productos y harán pedidos

Mediante los productos van pasando los dias y va bajando el precio
por la caducidad de producto. Es una aplicación donde habrá
CLIENTES que comprarán esos PRODUCTOS y harán PEDIDOS

Las entidades de momento son 3:
-Productos
id
caducidad
fecha_de_envase
nombre
precio
vitaminas
proteinas

-Clientes
id
nombre
apellidos
email
direccion

-Pedidos
id
fecha
cantidad
producto_id
cliente_id

CREATE DATABASE vitamins;

USE vitamins;

SHOW TABLES;

CREATE TABLE clientes(...);
CREATE TABLE pedidos(...);
CREATE TABLE productos(...);



Lo mismo pero depende de la oferta y la demanda sube y baja
```

**002- entrar em mysql.md**

```markdown
C:\xampp\mysql\bin\mysql.exe -u root -p
```

### Ejercicio base da dados 4/1-Ejercicios/003-Subconsultas y composiciones en órdenes de edición

**001-subconsultas.sql**

```sql
C:\xampp\mysql\bin\mysql.exe -u root -p

CREATE DATABASE subconsultas;

USE subconsultas;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE,
  cliente_id INT,
  cantidad DECIMAL(4,2)
);
```

**002-relleno con datos de muestra.py**

```python
-- =========================
-- CLIENTES
-- =========================

INSERT INTO clientes (nombre, apellidos) VALUES
('Ana', 'García López'),
('Carlos', 'Martínez Pérez'),
('Laura', 'Sánchez Ruiz'),
('David', 'Fernández Gómez'),
('Marta', 'Navarro Torres'),
('Javier', 'Romero Díaz'),
('Elena', 'Moreno Vidal'),
('Pablo', 'Jiménez Castro'),
('Sara', 'Ortega Molina'),
('Miguel', 'Ruiz Serrano'),
('Lucía', 'Gómez Ferrer'),
('Daniel', 'Torres Ramos'),
('Cristina', 'Vega Pastor'),
('Alejandro', 'Molina Gil'),
('Paula', 'Serrano León');


-- =========================
-- PEDIDOS
-- =========================

INSERT INTO pedidos (fecha, cliente_id, cantidad) VALUES
('2026-01-05', 1, 45.50),
('2026-01-12', 3, 89.90),
('2026-01-18', 2, 25.00),
('2026-01-25', 5, 120.75),

('2026-02-02', 1, 35.20),
('2026-02-08', 4, 67.80),
('2026-02-15', 6, 99.99),
('2026-02-21', 3, 42.50),
('2026-02-27', 8, 150.00),

('2026-03-03', 7, 74.30),
('2026-03-09', 2, 18.95),
('2026-03-14', 5, 210.50),
('2026-03-22', 9, 55.75),
('2026-03-29', 1, 130.00),

('2026-04-04', 10, 29.90),
('2026-04-11', 4, 84.60),
('2026-04-17', 11, 175.25),
('2026-04-23', 6, 62.40),
('2026-04-30', 3, 95.00),

('2026-05-05', 12, 48.50),
('2026-05-10', 8, 220.00),
('2026-05-16', 5, 36.90),
('2026-05-22', 13, 112.75),
('2026-05-28', 1, 59.99),

('2026-06-02', 7, 89.50),
('2026-06-08', 14, 145.00),
('2026-06-13', 2, 73.25),
('2026-06-19', 9, 199.99),
('2026-06-25', 4, 44.80),

('2026-07-01', 15, 32.50),
('2026-07-07', 3, 125.00),
('2026-07-12', 6, 58.75),
('2026-07-18', 10, 245.90),
('2026-07-24', 1, 76.40),

('2026-08-03', 11, 98.20),
('2026-08-09', 5, 134.50),
('2026-08-15', 8, 67.00),
('2026-08-21', 12, 185.75),
('2026-08-28', 2, 41.90),

('2026-09-04', 13, 92.50),
('2026-09-10', 7, 155.00),
('2026-09-16', 4, 38.75),
('2026-09-22', 9, 215.40),
('2026-09-29', 3, 64.30),

('2026-10-02', 1, 105.50),
('2026-10-04', 6, 49.90),
('2026-10-05', 10, 178.25),
('2026-10-06', 14, 87.60),
('2026-10-07', 5, 230.00);
```

**003-primero join para ilustrar.sql**

```sql
SELECT 
pedidos.fecha,
pedidos.cantidad,
clientes.nombre,
clientes.apellidos
FROM pedidos
LEFT JOIN clientes
ON pedidos.cliente_id = clientes.id;
```

**004-ampliar dato decimal.sql**

```sql
ALTER TABLE pedidos
MODIFY cantidad DECIMAL(8,2);

-- ejecutamos esto para ampliar los datos enteros y decimales
```

**004b-hacemos un usuario.sql**

```sql
-- Creo un usuario tiendaestetoscopios
CREATE USER 'subconsultas'@'localhost' IDENTIFIED BY 'Subconsultas123$';

-- A ese usuario le pemito acceder a todo en el servidor
GRANT USAGE ON *.* TO 'subconsultas'@'localhost';

-- A ese usuario le quito limites para que pueda hacer de todo
ALTER USER 'subconsultas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- Garantizo privilegios al usuario en su base de datos
GRANT ALL PRIVILEGES ON subconsultas.* 
TO 'subconsultas'@'localhost';

-- Recargo la tabla de privilegios
FLUSH PRIVILEGES;
```

**005-consulta desde python.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='subconsultas',
  password='Subconsultas123$',
  database='subconsultas'
)

# Creo un cursor
cursor = connection.cursor()
################### PRIMERO PIDO UN CLIENTE ################
cursor.execute("""
	SELECT * FROM clientes
  WHERE nombre = "Laura"
  """)	
filas = cursor.fetchall()	
idcliente = 0
for fila in filas:
  print(fila)
  idcliente = fila[0]
print("el id del cliente es: ",idcliente)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

**006-nueva consulta.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='subconsultas',
  password='Subconsultas123$',
  database='subconsultas'
)

# Creo un cursor
cursor = connection.cursor()
################### PRIMERO PIDO UN CLIENTE ################
cursor.execute("""
	SELECT * FROM clientes
  WHERE nombre = "Laura"
  """)	
filas = cursor.fetchall()	
idcliente = 0
for fila in filas:
  print(fila)
  idcliente = fila[0]
print("el id del cliente es: ",idcliente)

################### AHORA PIDO LOS PEDIDOS ################

cursor.execute("""
	SELECT * FROM pedidos
  WHERE cliente_id = """+str(idcliente)+"""
  """)
filas = cursor.fetchall()	
for fila in filas:
  print(fila)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

### Ejercicio base da dados 4/1-Ejercicios/004-Transacciones

**001-Ejercicio para poner todo en practica.md**

```markdown
1.-Seleccionar
2.-Insertar
3.-Actualizar
4.-Eliminar

Hacer un ejercicio que implemente todas las operaciones

Unidad 3 consultas - Seleccionar
Unidad 4 (actual) tratamiento - insertar, actualizar, eliminar

Lo que tenéis que hacer es:
1.-Crear una base de datos
2.-Usar la base de datos
3.-Crear tablas (hoy con una vale) (si es proyecto intermodular mejor)
4.-Insertar
5.-Leer
6.-Actualizar
7.-Eliminar

Ejemplo psicólogos:
Elegís una entidad (facultativo o clientes)
Creáis una base de datos
Creáis tabla de facultativos
Insertais facultativos de ejemplo
Seleccionais
Eliminais
Actualizáis

Porque luego en la segunda mitad de la mañana
Igual en lenguajes de marcas hago una web
Que nos enseñe los facultativos que están a tu disposición
en esa web




```

### Ejercicio base da dados 4/2-Proyecto/001-Inserción, borrado y modificación de registros

**001-crear base de datos.sql**

```sql
C:\xampp\mysql\bin\mysql.exe -u root -p

-- La base de datos que creé en clase (si ya existe no hace nada)
CREATE DATABASE IF NOT EXISTS ciudades;

USE ciudades;

CREATE TABLE IF NOT EXISTS ciudades(
	id INT PRIMARY KEY AUTO_INCREMENT,
	ciudades VARCHAR(100),
	país VARCHAR(100),
	continente VARCHAR(100)
);

DESCRIBE ciudades;

SELECT * FROM ciudades;
```

**002-insertar una ciudad.sql**

```sql
USE ciudades;

INSERT INTO ciudades
(id,ciudades,país,continente)
VALUES
(NULL,"Salvador","Brasil","América del Sur");

SELECT * FROM ciudades;
```

**003-insertar muchas ciudades.sql**

```sql
USE ciudades;

INSERT INTO ciudades
(ciudades,país,continente)
VALUES
("Brasilia","Brasil","América del Sur"),
("Rosario","Argentina","América del Sur"),
("Valparaíso","Chile","América del Sur"),
("Cusco","Perú","América del Sur"),
("Cali","Colombia","América del Sur"),
("Bilbao","España","Europa"),
("Zaragoza","España","Europa"),
("Málaga","España","Europa"),
("Múnich","Alemania","Europa"),
("Osaka","Japón","Asia");

SELECT * FROM ciudades;
```

**004-insertar solo unos campos.sql**

```sql
USE ciudades;

-- Solo meto la ciudad y el país, el continente se queda en NULL
INSERT INTO ciudades
(ciudades,país)
VALUES
("Granada","España");

SELECT * FROM ciudades;
```

**005-actualizar.sql**

```sql
USE ciudades;

-- Completo el continente que faltaba de Granada
UPDATE ciudades
SET continente = "Europa"
WHERE ciudades = "Granada";

-- Cambio el nombre de Bombay por el actual
UPDATE ciudades
SET ciudades = "Mumbai"
WHERE id = 42;

-- Nunca sin WHERE porque cambia todas las filas

SELECT * FROM ciudades;
```

**006-borrar.sql**

```sql
USE ciudades;

SELECT * FROM ciudades;

-- Borro una ciudad por su nombre
DELETE FROM ciudades
WHERE ciudades = "Granada";

-- Borro con varias condiciones
DELETE FROM ciudades
WHERE país = "España"
AND ciudades = "Málaga";

SELECT * FROM ciudades;
```

### Ejercicio base da dados 4/2-Proyecto/002-Integridad referencial

**001-pensar la base de datos.md**

```markdown
Es una base de datos de CIUDADES del mundo.
Cada ciudad es de un PAÍS y de un continente.

Las entidades de momento son 2:
-Ciudades
id
ciudades
país
continente
pais_id

-Paises
id
nombre

Un país tiene muchas ciudades.
Las uno con pais_id (el id del país en la tabla paises).

CREATE DATABASE ciudades;

USE ciudades;

SHOW TABLES;

CREATE TABLE ciudades(...);
CREATE TABLE paises(...);
```

### Ejercicio base da dados 4/2-Proyecto/003-Subconsultas y composiciones en órdenes de edición

**001-crear tabla paises.sql**

```sql
C:\xampp\mysql\bin\mysql.exe -u root -p

USE ciudades;

CREATE TABLE paises(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100)
);

-- Añado a ciudades una columna con el id del país
ALTER TABLE ciudades
ADD pais_id INT;
```

**002-relleno con datos.sql**

```sql
USE ciudades;

INSERT INTO paises (nombre) VALUES
("Brasil"),
("Argentina"),
("España"),
("Portugal"),
("Japón");

-- Le pongo a cada ciudad el id de su país
UPDATE ciudades SET pais_id = 1 WHERE país = "Brasil";
UPDATE ciudades SET pais_id = 2 WHERE país = "Argentina";
UPDATE ciudades SET pais_id = 3 WHERE país = "España";
UPDATE ciudades SET pais_id = 4 WHERE país = "Portugal";
UPDATE ciudades SET pais_id = 5 WHERE país = "Japón";

SELECT * FROM paises;
SELECT * FROM ciudades;
```

**003-primero join.sql**

```sql
USE ciudades;

SELECT
ciudades.ciudades,
ciudades.continente,
paises.nombre
FROM ciudades
LEFT JOIN paises
ON ciudades.pais_id = paises.id;
```

**004-subconsulta.sql**

```sql
USE ciudades;

-- Primero busco el id de Brasil
SELECT id FROM paises
WHERE nombre = "Brasil";

-- Y lo meto dentro de otra consulta
SELECT * FROM ciudades
WHERE pais_id = (SELECT id FROM paises WHERE nombre = "Brasil");
```

**005-update con subconsulta.sql**

```sql
USE ciudades;

UPDATE ciudades
SET continente = "Sudamérica"
WHERE pais_id = (SELECT id FROM paises WHERE nombre = "Argentina");

SELECT * FROM ciudades;
```

**006-delete con subconsulta.sql**

```sql
USE ciudades;

SELECT * FROM ciudades;

DELETE FROM ciudades
WHERE pais_id = (SELECT id FROM paises WHERE nombre = "Portugal");

SELECT * FROM ciudades;
```

**007-guardar resultado de consulta en tabla.sql**

```sql
USE ciudades;

CREATE TABLE ciudades_brasil(
	id INT PRIMARY KEY AUTO_INCREMENT,
	ciudades VARCHAR(100)
);

-- Meto en la tabla nueva el resultado de un SELECT
INSERT INTO ciudades_brasil
(ciudades)
SELECT ciudades FROM ciudades
WHERE país = "Brasil";

SELECT * FROM ciudades_brasil;
```

**008-hacemos un usuario.sql**

```sql
-- Creo un usuario ciudades
CREATE USER 'ciudades'@'localhost' IDENTIFIED BY 'Ciudades123$';

-- A ese usuario le pemito acceder a todo en el servidor
GRANT USAGE ON *.* TO 'ciudades'@'localhost';

-- A ese usuario le quito limites para que pueda hacer de todo
ALTER USER 'ciudades'@'localhost'
REQUIRE NONE
WITH MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0
MAX_USER_CONNECTIONS 0;

-- Garantizo privilegios al usuario en su base de datos
GRANT ALL PRIVILEGES ON ciudades.*
TO 'ciudades'@'localhost';

-- Recargo la tabla de privilegios
FLUSH PRIVILEGES;
```

**009-consulta desde python.py**

```python
# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='ciudades',
  password='Ciudades123$',
  database='ciudades'
)

# Creo un cursor
cursor = connection.cursor()
################### PRIMERO PIDO UN PAIS ################
cursor.execute("""
	SELECT * FROM paises
  WHERE nombre = "Brasil"
  """)
filas = cursor.fetchall()
idpais = 0
for fila in filas:
  print(fila)
  idpais = fila[0]
print("el id del pais es: ",idpais)

################### AHORA PIDO SUS CIUDADES ################

cursor.execute("""
	SELECT * FROM ciudades
  WHERE pais_id = """+str(idpais)+"""
  """)
filas = cursor.fetchall()
for fila in filas:
  print(fila)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
```

## Ejercicio base da dados 4/2-Proyecto

**ciudades backup.sql**

```sql
-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: ciudades
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `ciudades`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ciudades` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `ciudades`;

--
-- Table structure for table `ciudades`
--

DROP TABLE IF EXISTS `ciudades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ciudades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ciudades` varchar(100) DEFAULT NULL,
  `país` varchar(100) DEFAULT NULL,
  `continente` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudades`
--

LOCK TABLES `ciudades` WRITE;
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` VALUES (2,'Sete Lagoas','Brasil','América del Sur'),(3,'São Paulo','Brasil','América del Sur'),(4,'Río de Janeiro','Brasil','América del Sur'),(5,'Belo Horizonte','Brasil','América del Sur'),(6,'Buenos Aires','Argentina','América del Sur'),(7,'Córdoba','Argentina','América del Sur'),(8,'Santiago','Chile','América del Sur'),(9,'Lima','Perú','América del Sur'),(10,'Bogotá','Colombia','América del Sur'),(11,'Medellín','Colombia','América del Sur'),(12,'Montevideo','Uruguay','América del Sur'),(13,'Quito','Ecuador','América del Sur'),(14,'Caracas','Venezuela','América del Sur'),(15,'Ciudad de México','México','América del Norte'),(16,'Guadalajara','México','América del Norte'),(17,'Nueva York','Estados Unidos','América del Norte'),(18,'Los Ángeles','Estados Unidos','América del Norte'),(19,'Chicago','Estados Unidos','América del Norte'),(20,'Toronto','Canadá','América del Norte'),(21,'Montreal','Canadá','América del Norte'),(22,'La Habana','Cuba','América Central'),(23,'San José','Costa Rica','América Central'),(24,'Ciudad de Panamá','Panamá','América Central'),(25,'Madrid','España','Europa'),(26,'Barcelona','España','Europa'),(27,'Valencia','España','Europa'),(28,'Sevilla','España','Europa'),(29,'Lisboa','Portugal','Europa'),(30,'Oporto','Portugal','Europa'),(31,'París','Francia','Europa'),(32,'Roma','Italia','Europa'),(33,'Milán','Italia','Europa'),(34,'Berlín','Alemania','Europa'),(35,'Londres','Reino Unido','Europa'),(36,'Ámsterdam','Países Bajos','Europa'),(37,'Atenas','Grecia','Europa'),(38,'Tokio','Japón','Asia'),(39,'Pekín','China','Asia'),(40,'Shanghái','China','Asia'),(41,'Seúl','Corea del Sur','Asia'),(42,'Bombay','India','Asia'),(43,'Bangkok','Tailandia','Asia'),(44,'Estambul','Turquía','Asia'),(45,'El Cairo','Egipto','África'),(46,'Lagos','Nigeria','África'),(47,'Nairobi','Kenia','África'),(48,'Ciudad del Cabo','Sudáfrica','África'),(49,'Casablanca','Marruecos','África'),(50,'Sídney','Australia','Oceanía'),(51,'Auckland','Nueva Zelanda','Oceanía');
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-11 14:09:31
```

## Ejercicio base da dados 4/3-Resultado de aprendizaje

**001-criterios de evaluacion.md**

```markdown
# Criterios de evaluación

**a) Se han identificado las herramientas y sentencias para modificar el contenido de la base de datos.**
He usado MySQL en XAMPP con INSERT, UPDATE y DELETE.

**b) Se han insertado, borrado y actualizado datos en las tablas.**
He metido ciudades nuevas, he cambiado algunas y he borrado otras.

**c) Se ha incluido en una tabla la información resultante de la ejecución de una consulta.**
He guardado las ciudades de Brasil en una tabla nueva.

**d) Se han diseñado guiones de sentencias para llevar a cabo tareas complejas.**
He hecho un script para crear la tabla de países y unirla con las ciudades.

**e) Se ha reconocido el funcionamiento de las transacciones.**
No lo he hecho porque todavía no lo hemos visto en clase.

**f) Se han anulado parcial o totalmente los cambios producidos por una transacción.**
No lo he hecho porque todavía no lo hemos visto en clase.

**g) Se han identificado los efectos de las distintas políticas de bloqueo de registros.**
No lo he hecho porque todavía no lo hemos visto en clase.

**h) Se han adoptado medidas para mantener la integridad y consistencia de la información.**
No lo he hecho porque todavía no lo hemos visto en clase.
```

