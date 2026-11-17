# Criterios de evaluación

**a) Se han identificado las diversas formas de automatizar tareas.**
Se pueden automatizar con guiones, procedimientos, funciones, disparadores y eventos.

**b) Se han reconocido los métodos de ejecución de guiones.**
Los he ejecutado desde phpMyAdmin, desde la consola con `mysql -u root -p < archivo.sql` y desde DB Browser.

**c) Se han identificado las herramientas disponibles para editar guiones.**
He usado VS Code, phpMyAdmin y DB Browser for SQLite.

**d) Se han definido y utilizado guiones para automatizar tareas.**
He hecho los guiones del 001 al 009 para crear la base de datos de la clínica paso a paso.

**e) Se ha hecho uso de las funciones proporcionadas por el sistema gestor.**
He usado NOW, CURDATE, CONCAT, TRIM, LOWER, COUNT y DATE_FORMAT.

**f) Se han definido procedimientos y funciones de usuario.**
He creado las funciones `edad` y `citas_pendientes` y los procedimientos `nueva_cita` y `generar_informe`.

**g) Se han utilizado estructuras de control de flujo.**
He usado IF, ELSEIF, CASE y LOOP.

**h) Se han definido eventos y disparadores.**
He hecho disparadores que validan el email, limpian los datos y guardan un registro de las citas. También un evento que caduca las citas pasadas cada día.

**i) Se han utilizado cursores.**
He usado un cursor en `generar_informe` para recorrer los médicos uno a uno.

**j) Se han utilizado excepciones.**
He lanzado errores con SIGNAL y los he capturado con DECLARE HANDLER.
