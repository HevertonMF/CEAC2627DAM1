USE ciudades;

INSERT INTO paises (nombre) VALUES
("Brasil"),
("Argentina"),
("España"),
("Portugal"),
("Japón");

-- Le pongo a cada ciudad el id de su país
UPDATE ciudades SET pais_id = 1 WHERE país = "Brasil";
UPDATE ciudades SET pais_id = 2 WHERE país = "Argentina";
UPDATE ciudades SET pais_id = 3 WHERE país = "España";
UPDATE ciudades SET pais_id = 4 WHERE país = "Portugal";
UPDATE ciudades SET pais_id = 5 WHERE país = "Japón";

SELECT * FROM paises;
SELECT * FROM ciudades;
