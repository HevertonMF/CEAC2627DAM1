USE ciudades;

SELECT
ciudades.ciudades,
ciudades.continente,
paises.nombre
FROM ciudades
LEFT JOIN paises
ON ciudades.pais_id = paises.id;
