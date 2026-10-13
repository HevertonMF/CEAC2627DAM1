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
