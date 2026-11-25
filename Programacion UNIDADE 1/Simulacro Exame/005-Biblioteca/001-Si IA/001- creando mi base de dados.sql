CREATE TABLE "libros" (
	"id"	INTEGER,
	"titulo"	TEXT,
	"autor"	TEXT,
	"fecha_de_publicacion"	TEXT,
	"sinopsis"	TEXT,
	"editorial"	TEXT,
	"isbn"	TEXT,
	"genero"	TEXT,
	"precio"	INTEGER,
	"disponible"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO libros VALUES(
  NULL,
  'Don Quijote',
  'Miguel de Cervantes',
  '1605-01-16',
  'Un hidalgo que lucha contra molinos de viento creyéndolos gigantes',
  'Nuevo Mundo',
  9788400000001,
  'Novela',
  22.99,
  'Sí'
);

