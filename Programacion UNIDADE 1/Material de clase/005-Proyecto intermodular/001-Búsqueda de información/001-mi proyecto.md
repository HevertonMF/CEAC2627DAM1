# Paso 1: Búsqueda de información

La demanda de psicólogos es real, el precio de una sesión en Valencia ronda los 50-60 € y el punto legal más delicado son los datos de salud.

## 1. Demanda
- Alrededor del 18,2 % de los españoles necesitó atención por salud mental en el último año (Barómetro Sanitario 2026). Entre los derivados a un especialista de la sanidad pública, la espera media hasta la primera consulta fue de 90 días.
- En el Barómetro 2025 (19,9 % con necesidad), solo el 26,7 % consiguió cita en menos de un mes y el 22,4 % esperó más de tres.
- Eurofound sitúa la espera para el primer contacto con un psicólogo en la sanidad pública en torno a seis meses. Las dos cifras miden cosas distintas, por eso cito ambas.
- En la Comunitat Valenciana hay algo más de 4 psicólogos clínicos por cada 100.000 habitantes, frente a 6 en España y 18 en la UE. Es un dato de hacia 2019, así que está desactualizado.

## 2. Precios en Valencia
- En los listados de Benimaclet hay sesiones individuales de entre 30 € y 60 €. En Benicalap aparecen precios de 40 € a 70 €.
- Para ciudades medianas como Valencia, una guía de precios de 2026 indica 50-70 € por sesión.
- Online, el rango habitual en España es de 35-70 € por sesión.
- Estas fuentes son portales comerciales y blogs, no tarifas oficiales. Sirven como orden de magnitud.

## 3. Requisitos legales
- **Quién puede ejercer:**
  - Para ejercer como psicólogo hace falta el grado y la inscripción en un Colegio Oficial.
  - Para actuar en el ámbito sanitario se exige además el Máster en Psicología General Sanitaria (Ley 33/2011). La alternativa es el título de especialista clínico por la vía PIR.
  - Por eso el campo de verificación debería pedir el **nº de colegiado y la habilitación sanitaria**, no solo la colegiación.
- **Datos de salud (RGPD):**
  - El psicólogo es el responsable del tratamiento de los datos de sus pacientes. Antes de usar una plataforma digital debe formalizar un contrato con el proveedor.
  - Si nuestra plataforma guarda mensajes o resúmenes de pacientes, pasa a tratar datos de salud. Eso exige consentimiento explícito y medidas de seguridad reforzadas.
- **Publicidad sanitaria:** la publicidad de centros sanitarios autorizados debe incluir el número de registro asignado por la autoridad sanitaria. Esta fuente es antigua, así que conviene confirmar con el COPCV o la Conselleria de Sanidad si aplica a un directorio.
- **Sobre el prototipo:** el artifact guarda todo en el navegador y usa un hash de contraseña simple, y el campo "resumen" de las solicitudes puede contener datos de salud. Sirve para demostrar el concepto, pero no debe recibir datos reales.

## Conclusiones para el proyecto
- Hay demanda y hay falta de oferta pública, lo que justifica el proyecto.
- Los competidores que vimos son nacionales u online. Mi hipótesis, que aún no he validado, es que un directorio local de Valencia con verificación de colegiado y habilitación sanitaria se diferenciaría.
- Para un directorio simple, el riesgo legal es bajo. Sube cuando la plataforma pasa a gestionar mensajes o citas con datos de los pacientes.

Falta validar la hipótesis con psicólogos y pacientes de Valencia (entrevistas o una encuesta corta). ¿Quieres que prepare las preguntas, o que lo pase a un documento?

Fuentes:
- [Barómetro Sanitario 2026 (Infocop)](https://www.infocop.es/casi-uno-de-cada-cinco-espanoles-ha-necesitado-atencion-por-problemas-de-salud-mental-en-el-ultimo-ano-segun-el-barometro-sanitario-2026/)
- [Barómetro Sanitario 2025 (Infocop)](https://www.infocop.es/una-de-cada-cinco-personas-adultas-ha-necesitado-atencion-en-salud-mental-segun-el-barometro-sanitario-2025/)
- [Listas de espera en atención psicológica (Infocop)](https://www.infocop.es/las-largas-listas-de-espera-en-espana-una-barrera-clave-para-el-acceso-a-la-atencion-psicologica/)
- [OCU pide más psicólogos clínicos en la sanidad valenciana (Valencia Plaza)](https://valenciaplaza.com/valenciaplaza/ocu-pide-multiplicar-cuatro-numero-psicologos-clinicos-sanidad-publica-valenciana)
- [Precios de psicólogos en Benimaclet (Masquemedicos)](https://masquemedicos.com/precios/psicologos_benimaclet-valencia_b/)
- [Guía de precios 2026 (Cuántome cuesta)](https://cuantomecuesta.com/es/psicologo/)
- [Psicólogo online: precio (BetterHelp)](https://www.betterhelp.com/es/blog/terapia/psic%C3%B3logo-online-precio-cu%C3%A1nto-cuesta-una-sesi%C3%B3n-y-qu%C3%A9-factores-influyen/)
- [Preguntas y respuestas sobre el ejercicio profesional (Infocop)](https://www.infocop.es/preguntas-y-respuestas-sobre-el-ejercicio-profesional-de-la-psicologia-en-espana-tras-la-aprobacion-de-la-ley-de-consumidores/)
- [Circular informativa COP sobre datos de pacientes (Infocop)](https://www.infocop.es/wp-content/uploads/2026/03/CIRCULAR-INFORMATIVA-1.pdf)
- [Publicidad sanitaria y psicólogos (Infocop)](https://www.infocop.es/?p=26956)