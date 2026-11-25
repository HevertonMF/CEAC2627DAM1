class Cliente():                             #creo una clase cliente

  def __init__(self,minombre,misapellidos):   #creo un constructor 
    self.nombre = minombre
    self.apellidos = misapellidos

class Producto():                           #creo una clase producto        

  def __init__(self,minombre,miprecio):     #creo un constructor 
    self.nombre = minombre
    self.precio = miprecio
    
class Pedido():                             #creo una clase pedido 

  def __init__(self,mifecha,minombre,misapellidos): #creo un constructor 
    self.fecha = mifecha
    self.cliente = Cliente(minombre,misapellidos)
    self.productos = []
    

pedido1 = Pedido("2026-11-02","Heverton","Marques") #creo un objeto de tipo pedido 

pedido1.productos.append(Producto("Ordenador",34))
pedido1.productos.append(Producto("Teléfono",45))

print(pedido1)    #print pedido1

