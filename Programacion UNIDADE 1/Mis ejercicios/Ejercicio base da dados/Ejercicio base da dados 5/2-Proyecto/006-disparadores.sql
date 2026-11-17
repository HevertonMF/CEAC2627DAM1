--Limpia y valida los datos del paciente antes de guardarlos

CREATE TRIGGER antes_insertar_paciente
BEFORE INSERT ON pacientes
FOR EACH ROW
BEGIN
  SET NEW.nombre = TRIM(NEW.nombre);
  SET NEW.email = LOWER(TRIM(NEW.email));
  IF NEW.email NOT LIKE '%_@_%._%' THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Email no válido';
  END IF;
END //

--Anota cada cita nueva 

CREATE TRIGGER despues_insertar_cita
AFTER INSERT ON citas
FOR EACH ROW
BEGIN
  INSERT INTO registro (accion)
  VALUES (CONCAT('Nueva cita ', NEW.id, ' el ', DATE_FORMAT(NEW.fecha, '%d/%m/%Y %H:%i')));
END //

--Anota cada cambio de estado de una cita

CREATE TRIGGER despues_cambiar_cita
AFTER UPDATE ON citas
FOR EACH ROW
BEGIN
  IF OLD.estado <> NEW.estado THEN
    INSERT INTO registro (accion)
    VALUES (CONCAT('Cita ', NEW.id, ': ', OLD.estado, ' -> ', NEW.estado));
  END IF;
END //

DELIMITER ;