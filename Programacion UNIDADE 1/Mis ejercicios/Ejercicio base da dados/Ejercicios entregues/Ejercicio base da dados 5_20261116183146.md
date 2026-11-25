# Reporte de proyecto

## Información de generación

- **Fecha:** 16/11/2026, 19:31:08
- **Proyecto documentado:** `Ejercicio base da dados 5`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio base da dados 5
    ├── 1-Ejercicios
    │   ├── 001-Introducción. Lenguaje de programación
    │   │   ├── 001-nos conectamos.sql
    │   │   ├── 002-datos personales.sql
    │   │   ├── 003-insertamos.sql
    │   │   ├── 004-datos de contacto.sql
    │   │   ├── 005-redes sociales.sql
    │   │   ├── 006-experiencias laborales.sql
    │   │   ├── 006-plantilla.html
    │   │   ├── 007-css.htm
    │   │   ├── 007-formacion.sql
    │   │   ├── 008-dos columnas.html
    │   │   ├── 008-habilidades.sql
    │   │   ├── 009-idiomas.sql
    │   │   ├── 009-meto imagen.html
    │   │   ├── 010-titulos.html
    │   │   ├── 011-secciones y articulos.html
    │   │   └── heverton.png
    │   ├── 002-Variables del sistema y variables de usuario
    │   │   ├── 001-cargocurriculum.py
    │   │   ├── 002-usuario para conectar.sql
    │   │   ├── static
    │   │   │   └── heverton.png
    │   │   └── templates
    │   │       └── curriculum.html
    │   ├── 003-Funciones
    │   │   ├── 001-SQLite.md
    │   │   ├── 002-crear tabla.sql
    │   │   ├── 003-me conecto desde python.py
    │   │   ├── 004-lo quiero como diccionario.py
    │   │   └── empresa.db [SQLite]
    │   ├── 004-Estructuras de control de flujo
    │   │   ├── 001-Introduccion.nd
    │   │   ├── 002-prompt para ia.md
    │   │   ├── 003-me conecto desde python.py
    │   │   ├── 004-ahora le pongo flask.py
    │   │   ├── blog.db [SQLite]
    │   │   ├── static
    │   │   │   └── estilo.css
    │   │   └── templates
    │   │       └── frente.html
    │   ├── 005-Procedimientos almacenados. Funciones de usuario
    │   │   ├── 001-resumen.md
    │   │   ├── 002-comentarios.sql
    │   │   ├── 003-crear base de datos.sql
    │   │   ├── 004-condicional sencillo.sql
    │   │   ├── 005-mas elaborado.sql
    │   │   ├── 006-Select.sql
    │   │   ├── 007-exixten funciones.sql
    │   │   └── 008-mi procedimiento almacenado.sql
    │   └── 006-Eventos y disparadores
    │       ├── 001-disparador.sql
    │       ├── 002-clientescopiadeseguridad.sql
    │       └── 003-creo evento.sql
    ├── 2-Proyecto
    │   ├── 001-Creo una base de dados.sql
    │   ├── 002-Creo tablas.sql
    │   ├── 003-funciones de usuario.sql
    │   ├── 004-procedimento com controle de fluxo e exceções.sql
    │   ├── 005-procedimento com cursor.sql
    │   ├── 006-disparadores.sql
    │   ├── 007-inserto dados.sql
    │   ├── 008-eventos.sql
    │   ├── 009-lo pruebo todo.sql
    │   └── clinica.db [SQLite]
    └── 3-Resultado de aprendizaje
        └── 001-criterios de evaluacion.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

### Ejercicio base da dados 5/2-Proyecto/clinica.db

```text
Ejercicio base da dados 5/2-Proyecto/clinica.db
├── tabla citas
│   ├── columnas
│   │   ├── id INTEGER PRIMARY KEY
│   │   ├── medico_id INTEGER NOT NULL
│   │   ├── paciente_id INTEGER NOT NULL
│   │   ├── fecha TEXT NOT NULL
│   │   └── estado TEXT NOT NULL DEFAULT 'pendiente'
│   └── claves foráneas
│       ├── paciente_id → pacientes.id (ON UPDATE NO ACTION, ON DELETE NO ACTION)
│       └── medico_id → medicos.id (ON UPDATE NO ACTION, ON DELETE NO ACTION)
├── tabla medicos
│   └── columnas
│       ├── id INTEGER PRIMARY KEY
│       ├── nombre TEXT NOT NULL
│       ├── especialidad TEXT NOT NULL
│       └── activo INTEGER NOT NULL DEFAULT 1
├── tabla pacientes
│   ├── columnas
│   │   ├── id INTEGER PRIMARY KEY
│   │   ├── nombre TEXT NOT NULL
│   │   ├── email TEXT NOT NULL
│   │   └── fecha_nacimiento TEXT NOT NULL
│   └── índices
│       └── sqlite_autoindex_pacientes_1 (UNIQUE): email
├── tabla registro
│   └── columnas
│       ├── id INTEGER PRIMARY KEY
│       ├── accion TEXT NOT NULL
│       └── fecha TEXT DEFAULT datetime('now','localtime')
└── vista informe_medicos
    └── SQL: CREATE VIEW "informe_medicos" AS SELECT m."nombre" AS medico, m."especialidad", COUNT(c."id") AS pendientes, CASE WHEN COUNT(c."id") = 0 THEN 'libre' WHEN COUNT(c."id") <= 2 THEN 'normal' ELSE 'saturado' END AS carga FROM "medicos" m LEFT JOIN "citas" c ON c."medico_id" = m."id" AND c."estado" = 'pendiente' WHERE m."activo" = 1 GROUP BY m."id"
```

### Ejercicio base da dados 5/1-Ejercicios/004-Estructuras de control de flujo/blog.db

```text
Ejercicio base da dados 5/1-Ejercicios/004-Estructuras de control de flujo/blog.db
└── tabla articulos
    └── columnas
        ├── id INTEGER PRIMARY KEY
        ├── titulo TEXT
        ├── fecha TEXT
        └── contenido TEXT
```

### Ejercicio base da dados 5/1-Ejercicios/003-Funciones/empresa.db

```text
Ejercicio base da dados 5/1-Ejercicios/003-Funciones/empresa.db
└── tabla clientes
    └── columnas
        ├── id INTEGER PRIMARY KEY
        ├── nombre TEXT
        ├── apellidos TEXT
        └── email TEXT
```

## Código (intercalado)

### Ejercicio base da dados 5/1-Ejercicios/001-Introducción. Lenguaje de programación

**001-nos conectamos.sql**

```sql
C:\xampp\mysql\bin\mysql.exe -u root -p
```

**002-datos personales.sql**

```sql
CREATE TABLE datos_personales(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  apellidos VARCHAR(100),
  ubicacion VARCHAR(100)
);

CREATE TABLE datos_contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  email VARCHAR(100),
  telefono VARCHAR(100)
);

CREATE TABLE redes_sociales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  linkedin VARCHAR(100),
  facebook VARCHAR(100),
  instagram VARCHAR(100),
  github VARCHAR(100)
);

CREATE TABLE experiencias_laborales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  empresa VARCHAR(100),
  descripcion TEXT,
  cargo VARCHAR(100),
  inicio VARCHAR(100),
  final VARCHAR(100)
);

CREATE TABLE formacion(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  centro VARCHAR(100),
  descripcion TEXT,
  titulo VARCHAR(100),
  inicio VARCHAR(100),
  final VARCHAR(100)
);

CREATE TABLE habilidades(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  habilidades VARCHAR(100) 
);

CREATE TABLE idiomas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  idioma VARCHAR(100),
  nivel VARCHAR(100)
);
```

**003-insertamos.sql**

```sql
CREATE TABLE datos_personales(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
  apellidos VARCHAR(100),
  ubicacion VARCHAR(100)
);

INSERT INTO datos_personales VALUES(
	NULL,
  'Heverton',
  'Marques Ferreira Maciel',
  'Canet d en Berenguer, Valencia, España'
);

SELECT * FROM datos_personales;
```

**004-datos de contacto.sql**

```sql
CREATE TABLE datos_contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  email VARCHAR(100),
  telefono VARCHAR(100)
);

INSERT INTO datos_contacto VALUES(
	NULL,
  1,
  'hevertonmf@gmail.com',
  '662353018'
);

SELECT * FROM datos_contacto;
```

**005-redes sociales.sql**

```sql
CREATE TABLE redes_sociales(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  linkedin VARCHAR(100),
  facebook VARCHAR(100),
  instagram VARCHAR(100),
  github VARCHAR(100)
);

INSERT INTO redes_sociales VALUES(
	NULL,
  1,
  "https://www.linkedin.com/in/heverton-marques-00a569196/",
  "https://facebook.com/hevertonmf",
  "https://www.instagram.com/heverton_marques",
  "https://github.com/HevertonMF"
);

SELECT * FROM redes_sociales;
```

**006-experiencias laborales.sql**

```sql
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
```

**006-plantilla.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
  </head>
  <body>
    <main>
    </main>
  </body>
</html>
```

**007-formacion.sql**

```sql
CREATE TABLE formacion(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  centro VARCHAR(100),
  descripcion TEXT,
  titulo VARCHAR(100),
  inicio VARCHAR(100),
  final VARCHAR(100)
);

INSERT INTO formacion VALUES
  (NULL, 1, 'Centro CEAC de Formación Profesional (España)', 'Ciclo Formativo de Grado Superior. Nivel MEC 5.', 'Desarrollo de Aplicaciones Multiplataforma (DAM)', '09/09/2026', 'Actual'),
  (NULL, 1, 'UNIFEMM (Brasil)', 'Grado universitario.', 'Grado en Administración', NULL, NULL),
  (NULL, 1, 'Escola Estadual Cel. Domingues Diniz Couto (Brasil)', 'Nivel MEC 4.', 'Bachillerato', NULL, '15/12/2009');

  SELECT * FROM formacion;
```

**008-dos columnas.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      main{
        width:210mm;
        height:297mm;
        background:white;
        margin:auto;
        display:flex;
      }
      #izquierda{
      	flex:1;
        background:#7368e6;
        color:white;
      }
      #derecha{
      	flex:3;
      }
    </style>
  </head>
  <body>
    <main>
      <div id="izquierda">
      </div>
      <div id="derecha">
      </div>
    </main>
  </body>
</html>
```

**008-habilidades.sql**

```sql
CREATE TABLE habilidades(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  habilidades VARCHAR(100) 
);

INSERT INTO habilidades VALUES
  (NULL, 1, 'Python, Java'),
  (NULL, 1, 'SQL (MySQL, MariaDB)'),
  (NULL, 1, 'HTML, CSS, JavaScript, XML'),
  (NULL, 1, 'Git, GitHub y Linux'),
  (NULL, 1, 'SAP'),
  (NULL, 1, 'Responsabilidad en el trabajo'),
  (NULL, 1, 'Trabajo en equipo'),
  (NULL, 1, 'Comunicación'),
  (NULL, 1, 'Resolución de problemas'),
  (NULL, 1, 'Organización y puntualidad'),
  (NULL, 1, 'Permiso de conducción B');

  SELECT * FROM habilidades;
```

**009-idiomas.sql**

```sql
CREATE TABLE idiomas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  idioma VARCHAR(100),
  nivel VARCHAR(100)
);

INSERT INTO idiomas VALUES
  (NULL, 1, 'Portugués', 'Lengua materna'),
  (NULL, 1, 'Español', 'Básico (en estudio)'),
  (NULL, 1, 'Inglés', 'Básico');

  SELECT * FROM idiomas;
```

**009-meto imagen.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
    <style>
      body{background:lightsteelblue;}
      main{
        width:210mm;
        height:297mm;
        background:white;
        margin:auto;
        display:flex;
      }
      #izquierda{
      	flex:1;
        background: royalblue;
        ;
        color:white;
      }
      #derecha{
      	flex:3;
      }
    </style>
  </head>
  <body>
    <main>
      <div id="izquierda">
        <img src="heverton.png">
      </div>
      <div id="derecha">
      </div>
    </main>
  </body>
</html>
```

**010-titulos.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
    <style>
      body{background:lightsteelblue;}
      main{
        width:210mm;
        height:297mm;
        background:white;
        margin:auto;
        display:flex;
      }
      #izquierda{
      	flex:1;
        background: royalblue;
        color:white;
        padding:20px;
      }
      #izquierda img{
      	width:100%;
      }
      #derecha{
      	flex:3;
        padding:20px;
      }
      p{
        text-align:justify;
      }
    </style>
  </head>
  <body>
    <main>
      <div id="izquierda">
        <img src="heverton.png">
      </div>
      <div id="derecha">
        <h1>Heverton Marques Ferreira Maciel</h1>
        <h2>Adiministrador, Programador y Estudiante de DAM</h2>
        <p>Mi nombre es Heverton Marques Ferreira Maciel, soy brasileño y tengo 23 años. Actualmente estoy estudiando el ciclo superior de Desarrollo de Aplicaciones Web.</p>
      </div>
    </main>
  </body>
</html>
```

**011-secciones y articulos.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
    <style>
      body{background:lightsteelblue;}
      main{
        width:210mm;
        height:355mm;
        background:white;
        margin:auto;
        display:flex;
      }
      #izquierda{
      	flex:1;
        background: royalblue;
        color:white;
        padding:20px;
      }
      #izquierda img{
      	width:100%;
      }
      #izquierda ul{
        padding-left:18px;
      }
      #izquierda li{
        word-break:break-all;
        margin-bottom:4px;
      }
      #derecha{
      	flex:3;
        padding:20px;
      }
      p{
        text-align:justify;
      }
    </style>
  </head>
  <body>
    <main>
      <div id="izquierda">
        <img src="heverton.png">
        <h3>Contacto</h3>
        <ul>
          <li>hevertonmf@gmail.com</li>
          <li>+34 662353018</li>
          <li>Canet de Berenguer (Valencia)</li>
        </ul>
        <h3>Redes sociales</h3>
        <ul>
          <li>https://www.linkedin.com/in/heverton-marques-00a569196/</li>
          <li>https://github.com/HevertonMF</li>
        </ul>
        <h3>Idiomas</h3>
        <ul>
          <li>Portugués: Lengua materna</li>
          <li>Español: Básico (en estudio)</li>
          <li>Inglés: Básico</li>
        </ul>
        <h3>Conocimientos</h3>
        <ul>
          <li>Python, Java</li>
          <li>SQL (MySQL, MariaDB)</li>
          <li>HTML, CSS, JavaScript, XML</li>
          <li>Git, GitHub y Linux</li>
          <li>SAP</li>
        </ul>
        <h3>Capacidades</h3>
        <ul>
          <li>Responsabilidad en el trabajo</li>
          <li>Trabajo en equipo</li>
          <li>Comunicación</li>
          <li>Resolución de problemas</li>
          <li>Organización y puntualidad</li>
        </ul>
        <h3>Permiso de conducción</h3>
        <ul>
          <li>Permiso B</li>
        </ul>
      </div>
      <div id="derecha">
        <h1>Heverton Marques Ferreira Maciel</h1>
        <h2>Administrador, Programador y Estudiante de DAM</h2>
        <p>Mi nombre es Heverton Marques Ferreira Maciel, soy brasileño y tengo 35 años. Actualmente estoy estudiando el ciclo superior de Desarrollo de Aplicaciones Multiplataforma.</p>
        <section id="experiencia">
          <h3>Experiencia profesional</h3>
        <article>
            <h4>Bourbon Automotive Plastics (Portugal)</h4>
            <p>Desde 2022 hasta 2025</p>
            <p>Abastecer la línea de producción, control de stock y movimientos de inventario en SAP, conducción de carretillas elevadoras.</p>
            <p>Operario de logística de almacén</p>
          </article>
          <article>
            <h4>Movelog Serviços Logísticos - AMBEV (Brasil)</h4>
            <p>Desde 2020 hasta 2022</p>
            <p>Control de recepción de carga de proveedores en el área de logística.</p>
            <p>Receptor de materia prima</p>
          </article>
          <article>
            <h4>Petrolub (Brasil)</h4>
            <p>Desde 2016 hasta 2019</p>
            <p>Hojas de cálculo de control, pago y jornada de conductores, seguimiento de flota, control de rutas y solicitudes de mantenimiento.</p>
            <p>Empleado administrativo</p>
          </article>
          <article>
            <h4>Iveco (Brasil)</h4>
            <p>Desde 2011 hasta 2015</p>
            <p>Programación de empleados, registros y tareas de oficina. Después, contacto con proveedores y resolución de problemas de calidad, con registros en CLICK, SAP y SQP.</p>
            <p>Empleado administrativo / Inspector de control de calidad</p>
          </article>
        </section>
        <section id="formacion">
          <h3>Formación</h3>
          <article>
            <h4>Centro CEAC de Formación Profesional (España)</h4>
            <p>Desde 2026 hasta la actualidad</p>
            <p>Ciclo Formativo de Grado Superior.</p>
            <p>Desarrollo de Aplicaciones Multiplataforma (DAM)</p>
          </article>
          <article>
            <h4>UNIFEMM (Brasil)</h4>
            <p>Grado universitario.</p>
            <p>Grado en Administración</p>
          </article>
          <article>
            <h4>Escola Estadual Cel. Domingues Diniz Couto (Brasil)</h4>
            <p>Hasta 2009</p>
            <p>Bachillerato</p>
          </article>
        </section>
      </div>
    </main>
  </body>
</html>
```

### Ejercicio base da dados 5/1-Ejercicios/002-Variables del sistema y variables de usuario

**001-cargocurriculum.py**

```python
# Primero importo Flask y la librería de conexión
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Función para quedarme solo con el año de una fecha "dd/mm/aaaa"
def anio(fecha):
  if fecha is None:
    return None
  if fecha == "Actual":
    return "la actualidad"
  return fecha[-4:]

@app.route("/")
def inicio():
  # Me conecto a la base de datos con el usuario que hemos creado
  connection = mysql.connector.connect(
    host='localhost',
    user='curriculum',
    password='CEAC123$',
    database='curriculum'
  )

  # Creo un cursor que me devuelve cada fila como diccionario
  cursor = connection.cursor(dictionary=True)

  # Datos personales (solo hay una fila)
  cursor.execute("SELECT * FROM datos_personales WHERE id = 1")
  persona = cursor.fetchone()

  # Datos de contacto
  cursor.execute("SELECT * FROM datos_contacto WHERE id_usuario = 1")
  contacto = cursor.fetchall()

  # Redes sociales
  cursor.execute("SELECT * FROM redes_sociales WHERE id_usuario = 1")
  redes = cursor.fetchall()

  # Idiomas
  cursor.execute("SELECT * FROM idiomas WHERE id_usuario = 1")
  idiomas = cursor.fetchall()

  # Habilidades
  cursor.execute("SELECT * FROM habilidades WHERE id_usuario = 1")
  habilidades = cursor.fetchall()

  # Experiencias laborales
  cursor.execute("SELECT * FROM experiencias_laborales WHERE id_usuario = 1 ORDER BY id")
  experiencias = cursor.fetchall()

  # Formación
  cursor.execute("SELECT * FROM formacion WHERE id_usuario = 1 ORDER BY id")
  formacion = cursor.fetchall()

  connection.close()

  # Le paso todos los datos a la plantilla
  return render_template(
    "curriculum.html",
    persona=persona,
    contacto=contacto,
    redes=redes,
    idiomas=idiomas,
    habilidades=habilidades,
    experiencias=experiencias,
    formacion=formacion,
    anio=anio
  )

if __name__ == "__main__":
  app.run(debug=True)
```

**002-usuario para conectar.sql**

```sql
C:\xampp\mysql\bin\mysql.exe -u root -p

CREATE USER 'curriculum'@'localhost' IDENTIFIED BY 'CEAC123$';

GRANT USAGE ON *.* TO 'curriculum'@'localhost';

ALTER USER 'curriculum'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON curriculum.* 
TO 'curriculum'@'localhost';

FLUSH PRIVILEGES;
```

#### Ejercicio base da dados 5/1-Ejercicios/002-Variables del sistema y variables de usuario/templates

**curriculum.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <style>
      body{background:lightsteelblue;}
      main{
        width:210mm;
        height:400mm;
        background:white;
        margin:auto;
        display:flex;
      }
      #izquierda{
      	flex:1;
        background: royalblue;
        color:white;
        padding:20px;
      }
      #izquierda img{
      	width:100%;
      }
      #izquierda ul{
        padding-left:18px;
      }
      #izquierda li{
        word-break:break-all;
        margin-bottom:4px;
      }
      #derecha{
      	flex:3;
        padding:20px;
      }
      p{
        text-align:justify;
      }
    </style>
  </head>
  <body>
    <main>
      <div id="izquierda">
        <img src="{{ url_for('static', filename='heverton.png') }}">
        <h3>Contacto</h3>
        <ul>
          {% for c in contacto %}
          <li>{{ c.email }}</li>
          <li>+34 {{ c.telefono }}</li>
          {% endfor %}
          <li>{{ persona.ubicacion }}</li>
        </ul>
        <h3>Redes sociales</h3>
        <ul>
          {% for r in redes %}
          {% if r.linkedin %}<li>{{ r.linkedin }}</li>{% endif %}
          {% if r.github %}<li>{{ r.github }}</li>{% endif %}
          {% if r.facebook %}<li>{{ r.facebook }}</li>{% endif %}
          {% if r.instagram %}<li>{{ r.instagram }}</li>{% endif %}
          {% endfor %}
        </ul>
        <h3>Idiomas</h3>
        <ul>
          {% for i in idiomas %}
          <li>{{ i.idioma }}: {{ i.nivel }}</li>
          {% endfor %}
        </ul>
        <h3>Habilidades</h3>
        <ul>
          {% for h in habilidades if 'Permiso' not in h.habilidades %}
          <li>{{ h.habilidades }}</li>
          {% endfor %}
        </ul>
        <h3>Permiso de conducción</h3>
        <ul>
          {% for h in habilidades if 'Permiso' in h.habilidades %}
          <li>{{ h.habilidades }}</li>
          {% endfor %}
        </ul>
      </div>
      <div id="derecha">
        <h1>{{ persona.nombre }} {{ persona.apellidos }}</h1>
        <h2>Administrador, Programador y Estudiante de DAM</h2>
        <p>Mi nombre es {{ persona.nombre }} {{ persona.apellidos }}, soy brasileño y tengo 35 años. Actualmente estoy estudiando el ciclo superior de Desarrollo de Aplicaciones Multiplataforma.</p>
        <section id="experiencia">
          <h3>Experiencia profesional</h3>
          {% for e in experiencias %}
          <article>
            <h4>{{ e.empresa }}</h4>
            <p>Desde {{ anio(e.inicio) }} hasta {{ anio(e.final) }}</p>
            <p>{{ e.descripcion }}</p>
            <p>{{ e.cargo }}</p>
          </article>
          {% endfor %}
        </section>
        <section id="formacion">
          <h3>Formación</h3>
          {% for f in formacion %}
          <article>
            <h4>{{ f.centro }}</h4>
            {% if f.inicio and f.final %}
            <p>Desde {{ anio(f.inicio) }} hasta {{ anio(f.final) }}</p>
            {% elif f.final %}
            <p>Hasta {{ anio(f.final) }}</p>
            {% endif %}
            <p>{{ f.descripcion }}</p>
            <p>{{ f.titulo }}</p>
          </article>
          {% endfor %}
        </section>
      </div>
    </main>
  </body>
</html>
```

### Ejercicio base da dados 5/1-Ejercicios/003-Funciones

**001-SQLite.md**

```markdown
SQLITE = SQL + lite (light)
MySQL es super potente, super poderoso... pero a veces no nos hace falta una base de datos tan fuerte

SQLite es una base de datos más ligera - pero que cumple con el estándar SQL
Todo lo que hemos aprendido, lo convservamos

Vamos a usar un gestor visual de bases de datos SQLite
El gestor se llama DB Browser

https://sqlitebrowser.org/

En linux es más fácil:
sudo apt install sqlitebrowser

Ventajas y desventajas:
Ventajas: ligero, está en un solo archivo
Desventajas: menos seguro, no tiene usuario y contraseña

```

**002-crear tabla.sql**

```sql
CREATE TABLE "clientes" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

**003-me conecto desde python.py**

```python
import sqlite3

conexion = sqlite3.connect("empresa.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM clientes")

resultados = cursor.fetchall()
print(resultados)

conexion.close()
```

**004-lo quiero como diccionario.py**

```python
import sqlite3

conexion = sqlite3.connect("empresa.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

for fila in cursor.fetchall():
    print(dict(fila))

conexion.close()
```

### Ejercicio base da dados 5/1-Ejercicios/004-Estructuras de control de flujo

**002-prompt para ia.md**

```markdown
CREATE TABLE "articulos" (
	"id"	INTEGER,
	"titulo"	TEXT,
	"fecha"	TEXT,
	"contenido"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
) dame 20 articulos de un blog de jocarsa para sqlite - insert into
```

**003-me conecto desde python.py**

```python
import sqlite3

conexion = sqlite3.connect("blog.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()
cursor.execute("SELECT * FROM articulos")

for fila in cursor.fetchall():
    print(dict(fila))

conexion.close()
```

**004-ahora le pongo flask.py**

```python
# Importo la librería de bases de datos
import sqlite3

# Importo la librería de web
from flask import Flask, render_template, request

# Creo una aplicación web
aplicacion = Flask(__name__)

# Escucho en la raíz /
@aplicacion.route("/")
def inicio():
    # Me conecto a la base de datos
    conexion = sqlite3.connect("blog.db")

    # Lo que venga lo quiero como diccionario
    conexion.row_factory = sqlite3.Row

    # Creo un cursor necesario
    cursor = conexion.cursor()

    # Le pido los artículos
    cursor.execute("SELECT * FROM articulos")

    # Cargo los artículos en una variable
    articulos = cursor.fetchall()

    # Cierro la conexión
    conexion.close()

    # Pinto la plantilla
    return render_template("frente.html", datos=articulos)


if __name__ == "__main__":
    aplicacion.run()
```

#### Ejercicio base da dados 5/1-Ejercicios/004-Estructuras de control de flujo/static

**estilo.css**

```css
body,html{background:rgb(80, 34, 91);}
header,main,footer{width:800px;background:white;padding:50px;margin:auto;font-family: Verdana, Geneva, Tahoma, sans-serif;}
```

#### Ejercicio base da dados 5/1-Ejercicios/004-Estructuras de control de flujo/templates

**frente.html**

```html
<!doctype html>
<html>
  <head>
    <title>El blog de Heverton Marques</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="static/estilo.css">
  </head>
  <body>
    <header>
      <h1>Heverton Marques</h1>
      <h2>Blog personal</h2>
    </header>
    <main>
      {% for articulo in datos %}
      	<article>
          <h3>{{articulo.titulo}}</h3>
          <time>{{articulo.fecha}}</time>
          <p>{{articulo.contenido}}</p>
      </article>
      {% endfor %}
    </main>
    <footer>
    </footer>
  </body>
</html>
```

### Ejercicio base da dados 5/1-Ejercicios/005-Procedimientos almacenados. Funciones de usuario

**001-resumen.md**

```markdown
Lenguajes de programación
  Variables
  Comentarios
  Entradas y salidas
  Estructuras de control
  Estructuras de datos
  Funciones
  Objetos
  
Lenguajes de datos:
	Seleccionar
  Insertar
  Actualizar
  Eliminar
  Crear - Eliminar (drop) - Vaciar
```

**002-comentarios.sql**

```sql
-- Esto es un comentario
-- Y esto es otro comentario
SELECT * FROM clientes;
```

**003-crear base de datos.sql**

```sql
C:\xampp\mysql\bin\mysql.exe -u root -p

-- Crear base de datos
CREATE DATABASE IF NOT EXISTS empresaclase
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Seleccionar base de datos
USE empresaclase;

-- Crear tabla clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    direccion VARCHAR(200),
    ciudad VARCHAR(100),
    provincia VARCHAR(100),
    codigo_postal VARCHAR(10),
    fecha_nacimiento DATE,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

-- Insertar datos de demostración
INSERT INTO clientes (
    nombre, apellidos, email, telefono,
    direccion, ciudad, provincia,
    codigo_postal, fecha_nacimiento, activo
) VALUES
('Juan', 'García López', 'juan.garcia@example.com',
 '612345678', 'Calle Mayor 15', 'Valencia',
 'Valencia', '46001', '1985-03-12', 1),

('María', 'Martínez Pérez', 'maria.martinez@example.com',
 '623456789', 'Avenida del Puerto 42', 'Valencia',
 'Valencia', '46021', '1990-07-25', 1),

('Pedro', 'Sánchez Ruiz', 'pedro.sanchez@example.com',
 '634567890', 'Calle Colón 8', 'Madrid',
 'Madrid', '28001', '1978-11-04', 1),

('Ana', 'Fernández Gómez', 'ana.fernandez@example.com',
 '645678901', 'Gran Vía 23', 'Madrid',
 'Madrid', '28013', '1995-01-18', 1),

('Carlos', 'Rodríguez Díaz', 'carlos.rodriguez@example.com',
 '656789012', 'Calle Aragón 56', 'Barcelona',
 'Barcelona', '08009', '1982-09-30', 1),

('Laura', 'López Hernández', 'laura.lopez@example.com',
 '667890123', 'Paseo de Gracia 101', 'Barcelona',
 'Barcelona', '08008', '1988-05-14', 1),

('Miguel', 'González Torres', 'miguel.gonzalez@example.com',
 '678901234', 'Calle Sierpes 12', 'Sevilla',
 'Sevilla', '41004', '1975-12-08', 1),

('Lucía', 'Pérez Navarro', 'lucia.perez@example.com',
 '689012345', 'Avenida Constitución 34', 'Sevilla',
 'Sevilla', '41001', '1998-04-22', 1),

('David', 'Romero Castillo', 'david.romero@example.com',
 '690123456', 'Calle Larios 7', 'Málaga',
 'Málaga', '29005', '1987-06-11', 1),

('Elena', 'Jiménez Morales', 'elena.jimenez@example.com',
 '601234567', 'Calle Nueva 19', 'Málaga',
 'Málaga', '29008', '1992-10-03', 1),

('Javier', 'Ruiz Ortega', 'javier.ruiz@example.com',
 '611223344', 'Calle Alfonso I 22', 'Zaragoza',
 'Zaragoza', '50003', '1980-02-17', 1),

('Carmen', 'Díaz Serrano', 'carmen.diaz@example.com',
 '622334455', 'Paseo Independencia 45', 'Zaragoza',
 'Zaragoza', '50001', '1993-08-09', 1),

('Sergio', 'Moreno Vega', 'sergio.moreno@example.com',
 '633445566', 'Calle San Vicente 14', 'Alicante',
 'Alicante', '03004', '1984-05-27', 1),

('Paula', 'Álvarez Molina', 'paula.alvarez@example.com',
 '644556677', 'Avenida Maisonnave 28', 'Alicante',
 'Alicante', '03003', '1997-12-15', 1),

('Raúl', 'Torres Campos', 'raul.torres@example.com',
 '655667788', 'Calle Trapería 9', 'Murcia',
 'Murcia', '30001', '1979-03-06', 1),

('Isabel', 'Vázquez Flores', 'isabel.vazquez@example.com',
 '666778899', 'Gran Vía 51', 'Murcia',
 'Murcia', '30004', '1991-09-21', 1),

('Alberto', 'Castro Medina', 'alberto.castro@example.com',
 '677889900', 'Calle Uría 33', 'Oviedo',
 'Asturias', '33003', '1986-07-13', 1),

('Natalia', 'Herrera León', 'natalia.herrera@example.com',
 '688990011', 'Calle Corrida 17', 'Gijón',
 'Asturias', '33206', '1994-11-29', 1),

('Fernando', 'Ramos Iglesias', 'fernando.ramos@example.com',
 '699001122', 'Calle Gran Vía 65', 'Bilbao',
 'Bizkaia', '48011', '1981-01-10', 0),

('Patricia', 'Gil Santos', 'patricia.gil@example.com',
 '600112233', 'Avenida Libertad 20', 'San Sebastián',
 'Gipuzkoa', '20004', '1996-06-02', 1);

-- Consultar todos los clientes
SELECT * FROM clientes;

-- Contar clientes
SELECT COUNT(*) AS total_clientes FROM clientes;
```

**004-condicional sencillo.sql**

```sql
SELECT IF(10 > 5, 'Verdadero', 'Falso');

```

**005-mas elaborado.sql**

```sql
SELECT
    nombre,
    apellidos,
    IF(ciudad = 'Bilbao', ciudad, NULL) AS ciudad,
    IF(ciudad = 'Bilbao', telefono, NULL) AS telefono
FROM clientes;
```

**006-Select.sql**

```sql
SELECT 

telefono/535
FROM clientes;
```

**007-exixten funciones.sql**

```sql
SELECT 

ROUND(telefono/535)
FROM clientes;
```

**008-mi procedimiento almacenado.sql**

```sql
SELECT * FROM clientes;

SELECT * FROM clientes
WHERE codigo_postal < 30000;

def dameCodig(codigo):
	SELECT * FROM clientes
	WHERE codigo_postal < codigo;
  
DELIMITER //

CREATE PROCEDURE dameCodigo(IN codigo INT)
BEGIN
    SELECT *
    FROM clientes
    WHERE codigo_postal < codigo;
END //

DELIMITER ;

CALL dameCodigo(30000); #puxa dados de clientes con codigo postal menor a 30000
```

### Ejercicio base da dados 5/1-Ejercicios/006-Eventos y disparadores

**001-disparador.sql**

```sql
DELIMITER //

CREATE TRIGGER borrar_direccion
BEFORE UPDATE ON clientes
FOR EACH ROW
BEGIN
    IF NOT (OLD.telefono <=> NEW.telefono) THEN
        SET NEW.direccion = NULL;
    END IF;
END //

DELIMITER ;

```

**002-clientescopiadeseguridad.sql**

```sql
CREATE TABLE IF NOT EXISTS clientescopia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    direccion VARCHAR(200),
    ciudad VARCHAR(100),
    provincia VARCHAR(100),
    codigo_postal VARCHAR(10),
    fecha_nacimiento DATE,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);
```

**003-creo evento.sql**

```sql
-- Activar el programador de eventos
SET GLOBAL event_scheduler = ON;

-- Eliminar el evento si ya existe
DROP EVENT IF EXISTS sincronizar_clientes;

-- Crear evento cada minuto
DELIMITER //

CREATE EVENT sincronizar_clientes
ON SCHEDULE EVERY 1 MINUTE
DO
BEGIN
    DELETE FROM clientescopia;

    INSERT INTO clientescopia
    SELECT * FROM clientes;
END //

DELIMITER ;

#comando excluir
DELETE FROM clientes 
WHERE id = 19;
```

## Ejercicio base da dados 5/2-Proyecto

**001-Creo una base de dados.sql**

```sql
CREATE DATABASE clinica;      --crear base de datos
USE clinica;



```

**002-Creo tablas.sql**

```sql
CREATE TABLE medicos (                    --crear tabla medicos
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  especialidad VARCHAR(100) NOT NULL,
  activo TINYINT NOT NULL DEFAULT 1
);

CREATE TABLE pacientes (                  --crear tabla pacientes
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  fecha_nacimiento DATE NOT NULL
);

CREATE TABLE citas (                      --crear tabla citas
  id INT PRIMARY KEY AUTO_INCREMENT,
  medico_id INT NOT NULL,
  paciente_id INT NOT NULL,
  fecha DATETIME NOT NULL,
  estado ENUM('pendiente','realizada','cancelada','caducada') NOT NULL DEFAULT 'pendiente',
  FOREIGN KEY (medico_id) REFERENCES medicos(id),
  FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

CREATE TABLE registro (                   --rellenan los disparadores
  id INT PRIMARY KEY AUTO_INCREMENT,
  accion VARCHAR(255) NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE informe_medicos (            --rellena el procedimiento con cursor
  medico VARCHAR(100),
  pendientes INT,
  carga VARCHAR(20),
  generado DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**003-funciones de usuario.sql**

```sql
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
```

**004-procedimento com controle de fluxo e exceções.sql**

```sql
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
```

**005-procedimento com cursor.sql**

```sql
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
```

**006-disparadores.sql**

```sql
--Limpia y valida los datos del paciente antes de guardarlos

CREATE TRIGGER antes_insertar_paciente
BEFORE INSERT ON pacientes
FOR EACH ROW
BEGIN
  SET NEW.nombre = TRIM(NEW.nombre);
  SET NEW.email = LOWER(TRIM(NEW.email));
  IF NEW.email NOT LIKE '%_@_%._%' THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Email no válido';
  END IF;
END //

--Anota cada cita nueva 

CREATE TRIGGER despues_insertar_cita
AFTER INSERT ON citas
FOR EACH ROW
BEGIN
  INSERT INTO registro (accion)
  VALUES (CONCAT('Nueva cita ', NEW.id, ' el ', DATE_FORMAT(NEW.fecha, '%d/%m/%Y %H:%i')));
END //

--Anota cada cambio de estado de una cita

CREATE TRIGGER despues_cambiar_cita
AFTER UPDATE ON citas
FOR EACH ROW
BEGIN
  IF OLD.estado <> NEW.estado THEN
    INSERT INTO registro (accion)
    VALUES (CONCAT('Cita ', NEW.id, ': ', OLD.estado, ' -> ', NEW.estado));
  END IF;
END //

DELIMITER ;
```

**007-inserto dados.sql**

```sql
INSERT INTO medicos (nombre, especialidad, activo) VALUES
('Lucía Fernández', 'Pediatría', 1),
('Javier Moreno', 'Cardiología', 1),
('Carmen López', 'Dermatología', 1),
('Pablo Martínez', 'Neurología', 0);

-- Espacios y mayúsculas a propósito: el disparador los limpia

INSERT INTO pacientes (nombre, email, fecha_nacimiento) VALUES
('Carlos Ruiz', 'CARLOS.RUIZ@EJEMPLO.COM', '1990-04-12'),
('Ana López', 'ana.lopez@ejemplo.com', '1985-09-30'),
('Marta Gil', 'marta.gil@ejemplo.com', '2001-01-15');

-- Cita en el pasado, insertada a mano (sin el procedimiento) para que el evento la caduque

INSERT INTO citas (medico_id, paciente_id, fecha) VALUES (2, 3, '2026-11-10 09:00:00');
```

**008-eventos.sql**

```sql
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
```

**009-lo pruebo todo.sql**

```sql
-- Procedimiento: casos correctos

CALL nueva_cita(1, 1, '2026-12-01 10:00:00');
CALL nueva_cita(1, 2, '2026-12-01 11:00:00');
CALL nueva_cita(1, 3, '2026-12-02 09:30:00');
CALL nueva_cita(2, 1, '2026-12-03 17:00:00');

-- Procedimiento: excepciones

CALL nueva_cita(4, 1, '2026-12-03 17:00:00');   -- SIGNAL: médico no activo
CALL nueva_cita(2, 2, '2026-01-01 10:00:00');   -- SIGNAL: fecha pasada
CALL nueva_cita(1, 99, '2026-12-03 17:00:00');  -- HANDLER: paciente no existe

-- Disparador BEFORE: email no válido

INSERT INTO pacientes (nombre, email, fecha_nacimiento)
VALUES ('Prueba', 'correo-malo', '2000-01-01');

-- Funciones

SELECT nombre, email, edad(fecha_nacimiento) AS edad FROM pacientes;
SELECT nombre, citas_pendientes(id) AS pendientes FROM medicos;

-- Cursor

CALL generar_informe();

-- Lo que han hecho los disparadores y el evento

SELECT * FROM citas;
SELECT * FROM registro;

-- Ver todo lo creado

SHOW FUNCTION STATUS WHERE Db = 'clinica';
SHOW PROCEDURE STATUS WHERE Db = 'clinica';
SHOW TRIGGERS;
SHOW EVENTS;
```

## Ejercicio base da dados 5/3-Resultado de aprendizaje

**001-criterios de evaluacion.md**

```markdown
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
```

