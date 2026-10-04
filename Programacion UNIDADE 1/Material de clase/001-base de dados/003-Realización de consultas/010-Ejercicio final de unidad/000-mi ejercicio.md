-- =====================================================
--  Base de datos: mi biblioteca personal
--  Ejercicio 1: CREATE TABLE + INSERT
-- =====================================================

DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE biblioteca;

-- -----------------------------------------------------
--  Tabla: categorias
-- -----------------------------------------------------
CREATE TABLE categorias (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nombre       VARCHAR(50) NOT NULL UNIQUE
);

-- -----------------------------------------------------
--  Tabla: autores
-- -----------------------------------------------------
CREATE TABLE autores (
  id_autor     INT AUTO_INCREMENT PRIMARY KEY,
  nombre       VARCHAR(100) NOT NULL,
  nacionalidad VARCHAR(50)
);

-- -----------------------------------------------------
--  Tabla: libros
--  fecha_fin_lectura = NULL  -> todavía no lo he terminado
--  valoracion (1-5)  = NULL  -> todavía no lo he valorado
-- -----------------------------------------------------
CREATE TABLE libros (
  id_libro          INT AUTO_INCREMENT PRIMARY KEY,
  titulo            VARCHAR(150) NOT NULL,
  id_autor          INT NOT NULL,
  id_categoria      INT NOT NULL,
  paginas           INT,
  precio            DECIMAL(6,2),
  fecha_compra      DATE NOT NULL,
  fecha_fin_lectura DATE NULL,
  valoracion        TINYINT NULL CHECK (valoracion BETWEEN 1 AND 5),
  FOREIGN KEY (id_autor)     REFERENCES autores(id_autor),
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- -----------------------------------------------------
--  Datos: categorias
--  (Poesía y Biografía no tienen libros: útil para LEFT JOIN)
-- -----------------------------------------------------
INSERT INTO categorias (nombre) VALUES
('Novela'),          -- 1
('Ciencia ficción'), -- 2
('Clásico'),         -- 3
('Infantil'),        -- 4
('Historia'),        -- 5
('Ensayo'),          -- 6
('Programación'),    -- 7
('Fantasía'),        -- 8
('Autoayuda'),       -- 9
('Finanzas'),        -- 10
('Poesía'),          -- 11
('Biografía');       -- 12

-- -----------------------------------------------------
--  Datos: autores
--  (Fernando Pessoa y Clarice Lispector no tienen libros: útil para LEFT JOIN)
-- -----------------------------------------------------
INSERT INTO autores (nombre, nacionalidad) VALUES
('Gabriel García Márquez',     'Colombiana'),    -- 1
('George Orwell',              'Británica'),     -- 2
('Miguel de Cervantes',        'Española'),      -- 3
('Antoine de Saint-Exupéry',   'Francesa'),      -- 4
('Yuval Noah Harari',          'Israelí'),       -- 5
('Robert C. Martin',           'Estadounidense'),-- 6
('Andrew Hunt',                'Estadounidense'),-- 7
('J. K. Rowling',              'Británica'),     -- 8
('J. R. R. Tolkien',           'Británica'),     -- 9
('Ray Bradbury',               'Estadounidense'),-- 10
('James Clear',                'Estadounidense'),-- 11
('Robert Kiyosaki',            'Estadounidense'),-- 12
('Paulo Coelho',               'Brasileña'),     -- 13
('José Saramago',              'Portuguesa'),    -- 14
('Carlos Ruiz Zafón',          'Española'),      -- 15
('Machado de Assis',           'Brasileña'),     -- 16
('Fernando Pessoa',            'Portuguesa'),    -- 17
('Clarice Lispector',          'Brasileña');     -- 18

-- -----------------------------------------------------
--  Datos: libros (20 libros, fechas ficticias)
-- -----------------------------------------------------
INSERT INTO libros
(titulo, id_autor, id_categoria, paginas, precio, fecha_compra, fecha_fin_lectura, valoracion) VALUES
('Cien años de soledad',                    1,  1, 471, 21.90, '2024-01-15', '2024-03-02', 5),
('El amor en los tiempos del cólera',       1,  1, 464, 19.50, '2024-05-10', '2024-07-01', 4),
('1984',                                    2,  2, 352, 12.95, '2024-02-03', '2024-02-25', 5),
('Rebelión en la granja',                   2,  1, 144,  9.95, '2024-02-03', '2024-02-10', 4),
('Don Quijote de la Mancha',                3,  3, 1376, 25.00, '2024-03-20', NULL,        NULL),
('El principito',                           4,  4, 96,   8.50, '2024-04-01', '2024-04-03', 5),
('Sapiens: de animales a dioses',           5,  5, 496, 22.90, '2024-06-12', '2024-08-20', 5),
('Homo Deus: breve historia del mañana',    5,  6, 496, 22.90, '2024-09-05', '2024-11-15', 4),
('Código limpio',                           6,  7, 464, 39.90, '2025-01-10', '2025-03-30', 5),
('El programador pragmático',               7,  7, 352, 42.00, '2025-02-14', NULL,        NULL),
('Harry Potter y la piedra filosofal',      8,  8, 256, 15.95, '2024-07-07', '2024-07-20', 4),
('El Señor de los Anillos: La Comunidad del Anillo', 9, 8, 576, 23.95, '2024-10-01', '2024-12-10', 5),
('El hobbit',                               9,  8, 320, 14.95, '2024-08-15', '2024-09-01', 4),
('Fahrenheit 451',                         10,  2, 192, 10.95, '2025-03-05', '2025-03-18', 4),
('Hábitos atómicos',                       11,  9, 336, 19.90, '2025-01-02', '2025-01-28', 4),
('Padre rico, padre pobre',                12, 10, 272, 16.90, '2025-04-11', '2025-05-02', 3),
('El alquimista',                          13,  1, 192, 12.90, '2025-05-20', '2025-05-30', 3),
('Ensayo sobre la ceguera',                14,  1, 432, 20.90, '2025-07-01', '2025-08-14', 5),
('La sombra del viento',                   15,  1, 576, 21.90, '2025-09-10', NULL,        NULL),
('Dom Casmurro',                           16,  3, 256, 11.50, '2026-01-08', '2026-02-20', 4);
