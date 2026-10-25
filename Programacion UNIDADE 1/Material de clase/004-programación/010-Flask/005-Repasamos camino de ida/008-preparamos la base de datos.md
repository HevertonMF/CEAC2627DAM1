C:\xampp\mysql\bin\mysql.exe -u root -p


CREATE DATABASE psicologos;
USE psicologos;

CREATE TABLE psicologos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  especialidad VARCHAR(100),
  numero_de_colegiado VARCHAR(100)
);