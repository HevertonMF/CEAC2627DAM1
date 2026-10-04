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
