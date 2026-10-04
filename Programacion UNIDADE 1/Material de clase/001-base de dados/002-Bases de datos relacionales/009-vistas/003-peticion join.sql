SELECT 
Pedidos.fecha,
Pedidos.numero_de_pedido,
Clientes.nombre,
Clientes.apellidos,
Productos.nombre
FROM Pedidos
LEFT JOIN Clientes ON Pedidos.cliente_id = Clientes.Identificador
LEFT JOIN Productos ON Pedidos.producto_id = Clientes.Identificador;


SELECT 
Pedidos.fecha,
Pedidos.numero_de_pedido,
Clientes.nombre AS 'nombre del cliente',
Clientes.apellidos,
Productos.nombre AS 'nombre del producto'
FROM Pedidos
LEFT JOIN Clientes ON Pedidos.cliente_id = Clientes.Identificador
LEFT JOIN Productos ON Pedidos.producto_id = Clientes.Identificador;


SELECT 
Pedidos.fecha,
Pedidos.numero_de_pedido,
Clientes.Nombre AS 'nombre del cliente',
Clientes.Apellidos,
Pedidos.telefono,
Pedidos.email,
Productos.nombre AS 'nombre del producto',
Productos.precio
FROM Pedidos
LEFT JOIN Clientes ON Pedidos.cliente_id = Clientes.Identificador
LEFT JOIN Productos ON Pedidos.producto_id = Productos.Identificador;

