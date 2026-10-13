USE ciudades;

UPDATE ciudades
SET continente = "Sudamérica"
WHERE pais_id = (SELECT id FROM paises WHERE nombre = "Argentina");

SELECT * FROM ciudades;
