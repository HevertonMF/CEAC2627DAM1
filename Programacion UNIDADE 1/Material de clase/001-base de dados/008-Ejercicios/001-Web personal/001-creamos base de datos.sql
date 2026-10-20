C:\xampp\mysql\bin\mysql.exe -u root -p

CREATE DATABASE miweb;
USE miweb;

-- esta tabla será para escribir
CREATE TABLE IF NOT EXISTS contacto (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL,
  mensaje TEXT NOT NULL,
  fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- esta tabla será para leer
CREATE TABLE IF NOT EXISTS proyectos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  fecha DATE,
  descripcion TEXT,
  imagen VARCHAR(255)
);

SHOW TABLES;

