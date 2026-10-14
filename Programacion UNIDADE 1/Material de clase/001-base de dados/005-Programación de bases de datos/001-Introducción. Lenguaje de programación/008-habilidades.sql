CREATE TABLE habilidades(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  habilidades VARCHAR(100) 
);

INSERT INTO habilidades VALUES
  (NULL, 1, 'Python, Java'),
  (NULL, 1, 'SQL (MySQL, MariaDB)'),
  (NULL, 1, 'HTML, CSS, JavaScript, XML'),
  (NULL, 1, 'Git, GitHub y Linux'),
  (NULL, 1, 'SAP'),
  (NULL, 1, 'Responsabilidad en el trabajo'),
  (NULL, 1, 'Trabajo en equipo'),
  (NULL, 1, 'Comunicación'),
  (NULL, 1, 'Resolución de problemas'),
  (NULL, 1, 'Organización y puntualidad'),
  (NULL, 1, 'Permiso de conducción B');

  SELECT * FROM habilidades;