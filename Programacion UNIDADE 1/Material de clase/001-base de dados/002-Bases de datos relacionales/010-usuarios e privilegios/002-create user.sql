-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER 
'Heverton'@'localhost' 
IDENTIFIED  BY 'EAEA9A297a*';
@ = at (en)

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'Heverton'@'localhost';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len
GRANT USAGE ON *.* TO 'Heverton'@'localhost';


-- quitale todos los limites que tenga
ALTER USER 'Heverton'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

ALTER USER 'Heverton'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON empresadan2627.*  
TO 'Heverton'@'localhost';

GRANT ALL PRIVILEGES ON empresadan2627.* 
TO 'Heverton'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;

