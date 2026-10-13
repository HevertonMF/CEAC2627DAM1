C:\xampp\mysql\bin\mysql.exe -u root -p

USE ciudades;

CREATE TABLE paises(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100)
);

-- Añado a ciudades una columna con el id del país
ALTER TABLE ciudades
ADD pais_id INT;
