# Reporte de proyecto

## Información de generación

- **Fecha:** 3/10/2026, 14:36:29
- **Proyecto documentado:** `Ejercicio Lenguajes de marcas 2`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio Lenguajes de marcas 2
    ├── 1-Ejercicios
    │   ├── 001-Estándares web. Versiones. Clasificación
    │   │   ├── 000-introdución.md
    │   │   └── 002-CERN.md
    │   ├── 002-Estructura de un documento HTML
    │   │   ├── 000-introdución.md
    │   │   ├── 001-doctype.html
    │   │   ├── 002-etiqueta html.html
    │   │   ├── 003-cabeza y cuerpo.html
    │   │   ├── 004-comentarios.html
    │   │   ├── 005-lenguaje html.html
    │   │   ├── 006-titulo.html
    │   │   └── 007-meta charset.html
    │   ├── 003-Identificación de etiquetas y atributos de HTML
    │   │   ├── 000-introdución.md
    │   │   ├── 002-cabecera.html
    │   │   ├── 003-navegacion.html
    │   │   └── 004-anclas.html
    │   ├── 004-Herramientas de diseño web
    │   │   ├── 001-empezamos desde donde ayer.html
    │   │   ├── 002-nuevo formulario.html
    │   │   ├── 003-ahora creo input.html
    │   │   ├── 004-label.html
    │   │   ├── 005-ahora el correo.html
    │   │   ├── 006-ahora una caja de texto.html
    │   │   ├── 007-imagen.html
    │   │   ├── 007-meto una imagen.html
    │   │   ├── 008-etiqueta tabla.html
    │   │   ├── 009-cabeza y cuerpo.html
    │   │   ├── 010-cabeceras de tabla.html
    │   │   ├── 011-datos de la tabla.html
    │   │   └── images.jpeg
    │   ├── 005-Hojas de estilo (CSS)
    │   │   ├── 001-continuamos desde el bloque anterior.html
    │   │   ├── 002-css interno.html
    │   │   ├── 003-selectores.html
    │   │   ├── 004-color de fondo.html
    │   │   ├── 005-nombres de colores.md
    │   │   ├── 006-bloques principales.html
    │   │   ├── 007-anchura de los bloques.html
    │   │   ├── 008-una forma de centrar elementos.html
    │   │   ├── 009-margen interior.html
    │   │   ├── 010-letra serif.html
    │   │   ├── 011-sans serif.html
    │   │   ├── 012-monoespaciada.html
    │   │   ├── 013-fuente mas grande.html
    │   │   ├── 014-elimino los estilos por defecto.html
    │   │   ├── 015-negrita.html
    │   │   ├── 016-alineacion del parrafo.html
    │   │   ├── 017-estilo de los vinculos.html
    │   │   ├── 018-imagen de portada.html
    │   │   ├── 019-formulario en flex.html
    │   │   ├── 020-blog en grid.html
    │   │   ├── 021-alineacion del menu.html
    │   │   ├── 022-mi pagina web.html
    │   │   ├── 023-ahora com IA.html
    │   │   └── heverton.png
    │   ├── 006-Validación de documentos HTML y CSS
    │   │   ├── 001-Recordad validar vuestra web.html
    │   │   ├── 002-codigo actual.html
    │   │   ├── 003-corrijo errores.html
    │   │   └── heverton.png
    │   └── 007-Lenguajes de marcas para la sindicación de contenidos
    │       └── 001-Ejercicio final de unidad.md
    ├── 2-Proyecto
    │   ├── 022-mi pagina web.html
    │   ├── 023-ahora com IA.html
    │   └── heverton.png
    └── 3-Resultado de aprendizaje
        └── Resultado de aprendizaje.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite.

## Código (intercalado)

### Ejercicio Lenguajes de marcas 2/1-Ejercicios/001-Estándares web. Versiones. Clasificación

**000-introdución.md**

```markdown
```

**002-CERN.md**

```markdown
Tim Berners-Lee durante su estancia en el CERN (Suiza)
Empezó a trabajar en un proyecto llamado HTML

Hyper Text
Markup Language

Originalmente HTML creado para crear documentos
Documentos enlazados entre sí

1991 lanza
-La especificación 1.0 HTML
-Un servidor web 
-Un navegador web para que la gente pueda conectarse 
al servidor y "ver" documentos HTML

'90 adopción brutal de HTML
Documento -> página web -> Sitio web
'00 
Sitio web -> Aplicación web
'10
LA web está en todas partes


```

### Ejercicio Lenguajes de marcas 2/1-Ejercicios/002-Estructura de un documento HTML

**000-introdución.md**

```markdown
```

**001-doctype.html**

```html
<!doctype html>

```

**002-etiqueta html.html**

```html
<!doctype html>
<html>
  
</html>
```

**003-cabeza y cuerpo.html**

```html
<!doctype html>
<html>
  <head>
  </head>
  <body>
  </body>
</html>
```

**004-comentarios.html**

```html
<!doctype html>
<html>
  <head>
    <!-- Se transmite al navegador -->
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  </body>
</html>
```

**005-lenguaje html.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  </body>
</html>
```

**006-titulo.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>site Heverton Marques</title>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  </body>
</html>



```

**007-meta charset.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>site Heverton Marques</title>
  <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  </body>
</html>




```

### Ejercicio Lenguajes de marcas 2/1-Ejercicios/003-Identificación de etiquetas y atributos de HTML

**000-introdución.md**

```markdown
```

**002-cabecera.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>site Heverton Marques</title>
  <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
    <h2>Administrador, Alumno y Programador</h2>
    </header>
    <main>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**003-navegacion.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>site Heverton Marques</title>
  <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
    <h2>Administrador, Alumno y Programador</h2>
    <nav>
        
      </nav>
    </header>
    <main>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**004-anclas.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>site Heverton Marques</title>
  <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
    <h2>Administrador, Alumno y Programador</h2>
    <nav>
        <a href="#destacado">Destacado</a>
        <a href="#destacado">Sobre mi</a>
        <a href="#destacado">Blog</a>
        <a href="#destacado">Contacto</a>
      </nav>
    </header>
    <main>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

### Ejercicio Lenguajes de marcas 2/1-Ejercicios/004-Herramientas de diseño web

**001-empezamos desde donde ayer.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>site Heverton Marques</title>
  <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
    <h2>Administrador, Alumno y Programador</h2>
    <nav>
        <a href="#destacado">Reflexión</a>
        <a href="#destacado">Sobre mi</a>
        <a href="#destacado">Blog</a>
        <a href="#destacado">Contacto</a>
      </nav>
    </header>
    <main>
       <section id="destacado">
        <h3>Reflexión</h3>
        <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
        <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p> Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
        <ul>
          <li>Experiencia en administración y organización de procesos.</li>
          <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
          <li>Idiomas: portugués (nativo) y español.</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Python sigue en lo más alto del índice TIOBE</h4>
          <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
        </article>
        <article>
          <h4>Rust se consolida entre los diez lenguajes más populares</h4>
          <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
        </article>
        <article>
          <h4>Julia, cerca de volver al top 20</h4>
          <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
        </article>
        <article>
          <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
          <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
        </article>
        <article>
          <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
          <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <p>Si quieres contactar conmigo, puedes escribirme:</p>
        <ul>
          <li>Correo electrónico: <a href="mailto:tuemail@ejemplo.com">hevertonmf@gmail.com</a></li>
          <li>LinkedIn: <a href="https://www.linkedin.com/">https://www.linkedin.com/in/heverton-marques-00a569196/</a></li>
          <li>Ubicación: Valencia, España</li>
        </ul>
      </section>
    </main>
    <footer>
      <p>&copy; 2026 Heverton Marques Ferreira Maciel. Todos los derechos reservados.</p>
    </footer>
  </body>
</html>
```

**002-nuevo formulario.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>

003-Identificación de etiquetas y atributos de HTML

```

**003-ahora creo input.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <input type="text" name="nombre">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**004-label.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**005-ahora el correo.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**006-ahora una caja de texto.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**007-imagen.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="images.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**007-meto una imagen.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>site Heverton Marques</title>
  <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
  <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
    <h2>Administrador, Alumno y Programador</h2>
    <nav>
        <a href="#destacado">Reflexión</a>
        <a href="#destacado">Sobre mi</a>
        <a href="#destacado">Blog</a>
        <a href="#destacado">Contacto</a>
      </nav>
    </header>
    <main>
     <section id="destacado">
        <h3>Destacado</h3>
        <img src="images.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
      </section>
       <section id="destacado">
        <h3>Reflexión</h3>
        <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
        <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p> Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
        <ul>
          <li>Experiencia en administración y organización de procesos.</li>
          <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
          <li>Idiomas: portugués (nativo) y español.</li>
        </ul>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Python sigue en lo más alto del índice TIOBE</h4>
          <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
        </article>
        <article>
          <h4>Rust se consolida entre los diez lenguajes más populares</h4>
          <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
        </article>
        <article>
          <h4>Julia, cerca de volver al top 20</h4>
          <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
        </article>
        <article>
          <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
          <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
        </article>
        <article>
          <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
          <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <p>Si quieres contactar conmigo, puedes escribirme:</p>
        <ul>
          <li>Correo electrónico: <a href="mailto:tuemail@ejemplo.com">hevertonmf@gmail.com</a></li>
          <li>LinkedIn: <a href="https://www.linkedin.com/">https://www.linkedin.com/in/heverton-marques-00a569196/</a></li>
          <li>Ubicación: Valencia, España</li>
        </ul>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**008-etiqueta tabla.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table>
          
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**009-cabeza y cuerpo.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table>
          <thead>
          
          </thead>
          <tbody>
          	
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**010-cabeceras de tabla.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**011-datos de la tabla.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

### Ejercicio Lenguajes de marcas 2/1-Ejercicios/005-Hojas de estilo (CSS)

**001-continuamos desde el bloque anterior.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**002-css interno.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**003-selectores.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**004-color de fondo.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:whitesmoke;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**005-nombres de colores.md**

```markdown
https://colores.jocarsa.com/

aliceblue
antiquewhite
aqua
aquamarine
azure
beige
bisque
black
blanchedalmond
blue
blueviolet
brown
burlywood
cadetblue
chartreuse
chocolate
coral
cornflowerblue
cornsilk
crimson
cyan
darkblue
darkcyan
darkgoldenrod
darkgray
darkgreen
darkgrey
darkkhaki
darkmagenta
darkolivegreen
darkorange
darkorchid
darkred
darksalmon
darkseagreen
darkslateblue
darkslategray
darkslategrey
darkturquoise
darkviolet
deeppink
deepskyblue
dimgray
dimgrey
dodgerblue
firebrick
floralwhite
forestgreen
fuchsia
gainsboro
ghostwhite
gold
goldenrod
gray
green
greenyellow
grey
honeydew
hotpink
indianred
indigo
ivory
khaki
lavender
lavenderblush
lawngreen
lemonchiffon
lightblue
lightcoral
lightcyan
lightgoldenrodyellow
lightgray
lightgreen
lightgrey
lightpink
lightsalmon
lightseagreen
lightskyblue
lightslategray
lightslategrey
lightsteelblue
lightyellow
lime
limegreen
linen
magenta
maroon
mediumaquamarine
mediumblue
mediumorchid
mediumpurple
mediumseagreen
mediumslateblue
mediumspringgreen
mediumturquoise
mediumvioletred
midnightblue
mintcream
mistyrose
moccasin
navajowhite
navy
oldlace
olive
olivedrab
orange
orangered
orchid
palegoldenrod
palegreen
paleturquoise
palevioletred
papayawhip
peachpuff
peru
pink
plum
powderblue
purple
rebeccapurple
red
rosybrown
royalblue
saddlebrown
salmon
sandybrown
seagreen
seashell
sienna
silver
skyblue
slateblue
slategray
slategrey
snow
springgreen
steelblue
tan
teal
thistle
tomato
turquoise
violet
wheat
white
whitesmoke
yellow
yellowgreen
```

**006-bloques principales.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:whitesmoke;
      }
      header,main,footer{
      	background:white;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**007-anchura de los bloques.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
      }
      header,main,footer{
      	background:white;
        width:800px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**008-una forma de centrar elementos.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**009-margen interior.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**010-letra serif.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:serif;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**011-sans serif.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:sans-serif;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**012-monoespaciada.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**013-fuente mas grande.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**014-elimino los estilos por defecto.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1,h2{
      	margin:0px;padding:0px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**015-negrita.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1,h2{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**016-alineacion del parrafo.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1,h2{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**017-estilo de los vinculos.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.jpg">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**018-imagen de portada.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.png">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**019-formulario en flex.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
      form{
      	display:flex;
        flex-direction:column;
        gap:10px;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.png">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**020-blog en grid.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
      form{
      	display:flex;
        flex-direction:column;
        gap:10px;
      }
      #blog{
      	display:grid;
        grid-template-columns:repeat(3,1fr);
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.png">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**021-alineacion del menu.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
      form{
      	display:flex;
        flex-direction:column;
        gap:10px;
      }
      #blog{
      	display:grid;
        grid-template-columns:repeat(3,1fr);
      }
      nav{
      	text-align:right;
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario humano -->
    <header>
      <h1>Jose Vicente Carratala</h1>
      <h2>Programador, profesor y diseñador</h2>
      <nav>
        <a href="#destacado">Destacado</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Destacado</h3>
        <img src="josevicente.png">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a:</p>
        <ul>
          <li>Programación</li>
          <li>Formación</li>
          <li>Diseño</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
        <article>
          <h4>Título de la noticia</h4>
          <p>Texto de la noticia</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

**022-mi pagina web.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Heverton Marques</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
      form{
      	display:flex;
        flex-direction:column;
        gap:10px;
      }
      #blog{
      	display:grid;
        grid-template-columns:repeat(3,1fr);
         gap:10px;
      }
      #contacto a{
        background:none;
        color:indigo;
        padding:0;
        text-decoration:underline;
}
      img { 
        border: 0; }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario -->
    <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
      <h2>Administrador, alumno y programador</h2>
      <nav>
        <a href="#destacado">Reflexión</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Reflexión</h3>
        <img src="heverton.png" alt="Foto de Heverton Marques">
        <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
        <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
        <ul>
          <li>Experiencia en administración y organización de procesos.</li>
          <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
          <li>Idiomas: portugués (nativo) y español.</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Python sigue en lo más alto del índice TIOBE</h4>
          <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
        </article>
        <article>
          <h4>Rust se consolida entre los diez lenguajes más populares</h4>
          <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
        </article>
        <article>
          <h4>Julia, cerca de volver al top 20</h4>
          <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
        </article>
        <article>
          <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
          <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
        </article>
        <article>
          <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
          <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <p>Si quieres contactar conmigo, puedes escribirme:</p>
        <ul>
          <li>Correo electrónico: <a href="mailto:hevertonmf@gmail.com">hevertonmf@gmail.com</a></li>
          <li>LinkedIn: <a href="https://www.linkedin.com/in/heverton-marques-00a569196/">heverton-marques</a></li>
          <li>Ubicación: Valencia, España</li>
        </ul>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
      <p>&copy; 2026 Heverton Marques Ferreira Maciel. Todos los derechos reservados.</p>
    </footer>
  </body>
</html>
```

**023-ahora com IA.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>La web de Heverton Marques</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;700;800&display=swap" rel="stylesheet">
    <style>
      /* ===== Colores y medidas ===== */
      :root{
        --morado:#5b3fa6;
        --rosa:#e06be0;
        --morado-oscuro:#3d2a7a;
        --negro:#000;
        --blanco:#fff;
        --degradado:linear-gradient(100deg,var(--morado),var(--rosa));
        --ancho:1100px;
      }
      *{box-sizing:border-box;}
      body{
        margin:0;
        font-family:"Barlow",Arial,sans-serif;
        color:#1d1433;
        background:var(--blanco);
        line-height:1.6;
      }
      .contenedor{
        max-width:var(--ancho);
        margin:auto;
        padding:0 30px;
      }
      p{text-align:justify;}

      /* ===== Cabecera ===== */
      header{
        background:var(--blanco);
        position:sticky;
        top:0;
        z-index:10;
        box-shadow:0 1px 0 #e7e2f3;
      }
      header .contenedor{
        display:flex;
        align-items:center;
        justify-content:space-between;
        padding-top:14px;
        padding-bottom:14px;
        gap:20px;
      }
      .logo{
        text-decoration:none;
        color:var(--negro);
        line-height:1;
      }
      .logo .fila{
        display:flex;
        align-items:center;
        gap:8px;
      }
      .logo .nombre{
        font-weight:300;
        font-size:22px;
      }
      .logo .burbuja{
        width:90px;
        height:22px;
        background:var(--degradado);
        border-radius:12px 12px 12px 0;
      }
      .logo .apellido{
        font-weight:800;
        font-size:38px;
        letter-spacing:-1px;
      }
      nav{
        display:flex;
        align-items:center;
        gap:28px;
        flex-wrap:wrap;
      }
      nav a{
        color:var(--morado-oscuro);
        text-decoration:none;
        text-transform:uppercase;
        font-weight:500;
        font-size:16px;
      }
      nav a:hover{color:var(--rosa);}
      nav a.boton-nav{
        background:var(--degradado);
        color:var(--blanco);
        padding:10px 26px;
        border-radius:6px;
      }

      /* ===== Portada con degradado ===== */
      .portada{
        position:relative;
        overflow:hidden;
        background:var(--degradado);
        color:var(--blanco);
        padding:70px 0 50px;
      }
      /* Líneas diagonales de las esquinas */
      .portada::before,
      .portada::after{
        content:"";
        position:absolute;
        width:220px;
        height:220px;
        background:repeating-linear-gradient(-60deg,transparent 0 16px,rgba(0,0,0,.45) 16px 18px);
      }
      .portada::before{
        top:0;left:0;
        clip-path:polygon(0 0,45% 0,0 45%);
      }
      .portada::after{
        bottom:0;right:0;
        clip-path:polygon(100% 30%,100% 100%,30% 100%);
      }
      .portada .contenedor{
        position:relative;
        z-index:1;
      }
      .portada-grid{
        display:grid;
        grid-template-columns:1.2fr 1fr;
        gap:50px;
        align-items:center;
      }
      .etiqueta{
        display:inline-block;
        background:var(--negro);
        color:var(--blanco);
        font-weight:400;
        font-size:36px;
        line-height:1.2;
        padding:6px 24px;
        margin:0 0 24px;
      }
      .portada p{
        font-size:20px;
        max-width:560px;
      }
      .boton{
        display:inline-flex;
        align-items:center;
        gap:10px;
        margin-top:20px;
        background:var(--negro);
        color:var(--blanco);
        text-decoration:none;
        text-transform:uppercase;
        font-size:18px;
        padding:12px 30px;
        border-radius:6px;
        border:none;
        font-family:inherit;
        cursor:pointer;
      }
      .boton:hover{background:var(--morado-oscuro);}

      /* Foto con bocadillo negro detrás */
      .foto{
        position:relative;
        max-width:380px;
        justify-self:center;
      }
      .foto::before{
        content:"";
        position:absolute;
        inset:-18px 40px 40px -18px;
        background:var(--negro);
        border-radius:22px 22px 22px 0;
      }
      .foto img{
        position:relative;
        display:block;
        width:100%;
        aspect-ratio:4/5;
        object-fit:cover;
        border-radius:16px;
        background:rgba(255,255,255,.2);
        border:0;
      }

      /* Iconos de la portada */
      .iconos{
        display:grid;
        grid-template-columns:repeat(6,1fr);
        gap:20px;
        margin-top:80px;
        text-align:center;
      }
      .iconos svg{
        width:54px;
        height:54px;
        fill:none;
        stroke:var(--negro);
        stroke-width:2.2;
        stroke-linecap:round;
        stroke-linejoin:round;
      }
      .iconos span{
        display:block;
        font-weight:500;
        font-size:19px;
        line-height:1.2;
        margin-top:10px;
      }

      /* ===== Secciones ===== */
      section{
        padding:80px 0;
        scroll-margin-top:80px;
      }
      .titulo{
        display:inline-block;
        background:var(--negro);
        color:var(--blanco);
        font-weight:400;
        font-size:32px;
        padding:4px 22px;
        margin:0 0 30px;
      }
      .dos-columnas{
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:50px;
        font-size:18px;
      }

      /* Sobre mí */
      #sobremi{background:#f5f1fb;}
      .lista{
        list-style:none;
        padding:0;
        margin:0;
      }
      .lista li{
        padding:14px 0 14px 34px;
        border-bottom:2px solid #e2d8f2;
        position:relative;
      }
      .lista li::before{
        content:"";
        position:absolute;
        left:0;
        top:20px;
        width:16px;
        height:16px;
        background:var(--degradado);
        border-radius:6px 6px 6px 0;
      }

      /* Blog */
      .blog-grid{
        display:grid;
        grid-template-columns:repeat(3,1fr);
        gap:24px;
      }
      article{
        border:2px solid var(--negro);
        border-radius:6px;
        padding:24px;
        border-top:10px solid var(--rosa);
      }
      article:nth-child(odd){border-top-color:var(--morado);}
      article h4{
        font-size:21px;
        line-height:1.25;
        margin:0 0 12px;
      }
      article p{margin:0;}

      /* Contacto */
      #contacto{
        background:var(--degradado);
        color:var(--blanco);
      }
      #contacto ul{
        list-style:none;
        padding:0;
        font-size:19px;
      }
      #contacto li{margin-bottom:12px;}
      #contacto li a{
        color:var(--blanco);
        font-weight:700;
      }
      form{
        display:flex;
        flex-direction:column;
        gap:10px;
      }
      input,textarea{
        font-family:inherit;
        font-size:17px;
        padding:12px;
        border:none;
        border-radius:6px;
      }
      textarea{min-height:120px;}
      form .boton{align-self:flex-start;}

      /* Pie de página */
      footer{
        background:var(--negro);
        color:var(--blanco);
        text-align:center;
        padding:24px 0;
      }
      footer p{text-align:center;margin:0;}

      /* Foco visible con el teclado */
      a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{
        outline:3px solid var(--rosa);
        outline-offset:3px;
      }

      /* ===== Móvil ===== */
      @media (max-width:900px){
        header .contenedor{flex-direction:column;}
        nav{justify-content:center;gap:16px;}
        .portada-grid,.dos-columnas{grid-template-columns:1fr;}
        .iconos{grid-template-columns:repeat(3,1fr);}
        .blog-grid{grid-template-columns:1fr;}
        .etiqueta{font-size:28px;}
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario -->
    <header>
      <div class="contenedor">
        <a class="logo" href="#inicio">
          <div class="fila"><span class="nombre">Heverton</span><span class="burbuja"></span></div>
          <div class="apellido">Marques</div>
        </a>
        <nav>
          <a href="#reflexion">Reflexión</a>
          <a href="#sobremi">Sobre mí</a>
          <a href="#blog">Blog</a>
          <a class="boton-nav" href="#contacto">Contacto</a>
        </nav>
      </div>
    </header>

    <main>
      <!-- Portada -->
      <div class="portada" id="inicio">
        <div class="contenedor">
          <div class="portada-grid">
            <div>
              <h1 class="etiqueta">Heverton Marques Ferreira Maciel</h1>
              <p>Administrador, alumno y programador. Soy brasileño, vivo en Valencia y me estoy formando en CEAC Valencia para unir mi experiencia en gestión con el desarrollo de software.</p>
              <a class="boton" href="#contacto">Hablemos &rarr;</a>
            </div>
            <div class="foto">
              <img src="heverton.png" alt="Foto de Heverton Marques">
            </div>
          </div>

          <div class="iconos">
            <div>
              <svg viewBox="0 0 24 24"><path d="M12 22s7-7.5 7-13a7 7 0 0 0-14 0c0 5.5 7 13 7 13z"/><circle cx="12" cy="9" r="2.5"/></svg>
              <span>Vivo en Valencia</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>
              <span>De Brasil a España</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></svg>
              <span>Administración</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>
              <span>Programación</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>
              <span>Portugués y español</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10" rx="1"/><path d="M9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4"/></svg>
              <span>IA con criterio</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Reflexión -->
      <section id="reflexion">
        <div class="contenedor">
          <h2 class="titulo">Reflexión</h2>
          <div class="dos-columnas">
            <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
            <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
          </div>
        </div>
      </section>

      <!-- Sobre mí -->
      <section id="sobremi">
        <div class="contenedor">
          <h2 class="titulo">Sobre mí</h2>
          <div class="dos-columnas">
            <p>Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
            <ul class="lista">
              <li>Experiencia en administración y organización de procesos.</li>
              <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
              <li>Idiomas: portugués (nativo) y español.</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Blog -->
      <section id="blog">
        <div class="contenedor">
          <h2 class="titulo">Blog</h2>
          <div class="blog-grid">
            <article>
              <h3>Python sigue en lo más alto del índice TIOBE</h3>
              <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
            </article>
            <article>
              <h4>Rust se consolida entre los diez lenguajes más populares</h4>
              <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
            </article>
            <article>
              <h4>Julia, cerca de volver al top 20</h4>
              <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
            </article>
            <article>
              <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
              <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
            </article>
            <article>
              <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
              <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
            </article>
          </div>
        </div>
      </section>

      <!-- Contacto -->
      <section id="contacto">
        <div class="contenedor">
          <h2 class="titulo">Contacto</h2>
          <div class="dos-columnas">
            <div>
              <p>Si quieres contactar conmigo, puedes escribirme:</p>
              <ul>
                <li>Correo electrónico: <a href="mailto:hevertonmf@gmail.com">hevertonmf@gmail.com</a></li>
                <li>LinkedIn: <a href="https://www.linkedin.com/in/heverton-marques-00a569196/">heverton-marques</a></li>
                <li>Ubicación: Valencia, España</li>
              </ul>
            </div>
            <form>
              <label for="nombre">Introduce tu nombre</label>
              <input type="text" id="nombre" name="nombre">
              <label for="correo">Introduce tu correo</label>
              <input type="email" id="correo" name="correo">
              <label for="mensaje">Introduce tu mensaje</label>
              <textarea id="mensaje" name="mensaje"></textarea>
              <button class="boton" type="submit">Enviar mensaje &rarr;</button>
            </form>
          </div>
        </div>
      </section>
    </main>

    <footer>
      <p>&copy; 2026 Heverton Marques Ferreira Maciel. Todos los derechos reservados.</p>
    </footer>
  </body>
</html>
```

### Ejercicio Lenguajes de marcas 2/1-Ejercicios/006-Validación de documentos HTML y CSS

**001-Recordad validar vuestra web.html**

```html
https://validator.w3.org/
```

**002-codigo actual.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Heverton Marques</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
      form{
      	display:flex;
        flex-direction:column;
        gap:10px;
      }
      #blog{
      	display:grid;
        grid-template-columns:repeat(3,1fr);
         gap:10px;
      }
      #contacto a{
        background:none;
        color:indigo;
        padding:0;
        text-decoration:underline;
}
     img { 
        border: 0; }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario -->
    <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
      <h2>Administrador, alumno y programador</h2>
      <nav>
        <a href="#destacado">Reflexión</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Reflexión</h3>
        <img src="heverton.png" alt="Foto de Heverton Marques">
        <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
        <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
        <ul>
          <li>Experiencia en administración y organización de procesos.</li>
          <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
          <li>Idiomas: portugués (nativo) y español.</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Python sigue en lo más alto del índice TIOBE</h4>
          <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
        </article>
        <article>
          <h4>Rust se consolida entre los diez lenguajes más populares</h4>
          <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
        </article>
        <article>
          <h4>Julia, cerca de volver al top 20</h4>
          <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
        </article>
        <article>
          <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
          <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
        </article>
        <article>
          <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
          <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <p>Si quieres contactar conmigo, puedes escribirme:</p>
        <ul>
          <li>Correo electrónico: <a href="mailto:hevertonmf@gmail.com">hevertonmf@gmail.com</a></li>
          <li>LinkedIn: <a href="https://www.linkedin.com/in/heverton-marques-00a569196/">heverton-marques</a></li>
          <li>Ubicación: Valencia, España</li>
        </ul>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
      <p>&copy; 2026 Heverton Marques Ferreira Maciel. Todos los derechos reservados.</p>
    </footer>
  </body>
</html>
```

**003-corrijo errores.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Heverton Marques</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
      form{
      	display:flex;
        flex-direction:column;
        gap:10px;
      }
      #blog{
      	display:grid;
        grid-template-columns:repeat(3,1fr);
         gap:10px;
      }
      #contacto a{
        background:none;
        color:indigo;
        padding:0;
        text-decoration:underline;
}
     img { 
        border: 0; }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario -->
    <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
      <h2>Administrador, alumno y programador</h2>
      <nav>
        <a href="#destacado">Reflexión</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Reflexión</h3>
        <img src="heverton.png" alt="Foto de Heverton Marques">
        <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
        <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
        <ul>
          <li>Experiencia en administración y organización de procesos.</li>
          <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
          <li>Idiomas: portugués (nativo) y español.</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Python sigue en lo más alto del índice TIOBE</h4>
          <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
        </article>
        <article>
          <h4>Rust se consolida entre los diez lenguajes más populares</h4>
          <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
        </article>
        <article>
          <h4>Julia, cerca de volver al top 20</h4>
          <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
        </article>
        <article>
          <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
          <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
        </article>
        <article>
          <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
          <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <p>Si quieres contactar conmigo, puedes escribirme:</p>
        <ul>
          <li>Correo electrónico: <a href="mailto:hevertonmf@gmail.com">hevertonmf@gmail.com</a></li>
          <li>LinkedIn: <a href="https://www.linkedin.com/in/heverton-marques-00a569196/">heverton-marques</a></li>
          <li>Ubicación: Valencia, España</li>
        </ul>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
      <p>&copy; 2026 Heverton Marques Ferreira Maciel. Todos los derechos reservados.</p>
    </footer>
  </body>
</html>
```

### Ejercicio Lenguajes de marcas 2/1-Ejercicios/007-Lenguajes de marcas para la sindicación de contenidos

**001-Ejercicio final de unidad.md**

```markdown
Lo que tenéis que hacer en esta unidad
Es vuestra propia web, así de sencillo.

Usad tantas etiquetas html como podáis.
Usad las propiedades CSS que hemos visto de momento

Validad la web para que el código sea lo más correcto posible
```

## Ejercicio Lenguajes de marcas 2/2-Proyecto

**022-mi pagina web.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <title>La web de Heverton Marques</title>
    <meta charset="utf-8">
    <style>
      body{
      	background:lightgray;
        font-family:monospace;
      }
      header,main,footer{
      	background:white;
        width:800px;
        margin:auto;
        padding:50px;
      }
      h1{
      	font-size:48px;
      }
      h1{
      	margin:0px;padding:0px;
        font-weight:normal;
      }
      p{
      	text-align:justify;
      }
      a{
      	color:white;
        text-decoration:none;
        background:indigo;
        padding:10px;
      }
      img{
        width:100%;
      }
      form{
      	display:flex;
        flex-direction:column;
        gap:10px;
      }
      #blog{
      	display:grid;
        grid-template-columns:repeat(3,1fr);
         gap:10px;
      }
      #contacto a{
        background:none;
        color:indigo;
        padding:0;
        text-decoration:underline;
}
      img { 
        border: 0; }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario -->
    <header>
      <h1>Heverton Marques Ferreira Maciel</h1>
      <h2>Administrador, alumno y programador</h2>
      <nav>
        <a href="#destacado">Reflexión</a>
        <a href="#sobremi">Sobre mi</a>
        <a href="#blog">Blog</a>
        <a href="#contacto">Contacto</a>
      </nav>
    </header>
    <main>
      <section id="destacado">
        <h3>Reflexión</h3>
        <img src="heverton.png" alt="Foto de Heverton Marques">
        <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
        <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
      </section>
      <section id="sobremi">
        <h3>Sobre mi</h3>
        <p>Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
        <ul>
          <li>Experiencia en administración y organización de procesos.</li>
          <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
          <li>Idiomas: portugués (nativo) y español.</li>
        </ul>
        <table border=1>
          <thead>
          	<tr>
              <th>Lunes</th>
              <th>Martes</th>
              <th>Miércoles</th>
              <th>Jueves</th>
              <th>Viernes</th>
            </tr>
          </thead>
          <tbody>
          	<tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Sistemas informáticos</td>
          	</tr>
            <tr>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Programación</td>
              <td>Inglés</td>
          	</tr>
            <tr>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>Bases de datos</td>
              <td>IPE</td>
              <td>Lenguajes de marcas</td>
          	</tr>
          </tbody>
        </table>
      </section>
      <section id="blog">
        <h3>Blog</h3>
        <article>
          <h4>Python sigue en lo más alto del índice TIOBE</h4>
          <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
        </article>
        <article>
          <h4>Rust se consolida entre los diez lenguajes más populares</h4>
          <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
        </article>
        <article>
          <h4>Julia, cerca de volver al top 20</h4>
          <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
        </article>
        <article>
          <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
          <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
        </article>
        <article>
          <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
          <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
        </article>
      </section>
      <section id="contacto">
        <h3>Contacto</h3>
        <p>Si quieres contactar conmigo, puedes escribirme:</p>
        <ul>
          <li>Correo electrónico: <a href="mailto:hevertonmf@gmail.com">hevertonmf@gmail.com</a></li>
          <li>LinkedIn: <a href="https://www.linkedin.com/in/heverton-marques-00a569196/">heverton-marques</a></li>
          <li>Ubicación: Valencia, España</li>
        </ul>
        <form>
          <label>Introduce tu nombre</label>
          <input type="text" name="nombre">
          <label>Introduce tu correo</label>
          <input type="email" name="correo">
          <label>Introduce tu mensaje</label>
          <textarea name="mensaje"></textarea>
          <input type="submit">
        </form>
      </section>
    </main>
    <footer>
      <p>&copy; 2026 Heverton Marques Ferreira Maciel. Todos los derechos reservados.</p>
    </footer>
  </body>
</html>
```

**023-ahora com IA.html**

```html
<!doctype html>
<html lang="es">
  <head>
    <!-- Se transmite al navegador -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>La web de Heverton Marques</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;700;800&display=swap" rel="stylesheet">
    <style>
      /* ===== Colores y medidas ===== */
      :root{
        --morado:#5b3fa6;
        --rosa:#e06be0;
        --morado-oscuro:#3d2a7a;
        --negro:#000;
        --blanco:#fff;
        --degradado:linear-gradient(100deg,var(--morado),var(--rosa));
        --ancho:1100px;
      }
      *{box-sizing:border-box;}
      body{
        margin:0;
        font-family:"Barlow",Arial,sans-serif;
        color:#1d1433;
        background:var(--blanco);
        line-height:1.6;
      }
      .contenedor{
        max-width:var(--ancho);
        margin:auto;
        padding:0 30px;
      }
      p{text-align:justify;}

      /* ===== Cabecera ===== */
      header{
        background:var(--blanco);
        position:sticky;
        top:0;
        z-index:10;
        box-shadow:0 1px 0 #e7e2f3;
      }
      header .contenedor{
        display:flex;
        align-items:center;
        justify-content:space-between;
        padding-top:14px;
        padding-bottom:14px;
        gap:20px;
      }
      .logo{
        text-decoration:none;
        color:var(--negro);
        line-height:1;
      }
      .logo .fila{
        display:flex;
        align-items:center;
        gap:8px;
      }
      .logo .nombre{
        font-weight:300;
        font-size:22px;
      }
      .logo .burbuja{
        width:90px;
        height:22px;
        background:var(--degradado);
        border-radius:12px 12px 12px 0;
      }
      .logo .apellido{
        font-weight:800;
        font-size:38px;
        letter-spacing:-1px;
      }
      nav{
        display:flex;
        align-items:center;
        gap:28px;
        flex-wrap:wrap;
      }
      nav a{
        color:var(--morado-oscuro);
        text-decoration:none;
        text-transform:uppercase;
        font-weight:500;
        font-size:16px;
      }
      nav a:hover{color:var(--rosa);}
      nav a.boton-nav{
        background:var(--degradado);
        color:var(--blanco);
        padding:10px 26px;
        border-radius:6px;
      }

      /* ===== Portada con degradado ===== */
      .portada{
        position:relative;
        overflow:hidden;
        background:var(--degradado);
        color:var(--blanco);
        padding:70px 0 50px;
      }
      /* Líneas diagonales de las esquinas */
      .portada::before,
      .portada::after{
        content:"";
        position:absolute;
        width:220px;
        height:220px;
        background:repeating-linear-gradient(-60deg,transparent 0 16px,rgba(0,0,0,.45) 16px 18px);
      }
      .portada::before{
        top:0;left:0;
        clip-path:polygon(0 0,45% 0,0 45%);
      }
      .portada::after{
        bottom:0;right:0;
        clip-path:polygon(100% 30%,100% 100%,30% 100%);
      }
      .portada .contenedor{
        position:relative;
        z-index:1;
      }
      .portada-grid{
        display:grid;
        grid-template-columns:1.2fr 1fr;
        gap:50px;
        align-items:center;
      }
      .etiqueta{
        display:inline-block;
        background:var(--negro);
        color:var(--blanco);
        font-weight:400;
        font-size:36px;
        line-height:1.2;
        padding:6px 24px;
        margin:0 0 24px;
      }
      .portada p{
        font-size:20px;
        max-width:560px;
      }
      .boton{
        display:inline-flex;
        align-items:center;
        gap:10px;
        margin-top:20px;
        background:var(--negro);
        color:var(--blanco);
        text-decoration:none;
        text-transform:uppercase;
        font-size:18px;
        padding:12px 30px;
        border-radius:6px;
        border:none;
        font-family:inherit;
        cursor:pointer;
      }
      .boton:hover{background:var(--morado-oscuro);}

      /* Foto con bocadillo negro detrás */
      .foto{
        position:relative;
        max-width:380px;
        justify-self:center;
      }
      .foto::before{
        content:"";
        position:absolute;
        inset:-18px 40px 40px -18px;
        background:var(--negro);
        border-radius:22px 22px 22px 0;
      }
      .foto img{
        position:relative;
        display:block;
        width:100%;
        aspect-ratio:4/5;
        object-fit:cover;
        border-radius:16px;
        background:rgba(255,255,255,.2);
        border:0;
      }

      /* Iconos de la portada */
      .iconos{
        display:grid;
        grid-template-columns:repeat(6,1fr);
        gap:20px;
        margin-top:80px;
        text-align:center;
      }
      .iconos svg{
        width:54px;
        height:54px;
        fill:none;
        stroke:var(--negro);
        stroke-width:2.2;
        stroke-linecap:round;
        stroke-linejoin:round;
      }
      .iconos span{
        display:block;
        font-weight:500;
        font-size:19px;
        line-height:1.2;
        margin-top:10px;
      }

      /* ===== Secciones ===== */
      section{
        padding:80px 0;
        scroll-margin-top:80px;
      }
      .titulo{
        display:inline-block;
        background:var(--negro);
        color:var(--blanco);
        font-weight:400;
        font-size:32px;
        padding:4px 22px;
        margin:0 0 30px;
      }
      .dos-columnas{
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:50px;
        font-size:18px;
      }

      /* Sobre mí */
      #sobremi{background:#f5f1fb;}
      .lista{
        list-style:none;
        padding:0;
        margin:0;
      }
      .lista li{
        padding:14px 0 14px 34px;
        border-bottom:2px solid #e2d8f2;
        position:relative;
      }
      .lista li::before{
        content:"";
        position:absolute;
        left:0;
        top:20px;
        width:16px;
        height:16px;
        background:var(--degradado);
        border-radius:6px 6px 6px 0;
      }

      /* Blog */
      .blog-grid{
        display:grid;
        grid-template-columns:repeat(3,1fr);
        gap:24px;
      }
      article{
        border:2px solid var(--negro);
        border-radius:6px;
        padding:24px;
        border-top:10px solid var(--rosa);
      }
      article:nth-child(odd){border-top-color:var(--morado);}
      article h4{
        font-size:21px;
        line-height:1.25;
        margin:0 0 12px;
      }
      article p{margin:0;}

      /* Contacto */
      #contacto{
        background:var(--degradado);
        color:var(--blanco);
      }
      #contacto ul{
        list-style:none;
        padding:0;
        font-size:19px;
      }
      #contacto li{margin-bottom:12px;}
      #contacto li a{
        color:var(--blanco);
        font-weight:700;
      }
      form{
        display:flex;
        flex-direction:column;
        gap:10px;
      }
      input,textarea{
        font-family:inherit;
        font-size:17px;
        padding:12px;
        border:none;
        border-radius:6px;
      }
      textarea{min-height:120px;}
      form .boton{align-self:flex-start;}

      /* Pie de página */
      footer{
        background:var(--negro);
        color:var(--blanco);
        text-align:center;
        padding:24px 0;
      }
      footer p{text-align:center;margin:0;}

      /* Foco visible con el teclado */
      a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible{
        outline:3px solid var(--rosa);
        outline-offset:3px;
      }

      /* ===== Móvil ===== */
      @media (max-width:900px){
        header .contenedor{flex-direction:column;}
        nav{justify-content:center;gap:16px;}
        .portada-grid,.dos-columnas{grid-template-columns:1fr;}
        .iconos{grid-template-columns:repeat(3,1fr);}
        .blog-grid{grid-template-columns:1fr;}
        .etiqueta{font-size:28px;}
      }
    </style>
  </head>
  <body>
    <!-- Se enseña al usuario -->
    <header>
      <div class="contenedor">
        <a class="logo" href="#inicio">
          <div class="fila"><span class="nombre">Heverton</span><span class="burbuja"></span></div>
          <div class="apellido">Marques</div>
        </a>
        <nav>
          <a href="#reflexion">Reflexión</a>
          <a href="#sobremi">Sobre mí</a>
          <a href="#blog">Blog</a>
          <a class="boton-nav" href="#contacto">Contacto</a>
        </nav>
      </div>
    </header>

    <main>
      <!-- Portada -->
      <div class="portada" id="inicio">
        <div class="contenedor">
          <div class="portada-grid">
            <div>
              <h1 class="etiqueta">Heverton Marques Ferreira Maciel</h1>
              <p>Administrador, alumno y programador. Soy brasileño, vivo en Valencia y me estoy formando en CEAC Valencia para unir mi experiencia en gestión con el desarrollo de software.</p>
              <a class="boton" href="#contacto">Hablemos &rarr;</a>
            </div>
            <div class="foto">
              <img src="heverton.png" alt="Foto de Heverton Marques">
            </div>
          </div>

          <div class="iconos">
            <div>
              <svg viewBox="0 0 24 24"><path d="M12 22s7-7.5 7-13a7 7 0 0 0-14 0c0 5.5 7 13 7 13z"/><circle cx="12" cy="9" r="2.5"/></svg>
              <span>Vivo en Valencia</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>
              <span>De Brasil a España</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></svg>
              <span>Administración</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>
              <span>Programación</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>
              <span>Portugués y español</span>
            </div>
            <div>
              <svg viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10" rx="1"/><path d="M9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4"/></svg>
              <span>IA con criterio</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Reflexión -->
      <section id="reflexion">
        <div class="contenedor">
          <h2 class="titulo">Reflexión</h2>
          <div class="dos-columnas">
            <p>La informática ha pasado de ser una herramienta de oficina a convertirse en la base de casi todo lo que hacemos: trabajar, estudiar, comunicarnos y gestionar nuestra vida diaria. Hoy la inteligencia artificial (IA) da un paso más, porque ya no solo ejecuta instrucciones, sino que ayuda a escribir código, analizar datos y tomar decisiones.</p>
            <p>Creo que la IA no sustituye a las personas que saben programar, sino que multiplica lo que pueden hacer. Por eso es más importante que nunca entender los fundamentos: saber cómo funciona un programa, revisar lo que genera una máquina y usar la tecnología con criterio y responsabilidad. Aprender informática hoy no es solo aprender un lenguaje, es aprender a pensar, a resolver problemas y a adaptarse a un cambio constante.</p>
          </div>
        </div>
      </section>

      <!-- Sobre mí -->
      <section id="sobremi">
        <div class="contenedor">
          <h2 class="titulo">Sobre mí</h2>
          <div class="dos-columnas">
            <p>Me dedico a la administración y a la tecnología. Soy brasileño, vivo en España y actualmente estudio en CEAC Valencia, donde me estoy formando como programador para unir mi experiencia en gestión con el desarrollo de software.</p>
            <ul class="lista">
              <li>Experiencia en administración y organización de procesos.</li>
              <li>Formación en programación y desarrollo web (HTML, XML y más) en CEAC Valencia.</li>
              <li>Idiomas: portugués (nativo) y español.</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Blog -->
      <section id="blog">
        <div class="contenedor">
          <h2 class="titulo">Blog</h2>
          <div class="blog-grid">
            <article>
              <h3>Python sigue en lo más alto del índice TIOBE</h3>
              <p>En el índice TIOBE de septiembre de 2026 el top 10 no cambia: Python mantiene el primer puesto, aunque su popularidad baja del 18 %, y C++ amplía su ventaja sobre Java.</p>
            </article>
            <article>
              <h4>Rust se consolida entre los diez lenguajes más populares</h4>
              <p>Rust entró por primera vez en el top 10 de TIOBE en julio de 2026 y se ha mantenido en el puesto 10, subiendo su índice del 1,34 % al 1,45 % en agosto. Es uno de los lenguajes que más crece por su seguridad en la gestión de memoria.</p>
            </article>
            <article>
              <h4>Julia, cerca de volver al top 20</h4>
              <p>El lenguaje Julia alcanzó el puesto 21 en el índice de septiembre de 2026, gracias a su uso creciente en computación científica, modelado y procesamiento de datos, mientras MATLAB sigue perdiendo posiciones.</p>
            </article>
            <article>
              <h4>KDE debate cómo usar la IA en el desarrollo de software libre</h4>
              <p>La comunidad KDE está en el centro de la conversación por una propuesta para definir una política oficial sobre el uso de modelos de lenguaje (LLM) en sus proyectos. El debate muestra que la IA ya forma parte del día a día de los programadores.</p>
            </article>
            <article>
              <h4>Microsoft presenta Project Zenith para desarrolladores</h4>
              <p>Microsoft ha presentado Project Zenith, un entorno de Windows listo para programar, con herramientas preconfiguradas y soporte para IA local en el propio ordenador del desarrollador.</p>
            </article>
          </div>
        </div>
      </section>

      <!-- Contacto -->
      <section id="contacto">
        <div class="contenedor">
          <h2 class="titulo">Contacto</h2>
          <div class="dos-columnas">
            <div>
              <p>Si quieres contactar conmigo, puedes escribirme:</p>
              <ul>
                <li>Correo electrónico: <a href="mailto:hevertonmf@gmail.com">hevertonmf@gmail.com</a></li>
                <li>LinkedIn: <a href="https://www.linkedin.com/in/heverton-marques-00a569196/">heverton-marques</a></li>
                <li>Ubicación: Valencia, España</li>
              </ul>
            </div>
            <form>
              <label for="nombre">Introduce tu nombre</label>
              <input type="text" id="nombre" name="nombre">
              <label for="correo">Introduce tu correo</label>
              <input type="email" id="correo" name="correo">
              <label for="mensaje">Introduce tu mensaje</label>
              <textarea id="mensaje" name="mensaje"></textarea>
              <button class="boton" type="submit">Enviar mensaje &rarr;</button>
            </form>
          </div>
        </div>
      </section>
    </main>

    <footer>
      <p>&copy; 2026 Heverton Marques Ferreira Maciel. Todos los derechos reservados.</p>
    </footer>
  </body>
</html>
```

## Ejercicio Lenguajes de marcas 2/3-Resultado de aprendizaje

**Resultado de aprendizaje.md**

```markdown
Resultado de aprendizaje


**a)** Sí. HTML5, CSS3, SVG, XML y RSS/Atom. Mis páginas usan HTML5, CSS3 y SVG.

**b)** Sí. `doctype`, `<html>`, `<head>` (metadatos y estilos) y `<body>` con `header`, `nav`, `main`, `section` y `footer`.

**c)** Sí. Uso títulos, párrafos, listas, enlaces, imágenes, tablas y formularios, con atributos como `id`, `class`, `href` y `alt`.

**d)** Sí. HTML5 añade etiquetas semánticas y quita atributos de diseño como `border=1`, que ahora se hacen con CSS.

**e)** Sí. Editor de código, navegador, herramientas de desarrollo e IA en la 023.

**f)** Sí. Separan contenido y diseño, y con un solo cambio se modifica toda la web.

**g)** Sí. CSS básico en la 022; variables, degradados, `grid` y `@media` para móvil en la 023.

**h)** Sí. Encontré `border=1` obsoleto en la 022 y títulos `h3`/`h4` mezclados en la 023. Se valida en validator.w3.org.

**i)** Sí. Se basa en XML con los formatos RSS y Atom.

**j)** Sí. Se usa en blogs, noticias y podcasts. Mi sección Blog podría tener un RSS.
```

