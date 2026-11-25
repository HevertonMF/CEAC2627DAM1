-- Creación de la base de datos y la tabla videojuegos


CREATE TABLE "videojuegos" (
	"id"	INTEGER,
	"titulo"	TEXT,
	"desarrollador"	TEXT,
	"distribuidor"	TEXT,
	"genero"	TEXT,
	"descripcion"	TEXT,
	"anio_lanzamiento"	INTEGER,
	"fecha_lanzamiento"	TEXT,
	"plataforma"	TEXT,
	"pais"	TEXT,
	"idioma"	TEXT,
	"clasificacion_edades"	TEXT,
	"presupuesto"	TEXT,
	"ingresos"	TEXT,
	"valoracion_media"	TEXT,
	"numero_valoraciones"	INTEGER,
	"unidades_vendidas"	INTEGER,
	"disponible"	TEXT,
	"multijugador"	TEXT,
	"favorito"	TEXT,
	"imagen_portada"	TEXT,
	"url_trailer"	TEXT,
	"precio_original"	INTEGER,
	"precio_rebajado"	INTEGER,
	"espacio_requerido"	INTEGER,
	"compras_integradas"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- Insertar una película en la tabla videojuegos

INSERT INTO videojuegos VALUES(
  NULL,
  'Minecraft',
  'Mojang Studios',
  'Xbox Game Studios',
  'Aventura',
  'Mundo abierto de construcción...',
  2011,
  '2011-11-18',
  'PC',
  'Suecia',
  'Español',
  '7',
  '1000000.00',
  '50000000.00',
  '9.2',
  15000,
  300000000,
  'Verdadero',
  'Verdadero',
  'Falso',
  'minecraft.jpg',
  'https://...',
  29.99,
  19.99,
  '4.5',
  'Verdadero'
);
