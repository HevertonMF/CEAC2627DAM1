Es una base de datos de CIUDADES del mundo.
Cada ciudad es de un PAÍS y de un continente.

Las entidades de momento son 2:
-Ciudades
id
ciudades
país
continente
pais_id

-Paises
id
nombre

Un país tiene muchas ciudades.
Las uno con pais_id (el id del país en la tabla paises).

CREATE DATABASE ciudades;

USE ciudades;

SHOW TABLES;

CREATE TABLE ciudades(...);
CREATE TABLE paises(...);
