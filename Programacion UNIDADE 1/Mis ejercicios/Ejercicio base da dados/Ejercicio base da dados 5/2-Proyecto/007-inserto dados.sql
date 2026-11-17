INSERT INTO medicos (nombre, especialidad, activo) VALUES
('Lucía Fernández', 'Pediatría', 1),
('Javier Moreno', 'Cardiología', 1),
('Carmen López', 'Dermatología', 1),
('Pablo Martínez', 'Neurología', 0);

-- Espacios y mayúsculas a propósito: el disparador los limpia

INSERT INTO pacientes (nombre, email, fecha_nacimiento) VALUES
('Carlos Ruiz', 'CARLOS.RUIZ@EJEMPLO.COM', '1990-04-12'),
('Ana López', 'ana.lopez@ejemplo.com', '1985-09-30'),
('Marta Gil', 'marta.gil@ejemplo.com', '2001-01-15');

-- Cita en el pasado, insertada a mano (sin el procedimiento) para que el evento la caduque

INSERT INTO citas (medico_id, paciente_id, fecha) VALUES (2, 3, '2026-11-10 09:00:00');