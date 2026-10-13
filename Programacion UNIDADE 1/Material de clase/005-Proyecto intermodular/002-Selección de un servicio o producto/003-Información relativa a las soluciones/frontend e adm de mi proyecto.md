Encuéntrame

El frontend es la parte de la web que ve el paciente. Se genera desde Flask (Python): cada página se construye como una cadena de HTML con los datos que llegan de la base de datos MySQL. El diseño es propio, con CSS escrito a mano: colores morado y lima, tipografía Calibri, adaptado a móvil y con modo oscuro automático.

Página principal (/login)

Una cabecera con el logo y un menú que cambia según quién haya iniciado sesión (visitante, paciente o psicólogo).
Un bloque de presentación con dos botones: «Busco apoyo» y «Soy psicólogo/a».
Cuatro pasos que explican cómo funciona la web: explora, filtra, cuéntanos y te contactan.
El listado de psicólogos en tarjetas, con su foto (o sus iniciales), sus especialidades y una breve presentación.
Un buscador por nombre o tema y unos botones para filtrar por especialidad. Los filtros funcionan con JavaScript, sin recargar la página.

Solicitud de primera sesión
Al pulsar «Solicitar primera sesión» se abre una ventana (<dialog>) con un formulario donde el paciente cuenta brevemente su situación y elige si prefiere que le contacten por correo o por teléfono. Si ha iniciado sesión, su nombre y su correo ya aparecen rellenados.

Área del paciente

Registro e inicio de sesión (/registro y /entrar), con contraseñas guardadas cifradas (hash).
Mis solicitudes (/mis-solicitudes): el paciente ve a quién ha escrito, la fecha y si el psicólogo ya le ha contactado.
Eliminar mi cuenta: borra su cuenta y sus solicitudes después de confirmar con la contraseña.
Página de administración (panel del psicólogo)

El panel es la parte privada de la web. Solo pueden entrar los psicólogos que han iniciado sesión. Si alguien intenta entrar sin sesión, la web lo manda a la página de acceso.

Solicitudes recibidas (/panel)

Cada psicólogo ve únicamente sus propias solicitudes, ordenadas de la más reciente a la más antigua.
De cada solicitud se muestra el nombre del paciente, la fecha, el resumen de su situación, su correo, su teléfono y cómo prefiere que le contacten.
Con el botón «Marcar como contactado», la solicitud pasa de Pendiente a Contactado. Un psicólogo no puede cambiar las solicitudes de otro.

Mi perfil (/perfil)

Permite editar el nombre, el teléfono, la presentación y las especialidades.
Permite subir una foto de perfil (JPG, PNG o WEBP, máximo 2 MB). La foto nueva sustituye a la anterior y aparece en la página principal.
Desde aquí también puede eliminar su cuenta. Se borran su perfil, su foto y sus solicitudes, y deja de aparecer en la web.

Seguridad

Las contraseñas nunca se guardan en texto, solo su hash.
Todas las consultas a la base de datos usan parámetros (%s) para evitar la inyección SQL.
El texto que escriben los usuarios se escapa antes de mostrarlo, para que nadie pueda meter código HTML o JavaScript.
Pienso en hacerlo con JSON.
