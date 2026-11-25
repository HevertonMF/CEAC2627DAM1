# Preguntas sobre la aplicación de ciclistas

**a) Se ha reconocido la sintaxis, estructura y componentes típicos de una clase.**

Sí. Una clase es como un molde. Se escribe con `class`, y dentro tiene un `__init__` donde se guardan los datos y otras funciones que hacen cosas.

**b) Se han definido clases.**

Sí. He hecho dos: `Persona` y `Ciclista`.

**c) Se han definido propiedades y métodos.**

Sí. Las propiedades son los datos del ciclista: nombre, apellidos, email, equipo y bicicleta. Los métodos son las cosas que sabe hacer, como `mostrar()`, que enseña sus datos por pantalla.

**d) Se han creado constructores.**

Sí. El constructor es el `__init__`, que se ejecuta al crear un ciclista y guarda sus datos.

**e) Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente.**

Sí. Cuando el usuario mete los datos, creo un ciclista nuevo y lo guardo en una lista. Después lo puedo ver, cambiar o borrar.

**f) Se han utilizado mecanismos para controlar la visibilidad de las clases y de sus miembros.**

Sí. El email es privado (`__email`), así que no se puede tocar directamente desde fuera. Para verlo uso `get_email()` y para cambiarlo uso `set_email()`, que antes comprueba que el email esté bien.

**g) Se han definido y utilizado clases heredadas.**

Sí. `Ciclista` hereda de `Persona`, así que coge el nombre, los apellidos y el email sin tener que escribirlos otra vez. Además le añado el equipo y la bicicleta.

**h) Se han creado y utilizado métodos estáticos.**

Sí. `validar_email()` es estático, o sea, se puede usar sin tener un ciclista creado. Lo uso para comprobar que el email tenga `@` y `.`.

**i) Se han creado y utilizado conjuntos y librerías de clases.**

Sí. He puesto las clases en un archivo aparte, `001-Clases.py`, que funciona como mi librería, y en el programa principal la cargo con `importlib.import_module("001-Clases")`. Además guardo todos los ciclistas juntos en una lista.
