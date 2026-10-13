USE ciudades;

-- Primero busco el id de Brasil
SELECT id FROM paises
WHERE nombre = "Brasil";

-- Y lo meto dentro de otra consulta
SELECT * FROM ciudades
WHERE pais_id = (SELECT id FROM paises WHERE nombre = "Brasil");
