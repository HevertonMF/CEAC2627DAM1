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
