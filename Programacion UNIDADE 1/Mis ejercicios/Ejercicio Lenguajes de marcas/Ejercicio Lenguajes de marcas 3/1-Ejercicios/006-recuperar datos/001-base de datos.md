sudo mysql -u root -p

CREATE DATABASE encuentrame;

USE encuentrame;

CREATE TABLE facultativos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100),
  n_colegiado VARCHAR(100)
);

CREATE TABLE psicologos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  telefono VARCHAR(30),
  especialidades VARCHAR(255),
  bio TEXT,
  password_hash VARCHAR(255),
  foto VARCHAR(255),
  fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pacientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  telefono VARCHAR(30),
  fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE especialidades(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE psicologo_especialidad(
	psicologo_id INT NOT NULL,
  especialidad_id INT NOT NULL,
  PRIMARY KEY (psicologo_id, especialidad_id),
  FOREIGN KEY (psicologo_id) REFERENCES psicologos(id) ON DELETE CASCADE,
  FOREIGN KEY (especialidad_id) REFERENCES especialidades(id) ON DELETE CASCADE
);

CREATE TABLE solicitudes(
	id INT PRIMARY KEY AUTO_INCREMENT,
  psicologo_id INT NOT NULL,
  paciente_id INT,
  nombre_paciente VARCHAR(100) NOT NULL,
  email_paciente VARCHAR(150) NOT NULL,
  telefono VARCHAR(30),
  resumen TEXT NOT NULL,
  contacto ENUM('email','telefono') DEFAULT 'email',
  estado ENUM('pendiente','contactado') DEFAULT 'pendiente',
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (psicologo_id) REFERENCES psicologos(id) ON DELETE CASCADE,
  FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE SET NULL
);