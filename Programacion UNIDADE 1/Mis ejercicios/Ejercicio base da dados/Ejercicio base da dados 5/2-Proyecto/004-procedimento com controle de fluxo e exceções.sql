CREATE PROCEDURE nueva_cita(
  IN p_medico INT,
  IN p_paciente INT,
  IN p_fecha DATETIME
)
BEGIN
  DECLARE v_activo TINYINT;

  -- Capturo el error 1452 (el paciente no existe)
  DECLARE EXIT HANDLER FOR 1452
  BEGIN
    SELECT 'Error: el paciente no existe' AS mensaje;
  END;

  SELECT activo INTO v_activo FROM medicos WHERE id = p_medico;

  IF v_activo IS NULL THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El médico no existe';
  ELSEIF v_activo = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El médico no está activo';
  ELSEIF p_fecha <= NOW() THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La fecha de la cita ya ha pasado';
  ELSE
    INSERT INTO citas (medico_id, paciente_id, fecha)
    VALUES (p_medico, p_paciente, p_fecha);
    SELECT CONCAT('Cita creada con id ', LAST_INSERT_ID()) AS mensaje;
  END IF;
END //