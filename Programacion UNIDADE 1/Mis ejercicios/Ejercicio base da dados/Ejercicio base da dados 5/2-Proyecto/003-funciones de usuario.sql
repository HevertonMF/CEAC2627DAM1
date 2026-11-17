DELIMITER //



CREATE FUNCTION edad(p_fecha DATE)                           --Crea edad a partir de la fecha de nacimiento
NO SQL
BEGIN
  RETURN TIMESTAMPDIFF(YEAR, p_fecha, CURDATE());
END //


CREATE FUNCTION citas_pendientes(p_medico INT) RETURNS INT   --Número de citas pendientes de un médico
READS SQL DATA
BEGIN
  DECLARE total INT;
  SELECT COUNT(*) INTO total
  FROM citas
  WHERE medico_id = p_medico AND estado = 'pendiente';
  RETURN total;
END //