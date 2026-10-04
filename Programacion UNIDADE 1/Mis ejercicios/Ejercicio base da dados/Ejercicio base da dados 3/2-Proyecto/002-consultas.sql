-- =====================================================
--  Base de datos: mi biblioteca personal
--  Consultas
-- =====================================================

USE biblioteca;

-- =====================================================
--  a) SELECT, columnas, alias
-- =====================================================

-- Todas las columnas
SELECT * FROM libros;

-- Solo algunas columnas
SELECT titulo, paginas, precio FROM libros;

-- Alias de columnas
SELECT titulo AS 'Título', paginas AS 'Páginas', precio AS 'Precio (€)'
FROM libros;

-- Alias de tablas
SELECT l.titulo, l.fecha_compra
FROM libros AS l;


-- =====================================================
--  b) Operadores
-- =====================================================

-- Aritméticos: precio con IVA (4% en libros)
SELECT titulo, precio, ROUND(precio * 1.04, 2) AS precio_con_iva
FROM libros;

-- Comparación: libros de más de 400 páginas
SELECT titulo, paginas FROM libros WHERE paginas > 400;

-- Lógicos (AND): libros de más de 20 € con valoración 5
SELECT titulo, precio, valoracion FROM libros
WHERE precio > 20 AND valoracion = 5;

-- Lógicos (OR): libros de Novela (1) o Fantasía (8)
SELECT titulo, id_categoria FROM libros
WHERE id_categoria = 1 OR id_categoria = 8;

-- Lógicos (NOT): libros que no son de Novela
SELECT titulo, id_categoria FROM libros WHERE NOT id_categoria = 1;

-- BETWEEN: libros entre 10 y 20 €
SELECT titulo, precio FROM libros WHERE precio BETWEEN 10 AND 20;

-- IN: autores de varias nacionalidades
SELECT nombre, nacionalidad FROM autores
WHERE nacionalidad IN ('Brasileña', 'Portuguesa');

-- LIKE: títulos que empiezan por "El"
SELECT titulo FROM libros WHERE titulo LIKE 'El %';

-- IS NULL: libros que todavía no he terminado
SELECT titulo, fecha_compra FROM libros WHERE fecha_fin_lectura IS NULL;

-- IS NOT NULL: libros ya terminados
SELECT titulo, fecha_fin_lectura FROM libros WHERE fecha_fin_lectura IS NOT NULL;


-- =====================================================
--  c) Consultas de resumen
-- =====================================================

-- Cuántos libros tengo
SELECT COUNT(*) AS total_libros FROM libros;

-- Cuántos libros he terminado (COUNT ignora los NULL)
SELECT COUNT(fecha_fin_lectura) AS libros_leidos FROM libros;

-- Cuánto he gastado en total
SELECT SUM(precio) AS gasto_total FROM libros;

-- Precio medio y páginas medias
SELECT ROUND(AVG(precio), 2) AS precio_medio,
       ROUND(AVG(paginas))   AS paginas_medias
FROM libros;

-- Libro más caro y más barato
SELECT MAX(precio) AS mas_caro, MIN(precio) AS mas_barato FROM libros;

-- Valoración media de los libros valorados
SELECT ROUND(AVG(valoracion), 2) AS valoracion_media FROM libros;


-- =====================================================
--  d) Agrupamientos (GROUP BY / HAVING)
-- =====================================================

-- Cuántos libros hay por categoría (id)
SELECT id_categoria, COUNT(*) AS num_libros
FROM libros
GROUP BY id_categoria;

-- Gasto por autor
SELECT id_autor, SUM(precio) AS gasto
FROM libros
GROUP BY id_autor
ORDER BY gasto DESC;

-- Libros comprados por año
SELECT YEAR(fecha_compra) AS anio, COUNT(*) AS libros_comprados
FROM libros
GROUP BY YEAR(fecha_compra);

-- HAVING: autores de los que tengo más de un libro
SELECT id_autor, COUNT(*) AS num_libros
FROM libros
GROUP BY id_autor
HAVING COUNT(*) > 1;


-- =====================================================
--  e) Composiciones con LEFT JOIN
-- =====================================================

-- Libros con el nombre del autor y de la categoría
SELECT l.titulo, a.nombre AS autor, c.nombre AS categoria
FROM libros l
LEFT JOIN autores    a ON l.id_autor     = a.id_autor
LEFT JOIN categorias c ON l.id_categoria = c.id_categoria;

-- Todas las categorías con sus libros (Poesía y Biografía salen con NULL)
SELECT c.nombre AS categoria, l.titulo
FROM categorias c
LEFT JOIN libros l ON c.id_categoria = l.id_categoria;

-- Autores de los que no tengo ningún libro
SELECT a.nombre
FROM autores a
LEFT JOIN libros l ON a.id_autor = l.id_autor
WHERE l.id_libro IS NULL;

-- Número de libros por categoría, incluidas las que tienen 0
SELECT c.nombre AS categoria, COUNT(l.id_libro) AS num_libros
FROM categorias c
LEFT JOIN libros l ON c.id_categoria = l.id_categoria
GROUP BY c.nombre
ORDER BY num_libros DESC;

-- Gasto por nacionalidad del autor
SELECT a.nacionalidad, COUNT(l.id_libro) AS libros, IFNULL(SUM(l.precio), 0) AS gasto
FROM autores a
LEFT JOIN libros l ON a.id_autor = l.id_autor
GROUP BY a.nacionalidad;


-- =====================================================
--  f) Subconsultas
-- =====================================================

-- Libros más caros que la media
SELECT titulo, precio FROM libros
WHERE precio > (SELECT AVG(precio) FROM libros);

-- El libro más largo
SELECT titulo, paginas FROM libros
WHERE paginas = (SELECT MAX(paginas) FROM libros);

-- Libros de autores brasileños (subconsulta con IN)
SELECT titulo FROM libros
WHERE id_autor IN (SELECT id_autor FROM autores WHERE nacionalidad = 'Brasileña');

-- Categorías sin libros (subconsulta con NOT IN)
SELECT nombre FROM categorias
WHERE id_categoria NOT IN (SELECT id_categoria FROM libros);


-- =====================================================
--  g) Combinaciones (UNION)
-- =====================================================

-- Lista de libros con su estado: leído o pendiente
SELECT titulo, 'Leído' AS estado FROM libros WHERE fecha_fin_lectura IS NOT NULL
UNION
SELECT titulo, 'Pendiente' AS estado FROM libros WHERE fecha_fin_lectura IS NULL
ORDER BY estado, titulo;

-- Nombres de autores y categorías en una misma lista
SELECT nombre, 'Autor' AS tipo FROM autores
UNION
SELECT nombre, 'Categoría' AS tipo FROM categorias;


-- =====================================================
--  h) WHERE en las peticiones SELECT
-- =====================================================

-- Libros comprados en 2025
SELECT titulo, fecha_compra FROM libros
WHERE YEAR(fecha_compra) = 2025;

-- Libros con valoración 5 y su autor
SELECT l.titulo, a.nombre AS autor
FROM libros l
LEFT JOIN autores a ON l.id_autor = a.id_autor
WHERE l.valoracion = 5;

-- Días que tardé en leer cada libro terminado
SELECT titulo, DATEDIFF(fecha_fin_lectura, fecha_compra) AS dias_lectura
FROM libros
WHERE fecha_fin_lectura IS NOT NULL
ORDER BY dias_lectura;

-- Libros de autores británicos de menos de 300 páginas
SELECT l.titulo, l.paginas, a.nombre
FROM libros l
LEFT JOIN autores a ON l.id_autor = a.id_autor
WHERE a.nacionalidad = 'Británica' AND l.paginas < 300;
