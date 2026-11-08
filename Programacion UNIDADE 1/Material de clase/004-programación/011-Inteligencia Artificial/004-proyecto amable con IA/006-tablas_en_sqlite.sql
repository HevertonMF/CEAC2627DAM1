-- Tabla de proyectos (la de antes + 2 columnas nuevas)
CREATE TABLE "webs" (
	"id"	INTEGER,
	"usuario"	TEXT,
	"fecha"	TEXT,
	"pregunta"	TEXT,
	"respuesta"	TEXT,
	"titulo"	TEXT,          -- nombre editable del proyecto
	"actualizado"	TEXT,      -- fecha del último cambio (para ordenar el historial)
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- Cada cambio (IA, manual o restauración) guarda una versión
CREATE TABLE "versiones" (
	"id"	INTEGER,
	"web_id"	INTEGER,       -- a qué proyecto pertenece
	"fecha"	TEXT,
	"peticion"	TEXT,        -- lo que se pidió ("Edición manual" si fue a mano)
	"codigo"	TEXT,
	"tipo"	TEXT,            -- 'ia' | 'manual' | 'restaurar'
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- NOTA: no hace falta ejecutar esto a mano. 006-amable_mejorado.py crea/actualiza
-- las tablas solo al arrancar, sin perder los proyectos que ya tienes.
