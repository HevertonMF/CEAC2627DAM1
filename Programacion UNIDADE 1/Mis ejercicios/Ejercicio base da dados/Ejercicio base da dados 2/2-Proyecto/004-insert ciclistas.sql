ALTER TABLE ciclistas
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

DESCRIBE ciclistas;

INSERT INTO ciclistas VALUES(
	'Heverton',
  'Marques Ferreira',
  '1991-02-08', '662353018', 'hevertonmf@gmail.com', NULL);
  
SELECT * FROM ciclistas;

