USE ciudades;

SELECT * FROM ciudades;

DELETE FROM ciudades
WHERE pais_id = (SELECT id FROM paises WHERE nombre = "Portugal");

SELECT * FROM ciudades;
