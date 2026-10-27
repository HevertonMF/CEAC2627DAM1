-- Entrar en MySQL (XAMPP):
-- C:\xampp\mysql\bin\mysql.exe -u root -p

CREATE DATABASE blogceacdam2627 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE blogceacdam2627;

CREATE TABLE articulos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(255),
  fecha DATE,
  contenido TEXT
) DEFAULT CHARSET=utf8mb4;

INSERT INTO articulos (titulo, fecha, contenido) VALUES
('De Brasil a Valencia: cómo empezó todo', '2026-10-26', 'Soy brasileño y, después de una etapa en Portugal, en julio de 2026 me mudé a Valencia para empezar una nueva etapa personal y profesional.'),
('Mi primer mes estudiando en CEAC Valencia', '2026-10-24', 'Estudio programación y desarrollo web en CEAC, en Burjassot. Cada semana aprendo algo nuevo y ya empiezo a construir mis primeras páginas.'),
('De la administración al código', '2026-10-22', 'Vengo del mundo de la administración y la organización de procesos. Esa experiencia me ayuda mucho a planificar proyectos y a escribir código ordenado.'),
('Qué es HTML y por qué es la base de todo', '2026-10-20', 'HTML define la estructura de una página web. Aprender bien etiquetas como article, header o section es el primer paso para crear sitios claros y accesibles.'),
('CSS: dar estilo a mis páginas', '2026-10-18', 'Con CSS he descubierto que una misma página puede cambiar por completo. Colores, tipografías y márgenes marcan la diferencia en la experiencia del usuario.'),
('Mis primeros pasos con JavaScript', '2026-10-16', 'JavaScript es lo que hace que una web cobre vida. Estoy practicando con variables, funciones y eventos para crear páginas más interactivas.'),
('Nuestro proyecto: conectar psicólogos y pacientes', '2026-10-14', 'Estoy desarrollando una plataforma que ayuda a las personas a encontrar un psicólogo de forma sencilla y que da visibilidad a los profesionales de Valencia.'),
('Paso 1 del proyecto: investigar el sector', '2026-10-12', 'Antes de programar, estoy analizando empresas y plataformas que ya existen en el sector para entender qué funciona y qué puedo mejorar.'),
('Organizar un proyecto por pasos', '2026-10-10', 'Dividir un proyecto grande en pasos pequeños me permite avanzar sin perderme. Es algo que aprendí en administración y que aplico ahora al desarrollo web.'),
('Montar en bici por Valencia', '2026-10-08', 'El ciclismo es una de mis aficiones. Valencia es perfecta para la bici: es llana, tiene muchos carriles bici y rutas preciosas como el antiguo cauce del Turia.'),
('La bici como descanso para la mente', '2026-10-06', 'Después de horas delante del ordenador, salir a pedalear me ayuda a desconectar y a volver a programar con la cabeza más clara.'),
('Mi ordenador para programar y crear juegos', '2026-10-04', 'Trabajo con un Intel Core i5-10400F y una NVIDIA GeForce GTX 1660 SUPER, un equipo que me permite programar y probar herramientas como Unity y Godot.'),
('Por qué me interesa el desarrollo de videojuegos', '2026-10-02', 'Los videojuegos combinan programación, diseño y creatividad. Me gustaría explorar motores como Godot y Unity para crear mis propios juegos.'),
('Aprender idiomas mientras aprendo a programar', '2026-09-30', 'Mi lengua materna es el portugués. Ahora tomo clases de español y de inglés, porque ambos idiomas son clave para trabajar en tecnología.'),
('El inglés en la programación', '2026-09-28', 'Casi toda la documentación técnica está en inglés. Estudiar el idioma me ayuda a entender mejor los errores, los tutoriales y las herramientas que uso.'),
('Vivir en Valencia como estudiante', '2026-09-26', 'Valencia ofrece buen clima, playa y una vida tranquila. Es una ciudad ideal para estudiar y empezar de nuevo.'),
('Lo que aprendí de vivir en Portugal', '2026-09-24', 'Mi etapa en Portugal me enseñó a adaptarme a nuevos lugares y culturas, algo que me ha ayudado mucho en mi llegada a España.'),
('Herramientas que uso cada día', '2026-09-22', 'Mi día a día como estudiante incluye un editor de código, el navegador con sus herramientas de desarrollo y, cada vez más, Git para guardar mis proyectos.'),
('Errores que cometo al programar (y cómo los soluciono)', '2026-09-20', 'Olvidar cerrar una etiqueta o escribir mal una clase son errores comunes. Leer el código con calma y usar la consola del navegador me ayuda a encontrarlos.'),
('Mis objetivos para el próximo año', '2026-09-18', 'Quiero terminar mi formación, lanzar la plataforma de psicólogos, mejorar mi inglés y, quién sabe, publicar mi primer videojuego.');

-- Usuario de la base de datos para la web

CREATE USER 'blogceacdam2627'@'localhost' IDENTIFIED BY 'CEAC123$';

GRANT ALL PRIVILEGES ON blogceacdam2627.* TO 'blogceacdam2627'@'localhost';

FLUSH PRIVILEGES;
