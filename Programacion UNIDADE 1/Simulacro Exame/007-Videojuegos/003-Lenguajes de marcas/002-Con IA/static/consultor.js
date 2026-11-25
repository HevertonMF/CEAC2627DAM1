// Atajo para coger elementos por id
function $(id) { return document.getElementById(id); }

// Evita que el texto se convierta en HTML
function escapar(texto) {
  return String(texto).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
  });
}

// Pinta la tabla con columnas y filas
function pintarTabla(columnas, filas) {
  let html = "<tr>";
  for (const c of columnas) html += "<th>" + escapar(c) + "</th>";
  html += "</tr>";
  for (const fila of filas) {
    html += "<tr>";
    for (const v of fila) html += "<td>" + (v === null ? "-" : escapar(v)) + "</td>";
    html += "</tr>";
  }
  $("tabla").innerHTML = html;
  $("contador").textContent = "(" + filas.length + " filas)";
}

// Muestra un mensaje verde (ok) o rojo (error)
function mensaje(texto, tipo) {
  $("mensaje").textContent = texto;
  $("mensaje").className = "mensaje " + tipo;
}

// Manda la pregunta a Flask y enseña el resultado
async function consultar() {
  const pregunta = $("pregunta").value.trim();
  if (!pregunta) return;

  $("enviar").disabled = true;
  $("enviar").textContent = "Pensando...";
  $("mensaje").className = "mensaje oculto";
  $("caja-resultado").classList.add("oculto");

  try {
    const respuesta = await fetch("/consultar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pregunta: pregunta, permitir_cambios: $("permitir").checked })
    });
    const datos = await respuesta.json();

    // Enseño el SQL si lo hay
    if (datos.sql) {
      $("sql").textContent = datos.sql;
      $("caja-sql").classList.remove("oculto");
    }

    if (datos.error) {
      mensaje(datos.error, "error");
    } else if (datos.columnas.length > 0) {
      pintarTabla(datos.columnas, datos.filas);
      $("caja-resultado").classList.remove("oculto");
    } else {
      mensaje("Hecho. Filas afectadas: " + datos.afectadas, "ok");
    }
  } catch (e) {
    mensaje("No se pudo contactar con Flask.", "error");
  }

  $("enviar").disabled = false;
  $("enviar").textContent = "Generar y ejecutar";
}

// Botón y Ctrl+Enter
$("enviar").addEventListener("click", consultar);
$("pregunta").addEventListener("keydown", function (e) {
  if (e.key === "Enter" && e.ctrlKey) consultar();
});

// Las preguntas de ejemplo rellenan el cuadro y consultan
document.querySelectorAll(".chip").forEach(function (chip) {
  chip.addEventListener("click", function () {
    $("pregunta").value = chip.textContent;
    consultar();
  });
});
