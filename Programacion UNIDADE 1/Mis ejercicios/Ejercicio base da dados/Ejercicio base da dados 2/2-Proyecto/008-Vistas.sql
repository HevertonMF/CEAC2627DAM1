SELECT 
    c.nombre,
    c.apellidos,
    c.fecha_de_nacimiento,
    c.email,
    c.telefono,
    c.Identificador,
    dp.fecha AS 'día que practicó',
    mk.kilometros AS 'meta de kilómetros'
FROM ciclistas AS c
LEFT JOIN `día que practicó` AS dp ON c.Identificador = dp.ciclista_id
LEFT JOIN `meta de kilómetros` AS mk ON c.nombre = mk.nombre;
