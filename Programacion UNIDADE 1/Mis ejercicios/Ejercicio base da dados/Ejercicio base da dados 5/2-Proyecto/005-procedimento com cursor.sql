CREATE PROCEDURE generar_informe()
BEGIN
  DECLARE fin INT DEFAULT 0;
  DECLARE v_id INT;
  DECLARE v_nombre VARCHAR(100);
  DECLARE v_pend INT;

  DECLARE cur CURSOR FOR
    SELECT id, nombre FROM medicos WHERE activo = 1;

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = 1;

  DELETE FROM informe_medicos;

  OPEN cur;
  bucle: LOOP
    FETCH cur INTO v_id, v_nombre;
    IF fin = 1 THEN
      LEAVE bucle;
    END IF;

    SET v_pend = citas_pendientes(v_id);

    INSERT INTO informe_medicos (medico, pendientes, carga)
    VALUES (v_nombre, v_pend,
      CASE
        WHEN v_pend = 0 THEN 'libre'
        WHEN v_pend <= 2 THEN 'normal'
        ELSE 'saturado'
      END);
  END LOOP;
  CLOSE cur;

  SELECT * FROM informe_medicos;
END //