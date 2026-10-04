import tkinter as tk

ventana = tk.Tk()

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

marco = tk.Frame(ventana)

titulo = tk.Label(marco,text="Gestión de ciclistas v0.1")
titulo.pack(padx=20,pady=20)

#insertar un ciclista
nombre = tk.Label(marco,text="Introduce el nombre del ciclista")
nombre.pack(padx=2,pady=2)
inputnombre = tk.Entry(marco)
inputnombre.pack(padx=20,pady=20)

#insertar apellidos
apellidos = tk.Label(marco,text="Introduce los apellidos del ciclista")
apellidos.pack(padx=2,pady=2)
inputapellidos = tk.Entry(marco)
inputapellidos.pack(padx=20,pady=20)

#insertar email
email = tk.Label(marco,text="Introduce el email del ciclista")
email.pack(padx=2,pady=2)
inputemail = tk.Entry(marco)
inputemail.pack(padx=20,pady=20)

#insertar equipo
equipo = tk.Label(marco,text="Introduce el equipo del ciclista")
equipo.pack(padx=2,pady=2)
inputequipo = tk.Entry(marco)
inputequipo.pack(padx=20,pady=20)

#insertar tipo de bicicleta
tipobicicleta = tk.Label(marco,text="Introduce el tipo de bicicleta")
tipobicicleta.pack(padx=2,pady=2)
inputtipobicicleta = tk.Entry(marco)
inputtipobicicleta.pack(padx=20,pady=20)

boton = tk.Button(marco,text="Insertar ciclista",command=insertaCliente)
boton.pack(padx=20,pady=20)

marco.grid(row=0,column=0)

campodetexto = tk.Text(ventana)
campodetexto.grid(row=0,column=1,padx=20,pady=20)

ventana.mainloop()