# Reporte de proyecto

## Información de generación

- **Fecha:** 3/10/2026, 18:51:26
- **Proyecto documentado:** `Ejercicio base da dados 1`
- **Generador:** jocarsa | documentacion
- **Procesamiento:** local en navegador

## Estructura del proyecto

```text
└── Ejercicio base da dados 1
    ├── 1-Ejercicios
    │   ├── 001-Ficheros (planos, indexados, acceso directo, entre otros)
    │   │   ├── 000-instruciones.md
    │   │   ├── 001-agenda.txt
    │   │   ├── 002- agenda.csv
    │   │   └── 003-mejora genda.csv
    │   ├── 002-Bases de datos. Conceptos, usos y tipos según el modelo de datos, la ubicación de la información
    │   │   ├── 001-empresa 1
    │   │   │   ├── clientes.csv
    │   │   │   └── produtos.csv
    │   │   └── 002-empresa 2
    │   │       ├── clientes.csv
    │   │       └── produtos.csv
    │   ├── 003-Sistemas gestores de base de datos Funciones, componentes y tipos
    │   │   ├── 000-introducion.md
    │   │   ├── 001-definiciones.md
    │   │   ├── 002-repasso de questiones.md
    │   │   └── 003-instalar un sistema de gestao de base de dados.md
    │   ├── 007-Ejercicio final de unidad
    │   │   ├── 001-tipos de ficheros.md
    │   │   ├── 002-base de datos en carpetas con csv.md
    │   │   ├── 003-como instalar mysql.md
    │   │   └── ejercicio.md
    │   └── 100-repasso
    │       └── 001-recuerdo.md
    ├── 2-Proyecto
    │   ├── 000-introdución.md
    │   ├── 001-tipos de ficheros.md
    │   ├── 002-base de datos en carpetas con csv.md
    │   └── 003-como instalar mysql.md
    └── 3-Resultado de aprendizaje
        └── criterios bases de datos.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite.

## Código (intercalado)

### Ejercicio base da dados 1/1-Ejercicios/001-Ficheros (planos, indexados, acceso directo, entre otros)

**000-instruciones.md**

```markdown
```

**001-agenda.txt**

```text
Jaime 636435646
Jose 36456436
Juan 6435646
Jorge 6435646
Jose Vicente 634564
```

### Ejercicio base da dados 1/1-Ejercicios/003-Sistemas gestores de base de datos Funciones, componentes y tipos

**000-introducion.md**

```markdown
```

**001-definiciones.md**

```markdown
Programas informáticos
E0.0.nvuelven y protegen a los datos"
Tu no manejas la base de datos
Tú le pides cosas al sistema de gestión de bases de datos
Y el sistema decide si te las da o no

Cuando hay problema de concurrencia
Cuando hay problema de seguridad
Cuando hay problema de tamaño

SQL = Search Query Language
```

**002-repasso de questiones.md**

```markdown
editor.jocarsa.com -> Solo para el código que estoy haciendo en este momento

Cuando acaba el día, subo todo el código a GitHub:
https://github.com/jocarsa/ceac2627dam1
```

**003-instalar un sistema de gestao de base de dados.md**

```markdown
estar en Ubuntu
2.-Abrimos Terminal (Control + Alt + T)
3.-Actualizamos paquetes: sudo apt update
4.-Ponemos: sudo apt install mysql-server
5.-Introducís: mysql_secure_installation

sudo = super user do
apt = gestor de paquetes
install = quiero instalar un paquete
mysql-server = el paquete que quiero instalar

6.-Accedemos a MySQL con:
sudo mysql -u root -p

sudo = super user do
mysql = invocamos al gestor de bases de datos
-u = te paso el usuario
root = el nombre del usuario
-p = pideme la contraña

7.-Salir de mysql: exit;
```

### Ejercicio base da dados 1/1-Ejercicios/007-Ejercicio final de unidad

**001-tipos de ficheros.md**

```markdown
# Tipos de ficheros

**Fichero plano (TXT):** texto libre, sin estructura. Difícil de procesar.
```
Heverton Marques 634564
```

**CSV:** texto con estructura. Primera línea = cabecera, cada línea = registro, la coma separa campos.
```
id,nombre,telefono,email
1,Juan,6346346,juan@garcia.com
```

El `id` es único para cada registro (idea de **clave primaria**).
```

**002-base de datos en carpetas con csv.md**

```markdown
# Base de datos en carpetas con CSV

- **Carpeta** = base de datos (ej: `empresa 1`, `empresa 2`)
- **Fichero CSV** = tabla (ej: `clientes.csv`, `produtos.csv`)
- **Cabecera** = columnas
- **Cada línea** = registro

**Problemas:** concurrencia, seguridad y tamaño. Por eso se usa un SGBD.
```

**003-como instalar mysql.md**

```markdown
# Cómo instalar MySQL (Ubuntu)

1. Abrir terminal: `Ctrl + Alt + T`
2. `sudo apt update`
3. `sudo apt install mysql-server`
4. `sudo mysql_secure_installation`
5. Entrar: `sudo mysql -u root -p`
6. Salir: `exit;`

`sudo` = superusuario · `-u root` = usuario root · `-p` = pide contraseña
```

**ejercicio.md**

```markdown
Elabora un resumen como ejercicio final de todo 
lo que hemos visto en esta unidad

Tipos de ficheros, planos, txt, csv

Base de datos en carpetas con csv

Como instalar MySQL


```

### Ejercicio base da dados 1/1-Ejercicios/100-repasso

**001-recuerdo.md**

```markdown
1.-Entramos en Linux
2.-Accedemos a la terminal
3.-sudo mysql -u root -p

sudo = super usuario hace
mysql = motor de bases de datos
-u = el usuario con el que voy a entrar
root = el nombre de usuario
-p = preguntame la contraseña


```

## Ejercicio base da dados 1/2-Proyecto

**000-introdución.md**

```markdown
```

**001-tipos de ficheros.md**

```markdown
# Tipos de ficheros

**Fichero plano (TXT):** texto libre, sin estructura. Difícil de procesar.
```
Heverton Marques 634564
```

**CSV:** texto con estructura. Primera línea = cabecera, cada línea = registro, la coma separa campos.
```
id,nombre,telefono,email
1,Juan,6346346,juan@garcia.com
```

El `id` es único para cada registro (idea de **clave primaria**).
```

**002-base de datos en carpetas con csv.md**

```markdown
# Base de datos en carpetas con CSV

- **Carpeta** = base de datos (ej: `empresa 1`, `empresa 2`)
- **Fichero CSV** = tabla (ej: `clientes.csv`, `produtos.csv`)
- **Cabecera** = columnas
- **Cada línea** = registro

**Problemas:** concurrencia, seguridad y tamaño. Por eso se usa un SGBD.
```

**003-como instalar mysql.md**

```markdown
# Cómo instalar MySQL (Ubuntu)

1. Abrir terminal: `Ctrl + Alt + T`
2. `sudo apt update`
3. `sudo apt install mysql-server`
4. `sudo mysql_secure_installation`
5. Entrar: `sudo mysql -u root -p`
6. Salir: `exit;`

`sudo` = superusuario · `-u root` = usuario root · `-p` = pide contraseña
```

## Ejercicio base da dados 1/3-Resultado de aprendizaje

**criterios bases de datos.md**

```markdown
# Criterios de evaluación: Bases de datos

**a) ¿Se han analizado los sistemas lógicos de almacenamiento y sus características?**

Sí. Aprendí que los datos se pueden guardar en tablas, como en un Excel. En el ejercicio guardé clientes, productos y pedidos en tablas.

**b) ¿Se han identificado los distintos tipos de bases de datos según el modelo de datos utilizado?**

Sí. Hay varios tipos. El que usé yo es el relacional, que guarda los datos en tablas que se conectan entre sí.

**c) ¿Se han identificado los distintos tipos de bases de datos en función de la ubicación de la información?**

Sí. Una base de datos puede estar en un solo lugar o repartida en varios. La mía está en un solo lugar, en mi ordenador.

**d) ¿Se ha evaluado la utilidad de un sistema gestor de bases de datos?**

Sí. Sirve para guardar muchos datos ordenados y encontrarlos rápido. También ayuda a que no haya errores, por ejemplo, revisa que el email esté bien escrito.

**e) ¿Se ha reconocido la función de cada uno de los elementos de un sistema gestor de bases de datos?**

Sí. Unos comandos sirven para crear las tablas y otros para meter datos y mirarlos. En el ejercicio usé `CREATE TABLE` para crear, `INSERT` para añadir y `SELECT` para ver los datos.

**f) ¿Se han clasificado los sistemas gestores de bases de datos?**

Sí. Hay muchos, como MySQL, Oracle y MongoDB. Unos son gratis y otros de pago. Yo usé MySQL, que es gratis.

**g) ¿Se ha reconocido la utilidad de las bases de datos distribuidas?**

Sí. Son bases de datos con los datos repartidos en varios ordenadores. Sirven para que, si uno falla, el resto siga funcionando, y para empresas con muchas oficinas.

**h) ¿Se han analizado las políticas de fragmentación de la información?**

Sí. Fragmentar es partir los datos en trozos. Por ejemplo, separar los pedidos por año o los clientes por ciudad, para que sea más fácil manejarlos.

**i) ¿Se ha identificado la legislación vigente sobre protección de datos?**

Sí. En España la ley es el RGPD. Dice que los datos de las personas, como el nombre, el teléfono o el email, hay que cuidarlos y no usarlos sin permiso. En el ejercicio usé datos inventados.

**j) ¿Se han reconocido los conceptos de Big Data y de la inteligencia de negocios?**

Sí. Big Data es cuando hay tantísimos datos que una base normal no puede con ellos. La inteligencia de negocios es usar los datos para tomar mejores decisiones, por ejemplo, saber qué producto se vende más.
```

