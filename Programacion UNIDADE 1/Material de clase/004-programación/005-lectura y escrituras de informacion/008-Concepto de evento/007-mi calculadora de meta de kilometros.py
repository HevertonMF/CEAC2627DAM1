# sudo apt update && sudo apt install python3-tk -y
import tkinter as tk

def calcula():
  print("Vamos a calcular")
  km = float(distancia.get().replace(",", "."))
  minutos = float(tiempo.get().replace(",", "."))
  horas = minutos / 60
  velocidad = km / horas
  resultado.config(text=f"Velocidad media: {velocidad:.2f} km/h")

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Velocidad media")

# entrada de los kilómetros
etiqueta_km = tk.Label(text="¿Cuántos km has pedaleado?")
etiqueta_km.pack(padx=10, pady=5)

distancia = tk.Entry()
distancia.pack(padx=10, pady=5)

# entrada del tiempo
etiqueta_tiempo = tk.Label(text="¿Cuánto tiempo has tardado? (en minutos)")
etiqueta_tiempo.pack(padx=10, pady=5)

tiempo = tk.Entry()
tiempo.pack(padx=10, pady=5)

# dispara la acción
boton = tk.Button(text="Calcular velocidad media", command=calcula)
boton.pack(padx=10, pady=10)

# label para sacar el resultado
resultado = tk.Label(text="Resultado")
resultado.pack(padx=10, pady=10)

ventana.mainloop() # no te salgas, bucle infinito
