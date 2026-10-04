# Criterios de evaluación


a) Se han identificado las herramientas y sentencias para realizar consultas. 
MySQL (terminal y VS Code). USE biblioteca; y SELECT ... FROM ... WHERE.

b) Se han realizado consultas simples sobre una tabla. 
SELECT titulo AS Título FROM libros WHERE precio > 20;

c) Se han realizado consultas sobre el contenido de varias tablas mediante composiciones internas. 
INNER JOIN muestra solo lo que coincide. SELECT l.titulo, a.nombre FROM libros l INNER JOIN autores a ON l.id_autor = a.id_autor;

d) Se han realizado consultas sobre el contenido de varias tablas mediante composiciones externas. 
LEFT JOIN muestra todo, aunque no coincida (NULL). SELECT c.nombre, l.titulo FROM categorias c LEFT JOIN libros l ON c.id_categoria = l.id_categoria;

e) Se han realizado consultas resumen.
 COUNT, SUM, AVG, MAX, MIN y GROUP BY. SELECT id_categoria, COUNT(*) FROM libros GROUP BY id_categoria;

f) Se han realizado consultas con subconsultas. Una consulta dentro de otra. 
SELECT titulo FROM libros WHERE precio > (SELECT AVG(precio) FROM libros);

g) Se han realizado consultas que implican múltiples selecciones. 
UNION junta dos SELECT. SELECT nombre FROM autores UNION SELECT nombre FROM categorias;

h) Se han aplicado criterios de optimización de consultas.
Pedir solo las columnas necesarias, filtrar con WHERE, usar LIMIT y claves en los JOIN.