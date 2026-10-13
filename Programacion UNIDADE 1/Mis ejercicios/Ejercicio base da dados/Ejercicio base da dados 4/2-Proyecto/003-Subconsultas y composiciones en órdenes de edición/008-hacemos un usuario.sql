-- Creo un usuario ciudades
CREATE USER 'ciudades'@'localhost' IDENTIFIED BY 'Ciudades123$';

-- A ese usuario le pemito acceder a todo en el servidor
GRANT USAGE ON *.* TO 'ciudades'@'localhost';

-- A ese usuario le quito limites para que pueda hacer de todo
ALTER USER 'ciudades'@'localhost'
REQUIRE NONE
WITH MAX_QUERIES_PER_HOUR 0
MAX_CONNECTIONS_PER_HOUR 0
MAX_UPDATES_PER_HOUR 0
MAX_USER_CONNECTIONS 0;

-- Garantizo privilegios al usuario en su base de datos
GRANT ALL PRIVILEGES ON ciudades.*
TO 'ciudades'@'localhost';

-- Recargo la tabla de privilegios
FLUSH PRIVILEGES;
