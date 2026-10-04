import tkinter as tk

# ---------- Colores y fuentes ----------
FONDO = "#1e1e2e"
TARJETA = "#2a2a3d"
TEXTO = "#e4e4ef"
SECUNDARIO = "#a0a0b8"
ACENTO = "#f5a623"
ACENTO_HOVER = "#ffb84d"
CAMPO = "#38384f"

FUENTE_TITULO = ("Segoe UI", 18, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 10)
FUENTE_LABEL = ("Segoe UI", 10, "bold")
FUENTE_INPUT = ("Segoe UI", 11)
FUENTE_TEXTO = ("Consolas", 10)

ventana = tk.Tk()
ventana.title("Gestión de ciclistas")
ventana.configure(bg=FONDO)
ventana.resizable(False, False)

def insertaCliente():
  print("Voy a insertar un ciclista")
  stringnombre = inputnombre.get() #datos que se han introducido en el campo de texto
  stringapellidos = inputapellidos.get()
  stringemail = inputemail.get()
  stringequipo = inputequipo.get()
  stringtipobicicleta = inputtipobicicleta.get()
  archivo = open("ciclistas.csv",'a')
  archivo.write(stringnombre+","+stringapellidos+","+stringemail+","+stringequipo+","+stringtipobicicleta+"\n")
  archivo.close()
  campodetexto.delete("1.0", tk.END)	# Primero borra todo lo que haya
  archivo = open("ciclistas.csv",'r')
  lineas = archivo.readlines()
  for linea in lineas:
    campodetexto.insert(tk.END, linea)	# Insertame una linea
  archivo.close()

# Crea una etiqueta + campo de texto con el mismo estilo
def crearCampo(texto):
  etiqueta = tk.Label(marco, text=texto, font=FUENTE_LABEL, bg=TARJETA, fg=SECUNDARIO, anchor="w")
  etiqueta.pack(fill="x", padx=25, pady=(10, 3))
  campo = tk.Entry(marco, font=FUENTE_INPUT, bg=CAMPO, fg=TEXTO, insertbackground=TEXTO,
                   relief="flat", width=30, highlightthickness=1,
                   highlightbackground=CAMPO, highlightcolor=ACENTO)
  campo.pack(fill="x", padx=25, ipady=6)
  return campo

# ---------- Formulario (izquierda) ----------
marco = tk.Frame(ventana, bg=TARJETA)

titulo = tk.Label(marco, text="🚴 Gestión de ciclistas", font=FUENTE_TITULO, bg=TARJETA, fg=TEXTO)
titulo.pack(padx=25, pady=(25, 0), anchor="w")
subtitulo = tk.Label(marco, text="v0.1 · Registro de participantes", font=FUENTE_SUBTITULO, bg=TARJETA, fg=SECUNDARIO)
subtitulo.pack(padx=25, pady=(0, 10), anchor="w")

inputnombre = crearCampo("Nombre")
inputapellidos = crearCampo("Apellidos")
inputemail = crearCampo("Email")
inputequipo = crearCampo("Equipo")
inputtipobicicleta = crearCampo("Tipo de bicicleta")

boton = tk.Button(marco, text="Insertar ciclista", command=insertaCliente,
                  font=FUENTE_LABEL, bg=ACENTO, fg="#1e1e2e",
                  activebackground=ACENTO_HOVER, activeforeground="#1e1e2e",
                  relief="flat", cursor="hand2", pady=8)
boton.pack(fill="x", padx=25, pady=25)

# Efecto hover del botón
boton.bind("<Enter>", lambda e: boton.config(bg=ACENTO_HOVER))
boton.bind("<Leave>", lambda e: boton.config(bg=ACENTO))

marco.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="n")

# ---------- Listado (derecha) ----------
marcolista = tk.Frame(ventana, bg=TARJETA)
marcolista.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="ns")

tk.Label(marcolista, text="Ciclistas registrados", font=FUENTE_LABEL,
         bg=TARJETA, fg=SECUNDARIO, anchor="w").pack(fill="x", padx=15, pady=(15, 5))

campodetexto = tk.Text(marcolista, font=FUENTE_TEXTO, bg=CAMPO, fg=TEXTO,
                       insertbackground=TEXTO, relief="flat", width=60, height=24,
                       padx=10, pady=10)
campodetexto.pack(padx=15, pady=(0, 15))

ventana.mainloop()
