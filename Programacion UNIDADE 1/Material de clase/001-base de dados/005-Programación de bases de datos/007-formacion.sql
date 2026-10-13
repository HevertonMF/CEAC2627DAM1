CREATE TABLE formacion(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  centro VARCHAR(100),
  descripcion TEXT,
  titulo VARCHAR(100),
  inicio VARCHAR(100),
  final VARCHAR(100)
);

INSERT INTO formacion VALUES
  (NULL, 1, 'Centro CEAC de Formación Profesional (España)', 'Ciclo Formativo de Grado Superior. Nivel MEC 5.', 'Desarrollo de Aplicaciones Multiplataforma (DAM)', '09/09/2026', 'Actual'),
  (NULL, 1, 'UNIFEMM (Brasil)', 'Grado universitario.', 'Grado en Administración', NULL, NULL),
  (NULL, 1, 'Escola Estadual Cel. Domingues Diniz Couto (Brasil)', 'Nivel MEC 4.', 'Bachillerato', NULL, '15/12/2009');

  SELECT * FROM formacion;