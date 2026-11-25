# Reporte de proyecto

## Información de generación

- **Fecha:** 6/10/2026, 12:15:02
- **Proyecto documentado:** `Ejercicio base da dados 3`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio base da dados 3
    ├── 1-Ejercicios
    │   ├── 001-Proyección, selección y ordenación de registros
    │   │   ├── 000-introducion.md
    │   │   ├── 001-recordamos como me conecto.md
    │   │   ├── 002-crear tabla.sql
    │   │   ├── 003-datos de ejemplo.sql
    │   │   ├── 004-comprobacion.sql
    │   │   ├── 005-seleccion de columnas.sql
    │   │   ├── 006-proyecciones.sql
    │   │   ├── 007-ahora lo quiero todo de nuevo.sql
    │   │   ├── 008-ordenacion.sql
    │   │   ├── 009-asc por defecto.sql
    │   │   ├── 010-desc.sql
    │   │   └── 011-multiples columnas.sql
    │   ├── 002-Operadores. Operadores de comparación. Operadores lógicos
    │   │   ├── 000-introducion.md
    │   │   ├── 001-lista de productos.sql
    │   │   ├── 002-suma.sql
    │   │   ├── 003-resta.sql
    │   │   ├── 004-multiplicacion.sql
    │   │   ├── 005-division.sql
    │   │   ├── 006-iva por producto.sql
    │   │   ├── 007-producto barato.sql
    │   │   ├── 008-limite.sql
    │   │   └── 009-dos condiciones.sql
    │   ├── 003-Consultas de resumen
    │   │   ├── 000-introducion.md
    │   │   ├── 001-cuenteo.sql
    │   │   ├── 002-sumas.sql
    │   │   ├── 003-maximo.sql
    │   │   ├── 004-minimo.sql
    │   │   └── 005-promedio.sql
    │   ├── 004-Agrupamiento de registros
    │   │   ├── 000-introducion.md
    │   │   ├── 001-agrupamiento.sql
    │   │   ├── 002-rango.sql
    │   │   └── 003-in.sql
    │   ├── 005-Composiciones internas
    │   │   ├── 000-introdución.md
    │   │   ├── 001-kata.md
    │   │   ├── 002-empezamos poco a poco.sql
    │   │   ├── 003-cruzo con producto.sql
    │   │   ├── 004-operadores aritmeticos.sql
    │   │   ├── 005-saco el empleado.sql
    │   │   ├── 006-saco el cliente.sql
    │   │   └── 007-alterar.sql
    │   ├── 007-Subconsultas
    │   │   ├── 000-introdución.md
    │   │   ├── 002-listado de productos.sql
    │   │   └── 003-subconsulta.sql
    │   ├── 008-Combinación de múltiples selecciones
    │   │   ├── 000-introdución.md
    │   │   ├── 001-listar tablas.sql
    │   │   ├── 002-crear personas.sql
    │   │   ├── 003-datos de ejemplo para personas.sql
    │   │   ├── 004-UNION ALL.sql
    │   │   ├── 005-UNION.sql
    │   │   ├── 006-intersect.sql
    │   │   └── 007-EXCEPT.sql
    │   ├── 009-Optimización de consultas
    │   │   ├── 000-introdución.md
    │   │   ├── 001-where.sql
    │   │   ├── 002-similaridad.sql
    │   │   └── 010-productos.sql
    │   └── 010-Ejercicio final de unidad
    │       └── 001-Tarea a realizar.md
    ├── 2-Proyecto
    │   ├── 001-crear base de datos.sql
    │   ├── 002-consultas.sql
    │   └── Backup SQL Mi Biblioteca.sql
    ├── 3-Resultado de aprendizaje
    │   └── Criterios de evaluación.md
    └── biblioteca.db [SQLite]
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

### Ejercicio base da dados 3/biblioteca.db

```text
Ejercicio base da dados 3/biblioteca.db
├── tabla autores
│   └── columnas
│       ├── id_autor INTEGER PRIMARY KEY
│       ├── nombre TEXT NOT NULL
│       └── nacionalidad TEXT
├── tabla categorias
│   ├── columnas
│   │   ├── id_categoria INTEGER PRIMARY KEY
│   │   └── nombre TEXT NOT NULL
│   └── índices
│       └── sqlite_autoindex_categorias_1 (UNIQUE): nombre
└── tabla libros
    ├── columnas
    │   ├── id_libro INTEGER PRIMARY KEY
    │   ├── titulo TEXT NOT NULL
    │   ├── id_autor INTEGER NOT NULL
    │   ├── id_categoria INTEGER NOT NULL
    │   ├── paginas INTEGER
    │   ├── precio REAL
    │   ├── fecha_compra TEXT NOT NULL
    │   ├── fecha_fin_lectura TEXT
    │   └── valoracion INTEGER
    └── claves foráneas
        ├── id_categoria → categorias.id_categoria (ON UPDATE NO ACTION, ON DELETE NO ACTION)
        └── id_autor → autores.id_autor (ON UPDATE NO ACTION, ON DELETE NO ACTION)
```

## Código (intercalado)

### Ejercicio base da dados 3/1-Ejercicios/001-Proyección, selección y ordenación de registros

**000-introducion.md**

```markdown
```

**001-recordamos como me conecto.md**

```markdown
sudo mysql -u root -p

SHOW DATABASES;

CREATE DATABASE seleccion;

USE seleccion;

```

**002-crear tabla.sql**

```sql
CREATE TABLE departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL
);

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    email VARCHAR(150),
    salario DECIMAL(10,2),
    fecha_contratacion DATE,
    departamento_id INT,
    jefe_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id),
    FOREIGN KEY (jefe_id) REFERENCES empleados(id)
);

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    ciudad VARCHAR(100),
    pais VARCHAR(100) DEFAULT 'España',
    email VARCHAR(150),
    fecha_alta DATE
);

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    categoria VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    empleado_id INT,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);
```

**003-datos de ejemplo.sql**

```sql
INSERT INTO departamentos (nombre, ciudad) VALUES
('Informática', 'Valencia'),
('Ventas', 'Madrid'),
('Administración', 'Valencia'),
('Marketing', 'Barcelona'),
('Recursos Humanos', 'Madrid'),
('Logística', 'Sevilla'),
('Investigación', 'Valencia');

INSERT INTO empleados (nombre, apellidos, email, salario, fecha_contratacion, departamento_id, jefe_id) VALUES
('Ana', 'García López', 'ana@empresa.com', 32000, '2018-03-15', 1, NULL),
('Carlos', 'Martínez Pérez', 'carlos@empresa.com', 28000, '2020-06-01', 1, 1),
('Laura', 'Sánchez Ruiz', 'laura@empresa.com', 29500, '2019-11-20', 1, 1),
('Pedro', 'Gómez Torres', 'pedro@empresa.com', 35000, '2017-01-10', 2, NULL),
('Marta', 'Navarro Gil', 'marta@empresa.com', 24000, '2021-04-12', 2, 4),
('David', 'Romero Díaz', 'david@empresa.com', 26000, '2022-02-15', 2, 4),
('Lucía', 'Ortega Ramos', 'lucia@empresa.com', 23000, '2023-07-01', 2, 4),
('Javier', 'Vidal Serra', 'javier@empresa.com', 31000, '2016-09-01', 3, NULL),
('Elena', 'Molina Costa', 'elena@empresa.com', 22000, '2020-10-10', 3, 8),
('Raúl', 'Ibañez León', NULL, 21500, '2024-01-15', 3, 8),
('Sofía', 'Castro Vega', 'sofia@empresa.com', 38000, '2018-05-21', 4, NULL),
('Diego', 'Herrero Cano', 'diego@empresa.com', 27000, '2021-08-14', 4, 11),
('Paula', 'Soler Mora', 'paula@empresa.com', 26500, '2022-11-03', 4, 11),
('Miguel', 'Fuentes Lara', 'miguel@empresa.com', 33000, '2015-04-17', 5, NULL),
('Sara', 'Reyes Pastor', 'sara@empresa.com', 25000, '2020-12-01', 5, 14),
('Andrés', 'Campos Nieto', 'andres@empresa.com', 30000, '2019-02-10', 6, NULL),
('Cristina', 'Lozano Martí', 'cristina@empresa.com', 23500, '2023-03-05', 6, 16),
('Fernando', 'Blasco Puig', 'fernando@empresa.com', 42000, '2014-06-01', 7, NULL),
('Nuria', 'Marín Esteve', 'nuria@empresa.com', 34000, '2019-09-09', 7, 18),
('Alberto', 'Prieto Sanz', NULL, 29000, '2024-05-20', 7, 18);

INSERT INTO clientes (nombre, ciudad, pais, email, fecha_alta) VALUES
('Tecnologías Levante', 'Valencia', 'España', 'info@teclevante.es', '2019-01-10'),
('Soluciones Madrid', 'Madrid', 'España', 'info@solmadrid.es', '2020-03-15'),
('Informática Norte', 'Bilbao', 'España', 'contacto@infonorte.es', '2018-07-21'),
('Desarrollo Web BCN', 'Barcelona', 'España', 'hola@webbcn.es', '2021-01-14'),
('Servicios Sevilla', 'Sevilla', 'España', 'info@servsevilla.es', '2022-05-18'),
('Software Valencia', 'Valencia', 'España', 'info@softvalencia.es', '2023-02-20'),
('Digital Málaga', 'Málaga', 'España', NULL, '2020-10-10'),
('Tech Lisboa', 'Lisboa', 'Portugal', 'info@techlisboa.pt', '2021-09-01'),
('Paris Informatique', 'París', 'Francia', 'info@parisinfo.fr', '2019-11-11'),
('Roma Digital', 'Roma', 'Italia', 'info@romadigital.it', '2022-04-07'),
('Consultoría Mediterránea', 'Alicante', 'España', NULL, '2024-01-10'),
('Sistemas Castellón', 'Castellón', 'España', 'info@sistemascastellon.es', '2023-08-15');

INSERT INTO productos (nombre, categoria, precio, stock) VALUES
('Portátil Basic', 'Ordenadores', 599.00, 25),
('Portátil Pro', 'Ordenadores', 1199.00, 12),
('Workstation', 'Ordenadores', 1899.00, 5),
('Monitor 24 pulgadas', 'Monitores', 159.00, 40),
('Monitor 27 pulgadas', 'Monitores', 249.00, 20),
('Teclado USB', 'Periféricos', 29.90, 100),
('Ratón USB', 'Periféricos', 19.90, 150),
('Teclado mecánico', 'Periféricos', 89.00, 35),
('SSD 1TB', 'Almacenamiento', 79.00, 60),
('SSD 2TB', 'Almacenamiento', 139.00, 30),
('NAS 4TB', 'Almacenamiento', 399.00, 10),
('Router WiFi', 'Redes', 89.00, 50),
('Switch 24 puertos', 'Redes', 199.00, 15),
('Servidor Rack', 'Servidores', 2499.00, 3),
('Webcam HD', 'Periféricos', 59.00, 45);

INSERT INTO ventas (cliente_id, empleado_id, producto_id, cantidad, fecha) VALUES
(1,5,1,3,'2023-01-10'), (2,6,2,2,'2023-01-15'), (3,5,4,10,'2023-02-03'),
(4,7,6,20,'2023-02-20'), (5,6,9,5,'2023-03-05'), (1,5,2,1,'2023-03-15'),
(6,7,3,2,'2023-04-02'), (7,5,7,15,'2023-04-17'), (8,6,12,4,'2023-05-01'),
(9,7,5,6,'2023-05-19'), (10,5,14,1,'2023-06-03'), (2,6,8,5,'2023-06-20'),
(3,7,10,8,'2023-07-11'), (1,5,15,12,'2023-08-04'), (4,6,11,2,'2023-08-22'),
(5,7,1,4,'2023-09-05'), (6,5,13,3,'2023-09-21'), (2,6,4,8,'2023-10-10'),
(8,7,9,12,'2023-11-02'), (1,5,6,30,'2023-12-15'), (3,6,2,3,'2024-01-08'),
(4,7,5,5,'2024-01-25'), (6,5,3,1,'2024-02-14'), (7,6,7,25,'2024-03-01'),
(9,7,12,6,'2024-03-18'), (1,5,9,10,'2024-04-02'), (2,6,10,4,'2024-04-22'),
(5,7,14,2,'2024-05-06'), (8,5,1,5,'2024-05-20'), (10,6,4,15,'2024-06-03'),
(3,7,8,7,'2024-06-18'), (4,5,15,10,'2024-07-04'), (6,6,2,4,'2024-07-22'),
(7,7,11,3,'2024-08-10'), (1,5,13,2,'2024-08-28'), (2,6,6,25,'2024-09-12'),
(3,7,9,8,'2024-10-01'), (5,5,12,5,'2024-10-20'), (8,6,5,9,'2024-11-07'),
(9,7,3,2,'2024-12-02'), (1,5,2,3,'2025-01-10'), (4,6,7,20,'2025-01-25'),
(6,7,10,6,'2025-02-12'), (2,5,14,1,'2025-03-03'), (5,6,4,12,'2025-03-18'),
(3,7,1,7,'2025-04-05'), (8,5,8,4,'2025-04-21'), (9,6,11,2,'2025-05-09'),
(10,7,15,14,'2025-05-27'), (1,5,9,20,'2025-06-15');
```

**004-comprobacion.sql**

```sql
SHOW TABLES;

SELECT * FROM clientes;
```

**005-seleccion de columnas.sql**

```sql
SELECT 
nombre,
ciudad
FROM clientes;
```

**006-proyecciones.sql**

```sql
SELECT 
nombre AS 'Nombre del cliente',
ciudad AS 'Ciudad del cliente'
FROM clientes;
```

**007-ahora lo quiero todo de nuevo.sql**

```sql
SELECT * FROM clientes;


```

**008-ordenacion.sql**

```sql
SELECT * 
FROM clientes
ORDER BY ciudad;

```

**009-asc por defecto.sql**

```sql
SELECT * 
FROM clientes
ORDER BY ciudad ASC;

```

**010-desc.sql**

```sql
SELECT * 
FROM clientes
ORDER BY ciudad DESC;

```

**011-multiples columnas.sql**

```sql
SELECT * 
FROM clientes
ORDER BY ciudad,nombre ASC;


```

### Ejercicio base da dados 3/1-Ejercicios/002-Operadores. Operadores de comparación. Operadores lógicos

**000-introducion.md**

```markdown
```

**001-lista de productos.sql**

```sql
SHOW TABLES;

SELECT * FROM productos;
```

**002-suma.sql**

```sql
SELECT 
nombre,
precio,
precio+20
FROM productos;
```

**003-resta.sql**

```sql
SELECT 
nombre,
precio,
precio-20
FROM productos;
```

**004-multiplicacion.sql**

```sql
SELECT 
nombre,
precio,
precio*20
FROM productos;
```

**005-division.sql**

```sql
SELECT 
nombre,
precio,
precio/20
FROM productos;
```

**006-iva por producto.sql**

```sql
SELECT 
nombre,
precio AS 'Base imponible',
precio*0.21 AS 'IVA',
precio + precio*0.21 AS 'Total'
FROM productos;
```

**007-producto barato.sql**

```sql
SELECT 
nombre,
precio AS 'Base imponible',
precio*0.21 AS 'IVA',
precio + precio*0.21 AS 'Total',
precio < 500 AS 'Barato'
FROM productos;
```

**008-limite.sql**

```sql
SELECT 
nombre,
precio AS 'Base imponible',
precio*0.21 AS 'IVA',
precio + precio*0.21 AS 'Total',
precio < 500 AS 'Barato'
FROM productos
LIMIT 3;
```

**009-dos condiciones.sql**

```sql
SELECT 
nombre,
precio AS 'Base imponible',
precio*0.21 AS 'IVA',
precio + precio*0.21 AS 'Total',
precio < 500 AS 'Barato',
precio > 500 AND nombre = 'Portátil Basic'
FROM productos;


```

### Ejercicio base da dados 3/1-Ejercicios/003-Consultas de resumen

**000-introducion.md**

```markdown
```

**001-cuenteo.sql**

```sql
SELECT * FROM clientes;

SELECT COUNT(nombre) FROM clientes;
```

**002-sumas.sql**

```sql
SELECT SUM(precio)
FROM productos;
```

**003-maximo.sql**

```sql
SELECT MAX(precio)
FROM productos;
```

**004-minimo.sql**

```sql
SELECT MIN(precio)
FROM productos;
```

**005-promedio.sql**

```sql
SELECT AVG(precio)
FROM productos;
```

### Ejercicio base da dados 3/1-Ejercicios/004-Agrupamiento de registros

**000-introducion.md**

```markdown
```

**001-agrupamiento.sql**

```sql
SELECT * FROM clientes;

SELECT * FROM clientes
WHERE ciudad = 'Valencia';


```

**002-rango.sql**

```sql
SELECT * FROM productos
WHERE precio BETWEEN 1000 AND 2000;
```

**003-in.sql**

```sql
SELECT * FROM clientes
WHERE ciudad IN('Valencia','Alicante');exit
```

### Ejercicio base da dados 3/1-Ejercicios/005-Composiciones internas

**000-introdución.md**

```markdown
```

**001-kata.md**

```markdown
sudo mysql -u root -p

USE seleccion;

SHOW TABLES;

SELECT * FROM clientes;

SELECT * FROM productos;

SELECT * FROM ventas;


```

**002-empezamos poco a poco.sql**

```sql
SELECT
producto_id,
cantidad,
fecha
FROM ventas;
```

**003-cruzo con producto.sql**

```sql
SELECT

productos.nombre,
productos.precio,
ventas.cantidad,
ventas.fecha

FROM ventas

LEFT JOIN productos ON ventas.producto_id = productos.id;
```

**004-operadores aritmeticos.sql**

```sql
SELECT

productos.nombre AS 'nombre',
productos.precio AS 'precio',
ventas.cantidad AS 'unidades',
ventas.cantidad * productos.precio AS 'total',
ventas.fecha AS 'fecha'

FROM ventas

LEFT JOIN productos ON ventas.producto_id = productos.id;
```

**005-saco el empleado.sql**

```sql
SELECT

productos.nombre AS 'nombre',
productos.precio AS 'precio',

ventas.cantidad AS 'unidades',
ventas.cantidad * productos.precio AS 'total',
ventas.fecha AS 'fecha',

empleados.nombre,
empleados.apellidos

FROM ventas

LEFT JOIN productos ON ventas.producto_id = productos.id
LEFT JOIN empleados ON ventas.empleado_id = empleados.id;
```

**006-saco el cliente.sql**

```sql
SELECT

productos.nombre AS 'nombre',
productos.precio AS 'precio',

ventas.cantidad AS 'unidades',
ventas.cantidad * productos.precio AS 'total',
ventas.fecha AS 'fecha',

empleados.nombre,
empleados.apellidos,

clientes.nombre

FROM ventas

LEFT JOIN productos ON ventas.producto_id = productos.id
LEFT JOIN empleados ON ventas.empleado_id = empleados.id
LEFT JOIN clientes ON ventas.cliente_id = clientes.id;
```

**007-alterar.sql**

```sql
ALTER TABLE 
clientes
CHANGE 
COLUMN email correo_electronico VARCHAR(150);


```

### Ejercicio base da dados 3/1-Ejercicios/007-Subconsultas

**000-introdución.md**

```markdown
```

**002-listado de productos.sql**

```sql
SELECT * FROM productos;

SELECT AVG(precio) FROM productos;

SELECT 
nombre,
precio,
precio > 513.78
FROM productos;
```

**003-subconsulta.sql**

```sql
SELECT 
nombre,
precio,
precio > (
	SELECT AVG(precio) FROM productos
) AS 'media'
FROM productos;
```

### Ejercicio base da dados 3/1-Ejercicios/008-Combinación de múltiples selecciones

**000-introdución.md**

```markdown
```

**001-listar tablas.sql**

```sql
SHOW TABLES;


```

**002-crear personas.sql**

```sql
CREATE TABLE personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    email VARCHAR(150),
    salario DECIMAL(10,2),
    fecha_contratacion DATE,
    departamento_id INT,
    jefe_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id),
    FOREIGN KEY (jefe_id) REFERENCES empleados(id)
);
```

**003-datos de ejemplo para personas.sql**

```sql
INSERT INTO personas 
(nombre, apellidos, email, salario, fecha_contratacion, departamento_id, jefe_id) 
VALUES
-- Algunos registros conservados de empleados
('Ana', 'García López', 'ana@empresa.com', 32000, '2018-03-15', 1, NULL),
('Carlos', 'Martínez Pérez', 'carlos@empresa.com', 28000, '2020-06-01', 1, 1),
('Pedro', 'Gómez Torres', 'pedro@empresa.com', 35000, '2017-01-10', 2, NULL),
('Marta', 'Navarro Gil', 'marta@empresa.com', 24000, '2021-04-12', 2, 4),
('Javier', 'Vidal Serra', 'javier@empresa.com', 31000, '2016-09-01', 3, NULL),
('Sofía', 'Castro Vega', 'sofia@empresa.com', 38000, '2018-05-21', 4, NULL),
('Miguel', 'Fuentes Lara', 'miguel@empresa.com', 33000, '2015-04-17', 5, NULL),
('Fernando', 'Blasco Puig', 'fernando@empresa.com', 42000, '2014-06-01', 7, NULL),

-- Registros nuevos
('María', 'López Ferrer', 'maria@empresa.com', 27500, '2021-05-14', 1, 1),
('Roberto', 'Jiménez Alba', 'roberto@empresa.com', 30500, '2020-02-20', 2, 4),
('Patricia', 'Domínguez Gil', 'patricia@empresa.com', 25500, '2022-09-12', 3, 8),
('Alejandro', 'Muñoz Pérez', 'alejandro@empresa.com', 36000, '2019-07-01', 4, 11),
('Beatriz', 'Serrano Vidal', 'beatriz@empresa.com', 24500, '2023-01-18', 5, 14),
('Héctor', 'Rubio Torres', 'hector@empresa.com', 31500, '2020-11-23', 6, 16),
('Irene', 'Calvo Martínez', 'irene@empresa.com', 29000, '2022-04-07', 7, 18),
('Daniel', 'Pascual Romero', 'daniel@empresa.com', 22500, '2024-02-15', 1, 1),
('Eva', 'Méndez Navarro', NULL, 23500, '2024-06-10', 2, 4),
('Óscar', 'Gallego Ruiz', 'oscar@empresa.com', 28500, '2023-10-02', 3, 8);
```

**004-UNION ALL.sql**

```sql
SELECT * FROM empleados

UNION ALL

SELECT * FROM personas;
```

**005-UNION.sql**

```sql
SELECT * FROM empleados

UNION

SELECT * FROM personas;
```

**006-intersect.sql**

```sql
SELECT * FROM empleados

INTERSECT

SELECT * FROM personas;
```

**007-EXCEPT.sql**

```sql
SELECT * FROM empleados

EXCEPT

SELECT * FROM personas;
```

### Ejercicio base da dados 3/1-Ejercicios/009-Optimización de consultas

**000-introdución.md**

```markdown
```

**001-where.sql**

```sql
SELECT * FROM clientes;


SELECT * FROM clientes
WHERE ciudad = 'Valencia';
```

**002-similaridad.sql**

```sql

SELECT * FROM clientes
WHERE nombre LIKE '%ecno%';
```

**010-productos.sql**

```sql
SELECT * FROM productos;

SELECT * FROM productos
WHERE precio > 500;


SELECT * FROM productos
WHERE 
precio > 500
AND
categoria = 'Servidores';
```

### Ejercicio base da dados 3/1-Ejercicios/010-Ejercicio final de unidad

**001-Tarea a realizar.md**

```markdown
Debéis 

1.-Planificar una base de datos que tenga varias tablas relacionadas
Vosotros visteis que yo ESA parte del trabajo la hice con IA - vosotros tambien

CREATE TABLE + INSERT de este ejercicio, con IA - todo lo demás, a mano

2.-Realizar, sobre vuestra base de datos
a)select, columnas, alias
b) demostrar el uso de operadores
c)consultas de resumen, cuenteos, sumas, promedios, etc
d)agrupamientos
e)composiciones solo con left join
f)subconsultas
g)combinaciones
h) uso de where en las peticiones SELECT

De qué irá la base de datos? De lo que queráis.
Mi recomendación es que vaya de "algo" que os motive, que os sirva, que luego podáis
utilizar
```

## Ejercicio base da dados 3/2-Proyecto

**001-crear base de datos.sql**

```sql
-- =====================================================
--  Base de datos: mi biblioteca personal
--  Ejercicio 1: CREATE TABLE + INSERT
-- =====================================================


CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE biblioteca;

-- -----------------------------------------------------
--  Tabla: categorias
-- -----------------------------------------------------
CREATE TABLE categorias (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nombre       VARCHAR(50) NOT NULL UNIQUE
);

-- -----------------------------------------------------
--  Tabla: autores
-- -----------------------------------------------------
CREATE TABLE autores (
  id_autor     INT AUTO_INCREMENT PRIMARY KEY,
  nombre       VARCHAR(100) NOT NULL,
  nacionalidad VARCHAR(50)
);

-- -----------------------------------------------------
--  Tabla: libros
-- -----------------------------------------------------
CREATE TABLE libros (
  id_libro          INT AUTO_INCREMENT PRIMARY KEY,
  titulo            VARCHAR(150) NOT NULL,
  id_autor          INT NOT NULL,
  id_categoria      INT NOT NULL,
  paginas           INT,
  precio            DECIMAL(6,2),
  fecha_compra      DATE NOT NULL,
  fecha_fin_lectura DATE NULL,
  valoracion        TINYINT NULL CHECK (valoracion BETWEEN 1 AND 5),
  FOREIGN KEY (id_autor)     REFERENCES autores(id_autor),
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- -----------------------------------------------------
--  Datos: categorias
--  (Poesía y Biografía no tienen libros: útil para LEFT JOIN)
-- -----------------------------------------------------
INSERT INTO categorias (nombre) VALUES
('Novela'),          -- 1
('Ciencia ficción'), -- 2
('Clásico'),         -- 3
('Infantil'),        -- 4
('Historia'),        -- 5
('Ensayo'),          -- 6
('Programación'),    -- 7
('Fantasía'),        -- 8
('Autoayuda'),       -- 9
('Finanzas'),        -- 10
('Poesía'),          -- 11
('Biografía');       -- 12

-- -----------------------------------------------------
--  Datos: autores
--  (Fernando Pessoa y Clarice Lispector no tienen libros: útil para LEFT JOIN)
-- -----------------------------------------------------
INSERT INTO autores (nombre, nacionalidad) VALUES
('Gabriel García Márquez',     'Colombiana'),    -- 1
('George Orwell',              'Británica'),     -- 2
('Miguel de Cervantes',        'Española'),      -- 3
('Antoine de Saint-Exupéry',   'Francesa'),      -- 4
('Yuval Noah Harari',          'Israelí'),       -- 5
('Robert C. Martin',           'Estadounidense'),-- 6
('Andrew Hunt',                'Estadounidense'),-- 7
('J. K. Rowling',              'Británica'),     -- 8
('J. R. R. Tolkien',           'Británica'),     -- 9
('Ray Bradbury',               'Estadounidense'),-- 10
('James Clear',                'Estadounidense'),-- 11
('Robert Kiyosaki',            'Estadounidense'),-- 12
('Paulo Coelho',               'Brasileña'),     -- 13
('José Saramago',              'Portuguesa'),    -- 14
('Carlos Ruiz Zafón',          'Española'),      -- 15
('Machado de Assis',           'Brasileña'),     -- 16
('Fernando Pessoa',            'Portuguesa'),    -- 17
('Clarice Lispector',          'Brasileña');     -- 18

-- -----------------------------------------------------
--  Datos: libros (20 libros, fechas ficticias)
-- -----------------------------------------------------
INSERT INTO libros
(titulo, id_autor, id_categoria, paginas, precio, fecha_compra, fecha_fin_lectura, valoracion) VALUES
('Cien años de soledad',                    1,  1, 471, 21.90, '2024-01-15', '2024-03-02', 5),
('El amor en los tiempos del cólera',       1,  1, 464, 19.50, '2024-05-10', '2024-07-01', 4),
('1984',                                    2,  2, 352, 12.95, '2024-02-03', '2024-02-25', 5),
('Rebelión en la granja',                   2,  1, 144,  9.95, '2024-02-03', '2024-02-10', 4),
('Don Quijote de la Mancha',                3,  3, 1376, 25.00, '2024-03-20', NULL,        NULL),
('El principito',                           4,  4, 96,   8.50, '2024-04-01', '2024-04-03', 5),
('Sapiens: de animales a dioses',           5,  5, 496, 22.90, '2024-06-12', '2024-08-20', 5),
('Homo Deus: breve historia del mañana',    5,  6, 496, 22.90, '2024-09-05', '2024-11-15', 4),
('Código limpio',                           6,  7, 464, 39.90, '2025-01-10', '2025-03-30', 5),
('El programador pragmático',               7,  7, 352, 42.00, '2025-02-14', NULL,        NULL),
('Harry Potter y la piedra filosofal',      8,  8, 256, 15.95, '2024-07-07', '2024-07-20', 4),
('El Señor de los Anillos: La Comunidad del Anillo', 9, 8, 576, 23.95, '2024-10-01', '2024-12-10', 5),
('El hobbit',                               9,  8, 320, 14.95, '2024-08-15', '2024-09-01', 4),
('Fahrenheit 451',                         10,  2, 192, 10.95, '2025-03-05', '2025-03-18', 4),
('Hábitos atómicos',                       11,  9, 336, 19.90, '2025-01-02', '2025-01-28', 4),
('Padre rico, padre pobre',                12, 10, 272, 16.90, '2025-04-11', '2025-05-02', 3),
('El alquimista',                          13,  1, 192, 12.90, '2025-05-20', '2025-05-30', 3),
('Ensayo sobre la ceguera',                14,  1, 432, 20.90, '2025-07-01', '2025-08-14', 5),
('La sombra del viento',                   15,  1, 576, 21.90, '2025-09-10', NULL,        NULL),
('Dom Casmurro',                           16,  3, 256, 11.50, '2026-01-08', '2026-02-20', 4);
```

**002-consultas.sql**

```sql
-- =====================================================
--  Base de datos: mi biblioteca personal
--  Consultas
-- =====================================================

USE biblioteca;

-- =====================================================
--  a) SELECT, columnas, alias
-- =====================================================

-- Todas las columnas
SELECT * FROM libros;

-- Solo algunas columnas
SELECT titulo, paginas, precio FROM libros;

-- Alias de columnas
SELECT titulo AS 'Título', paginas AS 'Páginas', precio AS 'Precio (€)'
FROM libros;

-- Alias de tablas
SELECT l.titulo, l.fecha_compra
FROM libros AS l;


-- =====================================================
--  b) Operadores
-- =====================================================

-- Aritméticos: precio con IVA (4% en libros)
SELECT titulo, precio, ROUND(precio * 1.04, 2) AS precio_con_iva
FROM libros;

-- Comparación: libros de más de 400 páginas
SELECT titulo, paginas FROM libros WHERE paginas > 400;

-- Lógicos (AND): libros de más de 20 € con valoración 5
SELECT titulo, precio, valoracion FROM libros
WHERE precio > 20 AND valoracion = 5;

-- Lógicos (OR): libros de Novela (1) o Fantasía (8)
SELECT titulo, id_categoria FROM libros
WHERE id_categoria = 1 OR id_categoria = 8;

-- Lógicos (NOT): libros que no son de Novela
SELECT titulo, id_categoria FROM libros WHERE NOT id_categoria = 1;

-- BETWEEN: libros entre 10 y 20 €
SELECT titulo, precio FROM libros WHERE precio BETWEEN 10 AND 20;

-- IN: autores de varias nacionalidades
SELECT nombre, nacionalidad FROM autores
WHERE nacionalidad IN ('Brasileña', 'Portuguesa');

-- LIKE: títulos que empiezan por "El"
SELECT titulo FROM libros WHERE titulo LIKE 'El %';

-- IS NULL: libros que todavía no he terminado
SELECT titulo, fecha_compra FROM libros WHERE fecha_fin_lectura IS NULL;

-- IS NOT NULL: libros ya terminados
SELECT titulo, fecha_fin_lectura FROM libros WHERE fecha_fin_lectura IS NOT NULL;


-- =====================================================
--  c) Consultas de resumen
-- =====================================================

-- Cuántos libros tengo
SELECT COUNT(*) AS total_libros FROM libros;

-- Cuántos libros he terminado (COUNT ignora los NULL)
SELECT COUNT(fecha_fin_lectura) AS libros_leidos FROM libros;

-- Cuánto he gastado en total
SELECT SUM(precio) AS gasto_total FROM libros;

-- Precio medio y páginas medias
SELECT ROUND(AVG(precio), 2) AS precio_medio,
       ROUND(AVG(paginas))   AS paginas_medias
FROM libros;

-- Libro más caro y más barato
SELECT MAX(precio) AS mas_caro, MIN(precio) AS mas_barato FROM libros;

-- Valoración media de los libros valorados
SELECT ROUND(AVG(valoracion), 2) AS valoracion_media FROM libros;


-- =====================================================
--  d) Agrupamientos (GROUP BY / HAVING)
-- =====================================================

-- Cuántos libros hay por categoría (id)
SELECT id_categoria, COUNT(*) AS num_libros
FROM libros
GROUP BY id_categoria;

-- Gasto por autor
SELECT id_autor, SUM(precio) AS gasto
FROM libros
GROUP BY id_autor
ORDER BY gasto DESC;

-- Libros comprados por año
SELECT YEAR(fecha_compra) AS anio, COUNT(*) AS libros_comprados
FROM libros
GROUP BY YEAR(fecha_compra);

-- HAVING: autores de los que tengo más de un libro
SELECT id_autor, COUNT(*) AS num_libros
FROM libros
GROUP BY id_autor
HAVING COUNT(*) > 1;


-- =====================================================
--  e) Composiciones con LEFT JOIN
-- =====================================================

-- Libros con el nombre del autor y de la categoría
SELECT l.titulo, a.nombre AS autor, c.nombre AS categoria
FROM libros l
LEFT JOIN autores    a ON l.id_autor     = a.id_autor
LEFT JOIN categorias c ON l.id_categoria = c.id_categoria;

-- Todas las categorías con sus libros (Poesía y Biografía salen con NULL)
SELECT c.nombre AS categoria, l.titulo
FROM categorias c
LEFT JOIN libros l ON c.id_categoria = l.id_categoria;

-- Autores de los que no tengo ningún libro
SELECT a.nombre
FROM autores a
LEFT JOIN libros l ON a.id_autor = l.id_autor
WHERE l.id_libro IS NULL;

-- Número de libros por categoría, incluidas las que tienen 0
SELECT c.nombre AS categoria, COUNT(l.id_libro) AS num_libros
FROM categorias c
LEFT JOIN libros l ON c.id_categoria = l.id_categoria
GROUP BY c.nombre
ORDER BY num_libros DESC;

-- Gasto por nacionalidad del autor
SELECT a.nacionalidad, COUNT(l.id_libro) AS libros, IFNULL(SUM(l.precio), 0) AS gasto
FROM autores a
LEFT JOIN libros l ON a.id_autor = l.id_autor
GROUP BY a.nacionalidad;


-- =====================================================
--  f) Subconsultas
-- =====================================================

-- Libros más caros que la media
SELECT titulo, precio FROM libros
WHERE precio > (SELECT AVG(precio) FROM libros);

-- El libro más largo
SELECT titulo, paginas FROM libros
WHERE paginas = (SELECT MAX(paginas) FROM libros);

-- Libros de autores brasileños (subconsulta con IN)
SELECT titulo FROM libros
WHERE id_autor IN (SELECT id_autor FROM autores WHERE nacionalidad = 'Brasileña');

-- Categorías sin libros (subconsulta con NOT IN)
SELECT nombre FROM categorias
WHERE id_categoria NOT IN (SELECT id_categoria FROM libros);


-- =====================================================
--  g) Combinaciones (UNION)
-- =====================================================

-- Lista de libros con su estado: leído o pendiente
SELECT titulo, 'Leído' AS estado FROM libros WHERE fecha_fin_lectura IS NOT NULL
UNION
SELECT titulo, 'Pendiente' AS estado FROM libros WHERE fecha_fin_lectura IS NULL
ORDER BY estado, titulo;

-- Nombres de autores y categorías en una misma lista
SELECT nombre, 'Autor' AS tipo FROM autores
UNION
SELECT nombre, 'Categoría' AS tipo FROM categorias;


-- =====================================================
--  h) WHERE en las peticiones SELECT
-- =====================================================

-- Libros comprados en 2025
SELECT titulo, fecha_compra FROM libros
WHERE YEAR(fecha_compra) = 2025;

-- Libros con valoración 5 y su autor
SELECT l.titulo, a.nombre AS autor
FROM libros l
LEFT JOIN autores a ON l.id_autor = a.id_autor
WHERE l.valoracion = 5;

-- Días que tardé en leer cada libro terminado
SELECT titulo, DATEDIFF(fecha_fin_lectura, fecha_compra) AS dias_lectura
FROM libros
WHERE fecha_fin_lectura IS NOT NULL
ORDER BY dias_lectura;

-- Libros de autores británicos de menos de 300 páginas
SELECT l.titulo, l.paginas, a.nombre
FROM libros l
LEFT JOIN autores a ON l.id_autor = a.id_autor
WHERE a.nacionalidad = 'Británica' AND l.paginas < 300;
```

**Backup SQL Mi Biblioteca.sql**

```sql
-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: biblioteca
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
-- Table structure for table `autores`
--

DROP TABLE IF EXISTS `autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autores` (
  `id_autor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `nacionalidad` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_autor`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autores`
--

LOCK TABLES `autores` WRITE;
/*!40000 ALTER TABLE `autores` DISABLE KEYS */;
INSERT INTO `autores` VALUES (1,'Gabriel García Márquez','Colombiana'),(2,'George Orwell','Británica'),(3,'Miguel de Cervantes','Española'),(4,'Antoine de Saint-Exupéry','Francesa'),(5,'Yuval Noah Harari','Israelí'),(6,'Robert C. Martin','Estadounidense'),(7,'Andrew Hunt','Estadounidense'),(8,'J. K. Rowling','Británica'),(9,'J. R. R. Tolkien','Británica'),(10,'Ray Bradbury','Estadounidense'),(11,'James Clear','Estadounidense'),(12,'Robert Kiyosaki','Estadounidense'),(13,'Paulo Coelho','Brasileña'),(14,'José Saramago','Portuguesa'),(15,'Carlos Ruiz Zafón','Española'),(16,'Machado de Assis','Brasileña'),(17,'Fernando Pessoa','Portuguesa'),(18,'Clarice Lispector','Brasileña');
/*!40000 ALTER TABLE `autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id_categoria`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (9,'Autoayuda'),(12,'Biografía'),(2,'Ciencia ficción'),(3,'Clásico'),(6,'Ensayo'),(8,'Fantasía'),(10,'Finanzas'),(5,'Historia'),(4,'Infantil'),(1,'Novela'),(11,'Poesía'),(7,'Programación');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libros` (
  `id_libro` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(150) NOT NULL,
  `id_autor` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `paginas` int(11) DEFAULT NULL,
  `precio` decimal(6,2) DEFAULT NULL,
  `fecha_compra` date NOT NULL,
  `fecha_fin_lectura` date DEFAULT NULL,
  `valoracion` tinyint(4) DEFAULT NULL CHECK (`valoracion` between 1 and 5),
  PRIMARY KEY (`id_libro`),
  KEY `id_autor` (`id_autor`),
  KEY `id_categoria` (`id_categoria`),
  CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id_autor`),
  CONSTRAINT `libros_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
INSERT INTO `libros` VALUES (1,'Cien años de soledad',1,1,471,21.90,'2024-01-15','2024-03-02',5),(2,'El amor en los tiempos del cólera',1,1,464,19.50,'2024-05-10','2024-07-01',4),(3,'1984',2,2,352,12.95,'2024-02-03','2024-02-25',5),(4,'Rebelión en la granja',2,1,144,9.95,'2024-02-03','2024-02-10',4),(5,'Don Quijote de la Mancha',3,3,1376,25.00,'2024-03-20',NULL,NULL),(6,'El principito',4,4,96,8.50,'2024-04-01','2024-04-03',5),(7,'Sapiens: de animales a dioses',5,5,496,22.90,'2024-06-12','2024-08-20',5),(8,'Homo Deus: breve historia del mañana',5,6,496,22.90,'2024-09-05','2024-11-15',4),(9,'Código limpio',6,7,464,39.90,'2025-01-10','2025-03-30',5),(10,'El programador pragmático',7,7,352,42.00,'2025-02-14',NULL,NULL),(11,'Harry Potter y la piedra filosofal',8,8,256,15.95,'2024-07-07','2024-07-20',4),(12,'El Señor de los Anillos: La Comunidad del Anillo',9,8,576,23.95,'2024-10-01','2024-12-10',5),(13,'El hobbit',9,8,320,14.95,'2024-08-15','2024-09-01',4),(14,'Fahrenheit 451',10,2,192,10.95,'2025-03-05','2025-03-18',4),(15,'Hábitos atómicos',11,9,336,19.90,'2025-01-02','2025-01-28',4),(16,'Padre rico, padre pobre',12,10,272,16.90,'2025-04-11','2025-05-02',3),(17,'El alquimista',13,1,192,12.90,'2025-05-20','2025-05-30',3),(18,'Ensayo sobre la ceguera',14,1,432,20.90,'2025-07-01','2025-08-14',5),(19,'La sombra del viento',15,1,576,21.90,'2025-09-10',NULL,NULL),(20,'Dom Casmurro',16,3,256,11.50,'2026-01-08','2026-02-20',4);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-06 10:53:28
```

## Ejercicio base da dados 3/3-Resultado de aprendizaje

**Criterios de evaluación.md**

```markdown
# Criterios de evaluación


a) Se han identificado las herramientas y sentencias para realizar consultas. 
MySQL (terminal y VS Code). USE biblioteca; y SELECT ... FROM ... WHERE.

b) Se han realizado consultas simples sobre una tabla. 
SELECT titulo AS Título FROM libros WHERE precio > 20;

c) Se han realizado consultas sobre el contenido de varias tablas mediante composiciones internas. 
INNER JOIN muestra solo lo que coincide. SELECT l.titulo, a.nombre FROM libros l INNER JOIN autores a ON l.id_autor = a.id_autor;

d) Se han realizado consultas sobre el contenido de varias tablas mediante composiciones externas. 
LEFT JOIN muestra todo, aunque no coincida (NULL). SELECT c.nombre, l.titulo FROM categorias c LEFT JOIN libros l ON c.id_categoria = l.id_categoria;

e) Se han realizado consultas resumen.
 COUNT, SUM, AVG, MAX, MIN y GROUP BY. SELECT id_categoria, COUNT(*) FROM libros GROUP BY id_categoria;

f) Se han realizado consultas con subconsultas. Una consulta dentro de otra. 
SELECT titulo FROM libros WHERE precio > (SELECT AVG(precio) FROM libros);

g) Se han realizado consultas que implican múltiples selecciones. 
UNION junta dos SELECT. SELECT nombre FROM autores UNION SELECT nombre FROM categorias;

h) Se han aplicado criterios de optimización de consultas.
Pedir solo las columnas necesarias, filtrar con WHERE, usar LIMIT y claves en los JOIN.
```

