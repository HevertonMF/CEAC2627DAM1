USE ciudades;

-- Completo el continente que faltaba de Granada
UPDATE ciudades
SET continente = "Europa"
WHERE ciudades = "Granada";

-- Cambio el nombre de Bombay por el actual
UPDATE ciudades
SET ciudades = "Mumbai"
WHERE id = 42;

-- Nunca sin WHERE porque cambia todas las filas

SELECT * FROM ciudades;
