*Resultado de aprendizaje*

**a) ¿Se han identificado los conceptos de herencia, superclase y subclase?**
Sí. En `011-herencia.py`, `Pedido` es la superclase y `PedidoUrgente` es la subclase que hereda de ella.

**b) ¿Se han utilizado modificadores para bloquear y forzar la herencia de clases y métodos?**
Sí. Con `ABC` y `@abstractmethod` obligo a heredar de `Documento`, y con `@final` bloqueo la clase `PedidoUrgente`.

**c) ¿Se ha reconocido la incidencia de los constructores en la herencia?**
Sí. El constructor es `__init__`. En `PedidoUrgente` uso `super().__init__()` para usar el constructor del padre y luego añado el envío.

**d) ¿Se han creado clases heredadas que sobrescriben la implementación de métodos de la superclase?**
Sí. `PedidoUrgente` cambia el método `mostrar()` de `Pedido`.

**e) ¿Se han diseñado y aplicado jerarquías de clases?**
Sí. Con herencia: `Documento` → `Pedido` → `PedidoUrgente`. Y con composición: un `Pedido` tiene un `Cliente` y varios `Producto`.

**f) ¿Se han probado y depurado las jerarquías de clases?**
Sí. Lo hice paso a paso y fui corrigiendo errores, como cuando me faltaba `self.`.

**g) ¿Se han realizado programas que implementen y utilicen jerarquías de clases?**
Sí. Creo un pedido y lo guardo en JSON (Create), y luego lo leo (Read). También creo pedidos normales y urgentes.

**h) ¿Se ha comentado y documentado el código?**
Sí. Todos los archivos tienen comentarios y nombres claros por pasos.

**i) ¿Se han identificado y evaluado los escenarios de uso de interfaces?**
Sí. `Documento` funciona como una interfaz: obliga a las clases hijas a tener el método `mostrar()`.

**j) ¿Se han identificado y evaluado los escenarios de utilización de la herencia y la composición?**
Sí. Uso herencia cuando algo "es un" tipo de otra cosa (un pedido urgente es un pedido) y composición cuando algo "tiene" otra cosa (un pedido tiene un cliente).