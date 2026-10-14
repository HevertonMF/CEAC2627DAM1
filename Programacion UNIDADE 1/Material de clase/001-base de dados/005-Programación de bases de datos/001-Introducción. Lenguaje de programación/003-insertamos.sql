CREATE TABLE datos_personales(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  apellidos VARCHAR(100),
  ubicacion VARCHAR(100)
);

INSERT INTO datos_personales VALUES(
	NULL,
  'Heverton',
  'Marques Ferreira Maciel',
  'Canet d en Berenguer, Valencia, España'
);

SELECT * FROM datos_personales;