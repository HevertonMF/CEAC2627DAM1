# Primero importo las librerías
import mysql.connector                                  # Importo MySQL
from flask import Flask, request, redirect              # Importo Flask
from html import escape                                 # Para mostrar texto de BD de forma segura
from urllib.parse import quote                          # Para pasar texto por la URL


# Datos de conexión a la base de datos
DATOS_BD = {
    "host": "localhost",
    "user": "encuentrame",
    "password": "Encuentrame123$",
    "database": "encuentrame"
}


# Abro una conexión nueva en cada petición (así no se cae si MySQL la cierra)
def conectar():
    return mysql.connector.connect(**DATOS_BD)


# Ahora creo una aplicación base
# La carpeta "logo" se sirve en /logo
aplicacion = Flask(__name__, static_folder="logo", static_url_path="/logo")


# -------------------------------------------------
# ESTILOS (los comparten todas las páginas)
# -------------------------------------------------

ESTILOS = """
<style>

    :root{
        --fondo:#FFFFFF;
        --superficie:#F3EEFA;
        --tinta:#3A2A5C;
        --tinta-suave:#5E5378;
        --tinta-gris:#9389A8;
        --morado:#8E6FAE;
        --morado-fuerte:#6E4E9A;
        --lima:#D3E39A;
        --lima-fuerte:#C2D683;
        --borde:rgba(58,42,92,0.12);
        --ok:#3F4A25;
        --ok-fondo:#F1F6DD;
    }

    @media (prefers-color-scheme: dark){
        :root{
            --fondo:#241A38;
            --superficie:#2F2347;
            --tinta:#F3EEFA;
            --tinta-suave:#CBBFE0;
            --tinta-gris:#9C8FB8;
            --morado:#B69BD6;
            --morado-fuerte:#CDB8E6;
            --borde:rgba(243,238,250,0.14);
            --ok:#D3E39A;
            --ok-fondo:#3F4A25;
        }
    }

    *{
        box-sizing:border-box;
    }

    body{
        margin:0;
        font-family:Calibri, 'Carlito', 'Segoe UI', sans-serif;
        background:var(--fondo);
        color:var(--tinta);
        line-height:1.55;
    }

    .contenedor{
        max-width:1100px;
        margin:auto;
        padding:0 20px;
    }


    /* ----------------------------- */
    /* CABECERA                      */
    /* ----------------------------- */

    header{
        border-bottom:1px solid var(--borde);
    }

    .cabecera{
        display:flex;
        align-items:center;
        justify-content:space-between;
        padding:16px 0;
    }

    .logo{
        display:flex;
        align-items:center;
        gap:10px;
        text-decoration:none;
        color:var(--tinta);
        text-transform:uppercase;
        letter-spacing:0.4em;
        font-size:13px;
    }

    .logo img{
        width:38px;
        height:38px;
        border-radius:50%;
        background:#F7F4EE;
    }

    .menu a{
        color:var(--tinta-suave);
        text-decoration:none;
        margin-left:20px;
        font-weight:bold;
        font-size:14px;
    }

    .menu a:hover{
        color:var(--morado-fuerte);
    }


    /* ----------------------------- */
    /* BOTONES                       */
    /* ----------------------------- */

    .boton{
        display:inline-block;
        border:0;
        background:var(--lima);
        color:#3A2A5C;
        padding:12px 26px;
        border-radius:999px;
        font-weight:bold;
        font-size:15px;
        cursor:pointer;
        text-decoration:none;
        font-family:inherit;
    }

    .boton:hover{
        background:var(--lima-fuerte);
    }

    .boton-borde{
        background:transparent;
        border:1px solid rgba(255,255,255,0.75);
        color:white;
    }

    .boton-borde:hover{
        background:rgba(255,255,255,0.12);
    }

    .boton-pequeno{
        padding:8px 16px;
        font-size:13px;
    }


    /* ----------------------------- */
    /* HERO                          */
    /* ----------------------------- */

    .hero{
        margin-top:28px;
        padding:60px 50px;
        border-radius:22px;
        color:white;
        background:linear-gradient(135deg, #7A5A9E 0%, #A07FBE 45%, #6A4C93 100%);
    }

    .hero .mini{
        letter-spacing:0.4em;
        text-transform:uppercase;
        font-size:12px;
        opacity:0.85;
    }

    .hero h1{
        font-size:48px;
        line-height:1.1;
        margin:15px 0;
        max-width:650px;
    }

    .hero p{
        font-size:18px;
        max-width:520px;
        margin-bottom:28px;
    }


    /* ----------------------------- */
    /* PASOS                         */
    /* ----------------------------- */

    .pasos{
        display:grid;
        grid-template-columns:repeat(4,1fr);
        gap:16px;
        margin-top:40px;
    }

    .paso{
        background:var(--superficie);
        border-radius:18px;
        padding:22px;
    }

    .paso .numero{
        width:42px;
        height:42px;
        border-radius:50%;
        background:var(--morado);
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;
        font-weight:bold;
        font-size:19px;
        margin-bottom:14px;
    }

    .paso h3{
        margin:0 0 8px 0;
    }

    .paso p{
        margin:0;
        color:var(--tinta-suave);
    }


    /* ----------------------------- */
    /* BUSCADOR Y FILTROS            */
    /* ----------------------------- */

    main{
        margin:50px auto;
    }

    .titulo-seccion{
        display:flex;
        justify-content:space-between;
        align-items:end;
        margin-bottom:20px;
        gap:20px;
    }

    .titulo-seccion h2{
        margin:0;
        font-size:32px;
    }

    .titulo-seccion p{
        margin:5px 0 0 0;
        color:var(--tinta-suave);
    }

    .contador{
        color:var(--tinta-gris);
        font-size:14px;
        white-space:nowrap;
    }

    #busqueda{
        width:100%;
        padding:12px 18px;
        border-radius:999px;
        border:1px solid var(--borde);
        background:var(--fondo);
        color:var(--tinta);
        font-size:15px;
        font-family:inherit;
        outline:none;
        margin-bottom:14px;
    }

    #busqueda:focus{
        border-color:var(--morado);
    }

    .filtros{
        display:flex;
        flex-wrap:wrap;
        gap:8px;
        margin-bottom:24px;
    }

    .filtro{
        padding:7px 13px;
        border-radius:999px;
        border:1px solid var(--borde);
        background:var(--fondo);
        color:var(--tinta-suave);
        cursor:pointer;
        font-family:inherit;
        font-size:13px;
    }

    .filtro.activo{
        background:var(--lima);
        border-color:var(--lima);
        color:#3A2A5C;
        font-weight:bold;
    }


    /* ----------------------------- */
    /* TARJETAS DE PSICÓLOGOS        */
    /* ----------------------------- */

    #psicologos{
        display:grid;
        grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
        gap:18px;
    }

    article{
        border:1px solid var(--borde);
        border-radius:18px;
        padding:20px;
        display:flex;
        flex-direction:column;
        gap:10px;
        transition:transform 0.2s, box-shadow 0.2s;
    }

    article:hover{
        transform:translateY(-4px);
        box-shadow:0 12px 30px rgba(58,42,92,0.12);
    }

    .cabeza{
        display:flex;
        align-items:center;
        gap:12px;
    }

    .avatar{
        width:46px;
        height:46px;
        border-radius:50%;
        color:white;
        display:flex;
        align-items:center;
        justify-content:center;
        font-weight:bold;
        flex-shrink:0;
    }

    article h3{
        margin:0;
        font-size:17px;
    }

    .etiquetas{
        display:flex;
        flex-wrap:wrap;
        gap:6px;
    }

    .etiqueta{
        font-size:11.5px;
        font-weight:bold;
        padding:4px 9px;
        border-radius:999px;
        background:var(--superficie);
        color:var(--morado-fuerte);
    }

    .bio{
        color:var(--tinta-suave);
        font-size:13.5px;
        margin:0;
        flex:1;
    }

    .vacio{
        display:none;
        text-align:center;
        padding:40px;
        color:var(--tinta-suave);
    }


    /* ----------------------------- */
    /* VENTANA DE SOLICITUD          */
    /* ----------------------------- */

    dialog{
        border:0;
        border-radius:18px;
        padding:28px;
        max-width:520px;
        width:calc(100% - 32px);
        background:var(--fondo);
        color:var(--tinta);
    }

    dialog::backdrop{
        background:rgba(10,14,9,0.55);
    }

    .cerrar{
        float:right;
        border:0;
        background:none;
        font-size:20px;
        cursor:pointer;
        color:var(--tinta);
    }

    .campo{
        margin-bottom:14px;
    }

    .campo label{
        display:block;
        font-size:13px;
        font-weight:bold;
        color:var(--tinta-suave);
        margin-bottom:5px;
    }

    .campo input,
    .campo textarea{
        width:100%;
        padding:10px 12px;
        border:1px solid var(--borde);
        border-radius:9px;
        background:var(--fondo);
        color:var(--tinta);
        font-family:inherit;
        font-size:15px;
    }

    .campo textarea{
        min-height:90px;
        resize:vertical;
    }

    .opciones label{
        display:inline;
        font-weight:normal;
        margin-right:15px;
    }


    /* ----------------------------- */
    /* AVISOS Y SOLICITUDES          */
    /* ----------------------------- */

    .aviso{
        background:var(--ok-fondo);
        color:var(--ok);
        padding:14px 18px;
        border-radius:10px;
        margin-top:20px;
        font-weight:bold;
    }

    .solicitud{
        border:1px solid var(--borde);
        border-radius:18px;
        padding:16px 18px;
        margin-bottom:12px;
    }

    .solicitud .meta{
        color:var(--tinta-suave);
        font-size:13px;
    }

    .estado{
        font-size:11.5px;
        font-weight:bold;
        padding:3px 9px;
        border-radius:999px;
        background:var(--superficie);
        color:var(--morado-fuerte);
    }

    .estado.contactado{
        background:var(--ok-fondo);
        color:var(--ok);
    }

    .selector{
        padding:10px 14px;
        border-radius:999px;
        border:1px solid var(--borde);
        background:var(--fondo);
        color:var(--tinta);
        font-family:inherit;
        font-size:15px;
    }


    /* ----------------------------- */
    /* FOOTER                        */
    /* ----------------------------- */

    footer{
        border-top:1px solid var(--borde);
        padding:30px 20px;
        text-align:center;
        font-size:13px;
        color:var(--tinta-gris);
    }


    /* ----------------------------- */
    /* RESPONSIVE                    */
    /* ----------------------------- */

    @media(max-width:820px){

        .pasos{
            grid-template-columns:1fr 1fr;
        }

        .hero{
            padding:40px 26px;
        }

        .hero h1{
            font-size:34px;
        }

    }

    @media(max-width:500px){

        .pasos{
            grid-template-columns:1fr;
        }

        .logo span{
            display:none;
        }

        .titulo-seccion{
            flex-direction:column;
            align-items:flex-start;
        }

    }

</style>
"""


# -------------------------------------------------
# FUNCIONES DE AYUDA
# -------------------------------------------------

# Colores para los avatares
COLORES = ["#2A7272", "#0B2A45", "#C8714A", "#4A7FA6", "#8C5A7A", "#5C8A6E"]


# Saco las iniciales del nombre ("Marta Ibáñez" -> "MI")
def iniciales(nombre):
    partes = nombre.split()
    letras = ""
    for parte in partes[:2]:
        letras += parte[0]
    return letras.upper()


# Cada nombre tiene siempre el mismo color
def color(nombre):
    return COLORES[sum(ord(letra) for letra in nombre) % len(COLORES)]


# Parte de arriba de todas las páginas
def cabecera(titulo):
    return """
<!doctype html>
<html lang="es">
<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>""" + titulo + """</title>

    <link rel="icon" type="image/png" href="/logo/favicon-64.png">
    <link href="https://fonts.googleapis.com/css2?family=Carlito:wght@400;700&display=swap" rel="stylesheet">

""" + ESTILOS + """

</head>

<body>

<header>
    <div class="contenedor cabecera">

        <a class="logo" href="/">
            <img src="/logo/favicon-64.png" alt="">
            <span>Encuéntrame</span>
        </a>

        <nav class="menu">
            <a href="/#buscar">Buscar psicólogo</a>
            <a href="/panel">Soy psicólogo/a</a>
        </nav>

    </div>
</header>
"""


# Parte de abajo de todas las páginas
def pie():
    return """

<footer>
    © 2026 Encuéntrame · Proyecto de estudio DAM · Los perfiles son ficticios
</footer>

</body>
</html>
"""


# -------------------------------------------------
# PÁGINA PRINCIPAL
# -------------------------------------------------

@aplicacion.route("/")
def inicio():

    # Pido los psicólogos a la base de datos
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, especialidades, bio FROM psicologos ORDER BY nombre")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()

    # Junto todas las especialidades distintas para los filtros
    todas = []
    for fila in filas:
        for esp in (fila[2] or "").split(","):
            esp = esp.strip()
            if esp and esp not in todas:
                todas.append(esp)
    todas.sort()

    # Si vengo de enviar una solicitud, muestro un aviso
    aviso = ""
    if request.args.get("enviado"):
        aviso = '<div class="aviso">✓ Tu solicitud se envió a ' + escape(request.args.get("enviado")) + '. Te contactará pronto.</div>'

    cadena = cabecera("Encuéntrame — psicólogos y pacientes") + """

<div class="contenedor">

    """ + aviso + """

    <section class="hero">

        <div class="mini">Encuéntrame</div>

        <h1>Encuentra quien te escuche</h1>

        <p>
            Un espacio para conectar con psicólogos según lo que
            estás viviendo ahora mismo: duelo, ansiedad, pareja y más.
        </p>

        <a class="boton" href="#buscar">Busco apoyo</a>
        <a class="boton boton-borde" href="/panel">Soy psicólogo/a</a>

    </section>


    <section class="pasos">

        <div class="paso">
            <div class="numero">1</div>
            <h3>Explora</h3>
            <p>Mira los perfiles de los profesionales.</p>
        </div>

        <div class="paso">
            <div class="numero">2</div>
            <h3>Filtra</h3>
            <p>Busca por nombre o elige una especialidad.</p>
        </div>

        <div class="paso">
            <div class="numero">3</div>
            <h3>Cuéntanos</h3>
            <p>Explica brevemente tu situación.</p>
        </div>

        <div class="paso">
            <div class="numero">4</div>
            <h3>Te contactan</h3>
            <p>Por correo o teléfono, como prefieras.</p>
        </div>

    </section>


    <main id="buscar">

        <div class="titulo-seccion">

            <div>
                <h2>Nuestros psicólogos</h2>
                <p>Encuentra al profesional que mejor se adapta a ti.</p>
            </div>

            <div class="contador">
                <span id="visibles">""" + str(len(filas)) + """</span> de """ + str(len(filas)) + """ profesionales
            </div>

        </div>


        <input type="search" id="busqueda" placeholder="Buscar por nombre o tema...">


        <div class="filtros">
            <button class="filtro activo" data-esp="">Todas</button>
"""

    # Un botón por especialidad
    for esp in todas:
        cadena += '            <button class="filtro" data-esp="' + escape(esp) + '">' + escape(esp) + '</button>\n'

    cadena += """
        </div>


        <section id="psicologos">
"""


    # Recorro todos los psicólogos
    for fila in filas:

        id_psicologo = fila[0]
        nombre = escape(fila[1])
        especialidades = [e.strip() for e in (fila[2] or "").split(",") if e.strip()]
        bio = escape(fila[3] or "")

        etiquetas = ""
        for esp in especialidades:
            etiquetas += '<span class="etiqueta">' + escape(esp) + '</span>'

        cadena += f"""

            <article
                class="psicologo"
                data-nombre="{nombre.lower()}"
                data-bio="{bio.lower()}"
                data-especialidades="{escape('|'.join(especialidades))}"
            >

                <div class="cabeza">

                    <div class="avatar" style="background:{color(fila[1])}">
                        {escape(iniciales(fila[1]))}
                    </div>

                    <h3>{nombre}</h3>

                </div>

                <div class="etiquetas">
                    {etiquetas}
                </div>

                <p class="bio">
                    {bio}
                </p>

                <button
                    class="boton boton-pequeno"
                    data-id="{id_psicologo}"
                    data-nombre-mostrar="{nombre}"
                    onclick="abrirSolicitud(this)"
                >
                    Solicitar primera sesión
                </button>

            </article>
"""


    # Termino el documento HTML
    cadena += """
        </section>

        <div class="vacio" id="vacio">
            No hay psicólogos con este filtro. Prueba con otra búsqueda.
        </div>

    </main>

</div>


<dialog id="ventana">

    <button class="cerrar" onclick="ventana.close()">✕</button>

    <h2 style="margin-top:0">Solicitar sesión</h2>

    <p>Con <strong id="nombre-psicologo"></strong></p>

    <form method="post" action="/solicitud">

        <input type="hidden" name="psicologo_id" id="psicologo-id">

        <div class="campo">
            <label>Tu nombre</label>
            <input type="text" name="nombre" required>
        </div>

        <div class="campo">
            <label>Correo electrónico</label>
            <input type="email" name="email" required>
        </div>

        <div class="campo">
            <label>Teléfono (opcional)</label>
            <input type="tel" name="telefono">
        </div>

        <div class="campo">
            <label>Cuéntale brevemente tu situación</label>
            <textarea name="resumen" required
                placeholder="Por ejemplo: llevo unas semanas con mucha ansiedad por el trabajo..."></textarea>
        </div>

        <div class="campo opciones">
            <label style="display:block">Prefiero que me contacten por</label>
            <label><input type="radio" name="contacto" value="email" checked> Correo</label>
            <label><input type="radio" name="contacto" value="telefono"> Teléfono</label>
        </div>

        <button class="boton" style="width:100%">Enviar solicitud</button>

    </form>

</dialog>


<script>

    // -------------------------------
    // BUSCADOR Y FILTROS
    // -------------------------------

    let buscador = document.querySelector("#busqueda");
    let filtros = document.querySelectorAll(".filtro");
    let especialidadElegida = "";


    function filtrar(){

        let texto = buscador.value.toLowerCase();
        let psicologos = document.querySelectorAll(".psicologo");
        let visibles = 0;

        psicologos.forEach(function(psicologo){

            let coincideTexto =
                psicologo.dataset.nombre.includes(texto)
                ||
                psicologo.dataset.bio.includes(texto);

            let coincideEspecialidad =
                especialidadElegida == ""
                ||
                psicologo.dataset.especialidades.split("|").includes(especialidadElegida);

            if(coincideTexto && coincideEspecialidad){
                psicologo.style.display = "flex";
                visibles++;
            }else{
                psicologo.style.display = "none";
            }

        });

        document.querySelector("#visibles").textContent = visibles;
        document.querySelector("#vacio").style.display = visibles == 0 ? "block" : "none";

    }


    buscador.oninput = filtrar;


    filtros.forEach(function(boton){

        boton.onclick = function(){

            filtros.forEach(function(b){ b.classList.remove("activo"); });
            boton.classList.add("activo");

            especialidadElegida = boton.dataset.esp;
            filtrar();

        };

    });


    // -------------------------------
    // VENTANA DE SOLICITUD
    // -------------------------------

    let ventana = document.querySelector("#ventana");

    function abrirSolicitud(boton){

        document.querySelector("#psicologo-id").value = boton.dataset.id;
        document.querySelector("#nombre-psicologo").textContent = boton.dataset.nombreMostrar;

        ventana.showModal();

    }

</script>
""" + pie()


    # Devuelvo todo el HTML
    return cadena


# -------------------------------------------------
# GUARDAR UNA SOLICITUD
# -------------------------------------------------

@aplicacion.route("/solicitud", methods=["POST"])
def solicitud():

    # Recojo los datos del formulario
    psicologo_id = request.form.get("psicologo_id")
    nombre = request.form.get("nombre", "").strip()
    email = request.form.get("email", "").strip()
    telefono = request.form.get("telefono", "").strip()
    resumen = request.form.get("resumen", "").strip()
    contacto = request.form.get("contacto", "email")

    if contacto not in ("email", "telefono"):
        contacto = "email"

    # Si falta algo, vuelvo al inicio
    if not psicologo_id or not nombre or not email or not resumen:
        return redirect("/#buscar")

    conexion = conectar()
    cursor = conexion.cursor()

    # Compruebo que el psicólogo existe
    cursor.execute("SELECT nombre FROM psicologos WHERE id = %s", (psicologo_id,))
    psicologo = cursor.fetchone()

    if psicologo is None:
        cursor.close()
        conexion.close()
        return redirect("/#buscar")

    # Guardo la solicitud (con %s para evitar inyección SQL)
    cursor.execute(
        "INSERT INTO solicitudes (psicologo_id, nombre_paciente, email_paciente, telefono, resumen, contacto) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (psicologo_id, nombre, email, telefono, resumen, contacto)
    )
    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/?enviado=" + quote(psicologo[0]))


# -------------------------------------------------
# PANEL DEL PSICÓLOGO
# -------------------------------------------------

@aplicacion.route("/panel")
def panel():

    elegido = request.args.get("psicologo", "")

    conexion = conectar()
    cursor = conexion.cursor()

    # Lista de psicólogos con el número de solicitudes pendientes
    cursor.execute("""
        SELECT p.id, p.nombre,
               SUM(CASE WHEN s.estado = 'pendiente' THEN 1 ELSE 0 END)
        FROM psicologos p
        LEFT JOIN solicitudes s ON s.psicologo_id = p.id
        GROUP BY p.id, p.nombre
        ORDER BY p.nombre
    """)
    psicologos = cursor.fetchall()

    # Solicitudes del psicólogo elegido
    solicitudes = []
    if elegido:
        cursor.execute("""
            SELECT id, nombre_paciente, email_paciente, telefono, resumen, contacto, estado, fecha
            FROM solicitudes
            WHERE psicologo_id = %s
            ORDER BY fecha DESC
        """, (elegido,))
        solicitudes = cursor.fetchall()

    cursor.close()
    conexion.close()


    cadena = cabecera("Panel del psicólogo — Encuéntrame") + """

<main class="contenedor">

    <div class="titulo-seccion">
        <div>
            <h2>Solicitudes recibidas</h2>
            <p>Elige tu perfil para ver quién te ha escrito.</p>
        </div>
    </div>

    <form method="get" action="/panel">

        <select class="selector" name="psicologo" onchange="this.form.submit()">
            <option value="">— Elige tu perfil —</option>
"""

    for p in psicologos:
        pendientes = int(p[2] or 0)
        texto = escape(p[1]) + (" (" + str(pendientes) + " pendientes)" if pendientes else "")
        marcado = " selected" if str(p[0]) == elegido else ""
        cadena += f'            <option value="{p[0]}"{marcado}>{texto}</option>\n'

    cadena += """
        </select>

    </form>

    <div style="margin-top:25px">
"""

    if elegido and not solicitudes:
        cadena += '<p class="vacio" style="display:block">Aún no has recibido solicitudes.</p>'

    # Recorro las solicitudes
    for s in solicitudes:

        id_solicitud = s[0]
        contactado = s[6] == "contactado"

        boton = ""
        if not contactado:
            boton = f"""
            <form method="post" action="/contactado/{id_solicitud}">
                <input type="hidden" name="psicologo" value="{escape(elegido)}">
                <button class="boton boton-pequeno" style="margin-top:10px">Marcar como contactado</button>
            </form>
            """

        cadena += f"""

        <div class="solicitud">

            <div class="meta">
                <strong>{escape(s[1])}</strong> · {s[7].strftime('%d/%m/%Y %H:%M')} ·
                <span class="estado {'contactado' if contactado else ''}">
                    {'Contactado' if contactado else 'Pendiente'}
                </span>
            </div>

            <p>{escape(s[4])}</p>

            <div class="meta">
                ✉ {escape(s[2])}
                {'· ☎ ' + escape(s[3]) if s[3] else ''}
                · Prefiere {'correo' if s[5] == 'email' else 'teléfono'}
            </div>

            {boton}

        </div>
"""

    cadena += """
    </div>

</main>
""" + pie()

    return cadena


# -------------------------------------------------
# MARCAR UNA SOLICITUD COMO CONTACTADA
# -------------------------------------------------

@aplicacion.route("/contactado/<int:id_solicitud>", methods=["POST"])
def contactado(id_solicitud):

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE solicitudes SET estado = 'contactado' WHERE id = %s", (id_solicitud,))
    conexion.commit()
    cursor.close()
    conexion.close()

    return redirect("/panel?psicologo=" + quote(request.form.get("psicologo", "")))


# Ejecuto la aplicación
if __name__ == "__main__":

    aplicacion.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
