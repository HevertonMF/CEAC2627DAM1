CREATE TABLE experiencias_laborales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  empresa VARCHAR(100),
  descripcion TEXT,
  cargo VARCHAR(100),
  inicio VARCHAR(100),
  final VARCHAR(100)
);

INSERT INTO experiencias_laborales VALUES
  (NULL, 1, 'Bourbon Automotive Plastics (Portugal)', 'Abastecer la línea de producción, control de stock y movimientos de inventario en SAP, conducción de carretillas elevadoras.', 'Operario de logística de almacén', '22/08/2022', '06/06/2025'),
  (NULL, 1, 'Movelog Serviços Logísticos - AMBEV (Brasil)', 'Control de recepción de carga de proveedores en el área de logística.', 'Receptor de materia prima', '14/02/2020', '03/06/2022'),
  (NULL, 1, 'Petrolub (Brasil)', 'Hojas de cálculo de control, pago y jornada de conductores, seguimiento de flota, control de rutas y solicitudes de mantenimiento.', 'Empleado administrativo', '07/10/2016', '27/09/2019'),
  (NULL, 1, 'Iveco (Brasil)', 'Contacto con proveedores y resolución de problemas de calidad. Registros en CLICK, SAP y SQP.', 'Inspector de control de calidad', '02/02/2015', '31/08/2015'),
  (NULL, 1, 'Iveco (Brasil)', 'Programación de empleados, registros en general, traslados de empleados y tareas diarias de oficina.', 'Empleado administrativo', '07/11/2011', '30/01/2015');

SELECT * FROM experiencias_laborales;