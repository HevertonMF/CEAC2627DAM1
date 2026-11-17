SET GLOBAL event_scheduler = ON;   -- viene apagado por defecto

-- Cada día, marca como caducadas las citas pendientes que ya pasaron

CREATE EVENT caducar_citas
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO
  UPDATE citas
  SET estado = 'caducada'
  WHERE estado = 'pendiente' AND fecha < NOW();

-- Cada semana, regenera el informe de médicos

CREATE EVENT informe_semanal
ON SCHEDULE EVERY 1 WEEK
DO
  CALL generar_informe();