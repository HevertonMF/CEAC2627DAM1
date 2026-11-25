Subunidad 1:
Ejemplo:
ciclistas
	-nombre
  -apellidos
  -fecha_de_nacimiento
  -email
  -telefono


Subunidad 2:
sudo mysql -u root -p

CREATE DATABASE clase;
USE clase;
SHOW TABLES;

Subunidad 3:
CREATE TABLE ciclistas (
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    fecha_de_nacimiento VARCHAR(100),
    email VARCHAR(100),
    telefono VARCHAR(100)
);
SHOW TABLES;
DESCRIBE ciclistas;

Subunidad 4:
ALTER TABLE ciclistas
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

DESCRIBE ciclistas;

INSERT INTO ciclistas VALUES(
	'Heverton',
  'Marques Ferreira',
  '1991-02-08', '662353018', 'hevertonmf@gmail.com', NULL);
  
SELECT * FROM ciclistas;

Subunidad 5:
ALTER TABLE ciclistas
ADD CONSTRAINT chk_ciclistas_email
CHECK (
    email IS NULL
    OR email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
);

Subunidad 6: (nos la saltamos)

Subunidad 7: Claves ajenas

CREATE TABLE `meta de kilómetros` (
    Identificador INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100),
    kilometros DECIMAL(10,2),
    PRIMARY KEY (Identificador)
);

ALTER TABLE meta de kilómetros
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

CREATE TABLE `día que practicó` (
    fecha DATE,
);

ALTER TABLE día que practicó
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

Subunidad 9: Vistas: Pedir algo que involucre a todas las tablas

SELECT 
    c.Identificador,
    c.nombre,
    c.apellidos,
    dp.fecha AS 'día que practicó',
    mk.kilometros AS 'meta de kilómetros'
FROM ciclistas AS c
LEFT JOIN `día que practicó` AS dp ON c.Identificador = dp.ciclista_id
LEFT JOIN `meta de kilómetros` AS mk ON c.nombre = mk.nombre;

Subunidad 10:

CREATE USER 'heverton'@'localhost' IDENTIFIED BY 'EAEA9A297a*';
GRANT USAGE ON *.* TO 'heverton'@'localhost';

ALTER USER 'heverton'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON empresadan2627.* 
TO 'heverton'@'localhost';

GRANT ALL PRIVILEGES ON clase.* 
TO 'heverton'@'localhost';

FLUSH PRIVILEGES;

