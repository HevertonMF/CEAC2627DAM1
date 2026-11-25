CREATE USER 'tiendabicicleta'@'localhost' IDENTIFIED BY 'TiendaBicicleta123$';

GRANT USAGE ON *.* TO 'tiendabicicleta'@'localhost';

ALTER USER 'tiendabicicleta'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendabicicletas.* 
TO 'tiendabicicleta'@'localhost';

FLUSH PRIVILEGES;
