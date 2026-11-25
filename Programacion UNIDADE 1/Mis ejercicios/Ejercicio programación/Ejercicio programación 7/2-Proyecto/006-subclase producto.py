class Cliente():                             # Clase para representar a un cliente

  def __init__(self,minombre,misapellidos):  # Constructor de la clase Cliente
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():                             #clase para representar a un producto

  def __init__(self,minombre,miprecio):      # Constructor de la clase Producto
    self.nombre = minombre
    self.precio = miprecio
    
class Pedido():                                 # Clase para representar a un pedido

  def __init__(self,mifecha,minombre,misapellidos): # Constructor de la clase Pedido

    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []
    
# Agregar un producto al pedido

pedido1 = Pedido("2026-11-02","Heverton","Marques")
pedido1.productos.append(Producto("Ordenador",34))
pedido1.productos.append(Producto("Teléfono",45))
# Convertir el objeto a JSON y mostrarlo en
print(pedido1)