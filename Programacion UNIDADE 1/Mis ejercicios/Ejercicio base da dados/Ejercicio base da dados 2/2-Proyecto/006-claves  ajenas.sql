CREATE TABLE `meta de kilómetros` (
    Identificador INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100),
    kilometros DECIMAL(10,2),
    PRIMARY KEY (Identificador)
);

ALTER TABLE meta de kilómetros
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

CREATE TABLE `día que practicó` (
    fecha DATE,
);

ALTER TABLE día que practicó
ADD Identificador INT AUTO_INCREMENT PRIMARY KEY;

