-- Procedimiento: casos correctos

CALL nueva_cita(1, 1, '2026-12-01 10:00:00');
CALL nueva_cita(1, 2, '2026-12-01 11:00:00');
CALL nueva_cita(1, 3, '2026-12-02 09:30:00');
CALL nueva_cita(2, 1, '2026-12-03 17:00:00');

-- Procedimiento: excepciones

CALL nueva_cita(4, 1, '2026-12-03 17:00:00');   -- SIGNAL: médico no activo
CALL nueva_cita(2, 2, '2026-01-01 10:00:00');   -- SIGNAL: fecha pasada
CALL nueva_cita(1, 99, '2026-12-03 17:00:00');  -- HANDLER: paciente no existe

-- Disparador BEFORE: email no válido

INSERT INTO pacientes (nombre, email, fecha_nacimiento)
VALUES ('Prueba', 'correo-malo', '2000-01-01');

-- Funciones

SELECT nombre, email, edad(fecha_nacimiento) AS edad FROM pacientes;
SELECT nombre, citas_pendientes(id) AS pendientes FROM medicos;

-- Cursor

CALL generar_informe();

-- Lo que han hecho los disparadores y el evento

SELECT * FROM citas;
SELECT * FROM registro;

-- Ver todo lo creado

SHOW FUNCTION STATUS WHERE Db = 'clinica';
SHOW PROCEDURE STATUS WHERE Db = 'clinica';
SHOW TRIGGERS;
SHOW EVENTS;
