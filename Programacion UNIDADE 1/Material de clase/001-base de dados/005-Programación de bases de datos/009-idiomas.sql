CREATE TABLE idiomas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  idioma VARCHAR(100),
  nivel VARCHAR(100)
);

INSERT INTO idiomas VALUES
  (NULL, 1, 'Portugués', 'Lengua materna'),
  (NULL, 1, 'Español', 'Básico (en estudio)'),
  (NULL, 1, 'Inglés', 'Básico');

  SELECT * FROM idiomas;