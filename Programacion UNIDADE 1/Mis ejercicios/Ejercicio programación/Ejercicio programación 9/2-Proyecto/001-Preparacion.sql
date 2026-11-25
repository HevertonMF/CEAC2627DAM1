sudo mysql -u root -p

CREATE DATABASE tiendabicicletas;

USE tiendabicicletas;

CREATE TABLE bicicletas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  precio DECIMAL(7,2)
);
