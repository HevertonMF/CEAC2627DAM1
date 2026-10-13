USE ciudades;

SELECT * FROM ciudades;

-- Borro una ciudad por su nombre
DELETE FROM ciudades
WHERE ciudades = "Granada";

-- Borro con varias condiciones
DELETE FROM ciudades
WHERE país = "España"
AND ciudades = "Málaga";

SELECT * FROM ciudades;
