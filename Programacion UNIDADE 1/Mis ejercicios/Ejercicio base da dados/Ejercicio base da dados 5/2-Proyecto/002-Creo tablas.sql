CREATE TABLE medicos (                    --crear tabla medicos
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  especialidad VARCHAR(100) NOT NULL,
  activo TINYINT NOT NULL DEFAULT 1
);

CREATE TABLE pacientes (                  --crear tabla pacientes
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  fecha_nacimiento DATE NOT NULL
);

CREATE TABLE citas (                      --crear tabla citas
  id INT PRIMARY KEY AUTO_INCREMENT,
  medico_id INT NOT NULL,
  paciente_id INT NOT NULL,
  fecha DATETIME NOT NULL,
  estado ENUM('pendiente','realizada','cancelada','caducada') NOT NULL DEFAULT 'pendiente',
  FOREIGN KEY (medico_id) REFERENCES medicos(id),
  FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

CREATE TABLE registro (                   --rellenan los disparadores
  id INT PRIMARY KEY AUTO_INCREMENT,
  accion VARCHAR(255) NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE informe_medicos (            --rellena el procedimiento con cursor
  medico VARCHAR(100),
  pendientes INT,
  carga VARCHAR(20),
  generado DATETIME DEFAULT CURRENT_TIMESTAMP
);